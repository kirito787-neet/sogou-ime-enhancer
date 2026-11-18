"""Build the baseline-preserving enhanced module. Run from any directory."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import zipfile
import argparse

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'work/enhancer'
JAVA = ROOT / 'work/tools/jdk/jdk-21.0.12.1+1/bin/java.exe'
JAVAC = JAVA.with_name('javac.exe')
TMP = BASE / 'tmp'


def run(args):
    subprocess.run([str(a) for a in args], cwd=ROOT, check=True)


def java(*args):
    run([JAVA, '-Djava.io.tmpdir=' + str(TMP), '-Duser.home=' + str(TMP), *args])


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def allow_provider_retry(project):
    path = project/'smali/com/sogouenhance/Prefs.smali'
    text = path.read_text(encoding='utf-8').replace(
        '.field private static sProviderBroken:Z', '.field private static sProviderRetryAt:J')
    text = text.replace('''    sget-boolean v0, Lcom/sogouenhance/Prefs;->sProviderBroken:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_0''', '''    const/4 v1, 0x0
    invoke-static {}, Landroid/os/SystemClock;->elapsedRealtime()J
    move-result-wide v2
    sget-wide v4, Lcom/sogouenhance/Prefs;->sProviderRetryAt:J
    cmp-long v0, v2, v4
    if-gez v0, :cond_0''')
    text = text.replace('''    const/4 p0, 0x1

    sput-boolean p0, Lcom/sogouenhance/Prefs;->sProviderBroken:Z''',
                        '''    invoke-static {}, Landroid/os/SystemClock;->elapsedRealtime()J
    move-result-wide v2
    const-wide/16 v4, 0x7d0
    add-long/2addr v2, v4
    sput-wide v2, Lcom/sogouenhance/Prefs;->sProviderRetryAt:J''')
    if 'sProviderBroken' in text:
        raise ValueError('Unable to update the baseline preference provider retry')
    path.write_text(text, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--variant', choices=('a', 'b', 'both'), default='both')
    options = parser.parse_args()
    for folder in ('tmp', 'classes', 'stubs', 'dex', 'build'):
        (BASE / folder).mkdir(parents=True, exist_ok=True)
    if not (BASE/'baseline-apk/AndroidManifest.xml').exists():
        java('-jar', ROOT/'work/tools/apktool-fast.jar', 'd', '-o', BASE/'baseline-apk',
             '-p', ROOT/'work/framework',
             ROOT/'搜狗输入法/搜狗输入法-20.16.0(2610)/搜狗输入法增强模块.apk')
    stubs = ROOT / 'work/ads/mod/stubs'
    run([JAVAC, '-encoding', 'UTF-8', '-d', BASE/'stubs', *stubs.rglob('*.java')])
    stub_archive = TMP/'xposed-stubs.jar'
    with zipfile.ZipFile(stub_archive, 'w') as archive:
        for stub in sorted((BASE/'stubs').rglob('*.class')):
            archive.write(stub, stub.relative_to(BASE/'stubs').as_posix())
    run([JAVAC, '-source', '8', '-target', '8', '-encoding', 'UTF-8', '-implicit:none',
         '-sourcepath', BASE/'src', '-cp', BASE/'stubs', '-d', BASE/'classes',
         *(BASE/'src').rglob('*.java')])
    java('-cp', ROOT/'work/tools/r8.jar', 'com.android.tools.r8.D8', '--release',
         '--min-api', '24', '--lib', stub_archive, '--no-desugaring',
         '--output', BASE/'dex', *(BASE/'classes').rglob('*.class'))
    report_path = BASE/'build/modules.json'
    reports = json.loads(report_path.read_text(encoding='utf-8')) if report_path.exists() else {}
    variants = ('a', 'b') if options.variant == 'both' else (options.variant,)
    for variant in variants:
        project = BASE / ('module-' + variant)
        shutil.copytree(BASE/'baseline-apk', project, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns('build', 'original'))
        # Exactly two known 2610 -> 2620 obfuscated method renames; keep all baseline features.
        hook = project/'smali/com/sogouenhance/HookEntry.smali'
        text = hook.read_text(encoding='utf-8')
        assert text.count('const-string v1, "Kb"') == 1
        assert text.count('const-string v1, "dj"') == 1
        text = text.replace('const-string v1, "Kb"', 'const-string v1, "Jb"')
        text = text.replace('const-string v1, "dj"', 'const-string v1, "bj"')
        text = text.replace('"com.sogou.clipboard.repository.utils.i"',
                            '"com.sogou.clipboard.repository.utils.k"')
        text = text.replace('"com.sogou.imskit.feature.settings.impl.p0$a"',
                            '"com.sogou.imskit.feature.settings.impl.u0$a"')
        text = text.replace('const-string v3, "p4"', 'const-string v3, "v4"')
        text = text.replace('const-string v2, "cb"', 'const-string v2, "bb"')
        if variant == 'b':
            # Host settings are declared and copied into the single product APK by package_b.py.
            start = text.index('.method private openModuleSettings()V')
            end = text.index('.end method', start) + len('.end method')
            text = text[:start] + '''.method private openModuleSettings()V
    .locals 4
    :try_start
    invoke-static {}, Landroid/app/ActivityThread;->currentApplication()Landroid/app/Application;
    move-result-object v0
    if-eqz v0, :done
    new-instance v1, Landroid/content/Intent;
    invoke-direct {v1}, Landroid/content/Intent;-><init>()V
    const-string v2, "com.sohu.inputmethod.sogou.enhanced"
    const-string v3, "com.sogouenhance.SettingsActivity"
    invoke-virtual {v1, v2, v3}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;
    const v2, 0x10000000
    invoke-virtual {v1, v2}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;
    invoke-virtual {v0, v1}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V
    :try_end
    .catch Ljava/lang/Throwable; {:try_start .. :try_end} :failure
    :done
    return-void
    :failure
    move-exception v0
    invoke-static {v0}, Lde/robv/android/xposed/XposedBridge;->log(Ljava/lang/Throwable;)V
    return-void
.end method''' + text[end:]
        hook.write_text(text, encoding='utf-8')
        if variant == 'b':
            hook.write_text(hook.read_text(encoding='utf-8').replace(
                '"com.sohu.inputmethod.sogou"', '"com.sohu.inputmethod.sogou.enhanced"').replace(
                '"\\u6a21\\u5757\\u8bbe\\u7f6e"', '"增强设置"'), encoding='utf-8')
            settings_path = project/'smali/com/sogouenhance/SettingsActivity.smali'
            settings = settings_path.read_text(encoding='utf-8')
            # A single embedded app has no standalone module icon to hide or re-enable.
            start = settings.index('    .line 108\n')
            end = settings.index('    .line 120\n', start)
            assert '"hide_launcher_icon"' in settings[start:end]
            # The removed block also defined v2 = the "其它" card color; later code still reads it.
            settings = settings[:start] + '    .line 108\n    const v2, -0x83786c\n\n' + settings[end:]
            start = settings.index('.method private applyLauncherIconVisibility()V')
            end = settings.index('.end method', start) + len('.end method')
            settings = settings[:start] + '''.method private applyLauncherIconVisibility()V
    .locals 0
    return-void
.end method''' + settings[end:]
            settings = settings.replace('"\\u641c\\u72d7\\u8f93\\u5165\\u6cd5\\u589e\\u5f3a\\u6a21\\u5757"',
                                        '"增强功能设置"')
            settings_path.write_text(settings, encoding='utf-8')
            for name in ('Prefs', 'PrefProvider'):
                path = project/f'smali/com/sogouenhance/{name}.smali'
                value = path.read_text(encoding='utf-8').replace('com.sogouenhance.prefs',
                                        'com.sohu.inputmethod.sogou.enhanced.enhance.prefs')
                # Do not read standalone module preferences when embedded.
                value = value.replace('const-string v8, "com.sogouenhance"',
                                      'const-string v8, "com.sohu.inputmethod.sogou"')
                if name == 'Prefs':
                    start = value.index('.method private static fromXSharedPreferences(')
                    end = value.index('.end method', start) + len('.end method')
                    value = value[:start] + '''.method private static fromXSharedPreferences(Ljava/lang/String;)Ljava/lang/Boolean;
    .locals 1
    const/4 v0, 0x0
    return-object v0
.end method''' + value[end:]
                path.write_text(value, encoding='utf-8')
        manifest = project/'AndroidManifest.xml'
        text = manifest.read_text(encoding='utf-8').replace('android:debuggable="true"', 'android:debuggable="false"')
        text = text.replace('android:value="搜狗输入法增强模块"',
                            'android:value="保留原增强功能，新增 HyperOS/MIUI 全面屏键盘优化适配"')
        if variant == 'a':
            shutil.copytree(BASE/'companion-smali', project/'smali', dirs_exist_ok=True)
            allow_provider_retry(project)
            scope = project/'res/values/arrays.xml'
            scope.write_text(scope.read_text(encoding='utf-8').replace(
                '<item>com.sohu.inputmethod.sogou</item>',
                '<item>com.sohu.inputmethod.sogou</item>\n        <item>com.android.systemui</item>'),
                encoding='utf-8')
            text = text.replace('    <application ',
                                '    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>\n'
                                '    <application ', 1)
            text = text.replace('android:name=".PrefProvider"/>',
                                '''android:name=".PrefProvider">
            <grant-uri-permission android:path="/visibility"/>
        </provider>
        <receiver android:name=".PreferenceAccessReceiver" android:exported="false">
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED"/>
                <action android:name="android.intent.action.MY_PACKAGE_REPLACED"/>
            </intent-filter>
        </receiver>''', 1)
            text = text.replace('android:targetActivity=".SettingsActivity"',
                                'android:targetActivity=".AHomeActivity"')
            text = text.replace('        <activity-alias ',
                                '        <activity android:name=".AHomeActivity" android:exported="true" android:launchMode="singleTask" android:theme="@style/AppTheme"/>\n        <activity-alias ', 1)
            labels = project/'res/values/strings.xml'
            labels.write_text(labels.read_text(encoding='utf-8').replace(
                '<string name="app_name">搜狗输入法增强模块</string>',
                '<string name="app_name">搜狗增强·方案A</string>'), encoding='utf-8')
        manifest.write_text(text, encoding='utf-8')
        config = project/'apktool.yml'
        code, version = (11, '1.3.2') if variant == 'a' else (10, '1.2.6')
        config.write_text(config.read_text(encoding='utf-8').replace('versionCode: 1', f'versionCode: {code}')
                          .replace('versionName: 1.0', f'versionName: {version}'), encoding='utf-8')
        entries = ['com.sogouenhance.HookEntry', 'com.sogouenhance.bottom.BottomHook']
        if variant == 'a':
            entries.append('com.sogouenhance.bottom.GestureHandleHook')
        else:
            entries.insert(0, 'com.sogouenhance.bottom.EmbeddedGuard')
        (project/'assets/xposed_init').write_text('\n'.join(entries)+'\n', encoding='utf-8')
        unsigned = BASE/f'build/enhancer-{variant}-base.apk'
        java('-jar', ROOT/'work/tools/apktool-fast.jar', 'b', project, '-p', ROOT/'work/framework',
             '--aapt', ROOT/'work/compat/aapt2.exe', '-o', unsigned)
        packed = BASE/f'build/enhancer-{variant}.apk'
        with zipfile.ZipFile(unsigned) as source, zipfile.ZipFile(packed, 'w') as dest:
            for member in source.infolist():
                if member.filename == 'classes3.dex': raise ValueError('unexpected third baseline DEX')
                dest.writestr(member, source.read(member.filename))
            dest.writestr('classes3.dex', (BASE/'dex/classes.dex').read_bytes(), zipfile.ZIP_DEFLATED)
        signed_dir = BASE/f'build/signed-{variant}-{sha(packed)[:12]}'
        if not signed_dir.exists():
            java('-jar', ROOT/'work/tools/signer.jar', '-a', packed, '-o', signed_dir)
        signed = next(signed_dir.glob('*.apk'))
        reports[variant] = {'apk': str(signed.relative_to(ROOT)), 'sha256': sha(signed),
                            'version': version,
                            'baseline': 'com.sogouenhance 1.0', 'xposed_entries': entries,
                            'runtime': 'pending'}
    (BASE/'build/modules.json').write_text(json.dumps(reports, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
