"""Export the exact tested 1.2.3 artifacts; never rebuild during delivery."""
from pathlib import Path
import hashlib
from io import BytesIO
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT/'work/enhancer'
OUT = ROOT/'outputs/2026-10-21-1.2.3'


def main():
    modules = json.loads((BASE/'build/modules.json').read_text(encoding='utf-8'))
    single = json.loads((BASE/'build/single.json').read_text(encoding='utf-8'))
    assert modules['a']['version'] == '1.2.3', 'Use the matching version exporter.'
    assert modules['b']['version'] == '1.2.3'
    assert single['enhancement_version'] == '1.2.3'
    sources = {
        '方案A/搜狗输入法-20.17.0-官方.apk': BASE/'official/SogouInput_20.17.0_android_sweb.apk',
        '方案A/搜狗增强模块-1.2.3-底栏跟随皮肤版.apk': ROOT/modules['a']['apk'],
        '方案B/搜狗输入法-20.17.0-内置增强1.2.3-单APK.apk': ROOT/single['apk'],
    }
    with zipfile.ZipFile(ROOT/single['apk']) as product:
        assert product.testzip() is None
        embedded = [n for n in product.namelist() if n.startswith('assets/npatch/modules/')]
        assert embedded == ['assets/npatch/modules/com.sogouenhance.apk']
        assert hashlib.sha256(product.read(embedded[0])).hexdigest() == modules['b']['sha256']
        config = json.loads(product.read('assets/npatch/config.json'))
        assert config['newPackage'] == 'com.sohu.inputmethod.sogou.enhanced'
        assert config['useManager'] is False
        with zipfile.ZipFile(BytesIO(product.read('assets/npatch/origin.apk'))) as inside, \
                zipfile.ZipFile(sources['方案A/搜狗输入法-20.17.0-官方.apk']) as official:
            preserved = [n for n in official.namelist() if n == 'resources.arsc' or n.endswith('.so')]
            assert preserved
            assert all(inside.read(n) == official.read(n) for n in preserved)
            dexs = [n for n in inside.namelist() if n.startswith('classes') and n.endswith('.dex')]
            assert 'classes8.dex' in dexs, dexs
    checksums, assets = [], []
    for relative, source in sources.items():
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if relative.startswith('方案A/搜狗增强'):
            assert digest == modules['a']['sha256']
        if relative.startswith('方案B/'):
            assert digest == single['sha256']
        dest = OUT/relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)
        assert hashlib.sha256(dest.read_bytes()).hexdigest() == digest
        checksums.append(digest+'  '+relative)
        assets.append({'file': relative, 'sha256': digest, 'size': dest.stat().st_size})
    assert len(list((OUT/'方案A').glob('*.apk'))) == 2
    assert len(list((OUT/'方案B').glob('*.apk'))) == 1
    (OUT/'SHA256SUMS.txt').write_text('\n'.join(checksums)+'\n', encoding='utf-8')
    report = {'date': '2026-10-21', 'version': '1.2.3', 'assets': assets,
              'module_a_sha256': modules['a']['sha256'], 'module_b_sha256': modules['b']['sha256'],
              'single_apk_sha256': single['sha256'], 'embedded_module_matches_b': True,
              'settings_dex': single['settings_dex'],
              'fixed': [
                  'A: bottom bar now follows the Sogou skin (was frozen on the first palette)',
                  'B: settings page opens without java.lang.VerifyError'],
              'verified_on_device': [
                  'A dark skin: SKIN bg=#ff282828, bottom bar pixels (40,40,40) match keyboard',
                  'A light skin: SKIN bg=#fffaf9ff, bottom bar pixels (250,249,254) match keyboard',
                  'A skin switch in-session re-resolves: #ff282828 -> #ffefc8a7 -> #fffaf9ff',
                  'B keyboard shows native bottom bar recolored to the dark skin',
                  'B enhancement settings opens from the Sogou settings entry',
                  'B settings page renders all switch cards, no crash'],
              'not_verified': ['skin coverage matrix across all skin categories',
                               'long-duration stability', 'paid skin unlock (not added)']}
    (OUT/'测试记录.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    (OUT/'使用说明.md').write_text('''# 1.2.3

## 方案 A（两个 APK）
官方搜狗 20.17.0（2620）＋ 独立增强模块 1.2.3。
已有官方搜狗无需卸载；覆盖安装本模块即可，模块开关设置保留。
LSPosed 作用域只勾官方普通版搜狗，不要勾方案 B 或小米版。

## 方案 B（一个 APK）
单 APK，包名 com.sohu.inputmethod.sogou.enhanced，桌面只有一个“搜狗输入法·增强版”图标。
不需要装模块、不需要 LSPosed 作用域。与官方版共存。

## 本版修复
1. 底栏不随皮肤变色：A 模块的刷新任务原先投递到尚未 attach 的窗口视图上，
   一旦投递失败就永久卡住，之后所有刷新被入口守卫吞掉，底栏停在第一次的颜色。
   现改为投递到主线程 Handler，并加 3 秒超时兜底，投递失败也能自愈。
2. 方案 B 进不去模块设置：打包时删除“隐藏桌面图标”卡片，
   连带删掉了后面还要用的颜色常量，导致 SettingsActivity 校验失败（VerifyError）。
   现改为删除后回填该常量。

## 实测
- A 深色皮肤底栏与键盘同为 (40,40,40)；浅色皮肤同为 (250,249,254)。
- A 会话内换肤：#ff282828 → #ffefc8a7 → #fffaf9ff，底栏即时跟随。
- B 底栏同样跟随皮肤；增强设置在搜狗设置里点“增强设置”可正常打开。

未做：付费皮肤解锁；全部皮肤类别的覆盖矩阵；长时间稳定性。

官方包保留官方签名，模块与方案 B 使用原测试签名。哈希见 SHA256SUMS.txt。
新增代码和说明由 AI 修改；原软件和工具链为既有组件。
''', encoding='utf-8')
    print('Exported 1.2.3: A(2 apks) + B(1 apk), hashes matched.')


if __name__ == '__main__':
    main()
