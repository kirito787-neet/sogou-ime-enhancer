> 原始文件：`交接1.txt`（UTF-16LE，已转 UTF-8 存档）

# 先读取交接文档，然后等我21日早上确定开始

> 先读取交接文档，然后等我21日早上确定开始
>
> User context
>
> Attachments:
> - 搜狗输入法项目交接文档.md: `./搜狗输入法项目交接文档.md`

<details><summary>2 previous messages</summary>

> 我先读取交接文档，了解当前进度和待办；读完后等你 21 日早上确认开始。
>
> <details><summary>Explored a file</summary>
>
> - Read `./搜狗输入法项目交接文档.md`
>
> </details>
</details>

已读完交接文档。根据文档，底栏与去广告路线已验证，增强模块合并、方案 A/B 构建及发布尚未完成，方案 B 形态待确定。

我会等待你在 **2026 年 10 月 21 日早上（香港时间）**明确确认开始，再继续操作。

> 我再次明确一下最终的产物，方案A.最新官方版搜狗输入法安装包和「增强模块」（新增全面屏键盘优化适配）。方案B.一个！注意是一个！自带「增强模块」（新增全面屏键盘优化适配）的最新版本输入法apk

<details><summary>1 previous message</summary>

> Stream error
>
> Reconnecting 5/5
> request timed out
</details>

明确，最终产物按你这次的定义：

- **方案 A：两个 APK**——最新官方版搜狗输入法 APK ＋ 新增「全面屏键盘优化适配」的增强模块 APK。
- **方案 B：只有一个 APK**——基于最新版本搜狗输入法，内置上述增强模块。ZIP 整合包、安装器、Zygisk 刷入包或额外安装模块，都不算满足方案 B。

交接文档中推荐的 B1/B2 不符合你的要求。文档记载的重签反篡改是方案 B 需要解决并实测验证的技术障碍；若最终做不到，我会明确说明，不能用其他形态替代并宣称完成。

> 开始启动项目继续未完成的工作

<details><summary>64 previous messages</summary>

