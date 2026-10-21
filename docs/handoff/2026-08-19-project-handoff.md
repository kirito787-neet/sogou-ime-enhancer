# 搜狗输入法 · 全面屏键盘优化 项目交接文档

> **交接对象**：本项目最初的 GPT（工作区同为 `C:\Users\Kirito787\Documents\AI\DSH\sougou`）
> **交接方**：DSH 会话（接手时项目已中断，本文档负责把"做到哪、证据是什么、卡在哪、下一步怎么做"完整交代）
> **交接时间**：2026-08-19
> **本会话限制（重要）**：本会话的 shell（pwsh/win_bash）因自动审查服务故障不可用，`read`/`grep` 也时好时坏，因此文中标注 ❓ 的条目是"本会话未能亲手复核"的，附有复核命令，请优先用它们补证。

---

## 0. 交接摘要（TL;DR）

| 项 | 状态 |
|---|---|
| 让普通版搜狗（`com.sohu.inputmethod.sogou`）在 HyperOS/MIUI 上出现**原生「全面屏键盘优化」底栏** | ✅ **已验证可行**（Xposed 模块路线，不改 APK） |
| 去广告（键盘广告/互动广告/快捷栏广告/福利/开屏） | ✅ **已验证**（3 个 hook 实测命中） |
| 「改 APK 注入」路线（MiuiBottomCompat + LSPass） | ⛔ **已证不可行**（原生反篡改 + hidden API 封锁） |
| 用户最终要的 方案A / 方案B 产物 | ❌ **未构建**，且方案B 形态存在必须先拍板的分歧（见 §2.3） |
| 两方案上 GitHub（含优缺点 + AI 生成声明） | ❌ **未发布**（无仓库/凭据；README 与 Release 文案骨架见 §9） |

**一句话结论**：技术路线已经跑通且证据齐全，剩下的是"产品化"——把已验证的 hook 合并进一个增强模块、构建两套产物、写发布材料。

---

## 1. 项目目标与硬约束

**目标**：在 Xiaomi HyperOS / MIUI 设备上，让**官方普通版**搜狗输入法获得系统级「全面屏键盘优化」底栏（语音 / 语言 / 布局 / 收起 那排按钮），并顺带去广告。

**硬约束（不可违背）**：

1. **不修改、不重签官方搜狗 APK。** 搜狗有原生反篡改：`libsogouime.so +0xfd1a4` 校验签名，重签即 `SIGSEGV`（实测）。因此 NPatch / LSPatch / 任何"把模块塞进搜狗包再重签"的方案对搜狗**不可行**。
2. 走 **Xposed 模块**（LSPosed）在运行时 hook，目标 APK 保持官方原样。
3. 设备需要 **root**（本项目设备为临时 root：GhostLock 越狱 + ZygiskNext 1.5.2 + LSPosed 2.2.1 (7912, API 102)）。

---

## 2. 最终产物定义（用户最新口径，m00135）

> 用户原话（2026-08-19）：
> "方案A一个是最新官方版搜狗输入法安装包好一个是基于 `搜狗输入法\搜狗输入法-20.16.0(2610)\搜狗输入法增强模块.apk` 新增适配全面屏键盘优化的增强模块。方案B一个自带基于 `…增强模块.apk` 新增适配全面屏键盘优化的增强模块的最新版本安装包"

### 2.1 方案 A：官方包 + 增强模块（两个文件）

| 产物 | 说明 | 现状 |
|---|---|---|
| A-1 最新官方版搜狗输入法安装包 | `搜狗输入法.apk`（20.17.0 / 2620，SHA-256 `df10256e9228e9ed3831be4278a7b9046dd16b0e045d68dee8baafa2491c1574`） | ✅ 文件已在仓库根目录；⚠️ 需核对来源与官方签名证书 |
| A-2 「增强模块」（新增全面屏键盘优化适配） | 以现有 `搜狗输入法增强模块.apk` 为基线，**新增 MIUI 底栏 hook**（与去广告合并或共存） | ❌ 待构建（基线模块内容 ❓ 待解包确认，见 §5.1） |

### 2.2 方案 B：自带增强模块的「最新版本安装包」（单包）

用户期望：一个包，装完即有增强功能（类似 `微信输入法修改版.apk` 那种"自带模块"的包）。

### 2.3 ⚠️ 方案 B 的关键决策点（**必须先拍板**）

"自带模块的单包"在搜狗上有三条形态，可行性差别巨大：

