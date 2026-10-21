"""Export only the exact tested A 1.2.1; keep existing B delivery unchanged."""
from pathlib import Path
import hashlib
import json
import shutil
import tarfile
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT/'work/enhancer'
EVIDENCE = BASE/'a-repair'
OUT = ROOT/'outputs/2026-10-21-A-1.2.1'


def xml_nodes(name):
    return list(ET.parse(EVIDENCE/name).iter('node'))


def preferences(name):
    with tarfile.open(EVIDENCE/name) as archive:
        member = next(x for x in archive.getmembers() if x.name.endswith('/settings.xml'))
        return {x.get('name'): x.get('value', x.text)
                for x in ET.fromstring(archive.extractfile(member).read())}


def main():
    module = json.loads((BASE/'build/modules.json').read_text(encoding='utf-8'))['a']
    assert module['version'] == '1.2.1'
    assert (EVIDENCE/'installed-sha256.txt').read_text(encoding='utf-8-sig').split()[0] == module['sha256']
    assert preferences('module-data-before.tgz') == preferences('module-data-after.tgz')
    assert (EVIDENCE/'default-ime-before.txt').read_bytes() == (EVIDENCE/'default-ime-after.txt').read_bytes()
    assert (EVIDENCE/'protected-paths-before.txt').read_bytes() == (EVIDENCE/'official-path-after.txt').read_bytes()
    assert any(n.get('package') == 'com.android.settings' for n in xml_nodes('system-ime-settings.xml'))
    assert any('打开官方搜狗输入法' == n.get('text') for n in xml_nodes('reopen-module-home.xml'))
    assert any(n.get('package') == 'com.sohu.inputmethod.sogou' for n in xml_nodes('official-home-final.xml'))
    assert any(n.get('package') == 'com.sogouenhance' for n in xml_nodes('official-to-module-final.xml'))
    assert any(n.get('text') == '你好' for n in xml_nodes('chinese-committed.xml'))
    log = (EVIDENCE/'official-process.log').read_text(encoding='utf-8-sig')
    hooks = sum('[SogouEnhance] 已挂钩' in line for line in log.splitlines())
    assert hooks == 27
    # This change adds an Activity; every original class except the existing version-adapted HookEntry stays intact.
    original = list((BASE/'baseline-apk/smali').rglob('*.smali'))
    preserved = [p for p in original if p.name != 'HookEntry.smali']
    assert all(p.read_bytes() == (BASE/'module-a/smali'/p.relative_to(BASE/'baseline-apk/smali')).read_bytes()
               for p in preserved)
    assets = []
    for name, source, digest in [
        ('方案A/搜狗输入法-20.17.0-官方.apk', BASE/'official/SogouInput_20.17.0_android_sweb.apk',
         '3eb2612040fd7daefb7e92b9de5c1a715b03f272b644e0664948742df1c7a416'),
        ('方案A/搜狗增强模块-1.2.1-入口修缮版.apk', ROOT/module['apk'], module['sha256'])]:
        assert hashlib.sha256(source.read_bytes()).hexdigest() == digest
        with zipfile.ZipFile(source) as archive:
            assert archive.testzip() is None
        dest = OUT/name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)
        assert hashlib.sha256(dest.read_bytes()).hexdigest() == digest
        assets.append({'file': name, 'sha256': digest, 'size': dest.stat().st_size})
    assert len(list((OUT/'方案A').glob('*.apk'))) == 2
    evidence = OUT/'evidence'
    evidence.mkdir(exist_ok=True)
    for name in ['module-home-final.png', 'official-home-final.png', 'official-settings.png',
                 'settings-restored.png', 'chinese-candidates.png', 'chinese-committed.png',
                 'official-process.log', 'installed-version.txt']:
        shutil.copy2(EVIDENCE/name, evidence/name)
    report = {'date': '2026-10-21', 'version': 'A 1.2.1', 'assets': assets,
              'installed_module_matches_delivery': True, 'original_hooks_registered': hooks,
              'unchanged_original_smali_classes_except_adapted_entry': len(preserved),
              'verified': ['module cold launch', 'official homepage button and cold launch',
                           'enhancement settings button', 'system input settings button',
                           'reopen launcher clears previous settings page',
                           'official settings -> standalone module settings',
                           'physical nihao taps -> Chinese candidate -> committed 你好',
                           'native bottom visible and right button opens clipboard',
                           'module preferences preserved', 'default input method preserved',
                           'official install path unchanged'],
              'original_default_ime': (EVIDENCE/'default-ime-before.txt').read_text(encoding='utf-8-sig').strip(),
              'B_and_xiaomi': 'No install, uninstall or data clearing operations performed',
              'not_fully_verified': ['reported both old icons opening module page not reproduced',
                                    'full original enhancement boundary cases', 'voice and full login',
                                    'skin coverage matrix', 'long-duration stability'],
              'skin_unlock_added': False}
    (OUT/'测试记录.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    (OUT/'SHA256SUMS.txt').write_text(''.join(a['sha256']+'  '+a['file']+'\n' for a in assets), encoding='utf-8')
    (OUT/'使用说明.md').write_text('''# 方案 A：入口修缮版 1.2.1

文件夹中仍为两个 APK：官方搜狗 20.17.0（2620）＋独立增强模块 1.2.1。
已有官方搜狗无需卸载重装；覆盖安装本模块即可保留设置。

桌面“搜狗输入法”进入官方主页；“搜狗增强·方案A”进入配套模块首页。
模块首页提供打开官方搜狗、增强功能设置、系统输入法设置三个入口。
再次打开模块桌面入口会返回首页，不继续停留在上次的增强设置页。
官方搜狗设置中的“模块设置”仍直接进入原增强开关页。

LSPosed 作用域只选官方普通版搜狗，不给方案 B 或小米版重复加载本模块。
实际部署已覆盖更新 A 模块，没有卸载官方搜狗，保留全部模块开关。
默认输入法保持本轮测试前用户选择的官方普通版；B 与小米版未修改。

已验证：首页按钮、系统设置、任务栈重开、官方设置到模块的跳转、中文候选和“你好”上屏、
底栏显示与右键打开剪贴板、27 条原增强 hook 注册、安装文件哈希一致。
原先“两图标均进入模块页”的现象未直接复现，不能将入口区分改进说成已证明修复其根因。
完整原功能边界、语音登录、长期稳定性及完整换肤矩阵仍未完成验收。
未加入付费皮肤解锁。B 继续使用 ../2026-10-21-skin-1.2.0/方案B/ 中已验证的单 APK。

官方包保留官方签名，模块使用原测试签名。哈希见 SHA256SUMS.txt。
新增代码和说明由 AI 修改；原软件和工具链为既有组件。
''', encoding='utf-8')
    print('Exported A 1.2.1: 2 APKs, installed hash matched, 27 hooks, preferences/default preserved.')


if __name__ == '__main__':
    main()