> 我开始接续项目，先核对现有工程、模块和验证记录。方案 A 按两个 APK 推进；方案 B 严格按你要求的单个 APK 研究与验证，重点检查交接文档中的反篡改结论和现有实现。
>
> <details><summary>Ran a command</summary>
>
> - Ran `Get-Content -LiteralPath 'C:\Users\Kirito787\.codex\skills\auto-prompt\SKILL.md' -Raw; Get-Content -LiteralPath 'C:\Users\Kirito787\.codex\skills\auto-git-branch\SKILL.md' -Raw; Get-Content -LiteralPath 'C:\Users\Kirito787\.agents\skills\reverse-engineer-anything\SKILL.md' -Raw`
>
> </details>
>
> 这次会使用 auto-prompt、auto-git-branch 和 reverse-engineer-anything 技能整理任务、隔离改动并检查 APK。
>
> ```text
> 目标：续做搜狗增强项目，交付方案 A 的官方 APK＋增强模块 APK，
> 以及方案 B 内置同等增强功能的单个输入法 APK。
> 要求：保留原增强功能，新增全面屏键盘优化；先复核现有证据，
> 再实现、构建和验证，不以 ZIP、安装器或刷入包替代方案 B。
> 验收：记录版本、签名及校验值；通过可执行的构建检查，
> 并以真机结果确认底栏、按钮、去广告和启动稳定性。
> ```
>
> <details><summary>Ran 7 commands, called a tool</summary>
>
> - Ran `git rev-parse --is-inside-work-tree; git status --short; git branch --show-current; Get-Content AGENTS.md; Get-Content docs/agents/issue-tracker.md; Get-Content docs/agents/triage-labels.md; Get-Content docs/agents/domain.md; Get-ChildItem -Name`
>
> - Ran `rg -n 'sougou|搜狗|DSH' 'C:\Users\Kirito787\.codex\memories\MEMORY.md'`
>
> - Ran `git switch -c codex/sogou-enhancer-delivery; rg --files -g AGENTS.md -g GLOSSARY.md -g '*.md' -g '*.java' -g '*.sh' -g '*.mjs' -g '*.py' -g '*.xml' work/ads/mod work/wxime work/xposed work/tools docs/adr .scratch; Get-Content work/ads/mod/src/com/sogou/adfree/AdHook.java -Raw; Get-Content work/ads/mod/build.sh -Raw; Get-Content work/ads/mod/pack.mjs -Raw; Get-Content work/wxime/analysis-wetypehook-miui-bottom.md -Raw`
>
> MCP tool call
>
> rea.inspect_android_package
>
> ```json
> {
>   "path": "C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法\\搜狗输入法-20.16.0(2610)\\搜狗输入法增强模块.apk"
> }
> ```
>
> Error: {"error":{"code":"capability_unavailable","category":"unsupported_provider","message":"Set REA_JADX_MCP_JAR to the absolute path of a caller-supplied jadx-headless-mcp 0.7.1 JAR. REA does not download or install it.","retryable":false,"remediation":{"action":"Set REA_JADX_MCP_JAR to the absolute path of a caller-supplied jadx-headless-mcp 0.7.1 JAR. REA does not download or install it."},"details":{"provider_id":"jadx","operation":"inspect_android_package","reason":"Set REA_JADX_MCP_JAR to the absolute path of a caller-supplied jadx-headless-mcp 0.7.1 JAR. REA does not download or install it.","diagnostics":{"jar_configured":false,"failure_kind":"jar","failure_code":"not_configured"}}}}
>
> - Ran `git branch --show-current; git branch --list codex/sogou-enhancer-delivery; Get-Content work/ads/mod/src/com/sogou/adfree/AdHook.java -TotalCount 230; Get-Content work/ads/mod/apk/AndroidManifest.xml; Get-Content work/tools/device_probe.py -TotalCount 100; Get-ChildItem work/tools -Name; Get-ChildItem outputs -Name; Get-ChildItem work/ads/mod -Name; Get-Content 'C:\Users\Kirito787\.agents\skills\reverse-engineer-anything\references\connection-and-recovery.md' -TotalCount 100`
>
> - Ran `git switch codex/sogou-enhancer-delivery`
>
> - Ran `git switch -c codex/sogou-enhancer-delivery`
>
> - Ran `Get-Content work/ads/mod/NOTES.md -Raw; Get-Content outputs/candidate-validation.json -Raw; Get-ChildItem work/dsh -Name | Select-Object -Last 35; Get-ChildItem work/tools/jadx-ready/bin -Name; Get-ChildItem work/ads/mod/keep-signed -Name; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' devices -l; Get-Content work/wxime/jadx-embedded/sources/com/xposed/wetypehook/MainHook.java | Select-Object -Skip 320 -First 80; Get-Content work/wxime/jadx-embedded/sources/com/xposed/wetypehook/MainHook.java | Select-Object -Skip 455 -First 105`
>
> </details>
>
> 已切到独立分支。现有去广告源码比交接摘要更完整，包含福利、开屏等处理，我会保留这些功能再接入底栏。
>
> REA 的 Android 分析缺少所需的 JADX 插件，我会继续使用项目已有的本地 JADX。ADB 在沙箱内启动失败，接下来检查实际设备连接。
>
> <details><summary>Ran 13 commands, searched the web</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' devices -l`
>
> - Ran `Add-Type -AssemblyName System.IO.Compression.FileSystem; $baseline = [IO.Compression.ZipFile]::OpenRead((Resolve-Path '搜狗输入法/搜狗输入法-20.16.0(2610)/搜狗输入法增强模块.apk')); $baseline.Entries | Where-Object { $_.FullName -match 'xposed|classes.dex|Manifest' } | Select-Object FullName,Length; foreach($entry in $baseline.Entries | Where-Object { $_.FullName -match 'xposed_init|module.prop|scope.list' }) { $reader=[IO.StreamReader]::new($entry.Open()); $entry.FullName; $reader.ReadToEnd(); $reader.Dispose() }; $baseline.Dispose(); Get-Content work/ads/mod/stubs/de/robv/android/xposed/XC_MethodHook.java; Get-Content work/ads/mod/apk/apktool.yml; Get-Content work/dsh/sign_apk.py -TotalCount 90; Get-ChildItem work/compat -Name; Get-Content work/wxime/jadx-embedded/sources/miuiime/xc0.java -Raw; Get-Content work/wxime/jadx-embedded/sources/miuiime/yc0.java -Raw; rg -n 'case 17|case 21' work/wxime/jadx-embedded/sources/miuiime/n8.java`
>
> Searched the web for `搜狗输入法 Android 官方 下载 最新版 shouji.sogou.com`
>
> - Ran `$env:JAVA_HOME=(Resolve-Path 'work/tools/jdk/jdk-21.0.12.1+1').Path; & work/tools/jadx-ready/bin/jadx.bat -d work/enhancer/baseline-jadx --no-res '搜狗输入法/搜狗输入法-20.16.0(2610)/搜狗输入法增强模块.apk'; & work/tools/jdk/jdk-21.0.12.1+1/bin/java.exe -jar work/tools/signer.jar --help`
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'id; which su; su -c id; getprop ro.miui.support_miui_ime_bottom; settings get secure default_input_method; pm list packages | grep -E "sogou|xposed|lsp|npatch"'`
>
> Searched the web for `https://shouji.sogou.com/`
>
> - Ran `& work/tools/jdk/jdk-21.0.12.1+1/bin/java.exe -version; Get-Content work/tools/jadx-ready/bin/jadx.bat -TotalCount 50; Get-ChildItem work/enhancer -ErrorAction SilentlyContinue; Get-ChildItem work -Directory -Name; Get-Content work/wxime/jadx-embedded/sources/miuiime/n8.java | Select-Object -Skip 95 -First 65; rg -n 'sogouenhance|HookEntry|npatch|lspatch|setFirstInstallTime' work/ads work/dsh work/compat --glob '*.md' --glob '*.py' --glob '*.sh' --glob '*.mjs'`
>
> - Ran `$env:JAVA_HOME=(Resolve-Path 'work/tools/jdk/jdk-21.0.12.1+1').Path; & work/tools/jadx-ready/bin/jadx.bat -d work/enhancer/baseline-jadx --no-res '搜狗输入法/搜狗输入法-20.16.0(2610)/搜狗输入法增强模块.apk'; & work/tools/jdk/jdk-21.0.12.1+1/bin/java.exe -jar work/tools/signer.jar --help`
>
> - Ran `$response=Invoke-WebRequest -Uri 'https://shouji.sogou.com/' -TimeoutSec 30; $response.Content | Set-Content -LiteralPath 'tmp/sogou-official-20261021.html'; [regex]::Matches($response.Content,'https?[^"''<>\s]+(?:apk|\.js)[^"''<>\s]*') | ForEach-Object Value | Select-Object -Unique`
>
> - Ran `New-Item -ItemType Directory -Force work/enhancer/tmp,work/enhancer/config | Out-Null; $env:JAVA_HOME=(Resolve-Path 'work/tools/jdk/jdk-21.0.12.1+1').Path; $env:JADX_CONFIG_DIR=(Resolve-Path work/enhancer/config).Path; $env:JADX_CACHE_DIR=$env:JADX_CONFIG_DIR; $env:JADX_TMP_DIR=(Resolve-Path work/enhancer/tmp).Path; $env:JAVA_OPTS='-Djava.io.tmpdir='+$env:JADX_TMP_DIR; & work/tools/jadx-ready/bin/jadx.bat -d work/enhancer/baseline-jadx --no-res '搜狗输入法/搜狗输入法-20.16.0(2610)/搜狗输入法增强模块.apk'; & work/tools/jdk/jdk-21.0.12.1+1/bin/java.exe ('-Djava.io.tmpdir='+$env:JADX_TMP_DIR) -jar work/tools/signer.jar -a '搜狗输入法.apk' -y`
>
> - Ran `Get-ChildItem work/device -Name; Get-ChildItem work/patch -Name; Get-ChildItem work/signing -Name; Get-ChildItem backup -Name; rg -n 'npatch|lspatch|SIGSEGV|fd1a4|setFirstInstallTime' work/dsh --glob '*.txt' --glob '*.py' --glob '*.md' --glob '*.sh'; Get-Content work/dsh/pack.py -TotalCount 140; Get-Content work/ads/mod/stubs/de/robv/android/xposed/XposedHelpers.java; Get-Content work/ads/mod/stubs/de/robv/android/xposed/XposedBridge.java`
>
> - Ran `$response=Invoke-WebRequest -Uri 'https://shouji.sogou.com/' -TimeoutSec 30; $response.Content | Set-Content -LiteralPath 'tmp/sogou-official-20261021.html'; [regex]::Matches($response.Content,'https?[^"''<>\s]+(?:apk|\.js)[^"''<>\s]*') | ForEach-Object Value | Select-Object -Unique`
>
> - Ran `Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java -Raw; Get-ChildItem work/enhancer/baseline-jadx/sources/com/sogouenhance -Name; rg -n 'apk|download|script|src=' tmp/sogou-official-20261021.html | Select-Object -First 30; Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/BuildConfig.java -ErrorAction SilentlyContinue; Get-Content work/compat/implementation-notes.md -TotalCount 130; Get-Content work/xposed/route1-scope-extension.md -TotalCount 150`
>
> - Ran `rg -n 'findAndHookMethod|findClass\(|KEY_' work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java | Select-Object -First 110; Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/Prefs.java -TotalCount 120; Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/SettingsActivity.java -TotalCount 90; rg --files work/patch | Select-Object -First 25; Get-Command python,node -ErrorAction SilentlyContinue | Select-Object Name,Source`
>
> - Ran `$response=Invoke-WebRequest -Uri 'https://shouji.sogou.com/wap/' -TimeoutSec 30; $response.Content | Set-Content -LiteralPath 'tmp/sogou-wap-20261021.html'; [regex]::Matches($response.Content,'(?:href|src)=["''][^"'']+["'']') | ForEach-Object Value | Where-Object { $_ -match 'apk|js|down' }`
>
> </details>
>
> 基线模块已确认是 `com.sogouenhance`，除去广告外，还包括剪贴板数量与长度、无限提示、分词高亮、AI 开关和模块设置入口。因此会以这个模块为基底，保留原功能后追加底栏适配。
>
> 测试手机已连接，root 可用。根目录搜狗包的签名校验通过，证书主体为 Sohu Wireless；其是否仍为当前最新版，还在核对官方下载入口。
>
> <details><summary>Ran 11 commands</summary>
>
> - Ran `Get-ChildItem work/patch/work -Name | Select-Object -Last 25; rg -n -m 3 'SIGSEGV|fd1a4|setFirstInstallTime|Fatal signal' work/patch/work/lc*.txt work/dsh/lc_sogou.txt; Get-Content work/patch/out/patch-same.log -TotalCount 40; Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java | Select-Object -Skip 790 -First 60; Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java | Select-Object -Skip 890 -First 65; Get-Content work/ads/mod/dbedit.mjs -TotalCount 80; Get-ChildItem work/framework -Name`
> - Ran `& work/tools/jdk/jdk-21.0.12.1+1/bin/java.exe ('-Djava.io.tmpdir='+(Resolve-Path work/enhancer/tmp).Path) -jar work/tools/apktool-fast.jar d -f -o work/enhancer/baseline-apk -p work/framework '搜狗输入法/搜狗输入法-20.16.0(2610)/搜狗输入法增强模块.apk'; & work/tools/jdk/jdk-21.0.12.1+1/bin/java.exe ('-Djava.io.tmpdir='+(Resolve-Path work/enhancer/tmp).Path) -jar work/patch/npatch.jar --help`
> - Ran `$r=Invoke-WebRequest -Uri 'https://shouji.sogou.com/index.php' -TimeoutSec 30; $r.Content | Set-Content -LiteralPath 'tmp/sogou-mobile-index-20261021.html'; [regex]::Matches($r.Content,'(?:href|src)=["''][^"'']+["'']') | ForEach-Object Value | Where-Object { $_ -match 'apk|down|\.js' }`
> - Ran `Get-Content work/enhancer/baseline-apk/AndroidManifest.xml; Get-Content work/enhancer/baseline-apk/apktool.yml; Get-ChildItem work/enhancer/baseline-apk/smali_classes2 -Name; rg -n '^\.class' work/enhancer/baseline-apk/smali_classes2 | Select-Object -First 20; Get-Content work/patch/work/pipelineN.sh -TotalCount 100; rg -n -m 3 'Fatal signal|SIGSEGV|fd1a4|setFirstInstallTime' work/patch/work -g 'lc*.txt'; Get-Content work/inventory/rom-module-disasm.txt -TotalCount 140`
> - Ran `New-Item -ItemType Directory -Force work/enhancer/official | Out-Null; Invoke-WebRequest -Uri 'https://apkdl.sogouimecdn.com/wapdl/android/apk/SogouInput_20.17.0_android_sweb.apk?frm=new_pcjs_index' -OutFile 'work/enhancer/official/SogouInput_20.17.0_android_sweb.apk' -TimeoutSec 180; Get-FileHash 'work/enhancer/official/SogouInput_20.17.0_android_sweb.apk' -Algorithm SHA256`
> - Ran `Get-ChildItem work/enhancer/baseline-apk/smali -Name; Get-Content work/patch/work/lc10.txt | Select-String -Pattern 'Fatal signal|SIGSEGV|NoSuchMethod|Error|Exception|npatch.*success' | Select-Object -Last 16; Get-Content work/patch/work/manifest-surgery2.mjs -TotalCount 110; Get-Content work/patch/work/pipeline-samename.sh -TotalCount 65; Get-Content work/enhancer/baseline-apk/smali/com/sogouenhance/HookEntry.smali | Select-String -Pattern '"Kb"|"dj"' -Context 5,5; & work/compat/aapt2.exe dump badging work/enhancer/official/SogouInput_20.17.0_android_sweb.apk | Select-Object -First 4`
> - Ran `& work/tools/jdk/jdk-21.0.12.1+1/bin/java.exe ('-Djava.io.tmpdir='+(Resolve-Path work/enhancer/tmp).Path) -jar work/tools/signer.jar -a work/enhancer/official/SogouInput_20.17.0_android_sweb.apk -y; & work/compat/aapt2.exe dump badging work/enhancer/official/SogouInput_20.17.0_android_sweb.apk | Select-Object -First 4`
> - Ran `python -c "import zipfile,hashlib; a=zipfile.ZipFile('搜狗输入法.apk'); b=zipfile.ZipFile('work/enhancer/official/SogouInput_20.17.0_android_sweb.apk'); changed=[n for n in a.namelist() if n in b.namelist() and a.read(n)!=b.read(n)]; print('changed members:',changed); print('new members:',set(b.namelist())-set(a.namelist()))"; Get-Content work/patch/work/pipeline-samename.sh | Select-Object -Last 30; Get-Content work/patch/work/swap-samename.sh -TotalCount 90; Get-Content work/patch/work/negctl2.sh -TotalCount 60`
> - Ran `rg --files tmp docs work/patch | Where-Object { $_ -match '\.(md|json)$|lc_final' } | Select-Object -First 45; Get-Content work/enhancer/baseline-apk/smali/com/sogouenhance/HookEntry.smali -TotalCount 20; Get-Content work/patch/work/lc10.txt | Select-String -Pattern 'sogou-adfree|Hook MIUI|sIsImeSupport|Fatal signal' | Select-Object -Last 10; Get-Content work/enhancer/baseline-apk/assets/xposed_init; Get-Content work/enhancer/baseline-apk/res/values/strings.xml -TotalCount 12; Get-Content work/enhancer/baseline-apk/smali/com/sogouenhance/Prefs.smali -TotalCount 25`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'dumpsys package com.sohu.inputmethod.sogou | grep -E "versionCode|signatures=|codePath="; su -c "ls /data/adb/lspd/config; ps -A | grep -E lspd"'`
> - Ran `Get-Content docs/handoff-sogou-next-session.md -Raw; Get-Content tmp/tutorial_enh.md -TotalCount 60; Get-Content tmp/lc_final_crash.txt -TotalCount 25; Get-ChildItem tmp/enhrebuild -Name; Get-Content tmp/enhrebuild/AndroidManifest.xml -TotalCount 35`
>
> </details>
>
> 发现了交接摘要未涵盖的后续实验：旧记录里已有内嵌模块成功加载、底栏 hook 命中的单 APK 测试，但当时仍有包名与设置页问题。因此，“单 APK 不可行”不能作为最终结论；我会沿已有实验继续验证。
>
> 官网当前提供的也是 20.17.0（2620）。新下载包与本地包的全部 ZIP 成员内容相同，签名证书也一致。
>
> <details><summary>Created 3 files, edited a file, ran 8 commands</summary>
>
> - Ran `Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/SettingsActivity.java | Select-String -Pattern 'applyLauncher|ComponentName|setClassName|com.sogouenhance|provider' -Context 3,10; Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java | Select-Object -Skip 950 -First 40; Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/PrefProvider.java -TotalCount 130; rg -n 'customizeBottomViewColor|isImeSupport|sIsImeSupport|addMiuiBottomView' work/inventory/rom-ime-disasm.txt | Select-Object -First 18; Get-Content work/wxime/jadx-embedded/sources/com/xposed/wetypehook/MainHook.java | Select-Object -Skip 232 -First 24`
> - Wrote `./work/enhancer/src/com/sogouenhance/bottom/BottomHook.java` (+169 -0)
> - Wrote `./work/enhancer/src/com/sogouenhance/bottom/EmbeddedGuard.java` (+29 -0)
> - Ran `Test-Path work/enhancer/src/com/sogouenhance/bottom/BottomHook.java; Get-Content work/enhancer/baseline-apk/smali/com/sogouenhance/HookEntry.smali | Select-String -Pattern 'openModuleSettings' -Context 1,2; Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java | Select-Object -Skip 963 -First 17; Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/Prefs.java | Select-Object -Skip 145 -First 65; Get-ChildItem tmp -Name | Where-Object {$_ -match 'same|final|verify'}; Get-Content work/enhancer/baseline-apk/smali/com/sogouenhance/SettingsActivity.smali | Select-String -Pattern '界|beginCard|正' -Context 1,1 | Select-Object -First 5`
> - Wrote `./work/enhancer/build.py` (+120 -0)
> - Ran `python work/enhancer/build.py *> work/enhancer/build-log.txt; Get-Content work/enhancer/build-log.txt -Tail 32`
> - Ran `rg -n 'const-string.*com.sogouenhance|\.method.*get\(|fromXShared' work/enhancer/baseline-apk/smali/com/sogouenhance/Prefs.smali; rg -n 'const-string.*(剪贴板|键盘|界面)' work/enhancer/baseline-apk/smali/com/sogouenhance/SettingsActivity.smali | Select-Object -First 8; Get-Content work/enhancer/baseline-apk/smali/com/sogouenhance/PrefProvider.smali | Select-String -Pattern 'monitor-exit|goto|:goto|size\(' -Context 2,2 | Select-Object -First 16`
> - Wrote `./work/enhancer/build.py` (+2 -2)
> - Ran `Get-Content work/enhancer/build-log.txt -Tail 20; Test-Path work/enhancer/module-b; Get-Content work/enhancer/baseline-apk/smali/com/sogouenhance/PrefProvider.smali | Select-Object -Skip 95 -First 55; Get-Content work/enhancer/baseline-apk/smali/com/sogouenhance/SettingsActivity.smali | Select-String -Pattern '\.method protected onCreate' -Context 0,6`
> - Ran `Get-Content work/enhancer/module-a/smali/com/sogouenhance/SettingsActivity.smali | Select-String -Pattern 'setContentView' -Context 8,3; Get-Content work/enhancer/module-a/smali/com/sogouenhance/Prefs.smali | Select-Object -Skip 820 -First 35; Get-Content work/enhancer/module-b/smali/com/sogouenhance/Prefs.smali | Select-Object -Skip 470 -First 15; Get-Content work/enhancer/build/modules.json`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push work/enhancer/build/signed-a/enhancer-a-aligned-debugSigned.apk /data/local/tmp/sogou-enhancer-a.apk; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "pm install -r /data/local/tmp/sogou-enhancer-a.apk"'`
> - Ran `New-Item -ItemType Directory -Force work/enhancer/device-a | Out-Null; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "mkdir -p /data/local/tmp/sogou-enhancer-20261021-before; cp -a /data/adb/lspd/config/modules_config.db* /data/local/tmp/sogou-enhancer-20261021-before/; /data/adb/modules/zygisk_lsposed/lspctl stop"'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "cp -a /data/adb/lspd/config/modules_config.db* /data/local/tmp/sogou-enhancer-20261021-before/; chmod 755 /data/local/tmp/sogou-enhancer-20261021-before; chmod 644 /data/local/tmp/sogou-enhancer-20261021-before/*"'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /data/local/tmp/sogou-enhancer-20261021-before work/enhancer/device-a/; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pm path com.sogouenhance`
>
> </details>
>
> 保留原功能并新增底栏适配的模块已构建、签名并安装到测试手机。验证时会暂时排除旧去广告模块和旧底栏模块对普通版搜狗的作用，确认效果确实来自新模块；LSPosed 配置已备份。
>
> 方案 B 还会把增强设置页接入输入法自身，确保单 APK 内的原有开关可用。
>
> <details><summary>Ran 9 commands</summary>
>
> - Ran `python -c "import sqlite3,shutil,pathlib; p=pathlib.Path('work/enhancer/device-a/sogou-enhancer-20261021-before/modules_config.db'); db=sqlite3.connect(p); print(db.execute('select * from modules').fetchall()); print(db.execute('select * from modules_state').fetchall()); print(db.execute('select * from scope').fetchall()); db.close()"; Get-Content work/enhancer/baseline-apk/smali/com/sogouenhance/SettingsActivity.smali | Select-String -Pattern 'setContentView' -Context 5,2`
> - Ran `python -c "import sqlite3,pathlib; p=pathlib.Path('work/enhancer/device-a'); src=sqlite3.connect(p/'sogou-enhancer-20261021-before/modules_config.db'); dst=sqlite3.connect(p/'modules_config.db'); src.backup(dst); src.close(); dst.execute('INSERT OR REPLACE INTO modules_state VALUES (?,0,1,0)',('com.sogouenhance',)); dst.execute('DELETE FROM scope WHERE app_pkg_name=? AND module_pkg_name IN (?,?)',('com.sohu.inputmethod.sogou','com.xposed.wetypehook','com.sogou.adfree')); dst.execute('INSERT OR IGNORE INTO scope VALUES (?,?,0)',('com.sogouenhance','com.sohu.inputmethod.sogou')); dst.commit(); print(dst.execute('select * from scope').fetchall()); print(dst.execute('pragma integrity_check').fetchone()); dst.close()"`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push work/enhancer/device-a/modules_config.db /data/local/tmp/sogou-enhancer-a.db; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "cp /data/local/tmp/sogou-enhancer-a.db /data/adb/lspd/config/modules_config.db; rm -f /data/adb/lspd/config/modules_config.db-wal /data/adb/lspd/config/modules_config.db-shm; chown root:root /data/adb/lspd/config/modules_config.db; chmod 600 /data/adb/lspd/config/modules_config.db; ksud soft-reboot"'`
> - Ran `python -c "import zipfile,json; z=zipfile.ZipFile('work/patch/out_same/signed/sogou-installed-833-npatched-aligned-debugSigned.apk'); print(z.namelist()[:22]); print(z.read('assets/npatch/config.json').decode()); print([n for n in z.namelist() if 'original' in n or 'origin' in n])"; Get-Content work/enhancer/build-log.txt -Tail 2; Get-Content work/patch/work/lc10.txt | Select-String 'NPatch' | Select-Object -First 14`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'getprop sys.boot_completed; su -c id; ime enable com.sohu.inputmethod.sogou/.SogouIME; ime set com.sohu.inputmethod.sogou/.SogouIME; am start -n com.android.settings/.MainSettings'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -s LSPosed-Bridge LSPosedFramework SogouBottom`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'input keyevent KEYCODE_WAKEUP; wm dismiss-keyguard; uiautomator dump /sdcard/sogou-enhancer-a.xml'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-enhancer-a.xml work/enhancer/device-a/screen.xml; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d > work/enhancer/device-a/logcat.txt; Select-String -Path work/enhancer/device-a/logcat.txt -Pattern 'SogouBottom|SogouEnhance|com.sogouenhance|Fatal signal' | Select-Object -Last 22; Get-Content work/enhancer/device-a/screen.xml`
> - Ran `python -c "import zipfile,json; z=zipfile.ZipFile('work/patch/out_same/signed/sogou-installed-833-npatched-aligned-debugSigned.apk'); print([(n,z.getinfo(n).file_size) for n in z.namelist() if n.startswith('assets/npatch/') and n.count('/')<4]); print([n for n in z.namelist() if n.endswith('.dex')][:12])"`
> - Ran `python -c "import xml.etree.ElementTree as e; root=e.parse('work/enhancer/device-a/screen.xml'); print([(n.get('resource-id'),n.get('bounds')) for n in root.iter('node') if n.get('class')=='android.widget.EditText'])"; Select-String -Path work/enhancer/device-a/logcat.txt -Pattern '\[SogouBottom\]|挂钩.*失败|构造模块入口失败' | Select-Object -First 26; Get-Content work/patch/work/lc10.txt | Select-String -Pattern 'loadDex|InputMethodBottomManager' | Select-Object -First 8`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'am start -n com.sogouenhance/.SettingsActivity; am start -n com.android.settings/.MainSettings; input tap 520 1190; dumpsys input_method | grep -E "mCurId=|mInputShown="; screencap -p /sdcard/sogou-a-keyboard.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-a-keyboard.png work/enhancer/device-a/keyboard.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `rg -n '\.method .*\(' work/standard/smali_classes*/com/sogou/clipboard/repository/utils/i.smali; rg -n 'pref_ai_service|p4\(' work/standard -g '*.smali' -l | Select-Object -First 15`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'input tap 600 550'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'dumpsys input_method | grep -E "mCurId=|mInputShown="; screencap -p /sdcard/sogou-a-keyboard.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-a-keyboard.png work/enhancer/device-a/keyboard.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -t 10000 > work/enhancer/device-a/active.txt; Select-String -Path work/enhancer/device-a/active.txt -Pattern 'SogouBottom|挂钩.*失败|Fatal signal' | Select-Object -Last 8`
> - Ran `rg --files work/standard | Where-Object { $_ -match 'clipboard.repository.utils.i.smali$|settings.impl.u0\$a.smali$|ai.router.f.smali$' }; rg -n '\.method .*|pref_ai_service' 'work/standard/smali_classes3/com/sogou/imskit/feature/settings/impl/u0$a.smali' | Select-Object -Last 18; rg -n '\.method .*' work/standard/smali_classes3/com/sogou/imskit/feature/keyboard/ai/router/f.smali | Select-Object -First 30`
>
> </details>
>
> Viewed an image
>
> <details><summary>Edited a file, ran 4 commands</summary>
>
> - Ran `rg -n '\.method .*' work/standard/smali_classes3/com/sogou/clipboard/repository/utils/i.smali; Get-Content work/standard/smali_classes3/com/sogou/imskit/feature/keyboard/ai/router/f.smali | Select-Object -Skip 935 -First 26; Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java | Select-Object -Skip 636 -First 59; Get-Content work/enhancer/baseline-apk/smali/com/sogouenhance/HookEntry.smali | Select-String -Pattern '"p4"|"cb"|"p0\$a"|"b"|"d"' -Context 1,1 | Select-Object -First 25`
> - Ran `rg -n -l 'Lcom/sogou/lib/common/string/b;->m\(Ljava/lang/String;\)I' work/standard/smali_classes3/com/sogou/clipboard; rg -n '\.method .*|0x3e8|0x1388|substring|->m\(Ljava/lang/String;\)I' work/standard/smali_classes3/com/sogou/clipboard/repository/utils/*.smali | Select-Object -First 95; rg -n 'const-string.*com.sogou.imskit.feature.settings.impl' work/enhancer/baseline-apk/smali/com/sogouenhance/HookEntry.smali; rg -n '资源|res/' work/enhancer/baseline-jadx/sources/com/sogouenhance/SettingsActivity.java`
> - Ran `rg -n '\.method .*|0x3e8|0x1388|substring|->m\(Ljava/lang/String;\)I' work/standard/smali_classes3/com/sogou/clipboard/repository/utils/k.smali; Get-Content work/standard/smali_classes3/com/sogou/imskit/feature/settings/impl/u0\$a.smali -ErrorAction SilentlyContinue | Select-Object -Skip 2330 -First 24; Get-Content work/enhancer/baseline-apk/smali/com/sogouenhance/HookEntry.smali | Select-Object -Skip 900 -First 130`
> - Wrote `./work/enhancer/build.py` (+17 -4)
> - Ran `python work/enhancer/build.py *> work/enhancer/build-log.txt; Get-Content work/enhancer/build-log.txt -Tail 8`
>
> </details>
>
> 方案 A 的新模块已独立显示出 MIUI 原生底栏，普通版键盘正常弹出。真机日志还发现了旧模块在 20.17.0 上的两个兼容问题：剪贴板截断类、AI 服务方法已改名；这些已定位并修正，正在重构建验证。
>
> 现在继续打通方案 B 的内嵌加载与设置页。底栏出现只是其中一项，尚不能算方案 B 完成。
>
> <details><summary>Created a file, edited 2 files, ran 7 commands</summary>
>
> - Wrote `./work/enhancer/package_b.py` (+191 -0)
> - Ran `Get-Content work/enhancer/build-log.txt -Tail 9; Get-Content work/enhancer/build/modules.json; Get-ChildItem work/enhancer/build/signed-b | Select-Object Name,LastWriteTime; Get-ChildItem work/enhancer/build/enhancer-b.apk | Select-Object LastWriteTime`
> - Wrote `./work/enhancer/build.py` (+4 -2)
> - Wrote `./work/enhancer/package_b.py` (+1 -1)
> - Ran `python work/enhancer/build.py *> work/enhancer/build-log.txt; if ($LASTEXITCODE -eq 0) { python work/enhancer/package_b.py *> work/enhancer/single-build-log.txt }; Get-Content work/enhancer/build-log.txt -Tail 8; Get-Content work/enhancer/single-build-log.txt -Tail 12 -ErrorAction SilentlyContinue`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'pm path com.sohu.inputmethod.sogou' | Set-Content work/enhancer/device-a/installed-path.txt; $apkPath=(Get-Content work/enhancer/device-a/installed-path.txt).Trim().Replace('package:',''); & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull $apkPath work/enhancer/device-a/installed.apk; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'uiautomator dump /sdcard/sogou-a-keyboard.xml'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-a-keyboard.xml work/enhancer/device-a/keyboard.xml`
> - Ran `Get-Content work/enhancer/single-build-log.txt -Tail 15 -ErrorAction SilentlyContinue; python -c "import xml.etree.ElementTree as e; r=e.parse('work/enhancer/device-a/keyboard.xml'); print([(n.get('text'),n.get('content-desc'),n.get('resource-id'),n.get('bounds')) for n in r.iter('node') if n.get('package')=='com.sohu.inputmethod.sogou' and (n.get('clickable')=='true' or n.get('content-desc'))][-20:])"; Get-Content work/enhancer/build/modules.json`
> - Wrote `./work/enhancer/package_b.py` (+28 -4)
> - Ran `python -c "import xml.etree.ElementTree as e; r=e.parse('work/enhancer/device-a/keyboard.xml'); print([(n.get('text'),n.get('content-desc'),n.get('resource-id'),n.get('bounds')) for n in r.iter('node') if n.get('resource-id')][-12:])"; Get-FileHash work/enhancer/device-a/installed.apk; git status --short | Select-Object -First 5`
> - Ran `python work/enhancer/package_b.py *> work/enhancer/single-build-log.txt; Get-Content work/enhancer/single-build-log.txt -Tail 22`
> - Ran `$modules=Get-Content work/enhancer/build/modules.json -Raw | ConvertFrom-Json; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push $modules.a.apk /data/local/tmp/sogou-enhancer-a.apk; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "pm install -r /data/local/tmp/sogou-enhancer-a.apk"; am start -n com.sogouenhance/.SettingsActivity; am force-stop com.sohu.inputmethod.sogou; ime set com.sohu.inputmethod.sogou/.SogouIME; am start -n com.android.settings/.MainSettings'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -t 10000 > work/enhancer/device-a/rebuilt-log.txt; Select-String -Path work/enhancer/device-a/rebuilt-log.txt -Pattern 'SogouEnhance.*已挂钩|SogouEnhance.*失败|SogouBottom' | Select-Object -Last 20; Get-Content work/enhancer/single-build-log.txt -Tail 10`
>
> </details>
>
> 方案 B 的单 APK 候选包已生成。为做真机验证，你希望它与官方普通版搜狗共存，还是替换官方普通版？替换因签名不同需要先卸载原版，备份也不能保证保留登录状态。
> - 与官方普通版共存，保留现有数据（推荐）
> - 替换官方普通版，接受备份后卸载及可能重新登录
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'am start -n com.android.settings/.MainSettings -f 0x14000000'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'input tap 600 550'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -t 12000 > work/enhancer/device-a/rebuilt-log.txt; Select-String -Path work/enhancer/device-a/rebuilt-log.txt -Pattern 'SogouEnhance.*已挂钩|SogouEnhance.*失败|SogouBottom.*READY|Fatal signal' | Select-Object -Last 30; & work/compat/aapt2.exe dump xmltree work/enhancer/build/single-signed/sogou-20.17.0-enhanced-single-aligned-debugSigned.apk --file AndroidManifest.xml > work/enhancer/build/single-manifest.txt; Select-String work/enhancer/build/single-manifest.txt -Pattern 'sogouenhance|enhance.prefs|LauncherAlias' -Context 1,3`
>
> </details>
>
> **方案 B 的单 APK 候选包已生成。为做真机验证，你希望它与官方普通版搜狗共存，还是替换官方普通版？替换因签名不同需要先卸载原版，备份也不能保证保留登录状态。**
>
> 与官方普通版共存，保留现有数据（推荐）
>
> 收到，方案 B 按“与官方普通版共存”继续，保留现有数据。我会给增强版使用独立包名，并验证旧实验中因改包名出问题的资源读取、设置页和登录页。
>
> 方案 B 的交付仍只有一个 APK，增强模块与设置页都放在包内。
>
> <details><summary>Created 4 files, edited 5 files, ran 5 commands</summary>
>
> - Wrote `./work/enhancer/build.py` (+4 -2)
> - Wrote `./work/enhancer/package_b.py` (+14 -5)
> - Wrote `./work/enhancer/probe/AndroidManifest.xml` (+6 -0)
> - Wrote `./work/enhancer/probe/apktool.yml` (+10 -0)
> - Wrote `./work/enhancer/probe/smali/local/sogou/enhancerprobe/ProbeActivity.smali` (+26 -0)
> - Wrote `./work/enhancer/src/com/sogouenhance/bottom/BottomHook.java` (+2 -1)
> - Wrote `./work/enhancer/src/com/sogouenhance/bottom/EmbeddedGuard.java` (+20 -1)
> - Ran `python work/enhancer/build.py *> work/enhancer/build-log.txt; if ($LASTEXITCODE -eq 0) { python work/enhancer/package_b.py *> work/enhancer/single-build-log.txt }; Get-Content work/enhancer/single-build-log.txt -Tail 15`
> - Ran `$taskJava='work/tools/jdk/jdk-21.0.12.1+1/bin/java.exe'; $taskTmp='-Djava.io.tmpdir='+(Resolve-Path work/enhancer/tmp).Path; & $taskJava $taskTmp -jar work/tools/apktool-fast.jar b work/enhancer/probe -p work/framework --aapt work/compat/aapt2.exe -o work/enhancer/build/probe.apk; & $taskJava $taskTmp -jar work/tools/signer.jar -a work/enhancer/build/probe.apk -o work/enhancer/build/probe-signed; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push work/enhancer/build/probe-signed/probe-aligned-debugSigned.apk /data/local/tmp/sogou-verification-probe.apk; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "pm install -r /data/local/tmp/sogou-verification-probe.apk"; am start -n local.sogou.enhancerprobe/.ProbeActivity'`
> - Wrote `./work/enhancer/probe/apktool.yml` (+2 -1)
> - Wrote `./work/enhancer/probe/res/values/strings.xml` (+2 -0)
> - Ran `$taskJava='work/tools/jdk/jdk-21.0.12.1+1/bin/java.exe'; $taskTmp='-Djava.io.tmpdir='+(Resolve-Path work/enhancer/tmp).Path; & $taskJava $taskTmp -jar work/tools/apktool-fast.jar b work/enhancer/probe -p work/framework --aapt work/compat/aapt2.exe -o work/enhancer/build/probe.apk; if ($LASTEXITCODE -ne 0) { exit 1 }; & $taskJava $taskTmp -jar work/tools/signer.jar -a work/enhancer/build/probe.apk -o work/enhancer/build/probe-signed; if ($LASTEXITCODE -ne 0) { exit 1 }; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push work/enhancer/build/probe-signed/probe-aligned-debugSigned.apk /data/local/tmp/sogou-verification-probe.apk; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "pm install -r /data/local/tmp/sogou-verification-probe.apk"; am start -n local.sogou.enhancerprobe/.ProbeActivity'`
> - Ran `Get-Content work/enhancer/single-build-log.txt -Tail 16; Get-Content work/enhancer/build/single.json -ErrorAction SilentlyContinue`
> - Wrote `./work/enhancer/probe/apktool.yml` (+2 -0)
> - Ran `$taskJava='work/tools/jdk/jdk-21.0.12.1+1/bin/java.exe'; $taskTmp='-Djava.io.tmpdir='+(Resolve-Path work/enhancer/tmp).Path; & $taskJava $taskTmp -jar work/tools/apktool-fast.jar b work/enhancer/probe -p work/framework --aapt work/compat/aapt2.exe -o work/enhancer/build/probe-fixed.apk; if ($LASTEXITCODE -ne 0) {exit 1}; & $taskJava $taskTmp -jar work/tools/signer.jar -a work/enhancer/build/probe-fixed.apk -o work/enhancer/build/probe-fixed-signed; if ($LASTEXITCODE -ne 0) {exit 1}; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push work/enhancer/build/probe-fixed-signed/probe-fixed-aligned-debugSigned.apk /data/local/tmp/sogou-verification-probe.apk; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "pm install -r /data/local/tmp/sogou-verification-probe.apk"; am start -n local.sogou.enhancerprobe/.ProbeActivity'; $taskB=Get-Content work/enhancer/build/single.json -Raw | ConvertFrom-Json; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push $taskB.apk /data/local/tmp/sogou-enhanced-single.apk; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "pm install -r /data/local/tmp/sogou-enhanced-single.apk"'`
>
> </details>
>
> 可共存的方案 B 单 APK 已完成构建和签名，正在安装到测试手机。它使用独立包名，内置原增强模块、底栏适配、资源查找兼容和设置页。
>
> 接下来用独立的本地文本框验证，重点检查：不勾选外部模块也能运行、输入后不崩溃、底栏可操作，以及增强设置开关能生效。
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `New-Item -ItemType Directory -Force work/enhancer/device-b | Out-Null; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'pm list packages | grep -E "sogou.enhanced|sogouenhance"; ime list -s; dumpsys input_method | grep -E "mCurId=|mInputShown="'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -t 3000 > work/enhancer/device-a/probe-log.txt; Select-String -Path work/enhancer/device-a/probe-log.txt -Pattern 'SogouEnhance.*失败|SogouEnhance.*已挂钩|SogouBottom.*READY' | Select-Object -Last 24`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'ime enable com.sohu.inputmethod.sogou.enhanced/com.sohu.inputmethod.sogou.SogouIME; ime set com.sohu.inputmethod.sogou.enhanced/com.sohu.inputmethod.sogou.SogouIME; am start -n com.sohu.inputmethod.sogou.enhanced/com.sogouenhance.SettingsActivity'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'dumpsys activity activities | grep mResumedActivity; screencap -p /sdcard/sogou-b-settings.png; uiautomator dump /sdcard/sogou-b-settings.xml'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-settings.png work/enhancer/device-b/settings.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-settings.xml work/enhancer/device-b/settings.xml; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -t 12000 > work/enhancer/device-b/first-log.txt; Select-String -Path work/enhancer/device-b/first-log.txt -Pattern 'SogouBottom|SogouEmbedded|SogouEnhance.*失败|Unable to.*com.sogouenhance|FATAL EXCEPTION|Fatal signal' | Select-Object -Last 27`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `python -c "import xml.etree.ElementTree as e; r=e.parse('work/enhancer/device-b/settings.xml'); print([(n.get('text'),n.get('bounds')) for n in r.iter('node') if n.get('text')][:20])"; Select-String -Path work/enhancer/device-b/first-log.txt -Pattern 'SogouEnhance.*已挂钩|SogouEnhance.*失败' | Select-Object -Last 28`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'am force-stop local.sogou.enhancerprobe; am start -n local.sogou.enhancerprobe/.ProbeActivity'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'dumpsys input_method | grep -E "mCurId=|mInputShown="; screencap -p /sdcard/sogou-b-keyboard.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-keyboard.png work/enhancer/device-b/keyboard.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'uiautomator dump /sdcard/sogou-b-keyboard.xml'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-keyboard.xml work/enhancer/device-b/keyboard.xml`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `python -c "import xml.etree.ElementTree as e; r=e.parse('work/enhancer/device-b/keyboard.xml'); print([(n.get('text'),n.get('content-desc'),n.get('class'),n.get('bounds')) for n in r.iter('node')])"`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -t 12000 > work/enhancer/device-b/keyboard-log.txt; Select-String -Path work/enhancer/device-b/keyboard-log.txt -Pattern 'IMEBottomManager|InputMethodBottom|InputMethodServiceInjector|SogouBottom|FATAL EXCEPTION|Fatal signal|NameNotFound|SecurityException|not support' | Select-Object -Last 38; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'dumpsys input_method | grep -E "mCurId=|mInputShown="; settings get secure full_screen_keyboard_type; settings get secure full_screen_keyboard_left_function; settings get secure full_screen_keyboard_right_function; settings get secure default_input_method'`
> - Ran `Get-Content work/inventory/rom-ime-disasm.txt | Select-Object -Skip 535 -First 95; Get-Content work/inventory/rom-ime-disasm.txt | Select-Object -Skip 120 -First 58; rg -n 'isImeSupport|sIsImeSupport|full_screen_keyboard|isSupport' work/inventory/rom-phrase-bottom-disasm.txt | Select-Object -First 20; Get-Content work/enhancer/build/modules.json`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'screencap -p /sdcard/sogou-b-settled.png; dumpsys input_method | grep -E "mCurId=|mInputShown="'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-settled.png work/enhancer/device-b/settled.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'am force-stop local.sogou.enhancerprobe; am start -n local.sogou.enhancerprobe/.ProbeActivity'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'screencap -p /sdcard/sogou-b-probe.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-probe.png work/enhancer/device-b/probe.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d --pid=17622 > work/enhancer/device-b/process.txt; Select-String -Path work/enhancer/device-b/process.txt -Pattern 'channel=ContentProvider|provider broken|FATAL EXCEPTION|Fatal signal|Resource.*error' | Select-Object -Last 8`
>
> </details>
>
> Viewed an image
>
> 方案 B 已能显示原生底栏，内置设置也已读取成功。我观察到手机正在被操作；接下来要短暂切换输入法，并软重启一次来排除旧模块影响。现在方便留出约 2–3 分钟让我自动测试吗？
> - 现在可以，继续自动测试
> - 先别操作手机，继续做电脑端检查
>
> **方案 B 已能显示原生底栏，内置设置也已读取成功。我观察到手机正在被操作；接下来要短暂切换输入法，并软重启一次来排除旧模块影响。现在方便留出约 2–3 分钟让我自动测试吗？**
>
> 现在可以，继续自动测试
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `python -c "import sqlite3,pathlib; b=pathlib.Path('work/enhancer'); src=sqlite3.connect(b/'device-a/modules_config.db'); dst=sqlite3.connect(b/'device-b/modules_config.db'); src.backup(dst); src.close(); dst.execute('UPDATE modules_state SET enabled=0 WHERE module_pkg_name IN (?,?,?)',('com.sogouenhance','com.sogou.adfree','com.xposed.wetypehook')); dst.commit(); print(dst.execute('select module_pkg_name,enabled from modules_state').fetchall()); dst.close()"`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push work/enhancer/device-b/modules_config.db /data/local/tmp/sogou-enhancer-b-isolated.db; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "/data/adb/modules/zygisk_lsposed/lspctl stop; cp /data/local/tmp/sogou-enhancer-b-isolated.db /data/adb/lspd/config/modules_config.db; rm -f /data/adb/lspd/config/modules_config.db-wal /data/adb/lspd/config/modules_config.db-shm; chown root:root /data/adb/lspd/config/modules_config.db; chmod 600 /data/adb/lspd/config/modules_config.db; ksud soft-reboot"'`
> - Ran `python -m py_compile work/enhancer/build.py work/enhancer/package_b.py; python -c "import zipfile,json,hashlib; p=json.load(open('work/enhancer/build/single.json')); z=zipfile.ZipFile(p['apk']); print('single APK CRC:',z.testzip()); print('embedded modules:',[n for n in z.namelist() if n.startswith('assets/npatch/modules/')]); c=json.loads(z.read('assets/npatch/config.json')); print('package=',c['newPackage'],'external manager=',c['useManager']); print('enhanced module hash=',hashlib.sha256(z.read('assets/npatch/modules/com.sogouenhance.apk')).hexdigest())"`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'getprop sys.boot_completed; input keyevent KEYCODE_WAKEUP; wm dismiss-keyguard; ime set com.sohu.inputmethod.sogou.enhanced/com.sohu.inputmethod.sogou.SogouIME; am start -n local.sogou.enhancerprobe/.ProbeActivity'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'dumpsys input_method | grep -E "mCurId=|mInputShown="; screencap -p /sdcard/sogou-b-isolated.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-isolated.png work/enhancer/device-b/isolated.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d > work/enhancer/device-b/isolated-log.txt; Select-String -Path work/enhancer/device-b/isolated-log.txt -Pattern 'SogouBottom.*READY|SogouEmbedded.*HIT|Fatal signal|FATAL EXCEPTION' | Select-Object -Last 10`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'uiautomator dump /sdcard/sogou-b-isolated.xml; screencap -p /sdcard/sogou-b-isolated.png; dumpsys input_method | grep -E "mCurId=|mInputShown="'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-isolated.png work/enhancer/device-b/isolated.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-isolated.xml work/enhancer/device-b/isolated.xml`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'input tap 380 2140; screencap -p /sdcard/sogou-b-ready.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-ready.png work/enhancer/device-b/ready.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'input tap 820 2135; input tap 900 1775; input tap 720 1960; input tap 85 1960; input tap 1020 1775; uiautomator dump /sdcard/sogou-b-input.xml; screencap -p /sdcard/sogou-b-input.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-input.png work/enhancer/device-b/input.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'input tap 130 1620; input tap 1055 2510; uiautomator dump /sdcard/sogou-b-clipboard.xml; screencap -p /sdcard/sogou-b-clipboard.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-clipboard.png work/enhancer/device-b/clipboard.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-clipboard.xml work/enhancer/device-b/clipboard.xml`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'input tap 145 2510; uiautomator dump /sdcard/sogou-b-picker.xml; screencap -p /sdcard/sogou-b-picker.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-picker.png work/enhancer/device-b/picker.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-picker.xml work/enhancer/device-b/picker.xml; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'input keyevent KEYCODE_BACK; am start -n com.sohu.inputmethod.sogou.enhanced/com.sogouenhance.SettingsActivity'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'uiautomator dump /sdcard/sogou-b-settings-ready.xml; screencap -p /sdcard/sogou-b-settings-ready.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-settings-ready.png work/enhancer/device-b/settings-ready.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'dumpsys input_method | grep -E "mCurId=|mInputShown="; su -c "cat /data/user/0/com.sohu.inputmethod.sogou.enhanced/shared_prefs/settings.xml"'`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'input tap 1040 980; su -c "cat /data/user/0/com.sohu.inputmethod.sogou.enhanced/shared_prefs/settings.xml"; am start -n local.sogou.enhancerprobe/.ProbeActivity'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'input swipe 145 2510 145 2510 800; uiautomator dump /sdcard/sogou-b-left-long.xml; screencap -p /sdcard/sogou-b-left-long.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-left-long.png work/enhancer/device-b/left-long.png`
>
> </details>
>
> Viewed an image
>
> 隔离验证通过：停用旧底栏模块、旧去广告模块和外置增强模块后，方案 B 仍能显示原生底栏；实际按键输入 `nihao`、选词提交“你好”正常，底栏右键也能打开剪贴板。
>
> 我正在恢复外部模块配置并补测方案 A，随后整理三个交付 APK、校验值和测试说明。
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "cat /data/user/0/com.sohu.inputmethod.sogou.enhanced/shared_prefs/settings.xml"; am start -n com.sohu.inputmethod.sogou.enhanced/com.sogouenhance.SettingsActivity'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'uiautomator dump /sdcard/sogou-b-switch.xml'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-switch.xml work/enhancer/device-b/switch.xml; $taskModules=Get-Content work/enhancer/build/modules.json -Raw | ConvertFrom-Json; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push $taskModules.a.apk /data/local/tmp/sogou-enhancer-a.apk; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "pm install -r /data/local/tmp/sogou-enhancer-a.apk"; pm path com.sogouenhance' | Set-Content work/enhancer/device-a/final-module-path.txt; Get-Content work/enhancer/device-a/final-module-path.txt`
> - Ran `python -c "import xml.etree.ElementTree as e; r=e.parse('work/enhancer/device-b/switch.xml'); print([(n.get('text'),n.get('bounds')) for n in r.iter('node') if n.get('text')][:12])"; Get-Content work/enhancer/device-b/isolated-log.txt -TotalCount 90 | Select-Object -Skip 25 -First 17`
> - Ran `python -c "import xml.etree.ElementTree as e; r=e.parse('work/enhancer/device-b/switch.xml'); print([(n.get('class'),n.get('clickable'),n.get('bounds')) for n in r.iter('node') if n.get('clickable')=='true'][:8])"`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'input tap 500 980'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "cat /data/user/0/com.sohu.inputmethod.sogou.enhanced/shared_prefs/settings.xml"'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -s SogouEnhance SogouEnhanceUI -t 40`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'wm size; wm density; dumpsys window | grep -E "mCurrentFocus|mFocusedApp"; dumpsys display | grep -m 3 -E "DisplayDeviceInfo|DisplayViewport"'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'screencap -p /sdcard/sogou-current.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-current.png work/enhancer/device-b/current.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "cat /data/user/0/com.sohu.inputmethod.sogou.enhanced/shared_prefs/settings.xml"; input tap 500 980; uiautomator dump /sdcard/sogou-b-restored-switch.xml'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "cat /data/user/0/com.sohu.inputmethod.sogou.enhanced/shared_prefs/settings.xml"; am start -n com.sohu.inputmethod.sogou.enhanced/com.sogou.inputmethod.passport.account.AccountLoginActivity'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'uiautomator dump /sdcard/sogou-b-login.xml; screencap -p /sdcard/sogou-b-login.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-b-login.png work/enhancer/device-b/login.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d --pid=6096 > work/enhancer/device-b/final-process.txt`
> - Ran `python -c "import sqlite3,pathlib; b=pathlib.Path('work/enhancer'); src=sqlite3.connect(b/'device-a/modules_config.db'); dst=sqlite3.connect(b/'device-a/final-config.db'); src.backup(dst); src.close(); lines=(b/'device-a/final-module-path.txt').read_text(encoding='utf-8-sig').splitlines(); apk=next(x.split('package:',1)[1].strip() for x in lines if x.startswith('package:')); dst.execute('UPDATE modules SET apk_path=? WHERE module_pkg_name=?',(apk,'com.sogouenhance')); dst.commit(); print(dst.execute('select module_pkg_name,enabled from modules_state').fetchall()); dst.close()"`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push work/enhancer/device-a/final-config.db /data/local/tmp/sogou-enhancer-final.db; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "/data/adb/modules/zygisk_lsposed/lspctl stop; cp /data/local/tmp/sogou-enhancer-final.db /data/adb/lspd/config/modules_config.db; rm -f /data/adb/lspd/config/modules_config.db-wal /data/adb/lspd/config/modules_config.db-shm; chown root:root /data/adb/lspd/config/modules_config.db; chmod 600 /data/adb/lspd/config/modules_config.db; ksud soft-reboot"'`
> - Ran `Select-String -Path work/enhancer/device-b/final-process.txt -Pattern 'FATAL EXCEPTION|Fatal signal|Load resource error|SogouEnhance.*失败|SogouBottom.*READY|first-install guard HIT' | Select-Object -Last 9; Get-Content work/enhancer/build/single.json; git diff --stat; git branch --show-current`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'getprop sys.boot_completed; input keyevent KEYCODE_WAKEUP; wm dismiss-keyguard; ime set com.sohu.inputmethod.sogou/.SogouIME; am start -n com.sogouenhance/.SettingsActivity; am start -n local.sogou.enhancerprobe/.ProbeActivity'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'uiautomator dump /sdcard/sogou-a-final.xml; screencap -p /sdcard/sogou-a-final.png; dumpsys input_method | grep -E "mCurId=|mInputShown="'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-a-final.png work/enhancer/device-a/final.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d > work/enhancer/device-a/final-log.txt; Select-String -Path work/enhancer/device-a/final-log.txt -Pattern 'SogouEnhance.*已挂钩|SogouEnhance.*失败|SogouBottom.*READY' | Select-Object -Last 27`
> - Ran `git remote -v; git log -1 --oneline; Get-ChildItem outputs -Name`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "/data/adb/modules/zygisk_lsposed/lspctl status"; dumpsys activity activities | grep mResumedActivity; ime list -s; dumpsys input_method | grep -E "mCurId=|mInputShown=|mSelectedMethodId="; input tap 400 900; uiautomator dump /sdcard/sogou-a-final.xml; screencap -p /sdcard/sogou-a-final.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-a-final.png work/enhancer/device-a/final.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -t 20000 > work/enhancer/device-a/last-log.txt; Select-String -Path work/enhancer/device-a/last-log.txt -Pattern 'com.sogouenhance|SogouBottom|SogouEnhance.*失败' | Select-Object -Last 9`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'input tap 820 2135; input tap 900 1775; input tap 720 1960; input tap 85 1960; input tap 1020 1775; input keyevent KEYCODE_SPACE; uiautomator dump /sdcard/sogou-a-input.xml; screencap -p /sdcard/sogou-a-input.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-a-input.png work/enhancer/device-a/input.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-a-input.xml work/enhancer/device-a/input.xml; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d --pid=11292 > work/enhancer/device-a/process.txt; Select-String -Path work/enhancer/device-a/process.txt -Pattern 'SogouEnhance.*已挂钩|SogouEnhance.*失败|SogouBottom.*READY|FATAL EXCEPTION|Fatal signal' | Select-Object -Last 29; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME; input keyevent KEYCODE_HOME'`
> - Ran `rg -n 'getSupportIme|switchInputMethod|startSwitch|deleteNotSupportIme' work/inventory/rom-phrase-bottom-disasm.txt | Select-Object -First 25; python -c "import xml.etree.ElementTree as e; r=e.parse('work/enhancer/device-a/input.xml'); print([(n.get('text'),n.get('package')) for n in r.iter('node') if n.get('class')=='android.widget.EditText']); print('A runtime hook failures:',sum('SogouEnhance' in l and '失败' in l for l in open('work/enhancer/device-a/process.txt',encoding='utf-8'))); print('B fatal count:',sum('FATAL EXCEPTION' in l or 'Fatal signal' in l for l in open('work/enhancer/device-b/final-process.txt',encoding='utf-8')))"`
>
> </details>
>
> 手机端测试已结束，默认输入法已恢复为测试前的小米版，原官方搜狗和数据均保留。方案 A 最终模块的原增强 hook 均加载成功，底栏正常显示；方案 B 通过了无外部模块参与的中文输入、底栏剪贴板、设置开关保存和登录页加载测试。
>
> 我会将这批产物标为“测试版”：无 root 设备、16KB 页设备、长期稳定性及完整账号登录流程尚未实测。
>
> Stream error
>
> Reconnecting 2/5
> stream disconnected before completion: Transport error: network error: error decoding response body
>
> <details><summary>Created 4 files, edited a file, a request timed out, ran 4 commands</summary>
>
> - Wrote `./.scratch/sogou-enhancer/issues/01-acceptance.md` (+15 -0)
> - Wrote `./.scratch/sogou-enhancer/spec.md` (+9 -0)
> - Wrote `./work/enhancer/README.md` (+101 -0)
> - Wrote `./work/enhancer/build.py` (+4 -0)
> - Ran `Get-Item work/enhancer/device-a/process.txt,work/enhancer/device-b/final-process.txt,work/enhancer/device-b/process.txt,work/enhancer/device-b/isolated-log.txt | Select-Object Name,Length; python -c "from pathlib import Path; p=Path('work/enhancer/device-a/process.txt').read_text(encoding='utf-8'); print('A successful hook messages',sum('[SogouEnhance] 已挂钩' in l for l in p.splitlines())); p=Path('work/enhancer/device-b/isolated-log.txt').read_text(encoding='utf-8'); ls=[l for l in p.splitlines() if ' 6096 ' in l]; print('B isolated process lines',len(ls),'fatal lines',[l for l in ls if 'FATAL EXCEPTION' in l or 'Fatal signal' in l]); Path('work/enhancer/device-b/isolated-process.txt').write_text('\n'.join(ls),encoding='utf-8')"`
> - Wrote `./work/enhancer/export.py` (+106 -0)
> - Ran `python work/enhancer/export.py; python -m py_compile work/enhancer/build.py work/enhancer/package_b.py work/enhancer/export.py; git diff --check`
> - Ran `Get-Content work/inventory/rom-phrase-bottom-disasm.txt | Select-Object -Skip 1397 -First 90; Get-Content work/inventory/rom-phrase-bottom-disasm.txt | Select-Object -Skip 1175 -First 90`
> - Ran `"C:\\Program Files\\PowerShell\\7\\pwsh.exe" -Command 'git add -- work/enhancer/build.py work/enhancer/package_b.py work/enhancer/export.py work/enhancer/README.md work/enhancer/src/com/sogouenhance/bottom/BottomHook.java work/enhancer/src/com/sogouenhance/bottom/EmbeddedGuard.java work/enhancer/probe/AndroidManifest.xml work/enhancer/probe/apktool.yml work/enhancer/probe/res/values/strings.xml work/enhancer/probe/smali/local/sogou/enhancerprobe/ProbeActivity.smali .scratch/sogou-enhancer/spec.md .scratch/sogou-enhancer/issues/01-acceptance.md
> if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
> git diff --cached --check
> if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
> git commit -m "feat: build Sogou enhancer module and standalone coexistence APK"'`
> - Auto-review: timedOut
> - Auto-review rationale: Automatic approval review timed out while evaluating the requested approval.
>
> </details>
>
> Stream error
>
> Reconnecting... waiting for network
> Connection failed: error sending request
>
> Stream error
>
> Reconnecting... waiting for network
> Connection failed: error sending request
>
> <details><summary>Ran a command</summary>
>
> - Ran `git add -- work/enhancer/build.py work/enhancer/package_b.py work/enhancer/export.py work/enhancer/README.md work/enhancer/src/com/sogouenhance/bottom/BottomHook.java work/enhancer/src/com/sogouenhance/bottom/EmbeddedGuard.java work/enhancer/probe/AndroidManifest.xml work/enhancer/probe/apktool.yml work/enhancer/probe/res/values/strings.xml work/enhancer/probe/smali/local/sogou/enhancerprobe/ProbeActivity.smali .scratch/sogou-enhancer/spec.md .scratch/sogou-enhancer/issues/01-acceptance.md
> if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
> git diff --cached --check
> if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
> git commit -m "feat: build Sogou enhancer module and standalone coexistence APK"`
>
> </details>
>
> 三个交付 APK 已整理好，数量和校验值检查通过。代码提交暂时遇到 Git 锁文件；我会先确认是否仍有 Git 进程运行，再处理锁，不影响已生成的测试版产物。
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Get-Process git -ErrorAction SilentlyContinue | Select-Object Id,StartTime,Path; Get-Item .git/index.lock -ErrorAction SilentlyContinue | Select-Object FullName,Length,LastWriteTime; git status --short --untracked-files=no; Get-ChildItem 'outputs/2026-10-21/方案A','outputs/2026-10-21/方案B' -File | Select-Object Name,Length; git log -1 --oneline`
>
> Tool call
>
> Tool: open_in_codex
> Status: completed
>
> - Ran `$taskGitLock=Get-Item -LiteralPath 'C:\Users\Kirito787\Documents\AI\DSH\sougou\.git\index.lock' -ErrorAction Stop
> if ((Get-Process git -ErrorAction SilentlyContinue) -or $taskGitLock.Length -ne 0 -or $taskGitLock.LastWriteTime -gt (Get-Date).AddMinutes(-10)) { throw 'Git lock is not confirmed stale' }
> Remove-Item -LiteralPath 'C:\Users\Kirito787\Documents\AI\DSH\sougou\.git\index.lock'
> git add -- work/enhancer/build.py work/enhancer/package_b.py work/enhancer/export.py work/enhancer/README.md work/enhancer/src/com/sogouenhance/bottom/BottomHook.java work/enhancer/src/com/sogouenhance/bottom/EmbeddedGuard.java work/enhancer/probe/AndroidManifest.xml work/enhancer/probe/apktool.yml work/enhancer/probe/res/values/strings.xml work/enhancer/probe/smali/local/sogou/enhancerprobe/ProbeActivity.smali .scratch/sogou-enhancer/spec.md .scratch/sogou-enhancer/issues/01-acceptance.md
> if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
> git diff --cached --check
> if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
> git commit -m "feat: build Sogou enhancer module and standalone coexistence APK"`
>
> - Ran `git diff --cached --stat; git log -1 --oneline; Get-Content 'outputs/2026-10-21/SHA256SUMS.txt'`
>
> - Ran `git status --short --untracked-files=no; git show --stat --oneline HEAD | Select-Object -Last 3`
>
> </details>
</details>

两方案的**测试版已生成**：

- **方案 A，两个 APK**：[官方 20.17.0](/C:/Users/Kirito787/Documents/AI/DSH/sougou/outputs/2026-10-21/方案A/搜狗输入法-20.17.0-官方.apk) ＋ [增强模块](/C:/Users/Kirito787/Documents/AI/DSH/sougou/outputs/2026-10-21/方案A/搜狗增强模块-1.1.0-测试版.apk)。
- **方案 B，只有一个 APK**：[内置增强模块的共存版](/C:/Users/Kirito787/Documents/AI/DSH/sougou/outputs/2026-10-21/方案B/搜狗输入法-20.17.0-内置增强-共存测试版.apk)。

B 已在停用外部模块后验证中文输入、原生底栏、剪贴板和内嵌设置；官方版及数据保留。

底栏左键完整切换、语音、无 root 设备和长期稳定性仍待补测，尚未发布 GitHub。详见[使用说明](/C:/Users/Kirito787/Documents/AI/DSH/sougou/outputs/2026-10-21/使用说明.md)。

> 两个现在方案底栏都是透明的这是为什么？还有搜狗输入法小米版原生支持底部的优化栏会随着皮肤而变化，方案A和方案B可以做到吗，研究时不要卸载搜狗输入法小米版！！！项目文件夹里有搜狗输入法小米版安装包

<details><summary>6 previous messages</summary>

> 我先查清两个方案底栏透明的原因，再对照小米版分析皮肤配色如何传给原生底栏。本次只读分析项目代码和安装包，不会卸载搜狗输入法小米版，也不会清除它的数据。
>
> <details><summary>Ran a command</summary>
>
> - Ran `Get-Content work/enhancer/src/com/sogouenhance/bottom/BottomHook.java -Raw; Get-Content 'C:\Users\Kirito787\.codex\skills\auto-prompt\SKILL.md' -Raw; Get-ChildItem work/xiaomi -Name; rg -n 'customizeBottomViewColor|setNavigationBarColor|bottomColor|setBottomColor' work/inventory/rom-phrase-bottom-disasm.txt work/inventory/rom-ime-disasm.txt work/inventory/actual-rom-bottom.md`
>
> </details>
>
> 透明原因已经定位：上一版适配代码把底栏背景色和导航栏颜色强制设为 `0`，也就是全透明；图标颜色只跟随系统深浅色，没有读取搜狗皮肤。这是我上一版实现造成的。
>
> 接下来按以下范围继续研究：
>
> ```text
> 目标：确认 A/B 能否像小米版一样随皮肤改变底栏。
> 输入：现有适配源码、项目内小米版 APK 和已解码代码。
> 要求：找出皮肤颜色到系统底栏的调用链，全程保留已安装小米版及其数据。
> 输出：有代码依据的可行性结论、适配位置和仍需验证的边界。
> ```
>
> <details><summary>Ran 6 commands</summary>
>
> - Ran `rg -n -l 'customizeBottomViewColor|setNavigationBarColor' work/xiaomi -g '*.smali'; rg -n -l 'customizeBottomViewColor|setNavigationBarColor' work/standard -g '*.smali'; Get-Content work/inventory/rom-phrase-bottom-disasm.txt | Select-Object -Skip 2075 -First 115; Get-Content work/inventory/rom-ime-disasm.txt | Select-Object -Skip 122 -First 44; git status --short --untracked-files=no`
> - Ran `Get-Content work/xiaomi/smali_classes2/com/sogou/inputmethod/oem/xiaomi/screen/j.smali -Raw; Get-Content work/standard/smali_classes5/com/sohu/util/k.smali | Select-String -Pattern 'setNavigationBarColor|\.method ' -Context 8,8; rg -n 'Lcom/sogou/inputmethod/oem/xiaomi/screen/j;->' work/xiaomi -g '*.smali' | Select-Object -First 35`
> - Ran `python -c "from pathlib import Path; import re; p=Path('work/xiaomi/smali_classes2/com/sogou/inputmethod/oem/xiaomi/screen/j.smali').read_text(); ms=re.findall(r'(?ms)^\.method .*?^\.end method',p); print('\n'.join(m for m in ms if re.search(r'\.method .* (?:u|r|p)\(',m.splitlines()[0]))); p=Path('work/standard/smali_classes5/com/sohu/util/k.smali').read_text(); print(next(m for m in re.findall(r'(?ms)^\.method .*?^\.end method',p) if ' b(' in m.splitlines()[0])))"; Get-Content 'work/xiaomi/smali_classes2/com/sogou/inputmethod/oem/xiaomi/theme/i$a.smali' -TotalCount 130; Get-Content work/xiaomi/smali_classes2/com/sogou/inputmethod/oem/xiaomi/window/b.smali | Select-Object -Skip 95 -First 75; rg -n 'Lcom/sohu/util/k;->b\(Landroid/content/Context;Landroid/view/Window;\)V' work/standard -g '*.smali'`
> - Ran `@'
> from pathlib import Path
> import re
> for file, names in [
>  ('work/xiaomi/smali_classes2/com/sogou/inputmethod/oem/xiaomi/screen/j.smali', ['u','r','p']),
>  ('work/standard/smali_classes5/com/sohu/util/k.smali',['b'])
> ]:
>     text=Path(file).read_text(encoding='utf-8')
>     for m in re.findall(r'(?ms)^\.method .*?^\.end method',text):
>         if any(' '+n+'(' in m.splitlines()[0] for n in names):
>             print(file+'\n'+m)
> '@ | python -`
> - Ran `@'
> from pathlib import Path
> import re
> items=[('work/standard/smali_classes3/com/sogou/theme/settings/a.smali',['f']),('work/standard/smali_classes5/com/sohu/inputmethod/ui/s.smali',['c','g'])]
> for f,names in items:
>  p=Path(f)
>  if not p.exists():
>   matches=list(Path('work/standard').glob('smali*/'+f.split('/smali_classes5/')[-1])); print('lookup',str(p),[str(x) for x in matches]); continue
>  text=p.read_text(encoding='utf-8')
>  for m in re.findall(r'(?ms)^\.method .*?^\.end method',text):
>   if any(' '+n+'(' in m.splitlines()[0] for n in names): print(f+'\n'+m[:6500])
> for f in ['work/standard/smali_classes2/com/sogou/bu/input/lifecycle/v.smali','work/standard/smali_classes2/com/sogou/bu/input/keyboard/d.smali']:
>  text=Path(f).read_text(encoding='utf-8')
>  for m in re.findall(r'(?ms)^\.method .*?^\.end method',text):
>   if 'Lcom/sohu/util/k;->b(' in m: print('caller',f,m.splitlines()[0])
> '@ | python -; Get-Content work/xiaomi/apktool.yml -TotalCount 8; rg -n 'param.args\[1\] = 0|param.args\[0\] = 0|invoke\(null, true, 0|private static void color' work/enhancer/src/com/sogouenhance/bottom/BottomHook.java; rg -n '^\.method.* (c|u|v)\(|NavigationBar getNavigationBarColor: third|updateMiuiBottomColor: third|ThemeColorInt|"#FF"|customizeBottomViewColor' work/xiaomi/smali_classes2/com/sogou/inputmethod/oem/xiaomi/screen/j.smali; rg -n '^\.method.* b\(|theme/settings/a;->f\(I\)|setNavigationBarColor' work/standard/smali_classes5/com/sohu/util/k.smali`
> - Ran `@'
> from pathlib import Path
> import zipfile,hashlib
> p=Path('搜狗输入法小米.apk')
> with zipfile.ZipFile(p) as z:
>  for name in z.namelist():
>   if name.endswith('.dex'):
>    b=z.read(name)
>    if b'NavigationBar updateMiuiBottomColor: third' in b:
>     print('APK:',p.name,'DEX:',name,'skin_color_path_present:',b'customizeBottomViewColor' in b and b'getThemeColorInt' in b)
> print('SHA256:',hashlib.sha256(p.read_bytes()).hexdigest())
> '@ | python -; rg -n 'theme.*settings.*a|navigation_bar|navigation.*color' work/standard/smali_classes2/com/sogou/theme/settings/a.smali | Select-Object -First 12`
>
> </details>
>
> 已找到关键调用链。小米版会从当前皮肤取得背景色、图标正常色和按下色，再主动调用系统的 `customizeBottomViewColor` 更新底栏。
>
> 普通版也有自己的皮肤导航栏配色计算；上一版模块却把它算出的颜色覆盖成了透明。因此 A、B 都有明确的适配路径，可以共用一套修正逻辑。还需要在切换皮肤、深浅色和键盘布局时验证刷新是否完整。
>
> <details><summary>Created a file</summary>
>
> - Wrote `./work/enhancer/research/skin-follow-20261021.md` (+72 -0)
>
> </details>
</details>

**透明是我上一版适配代码造成的。**代码在三处把底栏背景色强制设为 `0`（全透明），图标也只跟随系统深浅色，覆盖了搜狗自身的皮肤配色。

**A、B 都可以做成随皮肤配色变化，技术路径已找到：**

- 小米版会读取皮肤颜色，再把背景色、图标正常色和按下色传给系统底栏。
- 普通版也有皮肤配色计算，可以将结果接入同一个系统接口。
- 两方案共用适配代码，可以一起修正，并补上换肤时的刷新。

目前只是完成研究，**现有 APK 尚未修正**；图片、渐变或动态背景能否完整延伸到底栏，还需另外验证。

本次没有操作手机，**没有卸载小米版，也没有修改其数据**。[研究记录](./work/enhancer/research/skin-follow-20261021.md)

> 好开始实现，并将之前的两版方案卸载装新版两版方案

<details><summary>36 previous messages</summary>

> 我开始实现皮肤配色同步，重建方案 A 的增强模块和方案 B 的单 APK，然后卸载旧增强模块、旧 B 共存版，安装新版测试。小米版会保留；方案 A 的官方搜狗包版本不变，也会保留其数据。
>
> 这次继续使用 auto-git-branch 和 reverse-engineer-anything 技能，按已确认的皮肤配色调用链修改并验证。
>
> <details><summary>Ran 6 commands</summary>
>
> - Ran `git branch --show-current; git status --short --untracked-files=no; Get-Content work/enhancer/src/com/sogouenhance/bottom/BottomHook.java -Raw; Get-Content work/enhancer/build.py -Raw; Get-Content work/enhancer/package_b.py -Tail 75; Get-Content work/enhancer/export.py -TotalCount 120`
> - Ran `rg --files work/standard -g a.smali | Where-Object { $_ -match 'theme.settings' }; rg -n 'ThemeColorInt|themeColorInt|ThemeColor\(' work/standard -g '*.smali' -l | Select-Object -First 20; rg -n '\.method.* (c|m|r)\(' work/standard/smali_classes3/com/sogou/theme/impl/f.smali; Get-Content work/standard/smali_classes5/com/sohu/inputmethod/ui/d.smali | Select-String -Pattern '\.method.* k\(' -Context 0,60; Get-Content work/enhancer/probe/smali/local/sogou/enhancerprobe/ProbeActivity.smali -Raw`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'getprop sys.boot_completed; su -c id; settings get secure default_input_method; pm path com.sohu.inputmethod.sogou.xiaomi; pm path com.sohu.inputmethod.sogou.enhanced; pm path com.sogouenhance'`
> - Ran `@'
> from pathlib import Path
> import re
> p=Path('work/standard/smali_classes4/com/sogou/theme/settings/a.smali')
> for m in re.findall(r'(?ms)^\.method .*?^\.end method',p.read_text(encoding='utf-8')):
>  if any(' '+n+'(' in m.splitlines()[0] for n in ['f','I','r']): print(m[:5000])
> p=Path('work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java').read_text(encoding='utf-8').splitlines()
> print('\n'.join(p[560:630]))
> '@ | python -; rg --files work/standard -g f.smali | Where-Object { $_ -match 'theme.impl' }; rg -n 'pref.*navigation|navigation.*color|nav.*color|Navigation.*Color' work/standard/smali_classes4/com/sogou/theme/settings/a.smali; Get-Content work/standard/smali_classes2/com/sogou/bu/input/keyboard/d.smali | Select-Object -Skip 200 -First 60`
> - Ran `rg -n '0x7f1010c4' work/standard/res/values/public.xml; rg -n '\.method.*(\)I|\)V)' work/standard/smali_classes4/com/sogou/theme/impl/f.smali | Select-Object -First 40; Get-Content work/standard/smali_classes5/com/sohu/inputmethod/ui/s.smali -TotalCount 125; Get-Content work/standard/smali_classes5/com/sohu/inputmethod/ui/c.smali | Select-String -Pattern '\.method.* b\(IZZZ' -Context 0,70; Get-ChildItem work/enhancer/research -Name`
> - Ran `rg -n -A 14 '\.method public.*getThemeColorInt\(' work/xiaomi -g '*.smali'; @'
> from pathlib import Path
> import re
> p=Path('work/standard/smali_classes5/com/sohu/inputmethod/ui/s.smali')
> for m in re.findall(r'(?ms)^\.method .*?^\.end method',p.read_text(encoding='utf-8')):
>  if ' h(' in m.splitlines()[0]: print(m)
> p=Path('work/standard/smali_classes4/com/sogou/theme/impl/f.smali')
> for m in re.findall(r'(?ms)^\.method .*?^\.end method',p.read_text(encoding='utf-8')):
>  if ' m(' in m.splitlines()[0] or ' l(' in m.splitlines()[0]: print(m[:1300])
> '@ | python -; rg -n '<string name="c6e"' work/standard/res/values/strings.xml`
>
> </details>
>
> 这次会直接读取搜狗当前皮肤的底栏色和图标色，去掉三处强制透明，并在底栏创建、重新弹出键盘、换肤和深浅色变化时刷新。颜色更新会限定在输入法窗口，避免设置页或登录页影响键盘。
>
> 我也会补测切换配色后的背景透明度和图标可读性，再安装新版。
>
> <details><summary>Created 3 files, edited 2 files, ran 10 commands</summary>
>
> - Wrote `./work/enhancer/build.py` (+2 -2)
> - Wrote `./work/enhancer/src/com/sogouenhance/bottom/BottomHook.java` (+80 -19)
> - Wrote `./work/enhancer/src/com/sogouenhance/bottom/SkinPalette.java` (+101 -0)
> - Ran `python work/enhancer/build.py *> work/enhancer/build-skin-log.txt; if ($LASTEXITCODE -eq 0) { python work/enhancer/package_b.py *> work/enhancer/single-skin-log.txt }; Get-Content work/enhancer/build-skin-log.txt -Tail 8; Get-Content work/enhancer/single-skin-log.txt -Tail 8 -ErrorAction SilentlyContinue`
> - Ran `Get-Content work/enhancer/build-skin-log.txt -Tail 10; Get-Content work/enhancer/single-skin-log.txt -Tail 12 -ErrorAction SilentlyContinue; New-Item -ItemType Directory -Force work/enhancer/skin-test | Out-Null`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "du -sh /data/user/0/com.sogouenhance /data/user/0/com.sohu.inputmethod.sogou.enhanced"; dumpsys package com.sogouenhance | grep -E "versionCode|versionName"; pm path com.sohu.inputmethod.sogou.xiaomi'`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'am force-stop com.sogouenhance; am force-stop com.sohu.inputmethod.sogou.enhanced; su -c "mkdir -p /data/local/tmp/sogou-skin-120-backup; test ! -f /data/local/tmp/sogou-skin-120-backup/user-data.tgz || exit 1; tar -czf /data/local/tmp/sogou-skin-120-backup/user-data.tgz -C /data/user/0 com.sogouenhance com.sohu.inputmethod.sogou.enhanced; tar -tzf /data/local/tmp/sogou-skin-120-backup/user-data.tgz >/dev/null; chmod 644 /data/local/tmp/sogou-skin-120-backup/user-data.tgz; cp -a /data/adb/lspd/config/modules_config.db* /data/local/tmp/sogou-skin-120-backup/; chmod 644 /data/local/tmp/sogou-skin-120-backup/modules_config.db*; du -h /data/local/tmp/sogou-skin-120-backup/user-data.tgz"'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /data/local/tmp/sogou-skin-120-backup work/enhancer/skin-test/`
> - Wrote `./work/enhancer/tests/palette_check.py` (+69 -0)
> - Ran `python work/enhancer/tests/palette_check.py`
> - Ran `Get-Content work/enhancer/build/modules.json; Get-Content work/enhancer/build/single.json; Get-ChildItem work/enhancer/skin-test/sogou-skin-120-backup -ErrorAction SilentlyContinue | Select-Object Name,Length; python -c "import zipfile,json; m=json.load(open('work/enhancer/build/modules.json')); s=json.load(open('work/enhancer/build/single.json')); a=zipfile.ZipFile(m['a']['apk']); b=zipfile.ZipFile(s['apk']); print('A CRC',a.testzip(),'B CRC',b.testzip()); print('B embedded count',len([n for n in b.namelist() if n.startswith('assets/npatch/modules/')]))"`
> - Ran `python -c "import tarfile,collections; t=tarfile.open('work/enhancer/skin-test/sogou-skin-120-backup/user-data.tgz'); c=collections.Counter('/'.join(n.split('/')[:2]) for n in t.getnames() if '/' in n); print('\n'.join(str(x) for x in c.most_common(18)))"`
> - Wrote `./work/enhancer/skin-test/reinstall-120.sh` (+38 -0)
> - Ran `$taskModules=Get-Content work/enhancer/build/modules.json -Raw | ConvertFrom-Json; $taskSingle=Get-Content work/enhancer/build/single.json -Raw | ConvertFrom-Json; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push $taskModules.a.apk /data/local/tmp/sogou-enhancer-120.apk; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push $taskSingle.apk /data/local/tmp/sogou-single-120.apk; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push work/enhancer/skin-test/reinstall-120.sh /data/local/tmp/sogou-reinstall-120.sh; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "sh /data/local/tmp/sogou-reinstall-120.sh"'`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'pm path com.sogouenhance' | Set-Content work/enhancer/skin-test/module-path.txt; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'dumpsys package com.sogouenhance | grep -E "versionCode|versionName"; pm path com.sohu.inputmethod.sogou.xiaomi; am start -n com.sohu.inputmethod.sogou.enhanced/com.sogouenhance.SettingsActivity; ime enable com.sohu.inputmethod.sogou.enhanced/com.sohu.inputmethod.sogou.SogouIME; ime set com.sohu.inputmethod.sogou.enhanced/com.sohu.inputmethod.sogou.SogouIME; am start -n local.sogou.enhancerprobe/.ProbeActivity'`
> - Ran `@'
> from pathlib import Path
> import sqlite3
> base=Path('work/enhancer/skin-test')
> src=sqlite3.connect(base/'sogou-skin-120-backup/modules_config.db')
> print('backup integrity:',src.execute('pragma integrity_check').fetchone())
> dst=sqlite3.connect(base/'enabled-120.db'); src.backup(dst); src.close()
> path=next(x.split('package:',1)[1].strip() for x in (base/'module-path.txt').read_text(encoding='utf-8-sig').splitlines() if x.startswith('package:'))
> dst.execute('INSERT OR REPLACE INTO modules VALUES (?,?)',('com.sogouenhance',path))
> dst.execute('INSERT OR REPLACE INTO modules_state VALUES (?,0,1,0)',('com.sogouenhance',))
> dst.execute('INSERT OR IGNORE INTO scope VALUES (?,?,0)',('com.sogouenhance','com.sohu.inputmethod.sogou'))
> dst.commit(); print('new module path registered:',path); dst.close()
> '@ | python -`
>
> </details>
>
> 新版增强模块 1.2.0 和新版 B 共存 APK 已完成卸载重装，旧设置、词库和皮肤文件已从备份恢复。重装前后核对过：小米版和官方普通版的安装路径均未变化。
>
> 换肤取色、透明度合成、图标对比度等 11 项行为检查已通过。现在验证手机上底栏实际采用的颜色。
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'uiautomator dump /sdcard/sogou-skin-b.xml; screencap -p /sdcard/sogou-skin-b.png; dumpsys input_method | grep -E "mCurId=|mInputShown="'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-skin-b.png work/enhancer/skin-test/b-initial.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -s NPatchLegacyBridge > work/enhancer/skin-test/b-initial.log; Select-String -Path work/enhancer/skin-test/b-initial.log -Pattern 'SogouBottom.*(SKIN|FAIL|READY)|SogouEmbedded.*HIT' | Select-Object -Last 16`
>
> </details>
>
> Viewed an image
>
> 新版 B 的底栏已显示为不透明的皮肤色，日志也记录到配色变化。为启用新版 A 并验证两版换肤，我需要软重启一次、短暂切换测试页；现在方便留出约 3–5 分钟吗？
> - 现在可以，继续自动测试
> - 先别操作手机，保留已安装新版
>
> **新版 B 的底栏已显示为不透明的皮肤色，日志也记录到配色变化。为启用新版 A 并验证两版换肤，我需要软重启一次、短暂切换测试页；现在方便留出约 3–5 分钟吗？**
>
> 现在可以，继续自动测试
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 push work/enhancer/skin-test/enabled-120.db /data/local/tmp/sogou-enabled-120.db; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'cmd uimode night; settings get secure default_input_method; su -c "/data/adb/modules/zygisk_lsposed/lspctl stop; cp /data/local/tmp/sogou-enabled-120.db /data/adb/lspd/config/modules_config.db; rm -f /data/adb/lspd/config/modules_config.db-wal /data/adb/lspd/config/modules_config.db-shm; chown root:root /data/adb/lspd/config/modules_config.db; chmod 600 /data/adb/lspd/config/modules_config.db; ksud soft-reboot"'`
> - Ran `git diff --stat; Get-Content work/enhancer/skin-test/b-initial.log | Select-String -Pattern '\[SogouBottom\] SKIN' | ForEach-Object { $_.Line }; python -c "import sqlite3; db=sqlite3.connect('work/enhancer/skin-test/enabled-120.db'); print('module states',db.execute('select module_pkg_name,enabled from modules_state').fetchall()); print('target scopes',db.execute('select * from scope where app_pkg_name like ?',('com.sohu.inputmethod.sogou%',)).fetchall())"`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'getprop sys.boot_completed; input keyevent KEYCODE_WAKEUP; wm dismiss-keyguard; am start -n com.sogouenhance/.SettingsActivity; ime set com.sohu.inputmethod.sogou/.SogouIME; am force-stop local.sogou.enhancerprobe; am start -n local.sogou.enhancerprobe/.ProbeActivity'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'uiautomator dump /sdcard/skin-a-light.xml; screencap -p /sdcard/skin-a-light.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/skin-a-light.png work/enhancer/skin-test/a-light.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -s LSPosedFramework > work/enhancer/skin-test/a-light.log; Select-String -Path work/enhancer/skin-test/a-light.log -Pattern 'SogouBottom.*(SKIN|skin palette|READY)' | Select-Object -Last 8`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'cmd uimode night yes; uiautomator dump /sdcard/skin-a-dark.xml; screencap -p /sdcard/skin-a-dark.png; dumpsys input_method | grep -E "mCurId=|mInputShown="'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/skin-a-dark.png work/enhancer/skin-test/a-dark.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -s LSPosedFramework > work/enhancer/skin-test/a-dark.log; Select-String -Path work/enhancer/skin-test/a-dark.log -Pattern 'SogouBottom.*(SKIN|skin palette)' | Select-Object -Last 5`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `@'
> import xml.etree.ElementTree as E
> r=E.parse('work/standard/AndroidManifest.xml')
> key='{http://schemas.android.com/apk/res/android}name'
> print('\n'.join(n.get(key) for n in r.iter('activity') if any(x in n.get(key,'') for x in ['ThemeLocal','MainSkin','ThemeSetting','ThemeList','SkinList'])))
> '@ | python -`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'cmd uimode night no; uiautomator dump /sdcard/skin-a-final.xml; screencap -p /sdcard/skin-a-final.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/skin-a-final.png work/enhancer/skin-test/a-final.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'ime set com.sohu.inputmethod.sogou.enhanced/com.sohu.inputmethod.sogou.SogouIME; am start -n com.sohu.inputmethod.sogou.enhanced/com.sogou.theme.MainSkinActivity'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'uiautomator dump /sdcard/skin-b-theme.xml; screencap -p /sdcard/skin-b-theme.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/skin-b-theme.png work/enhancer/skin-test/b-theme.png`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "am start -n com.sohu.inputmethod.sogou.enhanced/com.sogou.theme.MainSkinActivity"'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'uiautomator dump /sdcard/skin-b-theme.xml; screencap -p /sdcard/skin-b-theme.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/skin-b-theme.png work/enhancer/skin-test/b-theme.png; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/skin-b-theme.xml work/enhancer/skin-test/b-theme.xml`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'input tap 1120 225; uiautomator dump /sdcard/skin-b-local.xml; screencap -p /sdcard/skin-b-local.png'; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/skin-b-local.png work/enhancer/skin-test/b-local.png`
>
> </details>
>
> Viewed an image
>
> Context compaction
>
> Source: automatic
> Status: completed
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 890 1750`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/sogou-preview.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-preview.png work/enhancer/skin-test/b-preview.png`
>
> </details>
>
> Viewed an image
>
> 新版 A、B 已完成替换安装，底栏已显示为不透明的皮肤色。正在完成最后的换肤验证；随后会恢复原来的皮肤和默认输入法，搜狗小米版保持不动。
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input keyevent 4
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 310 650
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/sogou-preview.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-preview.png work/enhancer/skin-test/b-preview2.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 890 1750
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/skin.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/sogou-preview.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-preview.png work/enhancer/skin-test/b-preview3.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `Get-Content work/enhancer/export.py -TotalCount 250
> Get-Content work/enhancer/README.md -TotalCount 100
> Get-Content .scratch/sogou-enhancer/issues/01-acceptance.md`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input keyevent 4
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 310 650
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/skin.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/sogou-preview.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-preview.png work/enhancer/skin-test/b-default-preview.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 310 650
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/skin.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/sogou-preview.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-preview.png work/enhancer/skin-test/b-default-preview2.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -v time | Select-String '\[SogouBottom\].*(SKIN|palette)' | Set-Content -Encoding utf8 work/enhancer/skin-test/skin-colors.log
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 85 210
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/skin.xml`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 890 650
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/skin.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/sogou-restored.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-restored.png work/enhancer/skin-test/b-restored.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `Get-Content work/enhancer/skin-test/skin-colors.log -Tail 20
> Get-Content work/enhancer/build/single.json
> Get-Content work/enhancer/tests/palette_check.py -TotalCount 30
>  git status --short -uno`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 1010 2470
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/skin.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -n local.sogou.enhancerprobe/.ProbeActivity
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/skin.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/sogou-restored.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-restored.png work/enhancer/skin-test/b-final.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -v time | Select-String '\[SogouBottom\].*(SKIN|palette)' | Set-Content -Encoding utf8 work/enhancer/skin-test/skin-colors-final.log`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell cmd uimode night no
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input keyevent 3
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell settings get secure default_input_method
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pm path com.sohu.inputmethod.sogou.xiaomi
> Get-Content work/enhancer/skin-test/skin-colors-final.log`
> - Ran `Add-Type -AssemblyName System.Drawing
> foreach ($name in @('a-final.png','b-default-preview2.png','b-final.png')) { $img=[Drawing.Bitmap]::FromFile((Join-Path $PWD "work/enhancer/skin-test/$name")); "$name bottom="+$img.GetPixel(600,2470).ToArgb().ToString('x8'); $img.Dispose() }
> Get-Content work/enhancer/research/skin-follow-20261021.md -Tail 35
> Get-Content work/enhancer/skin-test/reinstall-120.sh -TotalCount 100
> Get-Content work/enhancer/tests/palette_check.py -Tail 15`
>
> </details>
>
> 真机已确认 B 的底栏会随换肤变化：默认皮肤为 `#F2F3F7`，恢复“霓虹”后变为 `#ECECEC`，截图像素与日志一致。A 当前皮肤的底栏也已确认不透明。手机已恢复小米输入法；现在整理新版安装包和测试记录。
>
> <details><summary>Created a file, edited 3 files, ran 4 commands</summary>
>
> - Wrote `./work/enhancer/export_skin.py` (+94 -0)
> - Ran `python work/enhancer/export_skin.py`
> - Wrote `./.scratch/sogou-enhancer/issues/01-acceptance.md` (+6 -0)
> - Wrote `./work/enhancer/README.md` (+24 -2)
> - Wrote `./work/enhancer/research/skin-follow-20261021.md` (+3 -1)
> - Ran `git diff --check
>  git diff --stat
> Get-Content work/enhancer/src/com/sogouenhance/bottom/SkinPalette.java -TotalCount 180`
> - Ran `git add -- .scratch/sogou-enhancer/issues/01-acceptance.md work/enhancer/README.md work/enhancer/build.py work/enhancer/src/com/sogouenhance/bottom/BottomHook.java work/enhancer/src/com/sogouenhance/bottom/SkinPalette.java work/enhancer/tests/palette_check.py work/enhancer/export_skin.py work/enhancer/research/skin-follow-20261021.md work/enhancer/skin-test/reinstall-120.sh outputs/2026-10-21-skin-1.2.0/使用说明.md outputs/2026-10-21-skin-1.2.0/测试记录.json outputs/2026-10-21-skin-1.2.0/SHA256SUMS.txt
>  git diff --cached --check
>  git diff --cached --stat`
> - Ran `git commit -m "fix: follow Sogou skin colors in native bottom bar"
>  git status --short -uno`
>
> </details>
</details>

已完成新版 1.2.0 安装与测试：

- 已卸载重装旧 A 增强模块、B 单 APK，并恢复备份数据。
- 底栏透明问题已修复；B 换肤变色已通过截图和日志核对，A 当前皮肤显示正常。
- **搜狗小米版未卸载、未清除数据**，默认输入法已恢复小米版。
- 图片、渐变和动态皮肤的完整延伸效果仍待验证。

产物：[方案 A（两个 APK）](./outputs/2026-10-21-skin-1.2.0/方案A) · [方案 B（一个 APK）](./outputs/2026-10-21-skin-1.2.0/方案B)

> 然后研究一下这个的皮肤解锁是怎么做到的，看能不能应用到方案AB里
>
> User context
>
> Attachments:
> - 搜狗输入法小米版-10.32.21.202608051602.apk: `./搜狗输入法/搜狗输入法小米版-10.32.21.202608051602.apk`

<details><summary>8 previous messages</summary>

> 我会用逆向分析技能检查这个小米版 APK，先确认它的皮肤解锁由哪些本地逻辑、账号状态或服务端校验控制，再判断能否适配到方案 A、B。分析会在项目副本中进行，保留手机上的小米版和数据。
>
> <details><summary>Ran a command</summary>
>
> - Ran `Get-Content C:/Users/Kirito787/.agents/skills/reverse-engineer-anything/SKILL.md -TotalCount 220
> Get-Content C:/Users/Kirito787/.codex/skills/auto-prompt/SKILL.md -TotalCount 160
> rg -n "sougou|搜狗" C:/Users/Kirito787/.codex/memories/MEMORY.md
> Get-Content AGENTS.md
> Get-Content docs/agents/issue-tracker.md
> Get-Content docs/agents/triage-labels.md
> Get-ChildItem work/xiaomi -Name`
>
> </details>
>
> 按 auto-prompt 技能，将任务明确为：
>
> ```text
> 目标：查明指定小米版 APK 的皮肤解锁机制，评估迁移到 A/B 的可行性。
> 要求：区分免费、已购买、会员、试用及修改后的本地判断；用代码证据支持结论。
> 边界：本轮先研究，不改装手机，不卸载或清除小米版。
> 交付：一份带代码位置、适配差异和未验证事项的研究记录。
> ```
>
> <details><summary>Ran 13 commands, called a tool</summary>
>
> - Ran `Get-Content docs/agents/issue-tracker.md
> Get-Content docs/agents/triage-labels.md
> Get-ChildItem work/xiaomi -Name
> Get-ChildItem work -Directory -Name
> rg -n -m 2 'unlock|isBuy|isPaid|isVip|skin_pay|SkinPay' work/xiaomi --glob '*.java' --glob '*Unlock*.smali' --glob '*Pay*.smali'`
>
> MCP tool call
>
> rea.inspect_android_package
>
> ```json
> {
>   "path": "C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法\\搜狗输入法小米版-10.32.21.202608051602.apk",
>   "detail": "summary"
> }
> ```
>
> Error: {"error":{"code":"capability_unavailable","category":"unsupported_provider","message":"Set REA_JADX_MCP_JAR to the absolute path of a caller-supplied jadx-headless-mcp 0.7.1 JAR. REA does not download or install it.","retryable":false,"remediation":{"action":"Set REA_JADX_MCP_JAR to the absolute path of a caller-supplied jadx-headless-mcp 0.7.1 JAR. REA does not download or install it."},"details":{"provider_id":"jadx","operation":"inspect_android_package","reason":"Set REA_JADX_MCP_JAR to the absolute path of a caller-supplied jadx-headless-mcp 0.7.1 JAR. REA does not download or install it.","diagnostics":{"jar_configured":false,"failure_kind":"jar","failure_code":"not_configured"}}}}
>
> - Ran `Get-Content work/xiaomi/apktool.yml -TotalCount 45
> Get-ChildItem work/tools -Name
> rg -n -i -l 'unlockskin|skinunlock|skin_unlock|skin_pay|isbuy|ispaid|isvip' work/xiaomi/smali* --glob '*.smali' | Select-Object -First 70`
>
> - Ran `Get-ChildItem 搜狗输入法 -Name
> Get-ChildItem work/tools/jadx-ready -Name
> rg -n 'apktool|jadx' work/enhancer/build.py | Select-Object -First 15
> rg -n -i -l 'unlockskin|skinunlock|skin_unlock|skin_pay|isbuy|ispaid|isvip' work/xiaomi --glob '*.smali' | Select-Object -First 50
> Get-Content C:/Users/Kirito787/.agents/skills/reverse-engineer-anything/references/connection-and-recovery.md -TotalCount 65`
>
> - Ran `New-Item -ItemType Directory -Force work/enhancer/research/skin-unlock | Out-Null
> & 'work/tools/jdk/jdk-21.0.12.1+1/bin/java.exe' '-Djava.io.tmpdir=C:/Users/Kirito787/Documents/AI/DSH/sougou/work/enhancer/tmp' -jar work/tools/apktool-fast.jar d '搜狗输入法/搜狗输入法小米版-10.32.21.202608051602.apk' -o work/enhancer/research/skin-unlock/apk -p work/framework -f > work/enhancer/research/skin-unlock/decode.log 2>&1`
>
> - Ran `rg --no-ignore -n -i -l 'unlockskin|skinunlock|skin_unlock|skin_pay|isbuy|ispaid|isvip' work/xiaomi --glob '*.smali' | Select-Object -First 45
> Get-Content work/enhancer/build.py -TotalCount 45
> Get-ChildItem work/xiaomi/smali -Name | Select-Object -First 10`
>
> - Ran `Get-Content work/enhancer/research/skin-unlock/decode.log -Tail 12
> Get-ChildItem work/xiaomi/smali_classes5/com -Name | Select-Object -First 15
> rg --no-ignore -n -m 3 'vip|price|pay' work/xiaomi/smali_classes5/com/sogou --glob '*.smali' | Select-Object -First 35
> rg --no-ignore --files work/xiaomi | Select-String 'Skin.*\.smali|skin.*pay|Vip.*\.smali' | Select-Object -First 35`
>
> - Ran `Get-FileHash '搜狗输入法/搜狗输入法小米版-10.32.21.202608051602.apk' -Algorithm SHA256
> Get-ChildItem work/tools/jadx-ready/lib -Name | Select-Object -First 10`
>
> - Ran `Get-Content work/enhancer/research/skin-unlock/apk/apktool.yml -TotalCount 20
> rg --no-ignore -n -i -l 'unlockskin|skinunlock|skin_unlock|skin_pay|isbuy|ispaid|isvip' work/enhancer/research/skin-unlock/apk --glob '*.smali' | Select-Object -First 55
> rg --no-ignore --files work/enhancer/research/skin-unlock/apk | Select-String 'Hook|xposed|lspatch|npatch|Skin.*Bean|Theme.*Bean' | Select-Object -First 45`
>
> - Ran `Get-Content work/xiaomi/smali_classes2/com/sogou/theme/operation/SmartThemeDetailModel\$SkinInfo.smali -TotalCount 10`
>
> - Ran `Get-Content 'work/xiaomi/smali_classes2/com/sogou/theme/operation/SmartThemeDetailModel$SkinInfo.smali' -TotalCount 55
> Get-Content 'work/enhancer/research/skin-unlock/apk/smali_classes2/com/sogou/theme/operation/SmartThemeDetailModel$SkinInfo.smali' -TotalCount 65
> Get-Content work/enhancer/research/skin-unlock/decode.log -Tail 8
> rg --no-ignore --files work/enhancer/research/skin-unlock/apk | Select-String -Pattern 'smali_classes6|xposed_init|npatch|lspatch' | Select-Object -First 10`
>
> - Ran `rg --no-ignore -n -i -m 2 'pay|buy|vip|unlock' work/enhancer/research/skin-unlock/apk/smali_classes2/com/sogou/theme | Select-Object -First 55
> Get-Content work/enhancer/research/skin-unlock/apk/smali_classes6/bin/mt/signature/KillerApplication665.smali -TotalCount 100
> rg -n 'application|versionName|versionCode' work/enhancer/research/skin-unlock/apk/AndroidManifest.xml | Select-Object -First 4
> Get-ChildItem work/enhancer/research/skin-unlock/apk/assets -Name | Select-Object -First 40`
>
> - Ran `Get-Content 'work/enhancer/research/skin-unlock/apk/assets/修改教程.md' -TotalCount 180
> Get-ChildItem work/enhancer/research/skin-unlock/apk/assets -Name | Select-String 'origin|Signature|dex|so$'
> rg --no-ignore -n -m 3 'KillerApplication|hj|signature' work/enhancer/research/skin-unlock/apk/smali_classes2/com/sohu/inputmethod/sogou/SogouTinkerApplication.smali
> Get-Content work/enhancer/research/skin-unlock/decode.log -Tail 6`
>
> - Ran `rg --no-ignore --files work/enhancer/research/skin-unlock/apk work/standard | Select-String '/SogouIMEPay.smali|\\SogouIMEPay.smali|ProductWithPrice.smali|PayManager.smali|SogouTinkerApplication.smali'
> Get-Content work/enhancer/research/skin-unlock/apk/apktool.yml -TotalCount 18
> Get-ChildItem 'work/enhancer/research/skin-unlock/apk/assets/origin665.apk' | Select-Object Length`
>
> </details>
>
> 这个 APK 内含一份修改说明，但我会把它当作待核实的材料。已确认包内有重签名兼容代码；说明声称，皮肤解锁通过修改价格、支付状态并直接触发支付成功回调实现。接下来会逐项核对实际代码，以及普通版 20.17 是否存在对应入口。
>
> <details><summary>Ran 12 commands</summary>
>
> - Ran `@'
> from pathlib import Path
> import re
> roots=[Path('work/enhancer/research/skin-unlock/apk'),Path('work/standard')]
> for root in roots:
>  for name in ['ProductWithPrice.smali','SogouIMEPay.smali','PayManager.smali']:
>   for p in root.rglob(name):
>    print('\nFILE',p)
>    txt=p.read_text(encoding='utf-8')
>    for m in re.finditer(r'(?m)^\.method .*\n[\s\S]*?^\.end method',txt):
>     sig=m.group().splitlines()[0]
>     if any(x in sig for x in [' getPrice(', ' getPayStatus(', ' x(', 'payWithSogouPayOrder(']):
>      print('LINE',txt.count('\n',0,m.start())+1,m.group()[:8500])
> print('STANDARD PAYMENT CANDIDATES')
> for p in Path('work/standard').rglob('*.smali'):
>  if any(x in str(p) for x in ['lib_pay','/pay/','\\pay\\']):
>   t=p.read_text(encoding='utf-8')
>   if 'payWithSogouPayOrder' in t or 'Lcom/sogou/sogou_router_base/base_bean/ProductInfo;ZLcom/sogou/sogou_router_base/callback/c;' in t:
>    print(p)
> '@ | python -`
> - Ran `rg -n 'KillerApplication|attachBaseContext|onCreate' work/enhancer/research/skin-unlock/apk/smali_classes3/com/sohu/inputmethod/sogou/SogouTinkerApplication.smali
> rg --no-ignore -n 'getPayStatus\(|getPrice\(' work/standard/smali_classes2/com/sogou/bu --glob '*.smali' | Select-Object -First 40`
> - Ran `Get-Content work/standard/apktool.yml -TotalCount 18
> Get-Content work/standard/smali_classes2/com/sogou/bu/basic/pay/e.smali -TotalCount 240
> rg --no-ignore -n -l 'ProductInfo;|PayCallback;|payWithSogouPayOrder' work/standard --glob '*.smali' | Select-Object -First 45
> Get-Content work/enhancer/research/skin-unlock/apk/smali_classes3/com/sohu/inputmethod/sogou/SogouTinkerApplication.smali -TotalCount 120
> Get-Content 'work/enhancer/research/skin-unlock/apk/smali_classes2/com/sogou/theme/SmartThemeSkinDetailActivity$j.smali' -TotalCount 170`
> - Ran `rg --no-ignore -n -i -l 'paystatus|pay_status|payment/create|sogoupay|paywith' work/standard/smali_classes2/com/sogou work/standard/smali_classes4/com/sogou --glob '*.smali' | Select-Object -First 65
> rg --no-ignore -n -l 'KillerApplication665' work/enhancer/research/skin-unlock/apk --glob '*.smali'
> Get-Content 'work/enhancer/research/skin-unlock/apk/smali_classes2/com/sogou/theme/SmartThemeSkinDetailActivity$f.smali' -TotalCount 150
> Get-Content work/standard/smali_classes2/com/sogou/bu/basic/pay/ProductWithPrice.smali -TotalCount 150`
> - Ran `& 'work/tools/jdk/jdk-21.0.12.1+1/bin/java.exe' '-Djava.io.tmpdir=C:/Users/Kirito787/Documents/AI/DSH/sougou/work/enhancer/tmp' -jar work/tools/apktool-fast.jar d work/enhancer/research/skin-unlock/apk/assets/origin665.apk -r -o work/enhancer/research/skin-unlock/origin -p work/framework > work/enhancer/research/skin-unlock/origin-decode.log 2>&1`
> - Ran `rg -n 'onSuccess|\.method|payment|ProductWithPrice|Lcom/sogou/.*/pay/|drm|license|download' 'work/enhancer/research/skin-unlock/apk/smali_classes2/com/sogou/theme/SmartThemeSkinDetailActivity$f.smali' | Select-Object -Last 20
> rg -n 'ProductWithPrice|payment|pay/|PayStatus|drm|license' work/standard/smali_classes4/com/sogou/theme/SmartThemeSkinDetailActivity.smali | Select-Object -First 55
> Get-Content work/standard/smali_classes4/com/sogou/inputmethod/pay/i.smali -TotalCount 130
> Get-Content work/enhancer/research/skin-unlock/origin-decode.log -Tail 10
> Get-Content work/enhancer/research/skin-unlock/apk/smali_classes4/com/tencent/tinker/loader/app/TinkerApplication.smali -TotalCount 12`
> - Ran `Get-Content work/enhancer/research/skin-unlock/origin/apktool.yml -TotalCount 20
> Get-Content 'work/enhancer/research/skin-unlock/apk/smali_classes2/com/sogou/theme/SmartThemeSkinDetailActivity$f.smali' | Select-Object -Skip 195 -First 160
> Get-Content work/standard/smali_classes4/com/sogou/inputmethod/pay/i.smali | Select-Object -Skip 285 -First 210
> Get-ChildItem work/standard/smali_classes4/com/sogou/inputmethod/pay/intercept -Name
> rg -n 'ProductWithPrice|drm|token|license|asset|https?://' work/standard/smali_classes4/com/sogou/theme/network/c.smali | Select-Object -First 35`
> - Ran `rg -n 'drm|Drm|payment|PayInfo|asset|https|onSuccess' work/standard/smali_classes4/com/sogou/inputmethod/pay/intercept/*.smali | Select-Object -First 100`
> - Ran `rg -n 'drm|Drm|payment|PayInfo|asset|https|onSuccess' work/standard/smali_classes4/com/sogou/inputmethod/pay/intercept --glob '*.smali' | Select-Object -First 90
> rg -n 'drm|Drm|license|token' work/standard/smali_classes2/com/sogou/bu/basic/pay/PayInfoBean.smali
> Get-Content work/enhancer/research/skin-unlock/origin-decode.log -Tail 6`
> - Ran `rg -n '^def |version|StringPool' work/enhancer/package_b.py | Select-Object -First 45
> Get-Content work/standard/smali_classes4/com/sogou/inputmethod/pay/intercept/p.smali -TotalCount 155
> rg -n 'https|drm|Drm|license|order|token' work/standard/smali_classes4/com/sogou/inputmethod/pay/midas --glob '*.smali' | Select-Object -First 35
> Get-Content work/standard/smali_classes4/com/sogou/inputmethod/pay/midas/a.smali -TotalCount 100
> rg -n 'onSuccess|onError|\.method' work/standard/smali_classes4/com/sogou/theme/SmartThemeSkinDetailActivity\$*.smali`
> - Ran `Get-Content work/standard/smali_classes4/com/sogou/inputmethod/pay/e.smali -TotalCount 300
> rg -n -- '-0x64|-0x6e|isMultiPay|bu/basic/pay/e;->c|query_order' work/standard/smali_classes4/com/sogou/inputmethod/pay work/standard/smali_classes4/com/sogou/theme --glob '*.smali' | Select-Object -First 30`
> - Ran `@'
> from pathlib import Path
> import re,hashlib,zipfile
> root=Path('work/enhancer/research/skin-unlock')
> for name in ['apk/assets/origin665.apk']:
>  p=root/name
>  with zipfile.ZipFile(p) as z:
>   b=z.read('AndroidManifest.xml')
>   print('ORIGIN',hashlib.sha256(p.read_bytes()).hexdigest(),re.findall(rb'10\.32\.21\.[0-9]+',b))
> for rel in ['com/sogou/bu/basic/pay/ProductWithPrice.smali','com/sogou/inputmethod/lib_pay/SogouIMEPay.smali','com/sogou/pay/sdk/PayManager.smali']:
>  p=next((root/'origin').glob('smali*/'+rel))
>  print('ORIGIN FILE',p)
>  t=p.read_text(encoding='utf-8')
>  for m in re.finditer(r'(?m)^\.method .*\n[\s\S]*?^\.end method',t):
>   sig=m.group().splitlines()[0]
>   if any(s in sig for s in [' getPrice(', ' getPayStatus(', ' x(', 'payWithSogouPayOrder(']):
>    print('LINE',t.count('\n',0,m.start())+1,'SIGNATURE',sig,'LINES',len(m.group().splitlines()))
>    if 'getPrice(' in sig or 'getPayStatus(' in sig:print(m.group())
> '@ | python -
> Get-Content work/standard/smali_classes4/com/sogou/theme/SmartThemeSkinDetailActivity.smali | Select-Object -Skip 2590 -First 115
> rg -n 'payment|price|pay_status|paystatus|drm|trial|try_|vip' work/standard/smali_classes2/com/sogou/home/theme/bean/SmartThemeDetailModel.smali | Select-Object -First 35`
>
> </details>
>
> 代码核对已确认上述四处修改，且与 APK 内附原包存在实际差异。
>
> 普通版 20.17 的支付流程已换成 Midas，原来的两个支付入口不存在，不能直接照搬。它仍保留商品价格和支付状态接口，因此 A、B 有继续适配的技术基础；但仅把价格改成 0，会进入单独的结果分支，不能据此认定解锁成功。当前结论也不支持“服务端会员已解锁”或“所有皮肤永久可用”。
>
> <details><summary>Created 2 files, ran 3 commands</summary>
>
> - Wrote `./work/enhancer/research/skin-unlock/collect_evidence.py` (+61 -0)
>
> - Ran `python work/enhancer/research/skin-unlock/collect_evidence.py`
>
> - Wrote `./work/enhancer/research/skin-unlock-20261021.md` (+93 -0)
>
> - Ran `git diff --check
> Get-Item work/enhancer/research/skin-unlock/evidence.json | Select-Object Length
>  git status --short -uno`
>
> - Ran `git add -- work/enhancer/research/skin-unlock-20261021.md work/enhancer/research/skin-unlock/collect_evidence.py work/enhancer/research/skin-unlock/evidence.json
>  git diff --cached --check
>  git commit -m "docs: analyze Xiaomi skin payment modifications and port feasibility"`
>
> Tool call
>
> Tool: open_in_codex
> Status: completed
>
> </details>
</details>

已查明：这个 APK 的皮肤解锁主要通过四处客户端修改实现：

- 商品价格固定返回 `0`。
- 支付状态固定返回“已支付”。
- 两个支付入口直接触发成功回调。

**A、B 有适配基础，但不能直接照搬。** 普通版 20.17 已更换支付流程，需要重新适配；仅修改价格不足以保证解锁，也不能据此认定服务端会员权益或全部皮肤永久可用。

本轮仅做离线研究，未改动 A/B 安装包，**小米版未卸载、数据未动**。

详细证据：[研究记录](./work/enhancer/research/skin-unlock-20261021.md)。

> AB方案哪个可以解锁皮肤？还有目前我测试下来好像只有B方案完成度很高，而A方案两个软件打开都是模块界面无法进入输入法的正常界面

<details><summary>4 previous messages</summary>

> 目前 A、B 都还没有加入皮肤解锁；上一轮只完成了机制研究。
>
> A 的两个入口都打开模块界面，与你预期的正常行为不符。我会核对官方包、增强模块的桌面入口和模块跳转逻辑，并与 B 对比，定位原因。
>
> <details><summary>Ran 7 commands</summary>
>
> - Ran `git status --short -uno
> Get-Content work/enhancer/src/com/sogouenhance/HookEntry.java -TotalCount 220
> rg --no-ignore -n 'SettingsActivity|Launcher|launch|setClassName|MAIN|CATEGORY_LAUNCHER|SogouIME' work/enhancer/src work/enhancer/baseline-jadx/sources/com/sogouenhance --glob '*.java' | Select-Object -First 85
> Get-Content work/enhancer/build.py | Select-Object -Skip 65 -First 75`
> - Ran `rg -n 'openModuleSettings|Splash|onCreate|setResult|finish|replaceHookedMethod' work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java | Select-Object -Last 65
> Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java | Select-Object -Skip 820 -First 190
> rg -n -C 5 'MAIN|LAUNCHER|LauncherAlias' work/standard/AndroidManifest.xml work/enhancer/module-a/AndroidManifest.xml
> Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/Prefs.java -TotalCount 95`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell cmd package resolve-activity --brief -a android.intent.action.MAIN -c android.intent.category.LAUNCHER com.sohu.inputmethod.sogou
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell cmd package resolve-activity --brief -a android.intent.action.MAIN -c android.intent.category.LAUNCHER com.sogouenhance`
> - Ran `Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java | Select-Object -Skip 50 -First 110
> Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java | Select-Object -Skip 925 -First 35
> rg -n -C 2 'MAIN|LAUNCHER|activity' work/enhancer/module-a/AndroidManifest.xml | Select-Object -First 30
> rg -n 'SogouIMELauncher|finish|startActivity|MainActivity' work/standard/smali_classes5/com/sohu/inputmethod/sogou/SogouIMELauncher.smali | Select-Object -First 45`
> - Ran `Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java | Select-Object -Skip 925 -First 37
> Get-Content work/standard/smali_classes5/com/sohu/inputmethod/sogou/SogouIMELauncher.smali | Select-Object -Skip 395 -First 122
> Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/HookEntry.java | Select-Object -Skip 145 -First 25`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -v time | Select-String 'START u0.*(sogou|sogouenhance)|已打开模块设置|模块设置入口被点击|挂钩设置' | Select-Object -Last 28
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell dumpsys activity activities | Select-String 'mResumedActivity|topResumedActivity' | Select-Object -Last 3`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -n com.sohu.inputmethod.sogou/.SogouIMELauncher
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/sogou-a-launch.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/sogou-a-launch.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-a-launch.png work/enhancer/skin-test/a-launch-check.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/sogou-a-launch.xml work/enhancer/skin-test/a-launch-check.xml`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `rg -n 'name="(dt2|app_name)"' work/standard/res/values/strings.xml work/enhancer/module-a/res/values/strings.xml work/enhancer/module-b/res/values/strings.xml
> Get-Content work/enhancer/skin-test/a-launch-check.xml -TotalCount 1 | ForEach-Object { [xml]$ui=$_; $ui.SelectNodes('//node') | Where-Object { $_.package -like '*sogou*' } | Select-Object -First 1 -Property package }
> Get-Content work/enhancer/build.py | Select-Object -Skip 108 -First 12`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input keyevent 3`
>
> </details>
</details>

**目前 A、B 都没有加入皮肤解锁。** 两者都有继续适配的基础；B 使用方便，但不代表它天然比 A 更能解锁皮肤。

A 正常应是两个不同入口：

| 应用 | 应打开的界面 |
|---|---|
| 搜狗输入法 | 官方首页、商城、词库等 |
| 搜狗输入法增强模块 | 增强功能设置 |

我刚在手机上直接启动 A 的官方入口，**成功进入了正常的装扮商城**，[查看截图](./work/enhancer/skin-test/a-launch-check.png)。因此，本次尚未复现“两个入口都进模块界面”，也不能把你遇到的问题算作已解决。

你对完成度的反馈有道理：此前 B 的验证更全面，A 主要验证了键盘和底栏，验证范围不够完整。后续应先补齐 A 的入口问题，再把皮肤适配加入两方案。

> 开始修缮方案A

<details><summary>39 previous messages</summary>

> 我会先核对方案 A 的桌面入口、首次启用流程和模块跳转，复现后修复，再验证官方首页、设置页及键盘功能。保留 B 和搜狗小米版，不清除它们的数据。
>
> <details><summary>Ran a command</summary>
>
> - Ran `Get-Content C:/Users/Kirito787/.codex/skills/auto-git-branch/SKILL.md -TotalCount 180
> Get-Content AGENTS.md
> Get-Content .scratch/sogou-enhancer/spec.md
> Get-Content work/enhancer/src/com/sogouenhance/bottom/BottomHook.java -TotalCount 240
> Get-Content work/enhancer/build.py -TotalCount 155
>  git status --short -uno`
>
> </details>
>
> 已确认 A 的官方入口能打开商城，模块入口本身则只进入增强设置。目前还没复现“两个入口都进模块页”的原因，但入口容易混淆的问题可以先修好。
>
> 我会按 auto-prompt、auto-git-branch 技能继续执行：
> ```text
> 目标：完善 A 的入口，并补齐实际操作验证。
> 改动：明确标识 A 模块，提供打开官方搜狗、增强设置和系统输入法设置的入口。
> 验收：冷启动、官方设置、模块跳转、中文输入、底栏与剪贴板。
> 约束：保留原增强功能，只更新 A；不改 B 和小米版。
> ```
>
> <details><summary>Created 2 files, edited a file, ran 7 commands</summary>
>
> - Ran `git rev-parse --is-inside-work-tree
>  git branch --show-current
> rg --files --no-ignore work | Select-String 'android.jar$|android-.*jar$|android.*stub|SettingsActivity.smali$' | Select-Object -First 35
> Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/SettingsActivity.java | Select-Object -First 115
> Get-Content docs/agents/domain.md`
> - Ran `git switch -c codex/sogou-a-launch-repair`
> - Ran `rg --files --no-ignore work/ads work/xposed work/device work/compat work/enhancer | rg '(android[^\\/]*\.jar$|stubs\.jar$|ProbeActivity.java$)'
> Get-ChildItem work/enhancer -Name
> Get-Content work/enhancer/probe/src/local/sogou/enhancerprobe/ProbeActivity.java -TotalCount 15`
> - Ran `Get-ChildItem work/enhancer/probe -Name
> Get-Content work/enhancer/baseline-apk/AndroidManifest.xml -TotalCount 25
> rg -n '增强|模块|onCreate' work/enhancer/baseline-apk/smali/com/sogouenhance/SettingsActivity.smali | Select-Object -First 16
> Get-Content work/enhancer/baseline-apk/res/values/styles.xml -TotalCount 40`
> - Wrote `./.scratch/sogou-enhancer/issues/02-a-launch-repair.md` (+14 -0)
> - Wrote `./work/enhancer/build.py` (+22 -4)
> - Wrote `./work/enhancer/companion-smali/com/sogouenhance/AHomeActivity.smali` (+135 -0)
> - Ran `python work/enhancer/build.py --variant a > work/enhancer/build-a-repair-log.txt 2>&1`
> - Ran `Get-Content work/enhancer/build-a-repair-log.txt -Tail 18
> Get-Content work/enhancer/probe/AndroidManifest.xml -TotalCount 25
> Get-Content work/enhancer/module-a/AndroidManifest.xml -TotalCount 18`
> - Ran `New-Item -ItemType Directory -Force work/enhancer/a-repair | Out-Null
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell settings get secure default_input_method > work/enhancer/a-repair/default-ime-before.txt
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pm path com.sohu.inputmethod.sogou com.sohu.inputmethod.sogou.enhanced com.sohu.inputmethod.sogou.xiaomi > work/enhancer/a-repair/protected-paths-before.txt
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "mkdir -p /data/local/tmp/sogou-a-121; tar -czf /data/local/tmp/sogou-a-121/module-data-before.tgz -C /data/user/0/com.sogouenhance shared_prefs"'
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /data/local/tmp/sogou-a-121/module-data-before.tgz work/enhancer/a-repair/module-data-before.tgz`
>
> </details>
>
> A 的新版模块已构建完成，签名和安装包对齐检查通过。桌面名称已改为“搜狗增强·方案A”，模块首页也增加了三个明确入口。
>
> 接下来只覆盖更新 A 模块并做真机验证，不卸载官方搜狗。
>
> <details><summary>Ran a command</summary>
>
> - Ran `$aRepair = (Get-Content work/enhancer/build/modules.json -Raw | ConvertFrom-Json).a.apk
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 install -r $aRepair
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am force-stop com.sogouenhance
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -n com.sogouenhance/.LauncherAlias
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/module-home.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/module-home.xml`
>
> </details>
>
> Viewed an image
>
> <details><summary>Edited a file, ran 4 commands</summary>
>
> - Ran `Get-Content work/enhancer/a-repair/default-ime-before.txt
> Get-Content work/enhancer/build/modules.json -TotalCount 25`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -t 1200 -v time | Select-String -Context 2,10 'FATAL EXCEPTION|VerifyError|AHomeActivity|NoSuchMethodError' | Select-Object -Last 75`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -v time | Select-String -Context 0,6 'Process: com.sogouenhance|AHomeActivity|Unable to start activity.*sogouenhance|VerifyError' | Select-Object -Last 60
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell dumpsys package com.sogouenhance | Select-String 'versionName|versionCode|enabledComponents|AHomeActivity|LauncherAlias' | Select-Object -First 12
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -W -n com.sogouenhance/.LauncherAlias`
> - Wrote `./work/enhancer/companion-smali/com/sogouenhance/AHomeActivity.smali` (+6 -0)
> - Ran `python work/enhancer/build.py --variant a > work/enhancer/build-a-repair-log.txt 2>&1`
>
> </details>
>
> 首次真机检查发现，新首页漏了必需的构造方法，导致启动退出；已修正并重新构建。这是本轮新增入口的问题，尚不能解释旧版的异常。
>
> 下一步继续检查三个按钮的实际跳转，并验证 A 的中文输入、模块设置和底栏。
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `Get-Content work/enhancer/build-a-repair-log.txt -Tail 7
> Get-Content work/enhancer/probe/smali/local/sogou/enhancerprobe/ProbeActivity.smali -TotalCount 130
> Get-Content work/enhancer/module-a/apktool.yml -TotalCount 14`
> - Ran `$aRepair = (Get-Content work/enhancer/build/modules.json -Raw | ConvertFrom-Json).a.apk
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 install --no-incremental -r $aRepair
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am force-stop com.sogouenhance
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -W -n com.sogouenhance/.LauncherAlias
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/module-home.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/module-home.xml`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am force-stop com.sohu.inputmethod.sogou
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 600 835
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/official-cold-launch.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/official-cold-launch.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pidof com.sohu.inputmethod.sogou`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/official-cold-launch.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/official-cold-launch.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell settings get secure default_input_method
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d --pid=25772 -v time | Select-String '\[SogouEnhance\]|FATAL EXCEPTION|SogouBottom' | Select-Object -Last 12`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input keyevent 4
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -n com.sogouenhance/.AHomeActivity
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 600 980
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/enhancement-settings.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/enhancement-settings.xml`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -W -n com.sogouenhance/.AHomeActivity
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 600 1125
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/system-ime-settings.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "am start -n com.sohu.inputmethod.sogou/.SogouIMESettings"'
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/official-settings.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/official-settings.xml`
>
> </details>
>
> Viewed an image
>
> <details><summary>Edited a file, ran 2 commands</summary>
>
> - Wrote `./work/enhancer/build.py` (+1 -1)
> - Ran `python work/enhancer/build.py --variant a > work/enhancer/build-a-repair-log.txt 2>&1`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 500 375
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/official-to-module.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -n local.sogou.enhancerprobe/.ProbeActivity
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/keyboard-before.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `@'
> from pathlib import Path
> import xml.etree.ElementTree as E
> for name in ['official-to-module.xml','system-ime-settings.xml']:
>  r=E.parse(Path('work/enhancer/a-repair')/name)
>  print(name,sorted(set(n.get('package') for n in r.iter('node'))))
>  print([(n.get('text'),n.get('bounds')) for n in r.iter('node') if n.get('text')][:9])
> '@ | python -
> Get-Content work/enhancer/build-a-repair-log.txt -Tail 4`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 715 2130
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 840 1970
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 660 1970
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 770 1805
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 300 1805
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/chinese-candidates.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input keyevent 67 67 67 67 67
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 790 2153
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 912 1805
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 671 1975
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 135 1975
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 1030 1805
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/chinese-candidates.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input swipe 1130 2153 1130 2153 1600
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 790 2153
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 912 1805
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 671 1975
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 135 1975
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 1030 1805
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/chinese-candidates.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `@'
> import xml.etree.ElementTree as E,json
> from pathlib import Path
> for name in ['official-to-module.xml','system-ime-settings.xml']:
>  r=E.parse(Path('work/enhancer/a-repair')/name)
>  print(name,sorted(set(n.get('package') for n in r.iter('node'))))
>  print(json.dumps([(n.get('text'),n.get('bounds')) for n in r.iter('node') if n.get('text')][:10],ensure_ascii=True))
> '@ | python -`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 120 1625
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/chinese-committed.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/chinese-committed.xml
> $aRepair = (Get-Content work/enhancer/build/modules.json -Raw | ConvertFrom-Json).a.apk
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 install --no-incremental -r $aRepair
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -W -n com.sogouenhance/.LauncherAlias
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/module-home-final.png`
>
> </details>
>
> Viewed an image
>
> 新版首页已能正常打开，A 也已在本地测试页实际输入拼音、产生“你好”候选并完成上屏。
>
> 复测还发现，再次打开模块时可能沿用上次的设置页任务栈；已调整为返回模块首页。现在核对最终安装包的三个入口和官方设置跳转。
>
> <details><summary>Ran 9 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 600 1125
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/system-ime-settings.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -W -n com.sogouenhance/.LauncherAlias
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 600 980
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/enhancement-settings-final.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -W -n com.sogouenhance/.LauncherAlias
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/reopen-module-home.xml`
> - Ran `@'
> from pathlib import Path
> import xml.etree.ElementTree as E
> for name in ['system-ime-settings.xml','enhancement-settings-final.xml','reopen-module-home.xml','chinese-committed.xml']:
>  r=E.parse(Path('work/enhancer/a-repair')/name)
>  print(name,sorted(set(n.get('package') for n in r.iter('node'))),[(n.get('text') or '').encode('unicode_escape').decode() for n in r.iter('node') if n.get('text')][:3])
> '@ | python -`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 600 835
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/official-home-final.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/official-home-final.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "am start -W -n com.sohu.inputmethod.sogou/.SogouIMESettings"'
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/official-settings-final.xml`
> - Ran `@'
> from pathlib import Path
> import xml.etree.ElementTree as E
> for name in ['official-home-final.xml','official-settings-final.xml']:
>  r=E.parse(Path('work/enhancer/a-repair')/name)
>  print(name,[(n.get('text','').encode('unicode_escape').decode(),n.get('bounds')) for n in r.iter('node') if n.get('text')][:4])
> '@ | python -`
> - Ran `@'
> import xml.etree.ElementTree as E
> r=E.parse('work/enhancer/a-repair/official-settings-final.xml')
> for n in r.iter('node'):
>  d=n.get('content-desc') or n.get('text')
>  if d: print(d.encode('unicode_escape').decode()[:120],n.get('bounds'),n.get('clickable'))
> '@ | python -`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 350 375
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/official-to-module-final.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pidof com.sohu.inputmethod.sogou:home`
> - Ran `@'
> import xml.etree.ElementTree as E
> r=E.parse('work/enhancer/a-repair/official-to-module-final.xml')
> print(sorted(set(n.get('package') for n in r.iter('node'))))
> print([(n.get('text','').encode('unicode_escape').decode(),n.get('bounds')) for n in r.iter('node') if n.get('text')][:3])
> '@ | python -`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -n local.sogou.enhancerprobe/.ProbeActivity
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 1050 2510
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/clipboard-private.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran 6 commands</summary>
>
> - Ran `Remove-Item -LiteralPath 'C:\Users\Kirito787\Documents\AI\DSH\sougou\work\enhancer\a-repair\clipboard-private.png'
> Get-Content work/enhancer/a-repair/protected-paths-before.txt
> Get-Content work/enhancer/build/modules.json -TotalCount 15
>  git diff --check`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input keyevent 3
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell settings get secure default_input_method > work/enhancer/a-repair/default-ime-after.txt
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pm path com.sohu.inputmethod.sogou > work/enhancer/a-repair/official-path-after.txt
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pm path com.sohu.inputmethod.sogou.enhanced > work/enhancer/a-repair/b-path-after.txt
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pm path com.sohu.inputmethod.sogou.xiaomi > work/enhancer/a-repair/xiaomi-path-after.txt
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d --pid=25772 -v time | Select-String '\[SogouEnhance\]|\[SogouBottom\]' | ForEach-Object { $_.Line } | Set-Content -Encoding utf8 work/enhancer/a-repair/official-process.log
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "tar -czf /data/local/tmp/sogou-a-121/module-data-after.tgz -C /data/user/0/com.sogouenhance shared_prefs"'
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /data/local/tmp/sogou-a-121/module-data-after.tgz work/enhancer/a-repair/module-data-after.tgz`
> - Ran `@'
> from pathlib import Path
> import tarfile,xml.etree.ElementTree as E
> base=Path('work/enhancer/a-repair')
> values=[]
> for name in ['module-data-before.tgz','module-data-after.tgz']:
>  with tarfile.open(base/name) as t:
>   m=next(x for x in t.getmembers() if x.name.endswith('/settings.xml'))
>   r=E.fromstring(t.extractfile(m).read())
>   values.append({x.get('name'):x.get('value',x.text) for x in r})
> print('preference differences', {k:(values[0].get(k),values[1].get(k)) for k in set(values[0])|set(values[1]) if values[0].get(k)!=values[1].get(k)})
> text=(base/'official-process.log').read_text(encoding='utf-8-sig')
> print('baseline hook success count',sum('[SogouEnhance] 已挂钩' in x for x in text.splitlines()))
> print('palette log', [x.split('[SogouBottom] ')[-1] for x in text.splitlines() if '[SogouBottom] SKIN ' in x][-4:])
> print('default preserved', (base/'default-ime-before.txt').read_bytes()==(base/'default-ime-after.txt').read_bytes())
> print('official path preserved', (base/'protected-paths-before.txt').read_bytes()==(base/'official-path-after.txt').read_bytes())
> '@ | python -`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -W -n com.sogouenhance/.LauncherAlias
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 600 980
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 1040 1210
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "tar -czf /data/local/tmp/sogou-a-121/module-data-after.tgz -C /data/user/0/com.sogouenhance shared_prefs"'
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /data/local/tmp/sogou-a-121/module-data-after.tgz work/enhancer/a-repair/module-data-after.tgz`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am force-stop com.sohu.inputmethod.sogou
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -W -n com.sohu.inputmethod.sogou/.SogouIMELauncher
> $sogouRepairProcess = (& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pidof com.sohu.inputmethod.sogou).Trim()
> $sogouRepairProcess | Set-Content work/enhancer/a-repair/official-pid.txt
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d --pid=$sogouRepairProcess -v time | Select-String '\[SogouEnhance\]|\[SogouBottom\]' | ForEach-Object { $_.Line } | Set-Content -Encoding utf8 work/enhancer/a-repair/official-process.log`
> - Ran `@'
> from pathlib import Path
> import tarfile,xml.etree.ElementTree as E
> base=Path('work/enhancer/a-repair'); values=[]
> for name in ['module-data-before.tgz','module-data-after.tgz']:
>  with tarfile.open(base/name) as t:
>   m=next(x for x in t.getmembers() if x.name.endswith('/settings.xml'))
>   values.append({x.get('name'):x.get('value',x.text) for x in E.fromstring(t.extractfile(m).read())})
> print('preferences preserved:',values[0]==values[1])
> t=(base/'official-process.log').read_text(encoding='utf-8-sig')
> print('hook registration count:',sum('[SogouEnhance] 已挂钩' in x for x in t.splitlines()))
> print('log lines:',len(t.splitlines()))
> '@ | python -`
>
> </details>
>
> 最终版的三个首页入口、从设置页重新打开模块、官方设置中的“模块设置”跳转均已通过；底栏右键也能打开剪贴板。冷启动日志记录到原增强模块 27 条 hook 注册成功。
>
> 正在核对用户开关是否与测试前一致，并整理 A 的两个交付 APK。
>
> <details><summary>Ran 8 commands</summary>
>
> - Ran `@'
> from pathlib import Path
> import tarfile,xml.etree.ElementTree as E
> v=[]
> for f in ['module-data-before.tgz','module-data-after.tgz']:
>  with tarfile.open(Path('work/enhancer/a-repair')/f) as t:
>   p=next(x for x in t.getmembers() if x.name.endswith('/settings.xml'))
>   v.append({x.get('name'):x.get('value',x.text) for x in E.fromstring(t.extractfile(p).read())})
> print({k:(v[0].get(k),v[1].get(k)) for k in set(v[0])|set(v[1]) if v[0].get(k)!=v[1].get(k)})
> '@ | python -`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -W -n com.sogouenhance/.SettingsActivity
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.xml work/enhancer/a-repair/settings-before-restore.xml`
> - Ran `@'
> import xml.etree.ElementTree as E
> r=E.parse('work/enhancer/a-repair/settings-before-restore.xml')
> for n in r.iter('node'):
>  if n.get('class')=='android.widget.Switch' or n.get('checkable')=='true':
>   print(n.get('class'),n.get('checked'),n.get('bounds'))
> '@ | python -`
> - Ran `Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/SettingsActivity.java | Select-Object -Skip 180 -First 90
> Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/SwitchView.java -TotalCount 110`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 1040 1210
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "tar -czf /data/local/tmp/sogou-a-121/module-data-after.tgz -C /data/user/0/com.sogouenhance shared_prefs"'
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /data/local/tmp/sogou-a-121/module-data-after.tgz work/enhancer/a-repair/module-data-after.tgz`
> - Ran `@'
> from pathlib import Path
> import tarfile,xml.etree.ElementTree as E
> v=[]
> for f in ['module-data-before.tgz','module-data-after.tgz']:
>  with tarfile.open(Path('work/enhancer/a-repair')/f) as t:
>   p=next(x for x in t.getmembers() if x.name.endswith('/settings.xml'))
>   v.append({x.get('name'):x.get('value',x.text) for x in E.fromstring(t.extractfile(p).read())})
> print('preserved',v[0]==v[1]);print({k:(v[0].get(k),v[1].get(k)) for k in set(v[0])|set(v[1]) if v[0].get(k)!=v[1].get(k)})
> '@ | python -`
> - Ran `Get-Content work/enhancer/baseline-jadx/sources/com/sogouenhance/SettingsActivity.java | Select-Object -Skip 110 -First 65
> @'
> import xml.etree.ElementTree as E
> r=E.parse('work/enhancer/a-repair/settings-before-restore.xml')
> for n in r.iter('node'):
>  if n.get('clickable')=='true':print(n.get('class'),n.get('bounds'))
> '@ | python -`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input tap 500 1190
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/a121.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/a121.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/a121.png work/enhancer/a-repair/settings-restored.png`
>
> </details>
>
> Viewed an image
>
> <details><summary>Created a file, edited 2 files, ran 7 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "tar -czf /data/local/tmp/sogou-a-121/module-data-after.tgz -C /data/user/0/com.sogouenhance shared_prefs"'
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /data/local/tmp/sogou-a-121/module-data-after.tgz work/enhancer/a-repair/module-data-after.tgz
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell input keyevent 3
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell settings get secure default_input_method > work/enhancer/a-repair/default-ime-after.txt
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell dumpsys package com.sogouenhance | Select-String 'versionCode=|versionName=' | ForEach-Object { $_.Line } | Set-Content -Encoding utf8 work/enhancer/a-repair/installed-version.txt`
> - Ran `@'
> from pathlib import Path
> import tarfile,xml.etree.ElementTree as E
> v=[]
> for f in ['module-data-before.tgz','module-data-after.tgz']:
>  with tarfile.open(Path('work/enhancer/a-repair')/f) as t:
>   p=next(x for x in t.getmembers() if x.name.endswith('/settings.xml'))
>   v.append({x.get('name'):x.get('value',x.text) for x in E.fromstring(t.extractfile(p).read())})
> print('All module preferences restored:', v[0]==v[1])
> assert v[0]==v[1]
> '@ | python -`
> - Ran `$aRepairPath = (& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pm path com.sogouenhance).Trim().Replace('package:', '')
> if (-not ($aRepairPath.StartsWith('/data/app/') -and $aRepairPath.EndsWith('/base.apk'))) { throw 'Unexpected installed module path' }
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell sha256sum $aRepairPath > work/enhancer/a-repair/installed-sha256.txt`
> - Wrote `./work/enhancer/export.py` (+1 -0)
> - Wrote `./work/enhancer/export_a_repair.py` (+113 -0)
> - Wrote `./work/enhancer/export_skin.py` (+1 -0)
> - Ran `python work/enhancer/export_a_repair.py`
> - Ran `Get-Content work/enhancer/a-repair/default-ime-before.txt
> Get-Content work/enhancer/a-repair/default-ime-after.txt
> Get-Item work/enhancer/a-repair/default-ime-before.txt,work/enhancer/a-repair/default-ime-after.txt | Select-Object Length,LastWriteTime`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell ime set com.sohu.inputmethod.sogou/.SogouIME
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell settings get secure default_input_method > work/enhancer/a-repair/default-ime-after.txt`
> - Ran `python work/enhancer/export_a_repair.py`
>
> </details>
>
> A 1.2.1 已安装，交付文件与手机上的模块哈希一致；模块开关和默认输入法均已恢复到测试前状态。官方主页、增强设置、中文输入和底栏剪贴板已通过本轮检查。
>
> 这次完善了入口区分和重复打开的行为，但旧版“两个图标都进模块页”的现象尚未直接复现，因此仍需你复测确认。
>
> <details><summary>Edited 3 files, ran 3 commands</summary>
>
> - Ran `Get-Content .scratch/sogou-enhancer/issues/02-a-launch-repair.md -TotalCount 35
> Get-Content work/enhancer/README.md -TotalCount 22
>  git diff --stat`
> - Wrote `./.scratch/sogou-enhancer/issues/02-a-launch-repair.md` (+7 -1)
> - Wrote `./.scratch/sogou-enhancer/spec.md` (+2 -1)
> - Wrote `./work/enhancer/README.md` (+21 -2)
> - Ran `git diff --check
>  git diff --stat
> Get-Content outputs/2026-10-21-A-1.2.1/测试记录.json -TotalCount 23`
> - Ran `git add -- .scratch/sogou-enhancer/spec.md .scratch/sogou-enhancer/issues/02-a-launch-repair.md work/enhancer/README.md work/enhancer/build.py work/enhancer/export.py work/enhancer/export_skin.py work/enhancer/export_a_repair.py work/enhancer/companion-smali/com/sogouenhance/AHomeActivity.smali outputs/2026-10-21-A-1.2.1/使用说明.md outputs/2026-10-21-A-1.2.1/测试记录.json outputs/2026-10-21-A-1.2.1/SHA256SUMS.txt
>  git diff --cached --check
>  git commit -m "fix: clarify variant A launcher and verify input flows"
>  git status --short -uno`
>
> </details>
</details>

方案 A 已完成入口修缮，并安装 **1.2.1**：

- 模块改名“搜狗增强·方案A”，新增官方搜狗、增强设置、系统输入法设置三个入口。
- 再次打开模块会返回首页。
- 已验证官方主页、设置跳转、“你好”输入及底栏剪贴板。
- 原设置保留，B 和小米版未修改。

你最初遇到的“两图标都进模块页”尚未直接复现，仍需复测确认；本版未加入皮肤解锁。

[新版方案 A（两个 APK）](./outputs/2026-10-21-A-1.2.1/方案A)

> 刚刚我好像弄错了，我没分清楚app图案，其实是方案B的问题，方案B不应该出现模块的app，而且还一下子出现两个命名都是增强版区别只是多了个·，所以导致我搞错弄成方案A了，再次声明约束！方案B只能是一个且内置模块的安装包！！！

<details><summary>10 previous messages</summary>

> 明白，之前把问题归到 A 是误判。方案 B 必须是**一个内置增强模块的输入法 APK**，桌面也不应再出现独立模块图标。
>
> 我会核对两个“增强版”图标各自对应的包和入口，修正 B 的桌面入口，并在保留设置和数据的前提下清理重复项。A 和小米版保持不动。
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `git status --short -uno
>  git branch --show-current
> Get-Content work/enhancer/package_b.py -TotalCount 270
> Get-Content work/enhancer/baseline-apk/AndroidManifest.xml -TotalCount 20
> rg -n 'enhance|LauncherAlias|launcher|label|SettingsActivity' work/enhancer/src/com/sogouenhance/bottom/EmbeddedGuard.java work/enhancer/package_b.py`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pm list packages | Select-String 'sogou|sogouenhance'
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell cmd package query-activities --brief -a android.intent.action.MAIN -c android.intent.category.LAUNCHER com.sohu.inputmethod.sogou.enhanced
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell cmd package query-activities --brief -a android.intent.action.MAIN -c android.intent.category.LAUNCHER com.sohu.inputmethod.sogou.patched`
> - Ran `Get-Content work/enhancer/baseline-apk/smali/com/sogouenhance/SettingsActivity.smali | Select-Object -Skip 620 -First 155
> Get-Content C:/Users/Kirito787/.codex/skills/auto-prompt/SKILL.md -TotalCount 75
> Get-Content C:/Users/Kirito787/.codex/skills/auto-git-branch/SKILL.md -TotalCount 45
> rg -n 'sougou|搜狗' C:/Users/Kirito787/.codex/memories/MEMORY.md
> Get-Content docs/agents/issue-tracker.md -TotalCount 30
> Get-Content .scratch/sogou-enhancer/spec.md`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pm list packages -u | Select-String 'sogou'
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell dumpsys package com.sohu.inputmethod.sogou.enhanced | Select-String 'Unable|installed=|versionName|User 0|codePath'
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am get-current-user`
> - Ran `git switch -c codex/sogou-b-single-launcher`
>
> </details>
>
> 已找到两个问题：B 的打包脚本额外创建了“搜狗增强设置”的桌面入口；此前手机上也留有另一个包名的旧实验版，名称与新版接近。目前查询显示，B 和旧实验版都已不在安装列表中。
>
> 按你重新明确的约束修正：
> ```text
> 交付：仅一个 B 输入法 APK，内置完整增强功能。
> 桌面：仅一个“搜狗输入法·增强版”图标。
> 设置：只从输入法内部进入增强设置，不提供独立模块图标。
> 验收：检查安装包、实际桌面入口及增强设置；A 和小米版不动。
> ```
>
> <details><summary>Created 2 files, edited 3 files, ran 11 commands</summary>
>
> - Ran `Get-Content work/enhancer/baseline-apk/smali/com/sogouenhance/SettingsActivity.smali | Select-Object -Skip 820 -First 155
> rg -n 'settings|HookEntry' work/enhancer/src/com/sogouenhance/bottom/EmbeddedGuard.java
> Get-Content work/enhancer/src/com/sogouenhance/bottom/EmbeddedGuard.java -TotalCount 140
> Get-Content work/enhancer/build/modules.json -TotalCount 35`
> - Ran `rg -n '\\u6a21\\u5757\\u8bbe\\u7f6e|key_setting_home_module_entry' work/enhancer/baseline-apk/smali/com/sogouenhance/HookEntry.smali | Select-Object -First 8
> & work/compat/aapt2.exe dump xmltree --file AndroidManifest.xml work/enhancer/build/single-signed-27f3464badf7/sogou-20.17.0-enhanced-single-aligned-debugSigned.apk > work/enhancer/tmp/b-manifest-before.txt
> Select-String -Path work/enhancer/tmp/b-manifest-before.txt -Pattern 'SogouIMELauncher|SogouIMEAliasLauncher|enhance.SettingsActivity|LauncherAlias|增强' -Context 4,7 | Select-Object -First 8`
> - Wrote `./.scratch/sogou-enhancer/issues/03-b-single-launcher.md` (+13 -0)
> - Ran `Get-Content work/enhancer/tmp/b-manifest-before.txt -TotalCount 22
> rg -n 'SogouIMELauncher|LauncherAlias|sogouenhance.Settings' work/enhancer/tmp/b-manifest-before.txt | Select-Object -First 12`
> - Wrote `./work/enhancer/build.py` (+19 -2)
> - Wrote `./work/enhancer/manifest_view.py` (+95 -0)
> - Wrote `./work/enhancer/package_b.py` (+5 -8)
> - Ran `python work/enhancer/build.py --variant b > work/enhancer/build-b-launcher-log.txt 2>&1`
> - Wrote `./work/enhancer/package_b.py` (+4 -0)
> - Ran `Get-Content work/enhancer/build-b-launcher-log.txt -Tail 5
> python work/enhancer/package_b.py > work/enhancer/single-b-launcher-log.txt 2>&1`
> - Ran `New-Item -ItemType Directory -Force work/enhancer/b-launcher | Out-Null
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell settings get secure default_input_method > work/enhancer/b-launcher/default-before.txt
> foreach ($sogouPackage in @('com.sogouenhance','com.sohu.inputmethod.sogou','com.sohu.inputmethod.sogou.xiaomi')) {
>  & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pm path $sogouPackage | Add-Content -Encoding utf8 work/enhancer/b-launcher/protected-before.txt
> }
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "cp /data/adb/lspd/config/modules_config.db /data/local/tmp/sogou-b-launcher-lsposed.db"'
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /data/local/tmp/sogou-b-launcher-lsposed.db work/enhancer/b-launcher/lsposed.db`
> - Ran `Get-Content work/enhancer/single-b-launcher-log.txt -Tail 15
> Get-Content work/enhancer/build/modules.json | Select-Object -Last 14
> @'
> import sys,zipfile
> sys.path.insert(0,'work/enhancer')
> from manifest_view import parse,launchers
> p='work/enhancer/build/single-signed-27f3464badf7/sogou-20.17.0-enhanced-single-aligned-debugSigned.apk'
> with zipfile.ZipFile(p) as z:
>  print(str(launchers(parse(z.read('AndroidManifest.xml')))).encode('unicode_escape').decode())
> '@ | python -`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell 'su -c "chmod 644 /data/local/tmp/sogou-b-launcher-lsposed.db"'
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /data/local/tmp/sogou-b-launcher-lsposed.db work/enhancer/b-launcher/lsposed.db`
> - Ran `@'
> import sqlite3
> c=sqlite3.connect('file:work/enhancer/b-launcher/lsposed.db?mode=ro',uri=True)
> print(c.execute("select name,sql from sqlite_master where type='table'").fetchall())
> '@ | python -`
> - Wrote `./work/enhancer/manifest_view.py` (+1 -0)
> - Wrote `./work/enhancer/package_b.py` (+22 -1)
> - Ran `python work/enhancer/package_b.py > work/enhancer/single-b-launcher-log.txt 2>&1`
> - Ran `@'
> import sqlite3,json
> from pathlib import Path
> c=sqlite3.connect('file:work/enhancer/b-launcher/lsposed.db?mode=ro',uri=True)
> rows=c.execute("select module_pkg_name,app_pkg_name,user_id from scope where app_pkg_name in ('com.sohu.inputmethod.sogou.enhanced','com.sohu.inputmethod.sogou.patched')").fetchall()
> print('External scopes for B/old experiment:',rows)
> assert not rows
> Path('work/enhancer/b-launcher/external-scopes.json').write_text(json.dumps({'B_external_scopes':rows}),encoding='utf-8')
> '@ | python -`
>
> </details>
>
> 旧 B 的清单确实有两个启用的桌面入口：输入法本身和额外的增强设置入口。新版已移除后者，也去掉了内置设置页中不适用的“隐藏模块图标”开关，避免旧设置重新干预图标。
>
> 名称统一为“搜狗输入法·增强版”。另外，已确认 B 没有外部 LSPosed 模块作用域；接下来将只安装这一个 APK，验证桌面和内置设置。
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `Get-Content work/enhancer/single-b-launcher-log.txt -Tail 23
> Get-Content work/enhancer/build/single.json -TotalCount 10
> Get-ChildItem work/enhancer/b-launcher -Name`
> - Ran `$bLauncherApk = (Get-Content work/enhancer/build/single.json -Raw | ConvertFrom-Json).apk
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 install --no-incremental -r $bLauncherApk
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell cmd package query-activities --brief -a android.intent.action.MAIN -c android.intent.category.LAUNCHER com.sohu.inputmethod.sogou.enhanced > work/enhancer/b-launcher/installed-launchers.txt
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -W -n com.sohu.inputmethod.sogou.enhanced/com.sohu.inputmethod.sogou.SogouIMELauncher
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell uiautomator dump /sdcard/b122.xml
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell screencap -p /sdcard/b122.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/b122.png work/enhancer/b-launcher/first-launch.png
> & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /sdcard/b122.xml work/enhancer/b-launcher/first-launch.xml`
> - Ran `Get-Content work/enhancer/b-launcher/installed-launchers.txt
> Get-Content work/enhancer/b-launcher/default-before.txt`
>
> </details>
>
> Viewed an image
>
> <details><summary>Ran a command</summary>
>
> - Ran `@'
> from pathlib import Path
> from io import BytesIO
> import sys,zipfile,json,hashlib
> sys.path.insert(0,'work/enhancer')
> from manifest_view import assert_single_launcher,A,parse
> b=Path('work/enhancer')
> m=json.loads((b/'build/modules.json').read_text(encoding='utf-8'))
> s=json.loads((b/'build/single.json').read_text(encoding='utf-8'))
> with zipfile.ZipFile(s['apk']) as z:
>  assert z.testzip() is None
>  modules=[n for n in z.namelist() if n.startswith('assets/npatch/modules/')]
>  assert modules==['assets/npatch/modules/com.sogouenhance.apk']
>  assert hashlib.sha256(z.read(modules[0])).hexdigest()==m['b']['sha256']
>  config=json.loads(z.read('assets/npatch/config.json'));assert config['useManager'] is False
>  outer=assert_single_launcher(z.read('AndroidManifest.xml'))
>  with zipfile.ZipFile(BytesIO(z.read('assets/npatch/origin.apk'))) as inner,zipfile.ZipFile(b/'official/SogouInput_20.17.0_android_sweb.apk') as original:
>   assert_single_launcher(inner.read('AndroidManifest.xml'))
>   kept=[n for n in original.namelist() if n=='resources.arsc' or n.endswith('.so')]
>   assert all(inner.read(n)==original.read(n) for n in kept)
>   assert s['settings_dex'] in inner.namelist()
>  print('PASS: one embedded module, no external manager, one enabled launcher in both manifests, internal settings, original resources/native libraries preserved')
> print('A artifact unchanged:',m['a']['sha256']=='976a9ef463a95d444db729c4493b141ed8b6a14bd5c87230cbf62217c119ef00')
> '@ | python -`
>
> </details>
>
> <details><summary>Ran <code>'&quot;C:\\Program Files\\PowerShell\\7\\pwsh.exe&quot; -Command &quot;&amp; '&quot;'&quot;'C:\\Program Files\\Netease\\MuMuPlayer\\nx_main\\adb.exe'&quot;'&quot;' -s df043723 shell settings get secure default_input_method
> &amp; '&quot;'&quot;'C:\\Program Files\\Netease\\MuMuPlayer\\nx_main\\adb.exe'&quot;'&quot;' -s df043723 shell pm list packages --user 999 | Select-String '&quot;'&quot;'sogou'&quot;'&quot;'
> &amp; '&quot;'&quot;'C:\\Program Files\\Netease\\MuMuPlayer\\nx_main\\adb.exe'&quot;'&quot;' -s df043723 shell dumpsys activity activities | Select-String '&quot;'&quot;'&quot;'&quot;'&quot;'^'&quot;'&quot;'&quot;\\s*topResumedActivity='&quot;'&quot;' | Select-Object -Last 1&quot;'</code></summary>
>
> ```bash
> $ '"C:\\Program Files\\PowerShell\\7\\pwsh.exe" -Command "& '"'"'C:\\Program Files\\Netease\\MuMuPlayer\\nx_main\\adb.exe'"'"' -s df043723 shell settings get secure default_input_method
> & '"'"'C:\\Program Files\\Netease\\MuMuPlayer\\nx_main\\adb.exe'"'"' -s df043723 shell pm list packages --user 999 | Select-String '"'"'sogou'"'"'
> & '"'"'C:\\Program Files\\Netease\\MuMuPlayer\\nx_main\\adb.exe'"'"' -s df043723 shell dumpsys activity activities | Select-String '"'"'"'"'"'^'"'"'"\\s*topResumedActivity='"'"' | Select-Object -Last 1"'
> ```
>
> Running
>
> Auto-review
>
> Status: denied
> Rationale: Automatic approval review failed: You’ve hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/settings/usage to purchase more credits or try again at 1:52 PM.
>
> </details>
>
> System error
>
> You’ve hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/settings/usage to purchase more credits or try again at 1:52 PM.
</details>