| 形态 | 做法 | 可行性 | 说明 |
|---|---|---|---|
| **B1 整合安装包**（推荐） | 一个 zip/一键安装器：官方 APK + 增强模块 APK + 安装脚本与说明 | ✅ 可行 | 不重签官方包，不触发反篡改；缺点：仍是"两个 APK"，且需要 root+LSPosed |
| **B2 Zygisk 刷入包** | 把增强逻辑做成 KernelSU/Magisk 模块（Zygisk 注入），刷入即生效 | 🟡 技术可行、工作量大 | 真正"单包"（一个 zip），不改 APK；需把现有 Xposed hook 改写为 Zygisk 模块 |
| **B3 重签单 APK** | NPatch/LSPatch 把模块塞进搜狗包并重签 | ⛔ **不可行** | 重签触发 `libsogouime.so` 反篡改 → 崩溃（实测） |

**建议**：方案 B 先按 **B1** 交付（立即可做），把 **B2** 列为后续增强项，**B3 明确排除**并在 README 里写清原因（避免用户/后来者重复踩坑）。

> 需要用户确认：方案 B 接受 B1（整合包）吗？还是要投入做 B2（Zygisk 单包）？

---

## 3. 环境

| 项 | 值 |
|---|---|
| 设备 | `df043723`，Redmi K90 Pro Max，SM8850，Android 16，MIUI OS V816 |
| root | 临时 root（GhostLock 越狱） |
| Zygisk | ZygiskNext 1.5.2 |
| Xposed | LSPosed 2.2.1 (7912)，API 102（libxposed） |
| 保活 | 改完 LSPosed 配置库后 `ksud soft-reboot` 软重启，可保住 root |
| adb | MuMu 自带 `C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe`（`work/tools/device_probe.py`） |
| 工具链 | JDK 21（`work/tools/jdk`）、R8/D8（`work/tools/r8.jar`）、apktool-fast（`work/tools/apktool-fast.jar`，需 `-p work/framework --aapt work/compat/aapt2.exe`）、jadx 1.5.6、uber-apk-signer 1.3.0（`work/tools/signer.jar`） |
| 本地测试证书 | `CN=Local Sogou Test Build`，SHA-256 `234d68d0…b312dd`，2036-10-17 到期，**非官方** |

---

## 4. 已验证结论（可信，附证据位置）

### 4.1 路线1：wetypehook 模块扩 scope → 底栏出现 ✅
文档：`work/xposed/route1-scope-extension.md`

- 做法：把已有模块 `com.xposed.wetypehook`（`work/dsh/wetypehook.apk`，4,973,489 B，SHA-256 `025d3a75…7f1940`，libxposed API 102）的 scope 从"微信输入法"扩展到 `com.sohu.inputmethod.sogou`，**完全不碰搜狗 APK**。
- 改库方式：直接编辑 LSPosed 的 `modules_config.db`，插入 scope 行（`work/dsh/live2` 为 8 行 scope 副本）；之后 `ksud soft-reboot` 软重启。
- 日志证据：
  - `Success:Hook field sIsImeSupport`
  - `Hook MIUI IME Done!`
  - `IMEBottomManager: ScreenHeight : 2608 density = 3.0 densityDpi = 480`
- 视觉 A/B：`work/dsh/c5.png`（13:41，无底栏） vs `work/dsh/kb3.png`（13:47，有底栏）。
- 结论：**纯 Xposed 层即可让普通版出底栏，且不触发反篡改**。这是整个项目最关键的可行性验证。

### 4.2 去广告模块 ✅
工程：`work/ads/mod/`（包名 `com.sogou.adfree`，v1.0，`xposedminversion=82`，`scope.list`=`com.sohu.inputmethod.sogou`，`xposed_init`=`com.sogou.adfree.AdHook`）
实测命中（`work/ads/mod/NOTES.md`）：

| hook 点 | 效果 |
|---|---|
| `AmsKv.l()Z` → `true` | 关闭键盘广告 |
| `AmsKv.v()Z` → `false` | 关闭互动广告 |
| `shortcut/l.Jb()I` → `0` | 关闭快捷栏广告 |

有意未补丁：`AmsKv.a()`、`AmsKv.u()`（见 `work/ads/findings.md`）。
构建链：`work/ads/mod/build.sh`（javac → stubs.jar → D8 → apktool b），`work/ads/mod/pack.mjs`（换 classes.dex 并校验只定义 `com/sogou/adfree/*`），产物 `work/ads/mod/build/signed/adfree-repacked-aligned-debugSigned.apk`。

