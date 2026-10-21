"""Export the exact tested artifacts; never rebuild during delivery."""
from pathlib import Path
import hashlib
from io import BytesIO
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT/'work/enhancer'
OUT = ROOT/'outputs/2026-10-21'


def main():
    modules = json.loads((BASE/'build/modules.json').read_text(encoding='utf-8'))
    single = json.loads((BASE/'build/single.json').read_text(encoding='utf-8'))
    sources = {
        '方案A/搜狗输入法-20.17.0-官方.apk': BASE/'official/SogouInput_20.17.0_android_sweb.apk',
        '方案A/搜狗增强模块-1.1.0-测试版.apk': ROOT/modules['a']['apk'],
        '方案B/搜狗输入法-20.17.0-内置增强-共存测试版.apk': ROOT/single['apk'],
    }
    with zipfile.ZipFile(ROOT/single['apk']) as product:
        assert product.testzip() is None
        embedded = [n for n in product.namelist() if n.startswith('assets/npatch/modules/')]
        assert embedded == ['assets/npatch/modules/com.sogouenhance.apk']
        assert hashlib.sha256(product.read(embedded[0])).hexdigest() == modules['b']['sha256']
        config = json.loads(product.read('assets/npatch/config.json'))
        assert config['newPackage'] == 'com.sohu.inputmethod.sogou.enhanced'
        assert config['useManager'] is False
        with zipfile.ZipFile(BytesIO(product.read('assets/npatch/origin.apk'))) as original_inside, \
                zipfile.ZipFile(sources['方案A/搜狗输入法-20.17.0-官方.apk']) as official:
            preserved = [n for n in official.namelist() if n == 'resources.arsc' or n.endswith('.so')]
            assert preserved
            assert all(original_inside.read(n) == official.read(n) for n in preserved)
    successful = sum('[SogouEnhance] 已挂钩' in line
                     for line in (BASE/'device-a/process.txt').read_text(encoding='utf-8', errors='replace').splitlines())
    assert successful == 27
    checksums = []
    assets = []
    for relative, source in sources.items():
        dest = OUT/relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if relative.startswith('方案A/搜狗增强'): assert digest == modules['a']['sha256']
        if relative.startswith('方案B/'): assert digest == single['sha256']
        shutil.copy2(source, dest)
        assert hashlib.sha256(dest.read_bytes()).hexdigest() == digest
        checksums.append(digest+'  '+relative)
        assets.append({'file': relative, 'sha256': digest, 'size': dest.stat().st_size})
    assert len(list((OUT/'方案A').glob('*.apk'))) == 2
    assert len(list((OUT/'方案B').glob('*.apk'))) == 1
    (OUT/'SHA256SUMS.txt').write_text('\n'.join(checksums)+'\n', encoding='utf-8')
    report = {'date': '2026-10-21', 'stage': 'smoke-tested experimental build',
              'device': 'Redmi K90 Pro Max, Android 16, HyperOS, 4KB pages',
              'assets': assets, 'A_baseline_hooks_registered': successful,
              'B_embedded_modules': embedded, 'B_external_manager': config['useManager'],
              'B_native_and_resources_preserved_members': len(preserved),
              'verified_runtime': ['A keyboard and native bottom visible',
                    'B external input-method modules disabled and soft-rebooted',
                    'B nihao physical key taps, candidate selection, committed 你好',
                    'B native bottom right button opens clipboard',
                    'B integrated settings and provider preferences read/write',
                    'B login activity resources load without old renamed-package exception'],
              'not_fully_verified': ['bottom-left complete IME switching behavior',
                    'voice input', 'account authentication', 'long-duration behavior',
                    'all baseline feature boundary cases', 'non-root device', '16KB page device'],
              'device_final_default_ime': 'com.sohu.inputmethod.sogou.xiaomi/.SogouIME',
              'github_published': False}
    (OUT/'测试记录.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    (OUT/'evidence').mkdir(exist_ok=True)
    for name, source in {'A-底栏.png': BASE/'device-a/final.png',
                         'B-中文候选.png': BASE/'device-b/input.png',
                         'B-底栏剪贴板.png': BASE/'device-b/clipboard.png',
                         'B-内嵌设置.png': BASE/'device-b/settings-ready.png',
                         'B-登录页.png': BASE/'device-b/login.png'}.items():
        shutil.copy2(source, OUT/'evidence'/name)
    (OUT/'使用说明.md').write_text('''# 搜狗输入法增强测试版（2026-10-21）

方案 A 文件夹中有两个 APK：官方 20.17.0（2620）＋增强模块 1.1.0。
安装两包，在 LSPosed 中启用增强模块并仅勾选普通版搜狗，重启输入法或软重启。
先打开一次增强模块设置页；如果系统拦截模块后台启动，需允许其自启动，保证开关读取。
不要同时给普通版勾选旧去广告模块或旧底栏模块，以免重复 hook。

方案 B 文件夹中只有一个 APK，已经内置完整增强模块与设置页，独立包名可与官方普通版共存。
安装后到系统输入法设置启用“搜狗输入法·增强版”，无需另装本项目模块或给它勾选 LSPosed。
增强开关在“搜狗增强设置”桌面入口；也保留搜狗设置中的模块设置入口。
官方版的数据和账号不会自动迁移到这个新包。

两方案都保留原模块的剪贴板、分词高亮、广告/福利/开屏处理、AI 开关等能力。
本轮修正 20.17 的方法改名，并新增 MIUI/HyperOS 原生底栏适配。
当前设备的底栏根据系统配置显示左右两个按钮。

已实测：A 原增强 hook 加载与底栏；B 在外部增强模块停用后仍可真实中文输入、
显示底栏、打开剪贴板、操作内嵌设置、打开登录页。详见测试记录.json 和 evidence/。
底栏左键完整切换、语音、完整账号登录、长期稳定性、无 root 设备、16KB 页设备尚未完成验证。
因此为测试版，不能把这次冒烟测试当成所有场景的最终验收。

官方包保持官方签名；增强模块与方案 B 使用非官方测试签名。
当前官网版本与来源：https://shouji.sogou.com/index.php 。文件校验见 SHA256SUMS.txt。
本轮新增代码和文档由 AI 生成/修改，原软件与第三方组件不是 AI 原创。
本轮未创建 GitHub 仓库或发布 Release。
''', encoding='utf-8')
    print(json.dumps({'output': str(OUT), 'assets': assets, 'preserved_native_and_resources': len(preserved)}, ensure_ascii=False, indent=2))


if __name__ == '__main__': main()
