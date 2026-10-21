> 原始文件：`交接0.txt`（UTF-16LE，已转 UTF-8 存档）

> [$reverse-engineer-anything](~//.agents/skills/reverse-engineer-anything/SKILL.md) 项目文件夹中有两个安卓apk，一个是搜狗输入法一个是搜狗输入法小米。我有3个需求：
> 1.搜狗输入法不支持小米的全面屏键盘优化，而搜狗输入法小米支持，所以我想让搜狗输入法也支持小米的全面屏键盘优化。
> 2.搜狗输入法的广告太多了，在不影响功能的情况下请帮我去除或者隐藏广告
> 3.要让这两个输入法版本共存可以同时安装互不影响

<details><summary>62 previous messages</summary>

> 我会使用 reverse-engineer-anything 技能对比两个 APK，定位小米全面屏适配、广告入口和共存冲突，再制作可验证的修改包。先保留原始 APK，确认版本、包名、签名和现有反编译工具。
>
> ```text
> 目标：让普通版支持小米全面屏键盘优化、隐藏广告，并与小米版共存。
> 要求：根据代码和资源证据修改；保留输入、语音、词库等功能；原包不覆盖。
> 输出：修改包、改动说明及验证结果；无法验证的项目明确标注。
> ```
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `Get-ChildItem -Force | Select-Object Mode,Length,Name; rg --files -g AGENTS.md -g '*.apk' -g '*apktool*' -g '*jadx*' -g '*sign*' -g '*.jar'; rg -n 'sougou|搜狗|APK|apktool' 'C:\Users\Kirito787\.codex\memories\MEMORY.md'`
> - Ran `Get-Content -LiteralPath 'C:\Users\Kirito787\.agents\skills\reverse-engineer-anything\references\android-applications.md' -TotalCount 190; Get-Content -LiteralPath 'C:\Users\Kirito787\.agents\skills\reverse-engineer-anything\references\connection-and-recovery.md' -TotalCount 100`
>
> </details>
>
> 请提供手机型号、MIUI/HyperOS 与 Android 版本；“全面屏键盘优化”具体指底部抬高/留白、手势条适配，还是小米系统中的某个开关？有这些信息才能确定适配目标。
>
> <details><summary>Ran a command, called a tool</summary>
>
> MCP tool call
>
> rea.inspect_android_package
>
> ```json
> {
>   "path": "C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法.apk",
>   "detail": "summary"
> }
> ```
>
> Error: {"error":{"code":"capability_unavailable","category":"unsupported_provider","message":"Set REA_JADX_MCP_JAR to the absolute path of a caller-supplied jadx-headless-mcp 0.7.1 JAR. REA does not download or install it.","retryable":false,"remediation":{"action":"Set REA_JADX_MCP_JAR to the absolute path of a caller-supplied jadx-headless-mcp 0.7.1 JAR. REA does not download or install it."},"details":{"provider_id":"jadx","operation":"inspect_android_package","reason":"Set REA_JADX_MCP_JAR to the absolute path of a caller-supplied jadx-headless-mcp 0.7.1 JAR. REA does not download or install it.","diagnostics":{"jar_configured":false,"failure_kind":"jar","failure_code":"not_configured"}}}}
>
> - Ran `$paths = 'C:\Users\Kirito787\Documents\AGENTS.md','C:\Users\Kirito787\Documents\AI\AGENTS.md','C:\Users\Kirito787\Documents\AI\GPT\AGENTS.md','C:\Users\Kirito787\Documents\AI\GPT\sougou\AGENTS.md'; foreach ($p in $paths) { if (Test-Path -LiteralPath $p) { Get-Content -LiteralPath $p } }; Get-Command java,python,python3,git,7z,adb -ErrorAction SilentlyContinue | Select-Object Name,Source; Get-ChildItem -LiteralPath 'C:\Program Files','C:\Users\Kirito787\AppData\Local\Android','C:\Users\Kirito787\.jdks','C:\Users\Kirito787\scoop\apps' -ErrorAction SilentlyContinue | Select-Object FullName; git rev-parse --is-inside-work-tree`
>
> </details>
>
> **请提供手机型号、MIUI/HyperOS 与 Android 版本；“全面屏键盘优化”具体指底部抬高/留白、手势条适配，还是小米系统中的某个开关？有这些信息才能确定适配目标。**
>
> REDMI K90 Pro Max
>
> <details><summary>Ran a command, called a tool, searched the web</summary>
>
> MCP tool call
>
> rea.open_binary
>
> ```json
> {
>   "path": "C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法.apk"
> }
> ```
>
> ```text
> {"result":{"path":"C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法.apk","format":"apk","kind":"archive","sha256":"df10256e9228e9ed3831be4278a7b9046dd16b0e045d68dee8baafa2491c1574","architecture":null}}
> ```
>
> ```json
> {
>   "result": {
>     "path": "C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法.apk",
>     "format": "apk",
>     "kind": "archive",
>     "sha256": "df10256e9228e9ed3831be4278a7b9046dd16b0e045d68dee8baafa2491c1574",
>     "architecture": null
>   }
> }
> ```
>
> - Ran `Get-ChildItem -LiteralPath 'C:\Program Files' -Directory | ForEach-Object FullName; Get-ChildItem -LiteralPath 'C:\Users\Kirito787\AppData\Local\Programs' -Directory | ForEach-Object FullName; python -c "import importlib.util; print({x:bool(importlib.util.find_spec(x)) for x in ['androguard','requests','cryptography']})"`
>
> Searched the web for `github iBotPeaches Apktool releases apktool jar latest ...`
>
> </details>
>
> 已确认两个原包都在目录中，也收到了你的机型：REDMI K90 Pro Max。REA 已成功打开普通版 APK，但 Android 反编译调用被缺少 JADX MCP 引擎阻断；我会继续检查包内容，并寻找可用于本地解包、修改和签名的工具。
>
> 全面屏适配还可能受系统对白名单包名、系统签名的限制影响，这部分需要结合两个包的代码判断，不能只添加一个配置就宣称完成。
>
> <details><summary>Ran 2 commands, called a tool</summary>
>
> - Ran `rg --files 'C:\Program Files\Microsoft' 'C:\Program Files\ldplayer9box' 'C:\Program Files\Netease' 'C:\Users\Kirito787\AppData\Local\Google' 'C:\Users\Kirito787\AppData\Local\Android' -g java.exe -g javac.exe -g adb.exe -g apksigner* -g aapt* -g '*apktool*' -g '*jadx*' -g '*jbr*' 2>$null; Get-ChildItem -LiteralPath 'C:\Program Files\Java','C:\Program Files\Eclipse Adoptium','C:\Program Files\Android','C:\Users\Kirito787\.jdks' -ErrorAction SilentlyContinue | ForEach-Object FullName`
>
> MCP tool call
>
> rea.inspect_artifact
>
> ```json
> {
>   "detail": "summary"
> }
> ```
>
> ```text
> {"evidence_id":"ev_fbe9ccc9845c951ac99059fa13268aecdfcf2875060668761cd09bfd99528b7f","subject":{"name":"搜狗输入法.apk","digest":{"sha256":"df10256e9228e9ed3831be4278a7b9046dd16b0e045d68dee8baafa2491c1574"},"local_path":"C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法.apk","format":"apk","architecture":null},"provider":{"id":"rea-analysis-view","name":"REA analysis view projection","version":"1"},"analysis_profile":null,"predicate_type":"rea.analysis-view","operation":"inspect_analysis_view","parameters":{"parent_evidence_id":"ev_71618c6487d2f908cf74118dc629894535eb722ebe40be2aa5778aecf61d2bf5","view":{"kind":"summary"}},"raw_result":null,"normalized_result":{"kind":"summary","view":{"kind":"summary"},"parent_evidence_id":"ev_71618c6487d2f908cf74118dc629894535eb722ebe40be2aa5778aecf61d2bf5","parent_operation":"inspect_artifact","parent_digest":"71618c6487d2f908cf74118dc629894535eb722ebe40be2aa5778aecf61d2bf5","view_digest":"6eff6ca4eff2f5581f8cc86bcf791fb26403c5f0a456bffd205fb7787cbaa69c","artifact":{"path":"C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法.apk","sha256":"df10256e9228e9ed3831be4278a7b9046dd16b0e045d68dee8baafa2491c1574"},"coverage":{"status":"complete-within-view","examined":42535,"total":42535,"next_offset":null,"exhausted":true},"limitations":["Inspection derives bounded static hypotheses and next probes; it does not execute the artifact or claim format-specific semantics.","ZIP inventory lists central-directory entries only. Non-entry bytes, including an APK Signing Block before the central directory or a ZIP comment after it, are not occurrences."],"unknowns":["Inventory does not establish application runtime behavior or complete format-specific analysis."],"summary":{"manifest":{"manifest_id":"agm_bb22e65f35d9bb5982ec9b43237e1b2c11ba17ad0fb9ac08f966ff08828aac9e","root_artifact_id":"art_2d88032561bdf0becf5cd49254697d6498152a2493fb086610736811ef406a14","root_sha256":"df10256e9228e9ed3831be4278a7b9046dd16b0e045d68dee8baafa2491c1574","root_format":"apk","graph_sha256":"2ac231445202e43d771cad1139066dbb2301133ca2ad47b35c51c98295b9563d","node_count":13238,"occurrence_count":14649,"edge_count":14648},"available_counts":{"nodes":13238,"occurrences":14649,"edges":14648,"integrity_contradictions":0},"observed_entry_kind_counts":{"file":14649,"directory":0,"symlink":0,"slice":0},"source_complete":true,"inventory_evidence_ids":["ev_b165c3183514b5535b063b2990ad996288a2289ee1b5d0aa11d774643b167529"],"inspection":{"coverage":{"status":"complete-within-substeps","substeps_completed":1,"observations_retained":1,"observations_omitted":0,"hypotheses_retained":0,"hypotheses_omitted":0,"unexplored_branches_retained":0,"unexplored_branches_omitted":0,"next_probes_retained":0,"next_probes_omitted":0},"unexplored_branches":[]},"limitation_count":2}},"confidence":"derived","authority":"shipped-artifact","environment":null,"limitations":["Inspection derives bounded static hypotheses and next probes; it does not execute the artifact or claim format-specific semantics.","ZIP inventory lists central-directory entries only. Non-entry bytes, including an APK Signing Block before the central directory or a ZIP comment after it, are not occurrences."],"relationship_coverage":null,"locations":[{"kind":"artifact-path","path":"C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法.apk"}],"evidence_links":["ev_71618c6487d2f908cf74118dc629894535eb722ebe40be2aa5778aecf61d2bf5"]}
> ```
>
> ```json
> {
>   "evidence_id": "ev_fbe9ccc9845c951ac99059fa13268aecdfcf2875060668761cd09bfd99528b7f",
>   "subject": {
>     "name": "搜狗输入法.apk",
>     "digest": {
>       "sha256": "df10256e9228e9ed3831be4278a7b9046dd16b0e045d68dee8baafa2491c1574"
>     },
>     "local_path": "C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法.apk",
>     "format": "apk",
>     "architecture": null
>   },
>   "provider": {
>     "id": "rea-analysis-view",
>     "name": "REA analysis view projection",
>     "version": "1"
>   },
>   "analysis_profile": null,
>   "predicate_type": "rea.analysis-view",
>   "operation": "inspect_analysis_view",
>   "parameters": {
>     "parent_evidence_id": "ev_71618c6487d2f908cf74118dc629894535eb722ebe40be2aa5778aecf61d2bf5",
>     "view": {
>       "kind": "summary"
>     }
>   },
>   "raw_result": null,
>   "normalized_result": {
>     "kind": "summary",
>     "view": {
>       "kind": "summary"
>     },
>     "parent_evidence_id": "ev_71618c6487d2f908cf74118dc629894535eb722ebe40be2aa5778aecf61d2bf5",
>     "parent_operation": "inspect_artifact",
>     "parent_digest": "71618c6487d2f908cf74118dc629894535eb722ebe40be2aa5778aecf61d2bf5",
>     "view_digest": "6eff6ca4eff2f5581f8cc86bcf791fb26403c5f0a456bffd205fb7787cbaa69c",
>     "artifact": {
>       "path": "C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法.apk",
>       "sha256": "df10256e9228e9ed3831be4278a7b9046dd16b0e045d68dee8baafa2491c1574"
>     },
>     "coverage": {
>       "status": "complete-within-view",
>       "examined": 42535,
>       "total": 42535,
>       "next_offset": null,
>       "exhausted": true
>     },
>     "limitations": [
>       "Inspection derives bounded static hypotheses and next probes; it does not execute the artifact or claim format-specific semantics.",
>       "ZIP inventory lists central-directory entries only. Non-entry bytes, including an APK Signing Block before the central directory or a ZIP comment after it, are not occurrences."
>     ],
>     "unknowns": [
>       "Inventory does not establish application runtime behavior or complete format-specific analysis."
>     ],
>     "summary": {
>       "manifest": {
>         "manifest_id": "agm_bb22e65f35d9bb5982ec9b43237e1b2c11ba17ad0fb9ac08f966ff08828aac9e",
>         "root_artifact_id": "art_2d88032561bdf0becf5cd49254697d6498152a2493fb086610736811ef406a14",
>         "root_sha256": "df10256e9228e9ed3831be4278a7b9046dd16b0e045d68dee8baafa2491c1574",
>         "root_format": "apk",
>         "graph_sha256": "2ac231445202e43d771cad1139066dbb2301133ca2ad47b35c51c98295b9563d",
>         "node_count": 13238,
>         "occurrence_count": 14649,
>         "edge_count": 14648
>       },
>       "available_counts": {
>         "nodes": 13238,
>         "occurrences": 14649,
>         "edges": 14648,
>         "integrity_contradictions": 0
>       },
>       "observed_entry_kind_counts": {
>         "file": 14649,
>         "directory": 0,
>         "symlink": 0,
>         "slice": 0
>       },
>       "source_complete": true,
>       "inventory_evidence_ids": [
>         "ev_b165c3183514b5535b063b2990ad996288a2289ee1b5d0aa11d774643b167529"
>       ],
>       "inspection": {
>         "coverage": {
>           "status": "complete-within-substeps",
>           "substeps_completed": 1,
>           "observations_retained": 1,
>           "observations_omitted": 0,
>           "hypotheses_retained": 0,
>           "hypotheses_omitted": 0,
>           "unexplored_branches_retained": 0,
>           "unexplored_branches_omitted": 0,
>           "next_probes_retained": 0,
>           "next_probes_omitted": 0
>         },
>         "unexplored_branches": []
>       },
>       "limitation_count": 2
>     }
>   },
>   "confidence": "derived",
>   "authority": "shipped-artifact",
>   "environment": null,
>   "limitations": [
>     "Inspection derives bounded static hypotheses and next probes; it does not execute the artifact or claim format-specific semantics.",
>     "ZIP inventory lists central-directory entries only. Non-entry bytes, including an APK Signing Block before the central directory or a ZIP comment after it, are not occurrences."
>   ],
>   "relationship_coverage": null,
>   "locations": [
>     {
>       "kind": "artifact-path",
>       "path": "C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法.apk"
>     }
>   ],
>   "evidence_links": [
>     "ev_71618c6487d2f908cf74118dc629894535eb722ebe40be2aa5778aecf61d2bf5"
>   ]
> }
> ```
>
> - Ran `New-Item -ItemType Directory -Path work\tools,outputs -Force | Out-Null; @'
> import requests
> for repo in ['iBotPeaches/Apktool','skylot/jadx','patrickfav/uber-apk-signer','adoptium/temurin21-binaries']:
>  r=requests.get('https://api.github.com/repos/'+repo+'/releases/latest',timeout=25);r.raise_for_status();j=r.json()
>  print(repo,j['tag_name'])
>  for a in j['assets']:
>   n=a['name']
>   if (repo.endswith('Apktool') and n.endswith('.jar')) or (repo.endswith('/jadx') and n.startswith('jadx-') and n.endswith('.zip') and 'gui' not in n) or (repo.endswith('uber-apk-signer') and n.endswith('.jar')) or (repo.endswith('temurin21-binaries') and 'jdk_x64_windows_hotspot' in n and n.endswith('.zip')):
>    print(n,a['size'],a['browser_download_url'])
> '@ | python -`
>
> </details>
>
> MIUI/HyperOS版本3.0.309.0.WPMCNXM.C09
> Android 版本16 安全更新2026-07-01
>
> <details><summary>Ran a command</summary>
>
> - Ran `@'
> import requests,concurrent.futures,pathlib,hashlib,zipfile
> root=pathlib.Path('work/tools')
> jobs=[('apktool.jar','https://github.com/iBotPeaches/Apktool/releases/download/v3.0.3/apktool_3.0.3.jar'),('jadx.zip','https://github.com/skylot/jadx/releases/download/v1.5.6/jadx-1.5.6.zip'),('signer.jar','https://github.com/patrickfav/uber-apk-signer/releases/download/v1.3.0/uber-apk-signer-1.3.0.jar'),('jdk.zip','https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.12.1%2B1/OpenJDK21U-jdk_x64_windows_hotspot_21.0.12.1_1.zip')]
> def get(job):
>  name,url=job;p=root/name
>  if not p.exists():
>   r=requests.get(url,timeout=(20,90),stream=True);r.raise_for_status()
>   with p.open('wb') as f:
>    for chunk in r.iter_content(1024*1024):f.write(chunk)
>  print(name,p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest(),flush=True)
>  if name in ['jdk.zip','jadx.zip']:
>   out=root/name[:-4];out.mkdir(exist_ok=True)
>   with zipfile.ZipFile(p) as z:z.extractall(out)
>  return name
> with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(get,jobs))
> '@ | Set-Content -LiteralPath work\download_tools.py -Encoding utf8; python work\download_tools.py`
>
> </details>
>
> <details><summary>Ran a command, called 2 tools</summary>
>
> MCP tool call
>
> rea.close_binary
>
> ```json
> {}
> ```
>
> ```text
> {"result":null}
> ```
>
> ```json
> {
>   "result": null
> }
> ```
>
> MCP tool call
>
> rea.open_binary
>
> ```json
> {
>   "path": "C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法小米.apk"
> }
> ```
>
> ```text
> {"result":{"path":"C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法小米.apk","format":"apk","kind":"archive","sha256":"1dba71c52a12bf773d5d78c50a414cbe45ed2a449bf86a19de6059eec20e763c","architecture":null}}
> ```
>
> ```json
> {
>   "result": {
>     "path": "C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法小米.apk",
>     "format": "apk",
>     "kind": "archive",
>     "sha256": "1dba71c52a12bf773d5d78c50a414cbe45ed2a449bf86a19de6059eec20e763c",
>     "architecture": null
>   }
> }
> ```
>
> - Ran `Get-ChildItem -LiteralPath work\tools | Select-Object Name,Length`
>
> </details>
>
> 已记录目标系统：HyperOS 3.0.309.0、Android 16。接下来会重点检查底部区域处理和系统对输入法包名的识别方式。
>
> 我正在项目内准备便携工具，不修改全局 Java 或 REA 配置。修改后的 APK 需要重新签名；因此账号登录、云词库等依赖官方签名的功能，也会列入验证范围。
>
> <details><summary>Ran 3 commands, called a tool</summary>
>
> MCP tool call
>
> rea.inspect_artifact
>
> ```json
> {
>   "detail": "summary"
> }
> ```
>
> ```text
> {"evidence_id":"ev_14c6995997af4706646c71f917fc7740e9459d65a845e8c6b302e9054da552f0","subject":{"name":"搜狗输入法小米.apk","digest":{"sha256":"1dba71c52a12bf773d5d78c50a414cbe45ed2a449bf86a19de6059eec20e763c"},"local_path":"C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法小米.apk","format":"apk","architecture":null},"provider":{"id":"rea-analysis-view","name":"REA analysis view projection","version":"1"},"analysis_profile":null,"predicate_type":"rea.analysis-view","operation":"inspect_analysis_view","parameters":{"parent_evidence_id":"ev_176bc6bc9205baddfc4460d4209a68ed4c8452f52f9b585e55f466c8518580c9","view":{"kind":"summary"}},"raw_result":null,"normalized_result":{"kind":"summary","view":{"kind":"summary"},"parent_evidence_id":"ev_176bc6bc9205baddfc4460d4209a68ed4c8452f52f9b585e55f466c8518580c9","parent_operation":"inspect_artifact","parent_digest":"176bc6bc9205baddfc4460d4209a68ed4c8452f52f9b585e55f466c8518580c9","view_digest":"7db258e26885812607245e8a437b2e2aca70d461b81b181f0c2b9b0f3d2f0b3e","artifact":{"path":"C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法小米.apk","sha256":"1dba71c52a12bf773d5d78c50a414cbe45ed2a449bf86a19de6059eec20e763c"},"coverage":{"status":"complete-within-view","examined":32893,"total":32893,"next_offset":null,"exhausted":true},"limitations":["Inspection derives bounded static hypotheses and next probes; it does not execute the artifact or claim format-specific semantics.","ZIP inventory lists central-directory entries only. Non-entry bytes, including an APK Signing Block before the central directory or a ZIP comment after it, are not occurrences."],"unknowns":["Inventory does not establish application runtime behavior or complete format-specific analysis."],"summary":{"manifest":{"manifest_id":"agm_c035fa55dc3bf4a12e78e69b74f0611cacd0d4241bb614e5f697fbb34bfcd2c6","root_artifact_id":"art_5258875cba5d07c04070dc272aa31ab1a32ffaf93bad882cf1dfc1743b8c2247","root_sha256":"1dba71c52a12bf773d5d78c50a414cbe45ed2a449bf86a19de6059eec20e763c","root_format":"apk","graph_sha256":"f10c6cb0c87006851122cd2d061638984a2440fbc1581b71493beb281281381c","node_count":10460,"occurrence_count":11217,"edge_count":11216},"available_counts":{"nodes":10460,"occurrences":11217,"edges":11216,"integrity_contradictions":0},"observed_entry_kind_counts":{"file":11217,"directory":0,"symlink":0,"slice":0},"source_complete":true,"inventory_evidence_ids":["ev_f895f4960d3871c3fd63a5274e857a072b85f1510ab1e6428bc15352d7a4a5c0"],"inspection":{"coverage":{"status":"complete-within-substeps","substeps_completed":1,"observations_retained":1,"observations_omitted":0,"hypotheses_retained":0,"hypotheses_omitted":0,"unexplored_branches_retained":0,"unexplored_branches_omitted":0,"next_probes_retained":0,"next_probes_omitted":0},"unexplored_branches":[]},"limitation_count":2}},"confidence":"derived","authority":"shipped-artifact","environment":null,"limitations":["Inspection derives bounded static hypotheses and next probes; it does not execute the artifact or claim format-specific semantics.","ZIP inventory lists central-directory entries only. Non-entry bytes, including an APK Signing Block before the central directory or a ZIP comment after it, are not occurrences."],"relationship_coverage":null,"locations":[{"kind":"artifact-path","path":"C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法小米.apk"}],"evidence_links":["ev_176bc6bc9205baddfc4460d4209a68ed4c8452f52f9b585e55f466c8518580c9"]}
> ```
>
> ```json
> {
>   "evidence_id": "ev_14c6995997af4706646c71f917fc7740e9459d65a845e8c6b302e9054da552f0",
>   "subject": {
>     "name": "搜狗输入法小米.apk",
>     "digest": {
>       "sha256": "1dba71c52a12bf773d5d78c50a414cbe45ed2a449bf86a19de6059eec20e763c"
>     },
>     "local_path": "C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法小米.apk",
>     "format": "apk",
>     "architecture": null
>   },
>   "provider": {
>     "id": "rea-analysis-view",
>     "name": "REA analysis view projection",
>     "version": "1"
>   },
>   "analysis_profile": null,
>   "predicate_type": "rea.analysis-view",
>   "operation": "inspect_analysis_view",
>   "parameters": {
>     "parent_evidence_id": "ev_176bc6bc9205baddfc4460d4209a68ed4c8452f52f9b585e55f466c8518580c9",
>     "view": {
>       "kind": "summary"
>     }
>   },
>   "raw_result": null,
>   "normalized_result": {
>     "kind": "summary",
>     "view": {
>       "kind": "summary"
>     },
>     "parent_evidence_id": "ev_176bc6bc9205baddfc4460d4209a68ed4c8452f52f9b585e55f466c8518580c9",
>     "parent_operation": "inspect_artifact",
>     "parent_digest": "176bc6bc9205baddfc4460d4209a68ed4c8452f52f9b585e55f466c8518580c9",
>     "view_digest": "7db258e26885812607245e8a437b2e2aca70d461b81b181f0c2b9b0f3d2f0b3e",
>     "artifact": {
>       "path": "C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法小米.apk",
>       "sha256": "1dba71c52a12bf773d5d78c50a414cbe45ed2a449bf86a19de6059eec20e763c"
>     },
>     "coverage": {
>       "status": "complete-within-view",
>       "examined": 32893,
>       "total": 32893,
>       "next_offset": null,
>       "exhausted": true
>     },
>     "limitations": [
>       "Inspection derives bounded static hypotheses and next probes; it does not execute the artifact or claim format-specific semantics.",
>       "ZIP inventory lists central-directory entries only. Non-entry bytes, including an APK Signing Block before the central directory or a ZIP comment after it, are not occurrences."
>     ],
>     "unknowns": [
>       "Inventory does not establish application runtime behavior or complete format-specific analysis."
>     ],
>     "summary": {
>       "manifest": {
>         "manifest_id": "agm_c035fa55dc3bf4a12e78e69b74f0611cacd0d4241bb614e5f697fbb34bfcd2c6",
>         "root_artifact_id": "art_5258875cba5d07c04070dc272aa31ab1a32ffaf93bad882cf1dfc1743b8c2247",
>         "root_sha256": "1dba71c52a12bf773d5d78c50a414cbe45ed2a449bf86a19de6059eec20e763c",
>         "root_format": "apk",
>         "graph_sha256": "f10c6cb0c87006851122cd2d061638984a2440fbc1581b71493beb281281381c",
>         "node_count": 10460,
>         "occurrence_count": 11217,
>         "edge_count": 11216
>       },
>       "available_counts": {
>         "nodes": 10460,
>         "occurrences": 11217,
>         "edges": 11216,
>         "integrity_contradictions": 0
>       },
>       "observed_entry_kind_counts": {
>         "file": 11217,
>         "directory": 0,
>         "symlink": 0,
>         "slice": 0
>       },
>       "source_complete": true,
>       "inventory_evidence_ids": [
>         "ev_f895f4960d3871c3fd63a5274e857a072b85f1510ab1e6428bc15352d7a4a5c0"
>       ],
>       "inspection": {
>         "coverage": {
>           "status": "complete-within-substeps",
>           "substeps_completed": 1,
>           "observations_retained": 1,
>           "observations_omitted": 0,
>           "hypotheses_retained": 0,
>           "hypotheses_omitted": 0,
>           "unexplored_branches_retained": 0,
>           "unexplored_branches_omitted": 0,
>           "next_probes_retained": 0,
>           "next_probes_omitted": 0
>         },
>         "unexplored_branches": []
>       },
>       "limitation_count": 2
>     }
>   },
>   "confidence": "derived",
>   "authority": "shipped-artifact",
>   "environment": null,
>   "limitations": [
>     "Inspection derives bounded static hypotheses and next probes; it does not execute the artifact or claim format-specific semantics.",
>     "ZIP inventory lists central-directory entries only. Non-entry bytes, including an APK Signing Block before the central directory or a ZIP comment after it, are not occurrences."
>   ],
>   "relationship_coverage": null,
>   "locations": [
>     {
>       "kind": "artifact-path",
>       "path": "C:\\Users\\Kirito787\\Documents\\AI\\DSH\\sougou\\搜狗输入法小米.apk"
>     }
>   ],
>   "evidence_links": [
>     "ev_176bc6bc9205baddfc4460d4209a68ed4c8452f52f9b585e55f466c8518580c9"
>   ]
> }
> ```
>
> - Ran `Get-ChildItem -LiteralPath work\tools | Select-Object Name,Length; Get-Content -LiteralPath work\inventory\summary.json -ErrorAction SilentlyContinue -TotalCount 20`
>
> - Ran `@'
> import requests,time
> for u in ['https://github.com/iBotPeaches/Apktool/releases/download/v3.0.3/apktool_3.0.3.jar','https://api.adoptium.net/v3/assets/latest/21/hotspot?architecture=x64&image_type=jre&os=windows']:
>  try:
>   t=time.time();r=requests.get(u,timeout=15,stream=True);print(r.status_code,r.headers.get('content-length'),r.url[:180],round(time.time()-t,1),flush=True)
>   if 'api.adoptium' in u: print(r.json()[0]['binary']['package']['link'],flush=True)
>  except Exception as e:print(type(e).__name__,str(e)[:180],flush=True)
> '@ | python -`
>
> - Ran `Get-ChildItem -LiteralPath work\tools | Select-Object Name,Length; Get-Process python -ErrorAction SilentlyContinue | Select-Object Id,CPU,WorkingSet`
>
> </details>
>
> Stream error
>
> Reconnecting... waiting for network
> Connection failed: error sending request
>
> <details><summary>Ran a command</summary>
>
> - Ran `@'
> import requests,time,pathlib
> u='https://github.com/iBotPeaches/Apktool/releases/download/v3.0.3/apktool_3.0.3.jar'
> t=time.time();r=requests.get(u,timeout=(10,15),stream=True,headers={'Range':'bytes=0-1048575','Cache-Control':'no-cache'})
> print(r.status_code,r.headers.get('content-range'),flush=True)
> p=pathlib.Path('work/tools/apktool-probe.bin')
> with p.open('wb') as f:
>  for c in r.iter_content(65536):
>   f.write(c)
>   if time.time()-t>25:break
> print(p.stat().st_size, time.time()-t,flush=True)
> '@ | python -`
>
> </details>
>
> 已找到明确差异：小米版包含专门的 `MiuiBottomManager`，读取 `ro.miui.support_miui_ime_bottom`，并处理底部栏、左右快捷功能和键盘偏移；普通版没有这组代码。
>
> 这说明适配涉及实际逻辑移植。接下来会检查它依赖哪些小米系统接口，以及共存时更改包名是否会影响系统识别。
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `Get-ChildItem -LiteralPath work\tools | Select-Object Name,Length; Get-ChildItem -LiteralPath work\inventory | Select-Object Name,Length`
> - Ran `rg --files --hidden 'C:\Users\Kirito787\.codex' 'C:\Program Files' 'C:\Program Files (x86)' 'D:\' -g java.exe -g javac.exe -g jvm.dll -g apktool*.jar -g jadx*.jar 2>$null`
> - Ran `@'
> import requests,pathlib,time
> u='https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.12.1%2B1/OpenJDK21U-jre_x64_windows_hotspot_21.0.12.1_1.zip'
> p=pathlib.Path('work/tools/jre.zip');r=requests.get(u,timeout=(15,45),stream=True);r.raise_for_status();print(r.headers.get('content-length'),flush=True)
> with p.open('wb') as f:
>  for c in r.iter_content(65536):f.write(c)
> print('jre downloaded',p.stat().st_size,flush=True)
> import zipfile
> with zipfile.ZipFile(p) as z:z.extractall('work/tools/jre')
> '@ | Set-Content work\download_jre.py -Encoding utf8; python work\download_jre.py`
> - Ran `Get-CimInstance Win32_Process -Filter "name='python.exe'" | Select-Object ProcessId,CommandLine; & 'D:\SteamLibrary\steamapps\common\SlayTheSpire\jre\bin\java.exe' -version; Get-Content -LiteralPath work\inventory\standard-manifest.json -TotalCount 35; Get-Content -LiteralPath work\inventory\xiaomi-manifest.json -TotalCount 35`
> - Ran `@'
> import requests,pathlib,concurrent.futures,time,zipfile
> root=pathlib.Path('work/tools');jobs=[('apktool-fast.jar','https://github.com/iBotPeaches/Apktool/releases/download/v3.0.3/apktool_3.0.3.jar',15478013),('jre-fast.zip','https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.12.1%2B1/OpenJDK21U-jre_x64_windows_hotspot_21.0.12.1_1.zip',48999141),('jadx-fast.zip','https://github.com/skylot/jadx/releases/download/v1.5.6/jadx-1.5.6.zip',72646741)]
> def download(job):
>  name,url,size=job;parts=root/(name+'.parts');parts.mkdir(exist_ok=True);step=1024*1024
>  def part(i):
>   start=i*step;end=min(size,start+step)-1;p=parts/str(i)
>   if p.exists() and p.stat().st_size==end-start+1:return
>   for attempt in range(3):
>    try:
>     r=requests.get(url,headers={'Range':f'bytes={start}-{end}'},stream=True,timeout=(15,45));r.raise_for_status()
>     if r.status_code!=206 or not r.headers.get('Content-Range','').startswith(f'bytes {start}-'):raise ValueError('range mismatch '+str(r.headers))
>     with p.open('wb') as f:
>      for c in r.iter_content(65536):f.write(c)
>     if p.stat().st_size!=end-start+1:raise ValueError('bad size')
>     return
>    except Exception:
>     if attempt==2:raise
>  with concurrent.futures.ThreadPoolExecutor(max_workers=16) as ex:list(ex.map(part,range((size+step-1)//step)))
>  with (root/name).open('wb') as f:
>   for i in range((size+step-1)//step):f.write((parts/str(i)).read_bytes())
>  print(name,'done',size,flush=True)
>  if name.endswith('.zip'):
>   with zipfile.ZipFile(root/name) as z:z.extractall(root/name[:-4])
> for j in jobs:download(j)
> '@ | Set-Content work\download_fast.py -Encoding utf8; python work\download_fast.py`
>
> </details>
>
> <details><summary>Ran 4 commands, searched the web</summary>
>
> - Ran `@'
> import json,pathlib
> p=pathlib.Path('work/inventory')
> a=json.loads((p/'standard-manifest.json').read_text('utf-8'));b=json.loads((p/'xiaomi-manifest.json').read_text('utf-8'))
> for label,items in [('standard',a),('xiaomi',b)]:
>  print(label)
>  for e in items:
>   if e['tag'] in ['application','provider','service','permission','instrumentation'] or e['tag']=='meta-data' and any(k in str(e).lower() for k in ['miui','input','ime']):print(e)
> '@ | python -`
>
> - Ran `Get-ChildItem -LiteralPath work\tools | Select-Object Name,Length; Get-ChildItem -LiteralPath work\tools\apktool-fast.jar.parts -ErrorAction SilentlyContinue | Measure-Object Length -Sum | Select-Object Count,Sum`
>
> - Ran `Get-ChildItem -LiteralPath work\tools\apktool-fast.jar.parts -ErrorAction SilentlyContinue | Select-Object Name,Length | Format-Table -AutoSize; python -c "import psutil; print([(p.pid,p.cmdline()) for p in psutil.process_iter(['name']) if p.info['name']=='python.exe'])"`
>
> Searched the web for `"InputMethodServiceInjector" "sogou" ...`
>
> - Ran `Get-Content -LiteralPath work\inventory\xiaomi-screen-disasm.txt -TotalCount 70; Get-ChildItem -LiteralPath work\tools | Select-Object Name,Length | Format-Table -AutoSize`
>
> </details>
>
> “全面屏键盘优化”你主要希望实现哪种效果？
> - 小米系统原生底部栏及语音/切换键盘按钮
> - 键盘底部抬高、不与手势条重叠
> - 以上两项都需要
>
> **“全面屏键盘优化”你主要希望实现哪种效果？**
>
> 以上两项都需要
>
> <details><summary>Ran a command</summary>
>
> - Ran `@'
> import requests
> u='https://api.azul.com/metadata/v1/zulu/packages/?java_version=21&os=windows&arch=x86_64&archive_type=zip&java_package_type=jre&release_status=ga&availability_types=CA&latest=true'
> r=requests.get(u,timeout=20);r.raise_for_status();j=r.json();print([(x['name'],x['download_url']) for x in j[:4]],flush=True)
> '@ | python -`
>
> </details>
>
> 共存这一项已核实：两个原包的包名不同，Provider authorities 和自定义权限也没有冲突，通常可以直接同时安装，无需改包名。这也避免了破坏原生输入引擎中写死的 JNI 类路径。
>
> 你希望同时保留原生底部按钮和底部抬高效果，我会按这个范围继续检查。目前还发现普通版部分原生库不支持原生 16KB 内存页；你的设备是否启用该模式，需要设备侧验证。
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `@'
> import requests,pathlib,zipfile
> p=pathlib.Path('work/tools/zulu-jre.zip');u='https://cdn.azul.com/zulu/bin/zulu21.52.203-ca-jre21.0.12.1-win_x64.zip'
> r=requests.get(u,timeout=(15,30),stream=True);r.raise_for_status();print(r.headers.get('content-length'),flush=True)
> with p.open('wb') as f:
>  for c in r.iter_content(65536):f.write(c)
> print('downloaded',p.stat().st_size,flush=True)
> with zipfile.ZipFile(p) as z:z.extractall('work/tools/zulu-jre')
> '@ | Set-Content work\download_zulu.py -Encoding utf8; python work\download_zulu.py`
> - Ran `python work\download_fast.py`
> - Ran `$javaPath = (Get-ChildItem -LiteralPath work\tools\zulu-jre -Filter java.exe -Recurse | Select-Object -First 1).FullName; & $javaPath -version; Get-ChildItem -LiteralPath work\tools\apktool-fast.jar.parts | Select-Object Name,Length | Format-Table -AutoSize; @'
> import socket
> try:
>  s=socket.create_connection(('127.0.0.1',5037),2);q=b'host:devices-l';s.sendall(f'{len(q):04x}'.encode()+q);print('ADB:',s.recv(8192));s.close()
> except Exception as e:print('Existing ADB server:',str(e))
> '@ | python -`
> - Ran `@'
> import requests,pathlib,zipfile,time
> u='https://github.com/skylot/jadx/releases/download/v1.5.6/jadx-1.5.6.zip?download=1';p=pathlib.Path('work/tools/jadx-ready.zip')
> for i in range(3):
>  try:
>   r=requests.get(u+'&attempt='+str(i),timeout=(10,20));r.raise_for_status();p.write_bytes(r.content)
>   with zipfile.ZipFile(p) as z:z.extractall('work/tools/jadx-ready')
>   print('jadx ready',len(r.content),flush=True);break
>  except Exception as e:print(type(e).__name__,str(e)[:120],flush=True)
> '@ | Set-Content work\download_jadx.py -Encoding utf8; python work\download_jadx.py`
>
> </details>
>
> <details><summary>Ran 6 commands</summary>
>
> - Ran `Get-ChildItem -LiteralPath work\tools\apktool-fast.jar.parts | Select-Object Name,Length | Format-Table -AutoSize; Get-ChildItem -LiteralPath work\tools | Select-Object Name,Length | Format-Table -AutoSize; $javaPath = (Get-ChildItem -LiteralPath work\tools\zulu-jre -Filter java.exe -Recurse | Select-Object -First 1).FullName; & $javaPath -jar work\tools\signer.jar --help`
> - Ran `@'
> import requests,pathlib,time,zipfile
> p=pathlib.Path('work/tools/apktool-final.jar');parts=pathlib.Path('work/tools/apktool-fast.jar.parts')
> u='https://github.com/iBotPeaches/Apktool/releases/download/v3.0.3/apktool_3.0.3.jar?part=12'
> r=requests.get(u,headers={'Range':'bytes=12582912-13631487'},timeout=(10,25));r.raise_for_status();print(r.status_code,len(r.content),r.headers.get('Content-Range'),flush=True)
> if len(r.content)==1048576 and r.status_code==206:
>  (parts/'12').write_bytes(r.content)
>  with p.open('wb') as f:
>   for i in range(15):f.write((parts/str(i)).read_bytes())
>  with zipfile.ZipFile(p) as z:print('apktool valid entries',len(z.infolist()),flush=True)
> '@ | python -`
> - Ran `Get-ChildItem work\ads -ErrorAction SilentlyContinue | Select-Object Name,Length | Format-Table -AutoSize; Get-ChildItem work\tools\apktool-fast.jar.parts\12 | Select-Object Length; Get-ChildItem work\tools\jadx-ready.zip -ErrorAction SilentlyContinue | Select-Object Length`
> - Ran `Get-ChildItem work\tools | Select-Object Name,Length | Format-Table -AutoSize; $javaPath = (Get-ChildItem -LiteralPath work\tools\zulu-jre -Filter java.exe -Recurse | Select-Object -First 1).FullName; if (Test-Path -LiteralPath work\tools\apktool-fast.jar) { & $javaPath -jar work\tools\apktool-fast.jar --version }`
> - Ran `$javaPath = (Get-ChildItem -LiteralPath work\tools\zulu-jre -Filter java.exe -Recurse | Select-Object -First 1).FullName; & $javaPath -Xmx3g -jar work\tools\apktool-fast.jar d -p work\framework -o work\standard '搜狗输入法.apk' *> work\decode-standard.log; Get-Content work\decode-standard.log -Tail 15`
> - Ran `$javaPath = (Get-ChildItem -LiteralPath work\tools\zulu-jre -Filter java.exe -Recurse | Select-Object -First 1).FullName; & $javaPath -Xmx2g -jar work\tools\apktool-fast.jar d -p work\framework-xiaomi -o work\xiaomi '搜狗输入法小米.apk' *> work\decode-xiaomi.log; Get-Content work\decode-xiaomi.log -Tail 15`
>
> </details>
>
> 广告部分找到了应用自带的“关闭键盘广告”开关，能沿着设置页面追到实际读取逻辑。我会优先使用这条现有路径，并单独检查开屏广告，避免粗暴删除网络权限或共享模块。
>
> 小米原生底栏则涉及 ROM 的 `InputMethodServiceInjector` / `InputMethodServiceStubImpl`。目前能证明小米版在调用它们，但还不能证明系统会允许普通版启用同样的底栏。
>
> <details><summary>Ran a command, searched the web</summary>
>
> - Ran `Get-Content work\decode-standard.log -Tail 12; Get-Content work\decode-xiaomi.log -Tail 12; rg --files work\standard -g '*SogouIME.smali' -g '*AmsKv.smali' -g '*Display*' -g '*Navigation*' | Select-Object -First 35`
>
> Searched the web for `"InputMethodServiceInjector" "isXiaoAiEnable" ...`
>
> </details>
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `Get-Content work\decode-standard.log -Tail 5; Get-Content work\decode-xiaomi.log -Tail 5; rg -n '^\.method.* (onCreateInputView|onCreateCandidatesView|onStartInputView|onComputeInsets|onWindowShown|onCreate|onFinishInputView)\(' work\standard\smali*\com\sohu\inputmethod\sogou\SogouIME.smali; rg -n 'key_close_ad_switch_status|KV_AMS_SPLASH_STATE' work\standard\smali_classes3\com\sogou\imskit\feature\lib\tangram\common\AmsKv.smali`
> - Ran `@'
> import zipfile
> with zipfile.ZipFile('work/tools/apktool-fast.jar') as z:
>  print('\n'.join(x for x in z.namelist() if x.endswith('/Main.class') or x.endswith('Smali.class')))
> '@ | python -; Get-Content work\standard\apktool.yml -TotalCount 70; rg --files work\standard -g SogouIME.smali`
>
> </details>
>
> <details><summary>Ran a command</summary>
>
> - Ran `Get-Content work\inventory\findings.md -TotalCount 90; Get-ChildItem -LiteralPath work\tools | Select-Object Name,Length | Format-Table -AutoSize`
>
> </details>
>
> 完整验证小米系统原生底栏，需要读取目标手机的系统接口和输入法日志；目前电脑未发现可用的 ADB 连接。你能否将这台手机通过 USB 调试连接到当前电脑？
> - 可以连接，稍后告知
> - 暂时不能，先制作本地候选包
>
> 普通版也自带“键盘底部高度”设置，支持标准、自适应、全面屏三种模式。我会优先复用它处理底部抬高，这样可以沿用现有的横屏、悬浮和高度调整逻辑。
>
> 广告候选补丁已收敛为三个现有开关：关闭总广告、关闭键盘广告、关闭开屏广告。图片结果等可能承载正常内容的分支会保留。原生小米按钮栏仍需手机侧验证，我已发出 USB 调试连接信息请求。
>
> <details><summary>Ran a command</summary>
>
> - Ran `Get-ChildItem work\ads | Select-Object Name,Length | Format-Table -AutoSize; rg -n '^\.method.* (onCreateInputView|onCreateCandidatesView|onStartInputView|onComputeInsets|onWindowShown|onCreate|onFinishInputView)\(' work\standard\smali_classes5\com\sohu\inputmethod\sogou\SogouIME.smali; rg -n 'pref_key_full_screen_bottom_offset|pref_key.*bottom|KEY_AD_SWITCH' work\standard\smali_classes3\com\sogou\feature\shortcut\l.smali work\standard\smali\com\sogou\base\special\screen -g '*.smali'`
>
> </details>
>
> **完整验证小米系统原生底栏，需要读取目标手机的系统接口和输入法日志；目前电脑未发现可用的 ADB 连接。你能否将这台手机通过 USB 调试连接到当前电脑？**
>
> 可以连接，稍后告知
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `New-Item -ItemType Directory -Path work\tmp,work\tool-home -Force | Out-Null; $javaPath = (Get-ChildItem -LiteralPath work\tools\zulu-jre -Filter java.exe -Recurse | Select-Object -First 1).FullName; & $javaPath ('-Djava.io.tmpdir=' + (Resolve-Path work\tmp).Path) ('-Duser.home=' + (Resolve-Path work\tool-home).Path) -jar work\tools\signer.jar -a '搜狗输入法.apk' '搜狗输入法小米.apk' -y *> work\original-signatures.log; Get-Content work\original-signatures.log -Tail 40`
> - Ran `@'
> import zipfile
> with zipfile.ZipFile('work/tools/apktool-fast.jar') as z:
>  print('\n'.join(z.namelist()[:25]));print('\n'.join(x for x in z.namelist() if 'smali' in x.lower())[:2500])
> '@ | python -; Get-Content work\ads\patch-plan.json -TotalCount 100; Get-Content work\inventory\standard-screen-settings-disasm.txt -TotalCount 130`
>
> </details>
>
> <details><summary>Ran a command</summary>
>
> - Ran `Get-Content work\inventory\standard-bottom-minimal.md; Get-Content work\original-signatures.log -Tail 45; Get-Content work\ads\patch_dex.py -TotalCount 180`
>
> </details>
>
> 手机已通过USB连接电脑
>
> 我先读取手机的连接状态、屏幕密度、内存页大小和当前输入法配置，确认系统原生底栏的接入条件。这一步不安装 APK，也不卸载或清除现有输入法数据。
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' version; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' devices -l`
>
> </details>
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' devices -l`
>
> </details>
>
> 电脑已识别到手机，但状态为 unauthorized。请在手机上确认“允许 USB 调试”的 RSA 授权弹窗；确认后告诉我。
>
> **电脑已识别到手机，但状态为 unauthorized。请在手机上确认“允许 USB 调试”的 RSA 授权弹窗；确认后告诉我。**
>
> 允许 USB 调试
>
> <details><summary>Ran 5 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell getprop ro.product.model; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell getprop ro.build.version.sdk; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell wm density; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell getconf PAGESIZE; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell settings get secure default_input_method; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell ime list -s; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell getprop ro.miui.support_miui_ime_bottom; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell settings get secure enable_miui_ime_bottom_view; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell settings get global force_fsg_nav_bar; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell settings get global hide_gesture_line`
> - Ran `New-Item -ItemType Directory -Path work\device -Force | Out-Null; @'
> import subprocess,json,pathlib
> ADB=r'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe'
> cmds={
>  'props':['shell','getprop'],
>  'standard_package':['shell','pm','path','com.sohu.inputmethod.sogou'],
>  'xiaomi_package':['shell','pm','path','com.sohu.inputmethod.sogou.xiaomi'],
>  'framework':['shell','ls','/system/framework'],
>  'system_ext_framework':['shell','ls','/system_ext/framework'],
>  'product_framework':['shell','ls','/product/framework'],
>  'permissions':['shell','ls','/system/etc/permissions'],
> }
> root=pathlib.Path('work/device')
> for name,args in cmds.items():
>  r=subprocess.run([ADB,'-s','df043723',*args],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=30)
>  (root/(name+'.txt')).write_text(r.stdout+r.stderr,'utf8')
>  if name=='props':
>   print(name,'\n'.join(x for x in r.stdout.splitlines() if any(k in x for k in ['ro.miui','ro.build.version','ro.product.model','ro.product.device','ro.product.cpu.abi'])))
>  else:print(name,r.returncode,r.stdout[:7000],r.stderr)
> '@ | Set-Content work\device_probe.py -Encoding utf8`
> - Ran `python work\device_probe.py`
> - Ran `@'
> from pathlib import Path
> for file in ['framework.txt','system_ext_framework.txt']:
>  print(file)
>  print('\n'.join(x for x in (Path('work/device')/file).read_text('utf8').splitlines() if any(k in x for k in ['miui-framework','miui-services','framework.jar','input'])))
> '@ | python -`
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /system_ext/framework/miui-framework.jar work\device\miui-framework.jar; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell ime list -a -s; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell dumpsys package com.sohu.inputmethod.sogou > work\device\standard-package-dump.txt; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell dumpsys package com.sohu.inputmethod.sogou.xiaomi > work\device\xiaomi-package-dump.txt`
>
> </details>
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `@'
> from pathlib import Path
> import hashlib,json,re,zipfile,subprocess,secrets
> root=Path.cwd();out=root/'outputs';out.mkdir(exist_ok=True);work=root/'work';sign=work/'signing';sign.mkdir(exist_ok=True)
> source=root/'搜狗输入法.apk';dex=work/'ads/classes3.dex';unsigned=work/'sogou-ad-switches-unsigned.apk'
> assert hashlib.sha256(source.read_bytes()).hexdigest()=='df10256e9228e9ed3831be4278a7b9046dd16b0e045d68dee8baafa2491c1574'
> assert hashlib.sha256(dex.read_bytes()).hexdigest()=='9c8860775d6a5a24997183c662562bdd4fdfe159790e278dde6ef02b2fc5ffff'
> with zipfile.ZipFile(source) as src,zipfile.ZipFile(unsigned,'w') as dst:
>  dst.comment=src.comment
>  for item in src.infolist():
>   if re.match(r'^META-INF/(?:[^/]+\.(?:SF|RSA|DSA|EC)|MANIFEST\.MF)$',item.filename,re.I):continue
>   dst.writestr(item,dex.read_bytes() if item.filename=='classes3.dex' else src.read(item.filename))
> java=next((work/'tools/zulu-jre').glob('*/bin/java.exe'));keytool=java.with_name('keytool.exe');meta=sign/'local-key.json';ks=sign/'local-test.p12'
> if not meta.exists():meta.write_text(json.dumps({'alias':'sogou-local-test','password':secrets.token_urlsafe(24)}),'utf8')
> m=json.loads(meta.read_text());props=['-Djava.io.tmpdir='+str(work/'tmp'),'-Duser.home='+str(work/'tool-home')]
> if not ks.exists():
>  r=subprocess.run([str(keytool),*['-J'+x for x in props],'-genkeypair','-alias',m['alias'],'-keyalg','RSA','-keysize','2048','-validity','3650','-dname','CN=Local Sogou Test Build','-storetype','PKCS12','-keystore',str(ks),'-storepass',m['password'],'-keypass',m['password']],capture_output=True,text=True,encoding='utf8',errors='replace')
>  assert r.returncode==0,r.stderr
> r=subprocess.run([str(java),*props,'-jar',str(work/'tools/signer.jar'),'-a',str(unsigned),'-o',str(work/'signed'), '--ks',str(ks),'--ksAlias',m['alias'],'--ksPass',m['password'],'--ksKeyPass',m['password']],capture_output=True,text=True,encoding='utf8',errors='replace')
> (work/'candidate-signature.log').write_text(r.stdout+r.stderr,'utf8');print(r.stdout[-2500:]);assert r.returncode==0,r.stderr
> signed=next((work/'signed').glob('*-signed.apk'));target=out/'sogou-20.17-ad-switches-TEST.apk';target.write_bytes(signed.read_bytes())
> with zipfile.ZipFile(source) as a,zipfile.ZipFile(target) as b:
>  names=[n for n in a.namelist() if not re.match(r'^META-INF/(?:[^/]+\.(?:SF|RSA|DSA|EC)|MANIFEST\.MF)$',n,re.I)]
>  changes=[n for n in names if a.read(n)!=b.read(n)]
>  assert changes==['classes3.dex'],changes
> report={'apk':target.name,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'changed_payloads':changes,'original_apk_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'signature':'local test certificate, not official','runtime':'not yet tested','full_miui_integration':'not implemented in this ad-only candidate'}
> (out/'candidate-validation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),'utf8');print(json.dumps(report,indent=2))
> '@ | Set-Content work\build_candidate.py -Encoding utf8; python work\build_candidate.py`
> - Ran `Select-String -LiteralPath work\device\standard-package-dump.txt,work\device\xiaomi-package-dump.txt -Pattern 'versionName=','versionCode=','flags=','pkgFlags=','signatures=','signing' | Select-Object -First 20; Get-ChildItem work\tools -Name; Get-Content work\candidate-signature.log -Tail 16 -ErrorAction SilentlyContinue`
>
> </details>
>
> 已从手机的实际系统框架确认原因：原生底栏有包名白名单，包含搜狗小米版，却不包含普通版。手机的底栏和手势开关均已开启，内存页大小是 4KB，前面发现的 16KB 库对齐问题不适用于当前环境。
>
> 现在有一个值得验证的方案：在普通版自己的进程内注册底栏支持，让系统加载真正的底栏插件，保留两个原包名。我会先检查插件是否还有第二层限制，再制作测试包。
>
> <details><summary>Ran 3 commands, called a tool</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell pm path com.miui.phrase; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell getprop ro.miui.ime_need_bottom`
>
> - Ran `Get-Content work\standard\smali_classes5\com\sohu\inputmethod\sogou\SogouIME.smali | Select-Object -Skip 620 -First 180; Get-ChildItem work\signed -ErrorAction SilentlyContinue | Select-Object Name,Length | Format-Table -AutoSize`
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /product/app/MIUIFrequentPhrase/MIUIFrequentPhrase.apk work\device\miui-phrase.apk`
>
> MCP tool call
>
> rea.close_binary
>
> ```json
> {}
> ```
>
> ```text
> {"result":null}
> ```
>
> ```json
> {
>   "result": null
> }
> ```
>
> </details>
>
> <details><summary>Ran 4 commands</summary>
>
> - Ran `Get-ChildItem -LiteralPath work\ads -Directory | ForEach-Object FullName; Get-Content work\ads\findings.md -Tail 30; @'
> import zipfile
> with zipfile.ZipFile('work/tools/apktool-fast.jar') as z:
>  print('\n'.join(x for x in z.namelist() if 'smali/' in x and (x.endswith('Options.class') or x.endswith('/Smali.class') or x.endswith('/Baksmali.class'))))
> '@ | python -`
> - Ran `Get-ChildItem -LiteralPath work\ads\verify-decoded -Force | Select-Object Name; Get-Content work\ads\verify-decoded\apktool.yml -TotalCount 25; @'
> import zipfile
> with zipfile.ZipFile('work/tools/apktool-fast.jar') as z:
>  print('\n'.join(x for x in z.namelist() if '/smali/' in x and ('Main' in x or 'Builder' in x or 'Smali' in x))[-2000:])
> '@ | python -`
> - Ran `@'
> import zipfile,struct
> with zipfile.ZipFile('搜狗输入法.apk') as z:
>  for name in ['classes2.dex','classes3.dex','classes5.dex']:
>   b=z.read(name);print(name,struct.unpack_from('<I',b,88)[0],'method refs')
> '@ | python -; Get-Content work\ads\verify-decoded\AndroidManifest.xml -TotalCount 15; Get-Content work\inventory\rom-ime-disasm.txt -TotalCount 30`
> - Ran `Get-ChildItem work\inventory -Filter '*phrase*' | Select-Object Name,Length; Get-Content work\inventory\rom-ime-disasm.txt | Select-String 'isCanLoadPlugin|addMiuiBottomView|sIsImeSupport|sVersionCode|sImeMinVersionSupport' | Select-Object -First 30; Get-Content work\standard\smali_classes5\com\sohu\inputmethod\sogou\SogouIME.smali -TotalCount 16; Get-Content work\ads\after-baksmali.txt -TotalCount 12`
>
> </details>
>
> 底栏插件里也有同样的白名单，但它的按钮广播会投递给当前输入法包名，并没有写死小米版包名。因此，方案已明确为：在普通版自身进程中注册两层支持，并接入现有的语音、键盘类型和语言切换入口。
>
> 广告候选包已通过签名、对齐和资源逐项比对。目前仍未安装测试包，也未改动手机上的应用数据。
>
> <details><summary>Ran a command</summary>
>
> - Ran `Select-String -LiteralPath work\original-signatures.log,work\candidate-signature.log -Pattern 'warnings|verified|SHA256' | ForEach-Object Line; Get-ChildItem work\ads\bridge -ErrorAction SilentlyContinue | Select-Object Name,Length | Format-Table -AutoSize; Get-ChildItem work\tools -Name`
>
> </details>
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 pull /system/framework/framework.jar work\device\framework.jar; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell dumpsys package com.miui.phrase > work\device\phrase-package-dump.txt`
> - Ran `Get-ChildItem work\compat -ErrorAction SilentlyContinue | Select-Object Name,Length | Format-Table -AutoSize; Get-Content work\device\standard-package-dump.txt | Select-Object -Skip 938 -First 16; Get-Content work\device\xiaomi-package-dump.txt | Select-String 'versionCode=|versionName=' | ForEach-Object Line`
>
> </details>
>
> <details><summary>Ran a command</summary>
>
> - Ran `Select-String -LiteralPath work\device\phrase-package-dump.txt -Pattern 'userId=|sharedUser=|codePath=|versionCode=|pkgFlags=' | ForEach-Object Line; Get-ChildItem work\compat -Recurse -File -ErrorAction SilentlyContinue | Select-Object -First 12 FullName,Length | Format-Table -AutoSize`
>
> </details>
>
> Stream error
>
> Reconnecting... waiting for network
> Connection failed: error sending request
>
> <details><summary>Ran 5 commands, searched the web</summary>
>
> Searched the web for `site.github.com LSPosed AndroidHiddenApiBypass Android 16 getStaticFields invoke ...`
>
> - Ran `Get-Content work\compat\source\MiuiBottomCompat.smali -TotalCount 50; Get-ChildItem work\outputs -ErrorAction SilentlyContinue`
>
> Searched the web for `https://github.com/LSPosed/AndroidHiddenApiBypass`
>
> - Ran `@'
> import requests,pathlib
> u='https://repo.maven.apache.org/maven2/org/lsposed/hiddenapibypass/hiddenapibypass/maven-metadata.xml'
> r=requests.get(u,timeout=15);print(r.status_code,r.text[:1200])
> '@ | python -`
>
> - Ran `@'
> import requests,pathlib,zipfile,hashlib
> p=pathlib.Path('work/tools/hiddenapi');p.mkdir(exist_ok=True)
> base='https://repo.maven.apache.org/maven2/org/lsposed/hiddenapibypass/hiddenapibypass/6.2/'
> u=base+'hiddenapibypass-6.2.aar';r=requests.get(u,timeout=25);r.raise_for_status();(p/'hiddenapibypass-6.2.aar').write_bytes(r.content)
> s=requests.get(u+'.sha256',timeout=15);print('aar',len(r.content),'sha256',hashlib.sha256(r.content).hexdigest(),'published',s.status_code,s.text[:80])
> with zipfile.ZipFile(p/'hiddenapibypass-6.2.aar') as z:z.extractall(p/'aar')
> u=base+'hiddenapibypass-6.2-sources.jar';r=requests.get(u,timeout=15);r.raise_for_status();(p/'sources.jar').write_bytes(r.content)
> with zipfile.ZipFile(p/'sources.jar') as z:z.extractall(p/'source')
> print('ready')
> '@ | python -`
>
> - Ran `Get-Content work\tools\hiddenapi\source\org\lsposed\hiddenapibypass\LSPass.java -TotalCount 190; Get-ChildItem work\tools\hiddenapi\aar -Name; @'
> import requests
> u='https://dl.google.com/dl/android/maven2/com/android/tools/r8/maven-metadata.xml';r=requests.get(u,timeout=15);print(r.status_code,r.text[-1600:])
> '@ | python -`
>
> - Ran `@'
> import requests,pathlib
> u='https://dl.google.com/dl/android/maven2/com/android/tools/r8/9.5.26/r8-9.5.26.jar';p=pathlib.Path('work/tools/r8.jar');r=requests.get(u,timeout=(10,30));r.raise_for_status();p.write_bytes(r.content);print('r8',len(r.content))
> '@ | python -`
>
> </details>
>
> <details><summary>Ran a command</summary>
>
> - Ran `New-Item -ItemType Directory -Path work\tools\hiddenapi\dex -Force | Out-Null; $javaPath = (Get-ChildItem -LiteralPath work\tools\zulu-jre -Filter java.exe -Recurse | Select-Object -First 1).FullName; & $javaPath -cp work\tools\r8.jar com.android.tools.r8.D8 --release --min-api 28 --output work\tools\hiddenapi\dex work\tools\hiddenapi\aar\classes.jar *> work\tools\hiddenapi\d8.log; Get-Content work\tools\hiddenapi\d8.log -Tail 18; Get-ChildItem work\tools\hiddenapi\dex | Select-Object Name,Length | Format-Table -AutoSize`
>
> </details>
>
> Stream error
>
> Reconnecting... waiting for network
> Connection failed: error sending request
>
> <details><summary>Ran 2 commands</summary>
>
> - Ran `@'
> from pathlib import Path
> import zipfile,subprocess,json,sys,hashlib
> root=Path.cwd();work=root/'work';java=next((work/'tools/zulu-jre').glob('*/bin/java.exe'));m=json.loads((work/'signing/local-key.json').read_text());ks=work/'signing/local-test.p12'
> source=Path(sys.argv[1]);dest=Path(sys.argv[2]);tag=dest.stem;staging=work/'signed'/tag;staging.mkdir(parents=True,exist_ok=True)
> r=subprocess.run([str(java),'-Djava.io.tmpdir='+str(work/'tmp'),'-Duser.home='+str(work/'tool-home'),'-jar',str(work/'tools/signer.jar'),'-a',str(source.resolve()),'-o',str(staging),'--ks',str(ks),'--ksAlias',m['alias'],'--ksPass',m['password'],'--ksKeyPass',m['password']],capture_output=True,text=True,encoding='utf8',errors='replace')
> (work/(tag+'-sign.log')).write_text(r.stdout+r.stderr,'utf8');assert r.returncode==0,r.stdout+r.stderr
> signed=list(staging.glob('*-signed.apk'));assert len(signed)==1
> assert 'signature verified' in r.stdout and 'zipalign verified' in r.stdout,r.stdout
> dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(signed[0].read_bytes());print(dest,hashlib.sha256(dest.read_bytes()).hexdigest());print(r.stdout[-1100:])
> '@ | Set-Content work\sign_apk.py -Encoding utf8; @'
> import zipfile,pathlib
> p=pathlib.Path('work/compat/probe-dual-unsigned.apk')
> with zipfile.ZipFile(p) as a,zipfile.ZipFile('work/compat/probe-dual-library.apk','w') as b:
>  for z in a.infolist():b.writestr(z,a.read(z.filename))
>  b.write('work/tools/hiddenapi/dex/classes.dex','classes2.dex')
> '@ | python -; python work\sign_apk.py work\compat\probe-dual-library.apk outputs\miui-bottom-compat-PROBE.apk`
> - Ran `Get-ChildItem outputs | Select-Object Name,Length | Format-Table -AutoSize; Get-Content work\compat\probe\AndroidManifest.xml -ErrorAction SilentlyContinue -TotalCount 35; Get-ChildItem work\compat -Directory | Select-Object -ExpandProperty Name`
>
> </details>
>
> 又确认了一道限制：白名单相关接口被 Android 标记为受限，普通反射预计会失败。我已生成一个 33KB 的[兼容性探针 APK](./outputs/miui-bottom-compat-PROBE.apk)，用于比较普通反射与进程内兼容库能否访问这两个接口。
>
> 探针不声明任何权限、不采集输入内容，也不替换现有输入法；它只会在自己的进程中测试并显示结果。
>
> 是否允许通过 ADB 安装并运行已生成的 REA MIUI Probe（33KB、无权限、新包名 local.rea.miuiprobe）？它不会替换或清除任何输入法，用于验证当前 ROM 的接口是否可用。
> - 允许安装并运行探针
> - 暂不安装，只保留分析结果
>
> **是否允许通过 ADB 安装并运行已生成的 REA MIUI Probe（33KB、无权限、新包名 local.rea.miuiprobe）？它不会替换或清除任何输入法，用于验证当前 ROM 的接口是否可用。**
>
> 允许安装并运行探针
>
> <details><summary>Ran a command</summary>
>
> - Ran `& 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 install outputs\miui-bottom-compat-PROBE.apk; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 shell am start -W -n local.rea.miuiprobe/.ProbeActivity; & 'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe' -s df043723 logcat -d -s MiuiBottomProbe:I MiuiBottomCompat:V AndroidRuntime:E '*:S' > work\device\probe-logcat.txt; Get-Content work\device\probe-logcat.txt -Tail 75`
>
> </details>
>
> Stream error
>
> Reconnecting... waiting for network
> Connection failed: error sending request
>
> 探针实测结果已返回：普通反射失败，兼容库则成功完成了两层注册。这个结果证明接口访问路径可行，但还不能等同于输入法底栏已经显示成功。
>
> 我正在把已验证的访问路径和三个按钮回调合入普通版。正式测试包会保留普通版包名和小米版原包；安装前还需处理重新签名与现有普通版数据的关系。
>
> <details><summary>Ran a command</summary>
>
> - Ran `@'
> import requests,pathlib,hashlib
> p=pathlib.Path('outputs');u='https://raw.githubusercontent.com/LSPosed/AndroidHiddenApiBypass/main/LICENSE';r=requests.get(u,timeout=15);r.raise_for_status();(p/'LICENSE-LSPass.txt').write_bytes(r.content)
> u='https://repo.maven.apache.org/maven2/org/lsposed/hiddenapibypass/hiddenapibypass/6.2/hiddenapibypass-6.2.aar.sha1';r=requests.get(u,timeout=15);r.raise_for_status();a=pathlib.Path('work/tools/hiddenapi/hiddenapibypass-6.2.aar').read_bytes();assert hashlib.sha1(a).hexdigest()==r.text.strip();print('Maven published sha1 matched')
> '@ | python -; Get-Content work\compat\implementation-notes.md -TotalCount 55; Get-Content work\ads\bridge\receiver-integration.md -TotalCount 55`
>
> </details>
>
> System error
>
> You’ve hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/settings/usage to purchase more credits or try again at 1:48 PM.
</details>