### 4.3 ROM / 插件 / hidden API 机制 ✅
文档：`work/inventory/actual-rom-bottom.md`、`work/inventory/findings.md`

- framework 侧 `sImeMinVersionSupport` 白名单：`com.sohu.inputmethod.sogou.xiaomi >= 624`、`com.iflytek.inputmethod.miui`、`com.baidu.input_mi >= …`、`com.miui.catcherpatch`、`com.xiaomi.type` 等；**普通版 `com.sohu.inputmethod.sogou` 不在白名单**。
- 底栏类 `InputMethodBottomManager`（`com.miui.inputmethod` 系），生命周期 `InputMethodService.initViews` PC `0x00c0` 调用 `addMiuiBottomView`。
- 插件 `com.miui.phrase`，`appId 10165`。
- **hidden API 被封锁**（flag=2 blocked）：普通反射不可行，需 LSPass 类方案绕过（这是注入式路线的额外成本）。

### 4.4 普通版自带"底部高度设置" ✅（可选参考）
文档：`work/inventory/standard-bottom-minimal.md`
- 普通版自身有 `pref_fullscreen_mode`（默认派生 adaptive/fullscreen），默认高度 69（物理像素）；`f()` PC `0x0012`、`e()` PC `0x0005`、迁移 `PC 0x006e` 三处需同步改才一致。
- 若模块接管底栏，注意与 MIUI 原生底栏高度算法（densityDpi 480 时约 179px）的视觉一致性。

### 4.5 注入式路线（改 APK） ⛔
文档：`work/dsh/`、`work/compat/implementation-notes.md`
- 做法：`pack.py` 把 `MiuiBottomCompat`（改 framework 静态白名单 + 加载 `com.miui.phrase`）注入 `classes8.dex`，`LSPass` 注入 `classes9.dex`，重签为 `work/dsh/signed/final-signed.apk`。
- 结果：**反篡改 `libsogouime.so+0xfd1a4` 校验失败 → SIGSEGV**；hidden API flag=2 另需 LSPass 绕。
- 结论：此路线**放弃**，`20.16.0(2610).apk`（含 classes8/classes9 的注入包）同源，真机不可用。
- 三按钮映射（若将来需要接管点击）已分析好：`work/ads/bridge/mapping.md`（语音→`voiceinput/stub/u.l(2,k.Eh(),ts)`；语言→`keyboard/d.F()`；布局→`keyboardswitch/data/b.c()+viewmodel/w.c(current,original,next,"")`）；广播接收端 `work/ads/bridge/receiver-integration.md`（Android 16 必须 `RECEIVER_NOT_EXPORTED=4`，仅 `onReceive` 主线程，`onDestroy` 注销）。

---

## 5. 未完成事项与阻塞点

### 5.1 ❓ 基线模块身份未确认
`搜狗输入法\搜狗输入法-20.16.0(2610)\搜狗输入法增强模块.apk`
- 已确认：是 **libxposed 模块**（中央目录含 `assets/xposed_init`、`META-INF/xposed/module.prop`、`scope.list`）。
- 未确认：包名、实现类、hook 点（本会话 grep 不到字符串是因为 dex 被压缩，非结论）。
- **复核命令**（Windows bsdtar）：
  ```powershell
  cd 'C:\Users\Kirito787\Documents\AI\DSH\sougou\搜狗输入法\搜狗输入法-20.16.0(2610)'
  tar -tf '搜狗输入法增强模块.apk' | Select-Object -First 40
  tar -xOf '搜狗输入法增强模块.apk' assets/xposed_init
  tar -xOf '搜狗输入法增强模块.apk' META-INF/xposed/module.prop
  tar -xOf '搜狗输入法增强模块.apk' assets/META-INF/xposed/scope.list
  ```
  再用 jadx 打开 `classes.dex` 看 `xposed_init` 指向的类与 hook 点。
- **预期判断**：从工程脉络看，它大概率是 `com.sogou.adfree` 去广告模块（或二合一"增强"模块）的 20.16.0 时期构建物；若确认为 adfree，则"新增底栏适配"= 把 §4.1 的 7 个 hook 点移植进来。

