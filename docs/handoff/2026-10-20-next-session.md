# 搜狗输入法改造 — 交接给新会话（梁神模式）

> 生成时间：2026-10-20（会话 m00001–m00259）
> 上一会话已把「改 APK」路线走死并查明原因，本文件是新会话的唯一起点。**先读完本文件再动手。**

## 1. 用户目标（三条需求，原文要点，m00037）

1. 搜狗输入法普通版不支持小米「全面屏键盘优化」，小米版支持 → 要让**普通版也支持**。
2. 去广告/隐藏广告，**不影响输入法功能**。
3. 两个版本**共存**、可同时安装互不影响。

**硬约束**：项目原由 GPT 做到一半、额度用尽；用户把项目拷进本仓库，明确要求「**不要去动 GPT 的项目文件**」，只在副本上工作。

工作目录：`C:\Users\Kirito787\Documents\AI\DSH\sougou`
仓库根有 `AGENTS.md`：issue 放在 `.scratch/<feature-slug>/`，五个 triage label，domain docs 用根 `GLOSSARY.md` + `docs/adr/`。

## 2. 已经证实的关键结论（别重复踩）

### 2.1 改 APK / 重签名 = 死路（已用对照实验证明）
- 把**完全未改动的官方 APK** 只用测试证书重签名，装到设备后与我们的改造包现象**完全一致**：
  - 键盘不弹（`mInputShown=false`）；
  - `Fatal signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x0`，线程 `input_engine_wo`；
  - 栈 `#00 pc 0xfd1a4 libsogouime.so` / `#01 pc 0xdcdcc libsogouime.so`（BuildId `e583a6c4c5aa44a6d74f706c3e54edcc9d2a24e7`）；
  - 同时弹 toast「你安装的是盗版搜狗输入法，请到搜狗官网下载」。
- 结论：**原生反篡改检测的是签名**，跟我们改的 dex/注入代码无关。任何重签名包都会崩。
- 因此：改包名做共存、改 dex 去广告、往 dex 里注入底栏代码 —— 全都被这一道原生检测挡住。

### 2.2 需求 3（共存）其实已经天然满足
设备上 `com.sohu.inputmethod.sogou`（普通版）与 `com.sohu.inputmethod.sogou.xiaomi`（小米版）**本来就是两个不同包名，可以同时安装**。不需要改包名。

### 2.3 注入逻辑本身是好的
之前的自建包里，`MiuiBottomCompat` 在搜狗进程内两层注册都成功了（logcat 有 `MiuiBottomCompat: framework registration succeeded` 与 `plugin registration succeeded on …`），只是随后被反篡改 SIGSEGV 杀掉。
→ 这段 Java/smali 逻辑可原样搬到 Xposed 模块里复用。

## 3. 设备与环境事实

- 设备 serial：`df043723`（Redmi，model `25102RKBEC`，Android 16 / MIUI OS3.0.309.0）。
- adb：`C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe`（不是 MuMu 模拟器，是真机）。
- 已 root：KernelSU（`su -c id` → `uid=0(root) context=u:r:ksu:s0`），包 `me.weishu.kernelsu`。
- 已装 LSPosed **v2.2.1 (7912)**：`/data/adb/modules/zygisk_lsposed/`（daemon.apk、framework.dex 236,600 B、manager.apk 7,082,334 B、lspctl），`lspd` 在跑。
- **没装 LSPosed 管理器**（`org.lsposed.manager` 不存在）→ 开模块作用域要么装 `manager.apk` 让用户点，要么 root 直接写配置库。
- `lspctl` 只有 `status` / `stop`，**没有模块管理子命令**（要 developer mode）。
- 配置库 `/data/adb/lspd/config/modules_config.db`（WAL，需连 `-wal`/`-shm` 一起拉），表：
  `modules(module_pkg_name, apk_path)`、`modules_state(module_pkg_name,user_id,enabled,scope_request_blocked)`、
  `scope(module_pkg_name,app_pkg_name,user_id)`、`module_configs(…)`、`app_configs(…)`、`lspd_configs(…)`。**当前为空**。设备**没有 sqlite3 可执行文件**（要用 Python 的 sqlite3 在 PC 端改完再推回）。
- 用户自己已装一个 Xposed 模块 `com.xposed.wetypehook`（`work/dsh/wetypehook.apk`），**这就是最好的格式参照**：
  - 新版 libxposed API 102（`io.github.libxposed.api.XposedModule`、`XposedInterface$HookBuilder/$Chain/$HookHandle/$Hooker`…）；
  - 模块元数据：`META-INF/xposed/java_init.list`（内容 `miuiime.dh0`）、`module.prop`（`minApiVersion=102 / targetApiVersion=102 / exceptionMode=protective / autoHotReload=true`）、`scope.list`；
  - `scope.list` 已覆盖小米版、微信键盘、讯飞、百度、Gboard 等，**唯独没有普通版 `com.sohu.inputmethod.sogou`**；
  - 用 DexKit（`org.luckypray.dexkit`）做运行时方法搜索。
  - 它是现成的「MIUI 输入法底栏」模块，理论上**只要把普通版搜狗加进它的作用域**，需求 1 可能直接成立（待验证：它是否只对小米版签名做特殊处理）。

