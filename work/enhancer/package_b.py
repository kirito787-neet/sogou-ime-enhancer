"""A single APK: NPatch + enhanced baseline, including in-app settings components.

Only two binary XML manifests and the additional settings DEX are changed after
NPatch. Existing resources and native library payloads are preserved byte-for-byte.
"""
from pathlib import Path
from io import BytesIO
import hashlib
import json
import re
import struct as s
import zipfile
import zlib
from build import BASE, ROOT, java, sha

U32 = lambda b, p: s.unpack_from('<I', b, p)[0]
ANDROID = 'http://schemas.android.com/apk/res/android'
NONE = 0xffffffff
HOST = 'com.sohu.inputmethod.sogou.enhanced'


def read_member(archive, name):
    """NPatch uses intentional overlapping ZIP entries for origin.apk.

    Validate the member's bounds, declared size and CRC explicitly instead of
    Python's non-overlap rule. Output is rewritten into an ordinary ZIP.
    """
    info = archive.getinfo(name)
    if info.file_size > 256 * 1024 * 1024: raise ValueError('oversized APK member')
    archive.fp.seek(info.header_offset)
    header = archive.fp.read(30)
    if header[:4] != b'PK\x03\x04': raise ValueError('missing ZIP local header')
    nl, el = s.unpack_from('<HH', header, 26)
    offset = info.header_offset+30+nl+el
    if offset+info.compress_size > archive.start_dir: raise ValueError('member out of bounds')
    archive.fp.seek(offset)
    raw = archive.fp.read(info.compress_size)
    if info.compress_type == 0: data = raw
    elif info.compress_type == 8: data = zlib.decompress(raw, -15)
    else: raise ValueError('unsupported ZIP compression')
    if len(data) != info.file_size or zlib.crc32(data) != info.CRC: raise ValueError('member CRC/size mismatch')
    return data


def chunks(blob):
    offset = 8
    while offset < len(blob):
        kind, header, size = s.unpack_from('<HHI', blob, offset)
        if size < header or offset + size > len(blob): raise ValueError('invalid AXML chunk')
        yield kind, blob[offset:offset+size]
        offset += size