### 5.2 ❌ 增强模块（含底栏）尚未构建
需要把 wetypehook 的底栏 hook 合并进增强模块。wetypehook 的 7 个 hook 点（详见 `work/wxime/analysis-wetypehook-miui-bottom.md`，模块 `MainHook.java` 1505 行）：
1. `sIsImeSupport` 置 1（白名单开关）
2. `customizeBottomViewColor` / `addMiuiBottomView`（底栏视图与配色）
3. `InputMethodModuleManager.loadDex`（吞原逻辑 + `addDexPath` 挂 `InputMethodBottomManager`）
4. `InputMethodBottomManager.getSupportIme` → `getEnabledInputMethodList`
5. `InputMethodBottomManager.deleteNotSupportIme` → `null`
6. `isXiaoAiEnable` → `false`
（第 7 点在 `MainHook.java` 行 75 附近的"原生支持集合"判断：`{com.iflytek.inputmethod.miui, com.sohu.inputmethod.sogou.xiaomi, com.baidu.input_mi, com.miui.catcherpatch, com.xiaomi.type}`，普通版不在集合 → 走完整改造。）

### 5.3 ❌ 方案 A/B 产物未构建
- A-1：核对 `搜狗输入法.apk`（20.17.0/2620）官方性（签名证书指纹）。
- A-2：构建合并版增强模块（去广告 + 底栏），产物签名用本地测试证书，并写清"非官方签名、仅供自用/测试"。
- B：按 §2.3 决策执行（B1 整合包 / B2 Zygisk 包）。

### 5.4 ❌ GitHub 未发布
见 §9（仓库结构、README 骨架、Release 资产命名、AI 声明已备好，缺的是建仓与上传——需要用户的仓库与凭据）。

### 5.5 其他遗留
- 16KB page size 兼容：标准版 16/43 个 so 不满足（Xiaomi 版 11/31），Redmi K90 Pro Max 为 4KB 页无碍，但**后续换机/上架说明要写**。
- 底栏高度视觉一致性（§4.4）。
- `搜狗输入法小米.apk`（10.32.21.202606111755/10461，`com.sohu.inputmethod.sogou.xiaomi`）**原生支持底栏**（白名单 ≥624）——若用户只求底栏、不在意包名/功能差异，这是零成本备选方案，建议在 README 里作为"备选方案 C"提及。

---

## 6. 文件与产物清单

### 6.1 根目录
| 文件 | 说明 |
|---|---|
| `搜狗输入法.apk` | 20.17.0/2620 官方最新（SHA-256 `df10256e…1c1574`） |
| `搜狗输入法小米.apk` | 小米版 10.32.21.202606111755/10461，**原生支持底栏** |
| `微信输入法修改版.apk` | NPatch 参考样本（内嵌 `com.xposed.wetypehook`，证明"自带模块"形态在无反篡改的 App 上可行） |

### 6.2 `搜狗输入法/`
- `搜狗输入法-20.16.0(2610)/搜狗输入法-20.16.0(2610) (原版).apk` — 官方 20.16.0 原版
- `搜狗输入法-20.16.0(2610)/搜狗输入法-20.16.0(2610).apk` — **注入式补丁包**（含 `classes8.dex`/`classes9.dex`，原版无）→ 反篡改，不可用
- `搜狗输入法-20.16.0(2610)/搜狗输入法增强模块.apk` — 基线增强模块 ❓ 待解包（§5.1）
- `搜狗输入法_20.11.0.apk`、`搜狗输入法小米版-10.32.21.202608051602.apk` — 历史版本留档

### 6.3 `work/`（工程与证据）
| 目录 | 内容 |
|---|---|
| `work/ads/mod/` | 去广告 Xposed 模块工程（`src/com/sogou/adfree/AdHook.java`、`build.sh`、`pack.mjs`、`apply.sh`、`NOTES.md`、`build/signed/*.apk`） |
| `work/ads/` | `classes3.dex`（DEX 补丁，SHA-256 `9c8860…ffff`）、`patch_dex.py`、`findings.md`、`bridge/mapping.md`、`bridge/receiver-integration.md` |
| `work/compat/` | `MiuiBottomCompat`（注入式白名单修改，需 LSPass）、`implementation-notes.md`、`source/*.smali` |
| `work/dsh/` | `pack.py`、`sign_apk.py`、`final-unsigned.apk`、`signed/final-signed.apk`、`wetypehook.apk`、`helper.apk`、`zt.sh`（zygiskd 诊断）、LSPosed 配置库操作（`mc.db`、`modules_config.db`、`dbedit`、`live2`）、真机截图（`shot1-5/lsp*/c1-5/d1-2/p1-2/kb1-4/kbui.xml`） |
| `work/inventory/` | `findings.md`（两包身份/共存/底栏类/16KB）、`actual-rom-bottom.md`（白名单/hidden API/插件/生命周期）、`standard-bottom-minimal.md`（普通版底部高度设置） |
| `work/wxime/` | `analysis-wetypehook-miui-bottom.md`（wetypehook 7 hook 点全文分析） |
| `work/xposed/` | `route1-scope-extension.md`（路线1 全流程与证据） |
| `work/tools/` | JDK21、r8.jar、apktool-fast.jar、signer.jar、jadx、zulu-jre、`device_probe.py` 等 |