## 4. 已有资产（可直接复用，勿重造）

| 路径 | 内容 |
| --- | --- |
| `work/compat/source/MiuiBottomCompat.smali` | 15,233 B，MIUI 底栏兼容类（框架白名单 + 插件层 + 3 个广播接收器），逻辑已验证可跑 |
| `work/ads/bridge/MiuiActionReceiver.smali` | 广告动作广播接收器 |
| `work/compat/implementation-notes.md` | 底栏注册机制的实现笔记（**新会话必读**） |
| `work/ads/patch-plan.json` | 广告补丁计划（3 个方法） |
| `work/dsh/build_helper.py` | 用 apktool 把 smali 编成 dex 的脚本 |
| `work/dsh/pack.py` | 组包脚本（改多 dex、删 v1 签名、STORED 条目 4 字节对齐） |
| `work/tools/signer.jar` | uber-apk-signer 1.3.0 |
| `work/signing/local-test.p12` | 测试证书（alias `sogou-local-test`，密码 `xof_WeLiydev5cflwXR2lXJcp4c8WT0J`） |
| `work/tools/zulu-jre/.../java.exe` | 便携 JDK 21 |
| `work/compat/build/smali/` | 官方包的完整反编译 smali 树（查方法体用） |
| `work/dsh/restore/official-orig.apk` | 官方原包 ASCII 副本（98,646,958 B），装设备用这个 |

广告 hook 目标（来自 patch-plan.json，方法签名需在新模块里重新确认）：
`Lcom/sogou/imskit/feature/lib/tangram/common/AmsKv;->l()Z` 返回 true、`->v()Z` 返回 false、`Lcom/sogou/feature/shortcut/l;->Jb()I` 返回 0。

## 5. 当前设备状态（本会话结束时已恢复）

- `com.sohu.inputmethod.sogou`：**官方原包**已装（`pm install -r /data/local/tmp/sogou-official.apk` → Success），已 `ime enable` + `ime set` 为默认输入法。可用、不崩。
- `com.sohu.inputmethod.sogou.xiaomi`：正常在装（但当前不在 `ime list -s` 里，即未启用）。
- 用户输入法数据在之前卸载时已丢失，无法恢复。

## 6. 下一步路线（按优先级）

1. **先验证最省事的一条**：把 `com.sohu.inputmethod.sogou` 加进 wetypehook 的 `scope.list`，装上重试，看普通版搜狗是否直接出现 MIUI 底栏。
   - 做法：解包 `work/dsh/wetypehook.apk` → 改 `META-INF/xposed/scope.list` 加一行 → 重打包（**这是用户的模块，改动前先备份**）。
2. **若不行 → 自己写 libxposed 102 模块**：`Hook` `com.sohu.inputmethod.sogou.SogouIME` 的 `onCreate`，在 `after` 里调 `MiuiBottomCompat.register(context)`；同一个模块再 hook 上面 3 个广告方法。参考 wetypehook 的 `module.prop` / `java_init.list` 格式。
3. **兜底 → 逆向 `libsogouime.so` 的签名校验**（`+0xdcdcc` 调用 `+0xfd1a4` 触发 SIGSEGV），patch 掉后改包路线重新可用。工作量大，最后做。
4. 模块启用：装 `/data/adb/modules/zygisk_lsposed/manager.apk`（用户手点勾选），或 PC 端 Python sqlite3 改 `modules`/`modules_state`/`scope` 三表后推回（注意 WAL）。

## 7. 命令坑（省时间）

- `adb install` 传**中文文件名**会炸：`IllegalArgumentException: Invalid name` → 回落又 `INSTALL_FAILED_USER_RESTRICTED`。**先复制成 ASCII 名**。
- `adb install` 仍报 `INSTALL_FAILED_USER_RESTRICTED` 时，走 root 绕过：
  `adb push x.apk /data/local/tmp/x.apk` → `adb shell su -c "pm install -r /data/local/tmp/x.apk"`（本会话实测有效）。
- 启用输入法必须用**缩写 ID**：`ime enable com.sohu.inputmethod.sogou/.SogouIME`；用全类名会报 `Unknown input method`。
- 只 `pm uninstall -k` 会留 `installed=false` 残记录，导致后续 `INSTALL_FAILED_UPDATE_INCOMPATIBLE`；要干净重装就先 `pm uninstall`（不加 -k）。
- 本机 pc 侧无 `sqlite3`，用 `python -c "import sqlite3…"`。

## 8. 新会话开场提示（可直接粘）

> 继续 `C:\Users\Kirito787\Documents\AI\DSH\sougou` 的搜狗输入法改造。先读 `docs/handoff-sogou-next-session.md`（必读）与 `work/compat/implementation-notes.md`，再从第 6 节路线 1 开始：把普通版 `com.sohu.inputmethod.sogou` 加进 wetypehook 的 scope 验证 MIUI 底栏是否直接生效。设备 serial `df043723`，已 root（KernelSU）+ LSPosed v2.2.1。不要重签/改搜狗 APK（原生反篡改会 SIGSEGV），不要动 GPT 遗留的原项目文件。
