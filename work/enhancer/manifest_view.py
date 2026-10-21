"""Small read-only binary XML view for verifying APK component declarations."""
import struct
import xml.etree.ElementTree as ET

A = '{http://schemas.android.com/apk/res/android}'


def parse(blob):
    strings, stack, root = [], [], None
    offset = 8
    while offset < len(blob):
        kind, header, size = struct.unpack_from('<HHI', blob, offset)
        assert size >= header and offset+size <= len(blob)
        data = blob[offset:offset+size]
        if kind == 1:
            count, _, flags, start, _ = struct.unpack_from('<IIIII', data, 8)
            utf8 = bool(flags & 0x100)

            def length(pos, wide):
                value = struct.unpack_from('<H' if wide else '<B', data, pos)[0]
                pos += 2 if wide else 1
                mask = 0x8000 if wide else 0x80
                if value & mask:
                    value = ((value & (mask-1)) << (16 if wide else 8)) | struct.unpack_from('<H' if wide else '<B', data, pos)[0]
                    pos += 2 if wide else 1
                return value, pos

            for i in range(count):
                pos = start+struct.unpack_from('<I', data, header+4*i)[0]
                n, pos = length(pos, not utf8)
                if utf8:
                    n, pos = length(pos, False)
                strings.append(data[pos:pos+n*(1 if utf8 else 2)].decode('utf-8' if utf8 else 'utf-16le'))
        elif kind == 0x102:
            name = strings[struct.unpack_from('<I', data, 20)[0]]
            start, width, count = struct.unpack_from('<HHH', data, 24)
            attrs = {}
            for i in range(count):
                pos = 16+start+width*i
                ns, key, raw = struct.unpack_from('<III', data, pos)
                value_type = data[pos+15]
                value = struct.unpack_from('<I', data, pos+16)[0]
                if value_type == 3:
                    value = strings[value]
                elif value_type == 0x12:
                    value = 'true' if value else 'false'
                elif value_type == 1:
                    value = f'@0x{value:08x}'
                else:
                    value = str(value)
                key = strings[key]
                if ns != 0xffffffff:
                    key = '{'+strings[ns]+'}'+key
                attrs[key] = value
            node = ET.Element(name, attrs)
            if stack:
                stack[-1].append(node)
            else:
                assert root is None
                root = node
            stack.append(node)
        elif kind == 0x103:
            assert stack and stack[-1].tag == strings[struct.unpack_from('<I', data, 20)[0]]
            stack.pop()
        offset += size
    assert root is not None and not stack
    return root


def launchers(root):
    app = root.find('application')
    result = []
    for node in app:
        if node.tag not in ('activity', 'activity-alias'):
            continue
        for intent in node.findall('intent-filter'):
            actions = [n.get(A+'name') for n in intent.findall('action')]
            categories = [n.get(A+'name') for n in intent.findall('category')]
            if 'android.intent.action.MAIN' in actions and 'android.intent.category.LAUNCHER' in categories:
                result.append({'name': node.get(A+'name'), 'label': node.get(A+'label'),
                               'enabled': node.get(A+'enabled', 'true') != 'false' and app.get(A+'enabled', 'true') != 'false'})
    return result


def assert_single_launcher(blob):
    root = parse(blob)
    assert root.get('package') == 'com.sohu.inputmethod.sogou.enhanced'
    active = [n for n in launchers(root) if n['enabled']]
    assert len(active) == 1, active
    assert active[0]['name'] == 'com.sohu.inputmethod.sogou.SogouIMELauncher', active
    assert active[0]['label'] == '搜狗输入法·增强版', active
    app = root.find('application')
    assert not any(n.get(A+'name', '').endswith('.LauncherAlias') for n in app)
    settings = [n for n in app.findall('activity') if n.get(A+'name') == 'com.sogouenhance.SettingsActivity']
    assert len(settings) == 1 and settings[0].get(A+'exported') == 'false'
    return active