---

## 7. 下一步任务清单（给 GPT，按优先级）

**P0（先做，1 小时内）**
1. 解包确认 `搜狗输入法增强模块.apk` 的包名/实现类/hook 点（命令见 §5.1），把结论写回本文档 §5.1。
2. 核对 `搜狗输入法.apk` 官方签名指纹（`apksigner verify --print-certs`），确认是官方包。
3. 与用户确认 §2.3 的方案 B 形态（B1 / B2 / 两者都做）。

**P1（核心开发）**
4. 新建/改造模块：以确认后的基线模块为骨架，移植 §5.2 的 7 个底栏 hook（参考 `work/wxime/analysis-wetypehook-miui-bottom.md` 与 `work/dsh/wetypehook.apk` 反编译结果），与去广告 hook 合并；`scope.list` 只留 `com.sohu.inputmethod.sogou`。
5. 用 `work/ads/mod/build.sh` 同款链路构建 → 本地证书签名 → 真机（df043723）A/B 验证：底栏出现、三按钮可用、广告消失、无崩溃。
6. 验证通过后冻结版本号（如 `v1.0.0`），记录 SHA-256。

**P2（产物与发布）**
7. 按 §9 建 GitHub 仓库，写 README（两方案对比 + 优缺点 + AI 声明），上传 Release 资产。
8. 方案 B 按确认形态构建（B1 整合包脚本；或 B2 Zygisk 模块）。
9. 可选：把 `work/inventory/standard-bottom-minimal.md` 的"底栏高度统一"做成模块里的可配置项。

**P3（收尾）**
10. 更新本文档状态标记，把 ✅/❌ 全部刷新为最终状态。
11. 在 README 里补"已知限制"：需 root+LSPosed、非官方签名、仅 20.17.0 验证、16KB 页说明。

---

## 8. 两方案优缺点对比

| 维度 | 方案 A（官方包 + 增强模块） | 方案 B（自带模块单包） |
|---|---|---|
| 安装步骤 | 2 个 APK：官方包 + 模块，再在 LSPosed 里勾选作用域 | 1 个包（B1 为 zip/安装器；B2 为刷入包） |
| 是否改官方包 | 否 | 否（B1/B2）；B3 会改，已排除 |
| 触发反篡改风险 | 无 | 无（B1/B2）；B3 必崩 |
| 需要 root | 是（LSPosed） | 是（B1 需 LSPosed；B2 需 KernelSU/Magisk） |
| 升级搜狗版本 | 只换官方包，模块通常继续可用 | B1 需重新打包；B2 不受影响 |
| 透明度/可审计 | 高（两包分离，来源清晰） | 中（B1 高；B2 需信任刷入包） |
| 制作成本 | 低 | B1 低；B2 高（需把 Xposed hook 改写为 Zygisk） |
| 适合人群 | 想自己控制、随时换版本 | 想"装完即用"的小白 |

---

## 9. GitHub 发布计划（README 骨架 + 声明）

> 说明：本会话无法建仓/上传（无仓库与凭据）。以下内容可直接粘贴使用。

**仓库名建议**：`sogou-ime-miui-bottom-enhancer`（或中文名 `搜狗输入法-全面屏键盘优化`）

**目录结构建议**
```
README.md
LICENSE            # 建议 MIT 或 CC-BY-NC（自用/非商用）
docs/
  HANDOFF.md       # 本交接文档
  EVIDENCE.md      # 关键日志/截图索引
release/
  方案A/  # 官方包说明 + 增强模块 apk（或指向官方下载）
  方案B/  # 整合包 / 刷入包
```

