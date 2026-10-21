"""Export the exact 1.2.0 skin-test artifacts with current evidence."""
from pathlib import Path
from io import BytesIO
import hashlib
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT/'work/enhancer'
OUT = ROOT/'outputs/2026-10-21-skin-1.2.0'


def main():
    modules = json.loads((BASE/'build/modules.json').read_text(encoding='utf-8'))
    single = json.loads((BASE/'build/single.json').read_text(encoding='utf-8'))
    sources = {
        '方案A/搜狗输入法-20.17.0-官方.apk': BASE/'official/SogouInput_20.17.0_android_sweb.apk',
        '方案A/搜狗增强模块-1.2.0-测试版.apk': ROOT/modules['a']['apk'],
        '方案B/搜狗输入法-20.17.0-内置增强1.2.0-共存测试版.apk': ROOT/single['apk'],
    }
    expected = [single['official_source_sha256'], modules['a']['sha256'], single['sha256']]
    with zipfile.ZipFile(ROOT/single['apk']) as product:
        assert product.testzip() is None
        embedded = [n for n in product.namelist() if n.startswith('assets/npatch/modules/')]
        assert embedded == ['assets/npatch/modules/com.sogouenhance.apk']
        assert hashlib.sha256(product.read(embedded[0])).hexdigest() == modules['b']['sha256']
        config = json.loads(product.read('assets/npatch/config.json'))
        assert config['useManager'] is False
        assert config['newPackage'] == 'com.sohu.inputmethod.sogou.enhanced'
        with zipfile.ZipFile(BytesIO(product.read('assets/npatch/origin.apk'))) as inner, \
                zipfile.ZipFile(next(iter(sources.values()))) as official:
            preserved = [n for n in official.namelist() if n == 'resources.arsc' or n.endswith('.so')]
            assert preserved and all(inner.read(n) == official.read(n) for n in preserved)
    assets = []
    for (relative, source), digest in zip(sources.items(), expected):
        assert hashlib.sha256(source.read_bytes()).hexdigest() == digest
        dest = OUT/relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)
        assert hashlib.sha256(dest.read_bytes()).hexdigest() == digest
        assets.append({'file': relative, 'sha256': digest, 'size': dest.stat().st_size})
    assert len(list((OUT/'方案A').glob('*.apk'))) == 2
    assert len(list((OUT/'方案B').glob('*.apk'))) == 1
    (OUT/'SHA256SUMS.txt').write_text(''.join(a['sha256']+'  '+a['file']+'\n' for a in assets), encoding='utf-8')
    evidence = OUT/'evidence'
    evidence.mkdir(exist_ok=True)
    for name in ['a-final.png', 'b-default-preview2.png', 'b-final.png', 'a-light.log',
                 'a-dark.log', 'skin-colors-final.log']:
        shutil.copy2(BASE/'skin-test'/name, evidence/name)
    report = {
        'date': '2026-10-21', 'enhancer_version': '1.2.0', 'stage': 'skin smoke-tested experimental build',
        'assets': assets, 'device': 'Redmi K90 Pro Max / Android16 / HyperOS / 4KB',
        'palette_behavior_checks_passed': 11,
        'A_current_skin': {'log_background': '#FFECECEC', 'screenshot_pixel_600_2470': '#FFECECEC'},
        'B_default_skin': {'log_background': '#FFF2F3F7', 'screenshot_pixel_600_2470': '#FFF2F3F7'},
        'B_restored_neon_skin': {'log_background': '#FFECECEC', 'screenshot_pixel_600_2470': '#FFECECEC'},
        'B_embedded_module_count': len(embedded), 'B_external_manager': config['useManager'],
        'preserved_native_and_resources_members': len(preserved),
        'deployment': 'Uninstalled/reinstalled only com.sogouenhance and com.sohu.inputmethod.sogou.enhanced; restored user data backup',
        'official_and_xiaomi_install_paths_unchanged': True,
        'final_default_ime': 'com.sohu.inputmethod.sogou.xiaomi/.SogouIME', 'final_night_mode': 'no',
        'not_fully_verified': ['A actual switch between distinct skins', 'dark and colored skin matrix for both variants',
                              'image/gradient/animation continuity', 'all original enhancement boundary cases',
                              'voice and full account login', 'non-root / 16KB devices', 'long-duration behavior'],
    }
    (OUT/'测试记录.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    (OUT/'使用说明.md').write_text('''# 搜狗增强 1.2.0 换肤适配测试版

方案 A：两个 APK，官方搜狗 20.17.0（2620）＋增强模块 1.2.0。
安装后在 LSPosed 启用增强模块，作用域只选官方普通版搜狗，软重启生效。
方案 B：只有一个 APK，内置完整增强模块及设置页，包名 com.sohu.inputmethod.sogou.enhanced。
可与官方普通版和小米版共存，不需要另装增强模块或设置外部 LSPosed 作用域。

1.2.0 移除错误的透明覆盖，读取当前皮肤底栏色与图标色，必要时叠为不透明背景，
并在弹出键盘、配置变化和搜狗原生配色更新后刷新。保留原模块的完整功能代码。
本轮已卸载重装旧 A 模块和 B 共存版，并恢复备份的设置、词库和皮肤数据。
官方普通版和小米版安装路径未变；未卸载小米版，未清除它的数据。

真机验证：A 当前皮肤底栏不透明；B 默认皮肤与霓虹皮肤切换时底栏颜色变化，
日志及截图像素一致。11 项配色行为检查通过。详见测试记录.json 和 evidence/。
A 实际换肤、两版深色和彩色皮肤矩阵、任意图片/渐变/动画连续延伸尚未完整验证。
此前 1.1.0 的功能测试记录在 ../2026-10-21/，不能替代新版本的完整回归。
语音、完整登录、长期稳定性、无 root、16KB 页设备仍待测试。

官方包保留官方签名；模块和 B 使用测试签名。校验见 SHA256SUMS.txt。
官网来源：https://shouji.sogou.com/index.php （2026-10-21 已核对版本）。
新增适配代码和文档由 AI 修改，原搜狗、原增强模块和第三方组件为既有软件。
''', encoding='utf-8')
    print(json.dumps({'output': str(OUT), 'assets': assets}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
