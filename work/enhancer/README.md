# 搜狗增强项目：2026-10-21 实现与验证

## 交付范围

方案 A 是两个 APK：官网原版搜狗 20.17.0（2620）及增强模块 1.2.1。
方案 B 是一个 APK：搜狗 20.17.0（2620）内置增强模块，包名
`com.sohu.inputmethod.sogou.enhanced`，可与官方普通版、小米版共存。
用户于本轮明确选择共存，禁止以卸载原版换签名方式部署 B。

当前 A 在 `outputs/2026-10-21-A-1.2.1/`，B 继续用 `outputs/2026-10-21-skin-1.2.0/方案B/`。
旧 1.2.0 A 与 1.1.0 产物仍保留作历史记录。
原始 APK、原工程、历史交接文档均保留。没有创建 GitHub 仓库或上传资产。

## 基线与修改

### A 1.2.1：入口与任务栈修缮

用户反馈 A 两入口均像模块界面。直接启动官方入口能显示商城，未复现官方跳转模块的原始现象。
新增仅 A 使用的 `companion-smali/com/sogouenhance/AHomeActivity.smali`；桌面名改为
“搜狗增强·方案A”，首页提供官方搜狗、增强设置、系统输入法设置三个入口。
首页使用 singleTask，实测再次打开不会停留在上次的增强设置页；原设置组件及隐藏图标逻辑保留。
官方包不修改；B 不重新构建或安装。构建支持 `python work/enhancer/build.py --variant a`，
保留 `modules.json` 中未构建的 B 项，A 版本 1.2.1（4）、B 模块保持 1.2.0（3）。

最终 APK 哈希 `976a9ef463a95d444db729c4493b141ed8b6a14bd5c87230cbf62217c119ef00` 与手机安装包相同。
通过签名、zipalign、ZIP CRC 检查；除既有版本适配 HookEntry 外，所有原 smali 类逐文件保持不变。
真机通过：首页冷启动、三个按钮、从增强设置再次打开模块桌面入口、官方设置到独立模块的跳转、
真实 nihao 点按候选与“你好”提交、原生底栏右键打开剪贴板、冷启动 27 条原 hook 注册。
原偏好逐项恢复一致，默认输入法恢复本轮测试前的官方普通版；B 和小米版无安装/卸载/清数据操作。
证据在 `a-repair/`，导出 `python work/enhancer/export_a_repair.py`，检查失败时不会宣称交付通过。
没有加入皮肤解锁。全部原功能边界、语音/完整登录、长期稳定性与完整换肤矩阵仍待验证。
原先“两图标均进模块”的根因尚未确认，不能将入口改善当作已证明修复根因。

### 1.2.0：底栏皮肤配色

旧 1.1.0 的 BottomHook 在三处强制透明，造成底栏露出背后内容。
1.2.0 移除覆盖；`SkinPalette` 复用普通版的 `theme.settings.a.t().f()`、
`ui.s.c()/g()/h()` 和 `ui.d.k()` 读取当前皮肤底栏色、图标色及深浅色转换。
透明背景合成到当前键盘底色，图标对比不足时使用可读颜色。
刷新限定为输入法窗口，并覆盖底栏创建、搜狗原配色回调、键盘重新弹出与配置变化。

11 项配色行为检查通过，脚本 `tests/palette_check.py`；真机证据在 `skin-test/`。
A 当前霓虹皮肤日志与截图像素均为 `#FFECECEC`；B 从默认皮肤 `#FFF2F3F7`
切换并恢复霓虹皮肤 `#FFECECEC`，日志和截图 `(600,2470)` 像素一致。
本轮 A 实际切换两款皮肤、两版深色和彩色皮肤矩阵尚未完整验证。
颜色同步不等于图片、渐变或动画背景连续延伸，这些效果仍待验证。

按用户要求卸载重装的包仅为 `com.sogouenhance` 与 `.sogou.enhanced`，
恢复备份的 shared_prefs/files/databases/no_backup，未恢复旧代码缓存。
普通版与小米版安装路径前后相同；未卸载或清除小米版。
LSPosed 更新新模块路径并软重启后 A 正常加载。收尾恢复 B 原霓虹皮肤、系统 night=no、
默认小米输入法。新版精确产物使用 `python work/enhancer/export_skin.py` 导出。

以下原功能冒烟记录来自 1.1.0，不作为 1.2.0 全量回归结论。

实际基线是用户提供的 `com.sogouenhance` 1.0，入口 `com.sogouenhance.HookEntry`，
使用 legacy Xposed API，**不是只有去广告功能的 com.sogou.adfree**。
保留剪贴板条数/长度解除、截断保护、无限文案、分词高亮、去广告、福利移除、
好评提示移除、AI 默认开关、启动页跳过、设置入口和隐藏设置图标。

在副本上修正 20.16 -> 20.17 的符号迁移：

- 快捷栏 `Kb()/dj(int)` -> `Jb()/bj(int)`。
- 剪贴板 `repository.utils.i` -> `repository.utils.k`，签名和 1000 字截断调用已核对。
- AI 服务 `settings.impl.p0$a.p4()/router.f.cb()` -> `u0$a.v4()/f.bb()`；均读取 `pref_ai_service`。

新增 `BottomHook` 在当前输入法进程设置 MIUI 支持标志、加载底栏插件、处理配色，
将支持的输入法列表替换为启用列表，保留原加载函数的错误回退。
此 ROM 没有旧的 `deleteNotSupportIme` 方法，作为可选兼容项报告，不阻断实际底栏。

