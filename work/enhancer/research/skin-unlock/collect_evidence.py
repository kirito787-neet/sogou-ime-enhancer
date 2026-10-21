"""Read-only comparison of selected payment methods; never patches or runs APKs."""
from pathlib import Path
import hashlib
import json
import re

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
METHOD = re.compile(r'(?m)^\.method .*\n[\s\S]*?^\.end method')


def methods(root, relative, names):
    found = list(root.glob('smali*/'+relative))
    if not found:
        return []
    assert len(found) == 1
    path = found[0]
    text = path.read_text(encoding='utf-8')
    return [{'path': str(path.relative_to(ROOT)), 'line': text.count('\n', 0, m.start())+1,
             'signature': m.group().splitlines()[0], 'body': m.group()}
            for m in METHOD.finditer(text)
            if any(' '+name+'(' in m.group().splitlines()[0] for name in names)]


def main():
    target = ROOT/'搜狗输入法/搜狗输入法小米版-10.32.21.202608051602.apk'
    entries = []
    for relative, names in [
        ('com/sogou/bu/basic/pay/ProductWithPrice.smali', ['getPrice', 'getPayStatus']),
        ('com/sogou/inputmethod/lib_pay/SogouIMEPay.smali', ['x']),
        ('com/sogou/pay/sdk/PayManager.smali', ['payWithSogouPayOrder'])]:
        before = methods(BASE/'origin', relative, names)
        after = methods(BASE/'apk', relative, names)
        for a in after:
            b = next(x for x in before if x['signature'] == a['signature'])
            # Remove disassembler labels, source lines and whitespace only for comparison.
            def normalize(body):
                return re.sub(r'\s+', '', re.sub(r'(?m)^\s*\.line .*$', '', body))
            entries.append({'changed': normalize(a['body']) != normalize(b['body']),
                            'before': b, 'after': a})
    assert len(entries) == 5
    assert sum(e['changed'] for e in entries) == 4
    standard = methods(ROOT/'work/standard', 'com/sogou/bu/basic/pay/ProductWithPrice.smali',
                       ['getPrice', 'getPayStatus'])
    assert len(standard) == 2
    for missing in ['com/sogou/inputmethod/lib_pay/SogouIMEPay.smali', 'com/sogou/pay/sdk/PayManager.smali']:
        assert not list((ROOT/'work/standard').glob('smali*/'+missing))
    result = {'authority': 'local static APK/smali comparison, not REA retained evidence',
              'rea_android_blocker': 'REA_JADX_MCP_JAR not configured',
              'target': str(target.relative_to(ROOT)),
              'sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
              'embedded_origin_sha256': hashlib.sha256((BASE/'apk/assets/origin665.apk').read_bytes()).hexdigest(),
              'selected_method_comparisons': entries, 'standard_product_methods': standard,
              'runtime_verified': False, 'device_modified': False,
              'limitation': 'Embedded origin is an untrusted comparison baseline, not independently authenticated as official.'}
    (BASE/'evidence.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('Verified 4 changed methods and 1 unchanged overload; recorded standard-version differences.')


if __name__ == '__main__':
    main()