**README 骨架（要点）**
1. 这是什么：让普通版搜狗在 HyperOS 上获得原生「全面屏键盘优化」底栏 + 去广告（Xposed 模块，不改 APK）。
2. 前提：root + ZygiskNext + LSPosed（API 102）；仅 Android 16 / HyperOS V816 实测。
3. 方案 A：官方 20.17.0(2620) + 增强模块 vX；安装三步（装官方包 → 装模块 → LSPosed 勾选 `com.sohu.inputmethod.sogou` → 软重启/重启）。
4. 方案 B：整合包（B1）/ Zygisk 刷入包（B2）二选一，写清差异。
5. **为什么不做"重签单 APK"**：搜狗原生反篡改 `libsogouime.so+0xfd1a4`，重签即崩；NPatch/LSPatch 路线不可行。
6. 已知限制：需 root；非官方签名（仅自用）；底栏高度与原生略有差异；16KB 页设备未适配。
7. **AI 生成声明**（见下）。
8. 免责：仅供学习研究，请支持官方正版；因使用产生的任何问题自负。

**Release 资产命名建议**
- `方案A-官方20.17.0(2620).apk`（或只给官方下载链接 + 校验值）
- `方案A-增强模块-v1.0.0.apk`
- `方案B-整合包-v1.0.0.zip`
- `SHA256SUMS.txt`

**AI 生成声明（建议原文）**
> 本项目（含模块代码、文档、构建脚本、发布说明）**全部由 AI 生成**（DSH 会话 + GPT 协作），未经人工逐行审计。使用前请自行评估风险；作者不对任何设备损坏、数据丢失或账号风险负责。请优先支持官方正版软件。

---

## 10. 待用户拍板的问题

1. **方案 B 形态**：B1（整合包，立即可做）/ B2（Zygisk 单包，工作量大）/ 都要？
2. **发布方式**：新建仓库还是用已有仓库？是否需要我准备好文件、由用户手动上传？
3. **签名**：继续用本地测试证书（`CN=Local Sogou Test Build`）即可，还是用户有自己的证书？
4. **是否保留注入式路线的产物**（`work/dsh/signed/final-signed.apk`、`20.16.0(2610).apk`）？建议 README 不提、仓库里标注"已废弃/勿用"，避免误导。
5. **备选方案 C**（直接装小米版）是否要在 README 里提一句？

---

## 附录 A · 关键证据索引

| 证据 | 位置 |
|---|---|
| 底栏出现的日志（sIsImeSupport / Hook MIUI IME Done / IMEBottomManager） | `work/xposed/route1-scope-extension.md` |
| 底栏视觉 A/B | `work/dsh/c5.png`、`work/dsh/kb3.png` |
| 去广告 3 hook 命中 | `work/ads/mod/NOTES.md` |
| wetypehook 7 hook 点全文 | `work/wxime/analysis-wetypehook-miui-bottom.md` |
| framework 白名单 / hidden API / 插件 | `work/inventory/actual-rom-bottom.md` |
| 反篡改崩溃（重签） | `work/dsh/`（final-signed 与崩溃记录）、`work/compat/implementation-notes.md` |
| 三按钮映射与广播集成 | `work/ads/bridge/mapping.md`、`work/ads/bridge/receiver-integration.md` |

## 附录 B · 踩过的坑（避免重复）

1. **不要试图重签搜狗 APK** —— 原生反篡改，必崩。
2. **不要内嵌 Xposed 框架类** 到模块里（`pack.mjs` 有校验，只允许 `com/sogou/adfree/*`）。
3. `getReturnType().getName()` 对基本类型返回 `boolean`/`int`，hook 前要判。
4. `hookMethod` 的真实签名返回 `Unhook`（不是 void）。
5. D8 输出目录要先 `mkdir`；apktool 要设 `-Djava.io.tmpdir`（见 `build.sh`）。
6. 模块重装后 LSPosed 的 `modules.apk_path` 要同步更新，否则 hook 不生效。
7. 改 LSPosed 配置库后要 `ksud soft-reboot`，否则重启丢临时 root。
8. Android 16 动态注册广播必须 `RECEIVER_NOT_EXPORTED=4`，且只回 `onReceive` 主线程。
9. 本会话 `pwsh` 在 workspace-write 沙箱下启动崩溃（`0xC0000002`），切 `danger-full-access` 后恢复；auto-review 服务 429 时工具调用会被跳过，重试即可。

---

*本文档由 DSH 会话整理，内容全部来自仓库内既有证据与本次会话复核；标注 ❓ 的部分请以 GPT 的复核结果为准。*