B 使用仓库已有 NPatch 1.0.9（833）打包器，内嵌且仅内嵌一个完整增强模块。
`useManager=false`，运行时模块来自自身 APK。内嵌原包另增加设置组件 DEX；
外层及内层二进制清单均声明设置页、独立偏好 provider、可隐藏的设置桌面入口。
保留官方 resources.arsc 和 native library 的内容，处理改包名后的动态资源查找，
避免旧 `.patched` 版本登录页的 `Load resource error!`。
仅 B 安装 `EmbeddedGuard`，拦截既有实验定位的 `setFirstInstallTime(long)` JNI 崩溃入口。
这不是声称破解了全部签名检查，也不是官方签名版本。

## 构建

在仓库根执行：

```powershell
python work/enhancer/build.py
python work/enhancer/package_b.py
```

依赖仓库现有 JDK21、R8/D8、apktool、aapt2、uber-apk-signer 和 NPatch。
`build.py` 自动解码用户原增强模块至副本，编译新增代码并替换已核实的符号。
旧模块 DEX 不用反编译后的 Java 重编译。Xposed 编译桩只在编译期使用。
`package_b.py` 使用官网下载包 `work/enhancer/official/SogouInput_20.17.0_android_sweb.apk`。
签名输出按内容哈希分目录保存；最终路径在 `build/modules.json` 与 `build/single.json`。
这些文件重构建后会重新标记运行时验证待做，不能沿用旧产物的测试结论。

NPatch 中 origin.apk 和外层成员故意共享 ZIP 数据范围；Python 3.13 会拒绝普通读取。
脚本对指定成员验证边界、大小、CRC 后读取，最终输出转换为不重叠的普通 ZIP。
最终 APK 通过 ZIP CRC、zipalign、v2/v3 签名验证。

## 实测与证据

设备 df043723 / Redmi K90 Pro Max / Android16 / HyperOS，4KB 页。

| 项目 | 结果 | 证据 |
|---|---|---|
| A：原版身份 | 当前安装 APK 哈希等于历史官方包；官网下载包逐成员内容相同，Sohu Wireless 证书相同 | `device-a/installed.apk`、官网来源记录 |
| A：原增强功能 hook | 本轮修正后全部 27 条成功日志，无原增强 hook 失败 | `device-a/process.txt` |
| A：原生底栏/键盘 | 已显示，`mInputShown=true` | `device-a/final.png` |
| B：真正单 APK | 仅一个内嵌模块，外部 manager 关闭，独立包名安装成功 | `build/single.json` |
| B：排除外部模块 | 临时禁用 wetypehook/adfree/sogouenhance 并软重启后仍正常 | `device-b/modules_config.db`、`isolated-log.txt` |
| B：真实拼音输入 | 点按 n/i/h/a/o，显示你好候选，选词后测试页收到你好 | `device-b/input.png`、`clipboard.png` |
| B：原生底栏右键 | 打开剪贴板页面 | `device-b/clipboard.png` |
| B：内嵌设置 | 页面显示完整，ContentProvider 读取成功，条数开关 false/true 持久化并恢复 | `device-b/settings-ready.png`、`process.txt` 与本轮命令记录 |
| B：登录资源 | 登录页正常打开，未输入手机号或提交验证 | `device-b/login.png` |
| B：进程稳定性 | 本轮隔离测试进程无 Java fatal 或 native fatal | `device-b/final-process.txt` |

测试不是完整功能验收：底栏左键的完整输入法切换行为尚未确认；语音、完整账号登录、
长期广告回流、全部剪贴板边界、16KB 页设备、无 root 设备仍待实测。
“hook 已挂上”不能等同于每个原功能都做过端到端测试。
当前 ROM 的底栏由系统设置决定，实测为左右两个按钮，不强制改成固定四按钮布局。

旧 `.patched` 包的登录异常仍出现在全局日志中，它不是本轮 `.enhanced` 包；
筛选本轮包名、PID 和时间后，不能把旧异常算成本轮结果。

## 设备收尾

保留原官方普通版、小米版以及用户数据；新装 `com.sogouenhance` 和共存增强版。
恢复其他应用原有模块启用状态；普通版搜狗只保留新完整增强模块的作用域，
去掉旧 adfree/wetypehook 对普通版的重叠作用域，防止重复 hook。
初始 LSPosed 快照在 `device-a/sogou-enhancer-20261021-before/` 及设备 `/data/local/tmp/` 同名目录。
默认输入法恢复为原来的 `com.sohu.inputmethod.sogou.xiaomi/.SogouIME`。
本地无网络、无权限、无保存的测试页应用 `local.sogou.enhancerprobe` 留作复测工具。

## 来源与 AI 声明

官网来源：<https://shouji.sogou.com/index.php>（2026-10-21 实时读取）。
下载：<https://apkdl.sogouimecdn.com/wapdl/android/apk/SogouInput_20.17.0_android_sweb.apk?frm=new_pcjs_index>。
官方证书 SHA256：`01cb5a64feb3f6169e9dbe9c4304b1a7fab12c92af6814dd5f9892aabc01f0f3`。
增强产物使用工具内置测试证书，SHA256：`1e08a903aef9c3a721510b64ec764d01d3d094eb954161b62544ea8f187b5953`。

本轮新增适配代码、构建脚本和文档由 AI 生成与修改。原版搜狗、用户提供的基线增强模块、
NPatch 和工具链为既有软件，不属于本轮 AI 原创。尚未经独立人工逐行审计；不对第三方代码
重新授予许可证。仅提供本地测试产物，公开发布需要先明确第三方分发许可。