def add_components(blob):
    parts = list(chunks(blob))
    pool = next(data for kind, data in parts if kind == 1)
    count, styles_count, flags, data_start, styles_start = s.unpack_from('<IIIII', pool, 8)
    header_size = s.unpack_from('<H', pool, 2)[0]
    utf8 = bool(flags & 0x100)

    def length(data, p, wide=False):
        n = s.unpack_from('<H' if wide else '<B', data, p)[0]
        p += 2 if wide else 1
        mask = 0x8000 if wide else 0x80
        if n & mask:
            n = ((n & (mask-1)) << (16 if wide else 8)) | s.unpack_from('<H' if wide else '<B', data, p)[0]
            p += 2 if wide else 1
        return n, p

    strings = []
    for i in range(count):
        p = data_start + U32(pool, header_size+4*i)
        n, p = length(pool, p, not utf8)
        if utf8: n, p = length(pool, p)
        strings.append(pool[p:p+n*(1 if utf8 else 2)].decode('utf-8' if utf8 else 'utf-16le'))
    # Unique custom permissions and explicit process names make coexistence possible.
    old = 'com.sohu.inputmethod.sogou'
    strings = [HOST if value == old else
               HOST + value[len(old):] if value.startswith(old+'.') and '.permission.' in value
               else value for value in strings]
    resource_data = next(data for kind, data in parts if kind == 0x180)
    resource_ids = list(s.unpack('<'+'I'*((len(resource_data)-8)//4), resource_data[8:]))

    def intern(value):
        try: return strings.index(value)
        except ValueError: strings.append(value); return len(strings)-1

    android_ns = intern(ANDROID)
    attr_ids = {'name': 0x01010003, 'label': 0x01010001, 'exported': 0x01010010,
                'theme': 0x01010000, 'authorities': 0x01010018,
                'targetActivity': 0x01010202, 'enabled': 0x0101000e}

    def attribute(name, value):
        resource_id = attr_ids[name]
        try: index = resource_ids.index(resource_id)
        except ValueError:
            index = intern(name)
            resource_ids.extend([0] * max(0, index+1-len(resource_ids)))
            resource_ids[index] = resource_id
        if isinstance(value, bool): raw, kind, data = NONE, 0x12, int(value)
        elif isinstance(value, int): raw, kind, data = NONE, 1, value
        else: raw, kind, data = intern(value), 3, intern(value)
        return s.pack('<IIIHBBI', android_ns, index, raw, 8, 0, kind, data)

    def node(name, attrs=(), children=b''):
        index = intern(name)
        records = b''.join(attribute(key, value) for key, value in attrs)
        # ResXMLTree_node (16), ResXMLTree_attrExt (20), attributes (20 each).
        start = s.pack('<HHIII', 0x102, 16, 36+len(records), 0, NONE)
        start += s.pack('<IIHHHHHH', NONE, index, 20, 20, len(attrs), 0, 0, 0) + records
        end = s.pack('<HHIIIII', 0x103, 16, 24, 0, NONE, NONE, index)
        return start + children + end

    added = node('activity', [('name', 'com.sogouenhance.SettingsActivity'), ('exported', True),
                              ('label', '搜狗增强设置'), ('theme', 0x01030237)])
    added += node('provider', [('name', 'com.sogouenhance.PrefProvider'), ('exported', False),
                              ('authorities', HOST+'.enhance.prefs')])
    intent = node('intent-filter', children=node('action', [('name', 'android.intent.action.MAIN')])
                  + node('category', [('name', 'android.intent.category.LAUNCHER')]))
    added += node('activity-alias', [('name', HOST+'.LauncherAlias'),
                                    ('exported', True), ('enabled', True), ('label', '搜狗增强设置'),
                                    ('targetActivity', 'com.sogouenhance.SettingsActivity')], intent)

    def enc_length(n, wide=False):
        if wide: return s.pack('<H', n) if n < 0x8000 else s.pack('<HH', 0x8000 | (n>>16), n & 0xffff)
        return bytes([n]) if n < 0x80 else bytes([0x80 | (n>>8), n & 0xff])

    encoded, offsets = [], []
    offset = 0
    for string in strings:
        raw = string.encode('utf-8' if utf8 else 'utf-16le')
        units = len(string.encode('utf-16le')) // 2
        value = enc_length(units, not utf8)
        if utf8: value += enc_length(len(raw))
        value += raw + (b'\0' if utf8 else b'\0\0')
        offsets.append(offset)
        encoded.append(value)
        offset += len(value)
    data = b''.join(encoded)
    data += b'\0' * (-len(data) % 4)
    style_offsets = pool[header_size+4*count:header_size+4*(count+styles_count)]
    style_data = pool[styles_start:] if styles_start else b''
    new_start = header_size+4*len(strings)+len(style_offsets)
    pool_header = bytearray(pool[:header_size])
    s.pack_into('<I', pool_header, 4, new_start+len(data)+len(style_data))
    s.pack_into('<IIIII', pool_header, 8, len(strings), styles_count, flags & ~1,
                new_start, new_start+len(data) if styles_start else 0)
    new_pool = bytes(pool_header)+s.pack('<'+'I'*len(offsets), *offsets)+style_offsets+data+style_data
    new_map = s.pack('<HHI', 0x180, 8, 8+4*len(resource_ids))+s.pack('<'+'I'*len(resource_ids), *resource_ids)
    output = []
    inserted = 0
    for kind, data in parts:
        if kind == 1: output.append(new_pool)
        elif kind == 0x180: output.append(new_map)
        else:
            if kind == 0x103 and strings[U32(data, 20)] == 'application':
                output.append(added)
                inserted += 1
            output.append(data)
    assert inserted == 1
    payload = b''.join(output)
    return s.pack('<HHI', 3, 8, 8+len(payload))+payload


def rewrite_apk(blob, replacements):
    out = BytesIO()
    with zipfile.ZipFile(BytesIO(blob)) as source, zipfile.ZipFile(out, 'w') as dest:
        written = set()
        for member in source.infolist():
            if re.match(r'META-INF/[^/]+\.(SF|RSA|DSA|EC)$', member.filename, re.I): continue
            if member.filename == 'META-INF/MANIFEST.MF': continue
            data = replacements[member.filename] if member.filename in replacements else read_member(source, member.filename)
            info = zipfile.ZipInfo(member.filename, member.date_time)
            info.compress_type = member.compress_type
            info.external_attr = member.external_attr
            if info.compress_type == zipfile.ZIP_STORED:
                align = 4096 if info.filename.endswith('.so') else 4
                padding = (-(out.tell()+30+len(info.filename.encode('utf-8')))) % align
                if padding:
                    if padding < 4: padding += align
                    info.extra = b'\x35\xd9'+s.pack('<H', padding-4)+b'\0'*(padding-4)
            dest.writestr(info, data)
            written.add(info.filename)
        for name, data in replacements.items():
            if name not in written: dest.writestr(name, data, zipfile.ZIP_DEFLATED)
    return out.getvalue()


def main():
    official = BASE/'official/SogouInput_20.17.0_android_sweb.apk'
    module = ROOT/json.loads((BASE/'build/modules.json').read_text(encoding='utf-8'))['b']['apk']
    patched_dir = BASE/'build/npatch'
    patched_dir.mkdir(exist_ok=True)
    java('-Xmx4g', '-jar', ROOT/'work/patch/npatch.jar', '-m', module,
         '-l', '3', '-f', '-npa', '-p', HOST, '--name', '搜狗输入法·增强版', '-o', patched_dir, official)
    patched = next(patched_dir.glob('*npatched.apk'))
    with zipfile.ZipFile(patched) as source:
        origin = read_member(source, 'assets/npatch/origin.apk')
        config = json.loads(read_member(source, 'assets/npatch/config.json'))
        with zipfile.ZipFile(BytesIO(origin)) as original, zipfile.ZipFile(module) as enhanced:
            manifest = add_components(original.read('AndroidManifest.xml'))
            dex_names = [n for n in original.namelist() if re.fullmatch(r'classes\d*\.dex', n)]
            dex_name = f'classes{len(dex_names)+1}.dex'
            modified_origin = rewrite_apk(origin, {'AndroidManifest.xml': manifest,
                                                  dex_name: enhanced.read('classes.dex')})
        outer_manifest = add_components(read_member(source, 'AndroidManifest.xml'))
    product = BASE/'build/sogou-20.17.0-enhanced-single-unsigned.apk'
    product.write_bytes(rewrite_apk(patched.read_bytes(), {'AndroidManifest.xml': outer_manifest,
                                  'assets/npatch/origin.apk': modified_origin}))
    signed_dir = BASE/f'build/single-signed-{sha(product)[:12]}'
    if not signed_dir.exists():
        java('-jar', ROOT/'work/tools/signer.jar', '-a', product, '-o', signed_dir)
    signed = next(signed_dir.glob('*.apk'))
    report = {'apk': str(signed.relative_to(ROOT)), 'sha256': sha(signed), 'version': '20.17.0 (2620)',
              'embedded_module_sha256': sha(module), 'official_source_sha256': sha(official),
              'original_signature_preserved_in_npatch_config': bool(config.get('originalSignature')),
              'settings_dex': dex_name, 'runtime': 'pending', 'separate_module_install_required': False}
    report['package'] = HOST
    (BASE/'build/single.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
