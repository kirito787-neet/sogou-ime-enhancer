# 搜狗输入法 · 全面屏键盘优化 + 去广告（AI 实验项目）

> ⚠️ **本项目由 AI 主导开发与维护。** 代码、文档和构建脚本由 AI 在用户指导下生成或修改。详见 [AI 产物声明](AI-GENERATED.md)。
>
> **本项目仅供个人学习和研究使用。** 禁止商业用途；按"现状"提供、不提供任何担保，使用风险自负；
> 与搜狐 / 搜狗公司无任何关联。完整条款见 [AI-GENERATED.md#免责声明--disclaimer](AI-GENERATED.md#免责声明--disclaimer)。

在 **Xiaomi HyperOS / MIUI** 上，为**官方普通版**搜狗输入法启用系统级「全面屏键盘优化」底栏，并移除键盘广告。

| 项 | 状态 |
|---|---|
| 普通版搜狗显示原生「全面屏键盘优化」底栏 | ✅ 真机验证 |
| 去广告（键盘 / 互动 / 快捷栏 / 福利 / 开屏） | ✅ 真机验证 |
| 付费皮肤解锁（A 已打通购买→下载→应用；B 同代码） | ✅ 方案 A 真机验证 |
| 方案 A · 官方包 + 独立增强模块（Xposed） | [v1.3.7](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.3.7) |
| 方案 B · 内置增强单 APK | [v1.3.7](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.3.7) |
| 完整回归、语音登录、长时间稳定性 | ❌ 未验收 |

## 为什么不能"改 APK 重签"

搜狗有原生反篡改：`libsogouime.so` 会校验签名，重签后启动即 `SIGSEGV`（已用对照实验证明）。
所以走 **Xposed 模块（LSPosed）运行时 hook** 路线，目标 APK 保持官方原样。
方案 B 的"单 APK"是 NPatch 式的**共存重打包**（独立包名 `com.sohu.inputmethod.sogou.enhanced`），
不是覆盖官方包。

## 两套方案

### 方案 A · 官方 APK + 增强模块

1. 安装官方搜狗 20.17.0（2620）
2. 安装 `sogou-enhancer` 模块 APK
3. LSPosed 里启用模块，作用域勾选官方普通版搜狗
4. 软重启输入法 / 设备

从 v1.3.0 起，HyperOS 4（Android 17）上的方案 A 可在模块作用域中额外勾选「系统界面」并重启设备。
启用后，主屏的软键盘弹出时会隐藏底部手势白条，收起后自动恢复。上滑回桌面等手势仍然可用。

在 K90 Pro Max 的 HyperOS 4 上，普通竖屏键盘的默认尺寸对齐系统内置搜狗。全面屏手势模式下，键盘底栏延伸至屏幕底边，两侧图标完整显示。「键盘调节」仍可保存自定义尺寸，点「重置」可回到对齐后的默认尺寸。

优点：官方包零改动、官方签名完整、跟随官方更新。
缺点：需要 root + LSPosed；是两个包。

### 方案 B · 内置增强单 APK

一个 APK，装完即用，**不需要** LSPosed 作用域。增强版作为独立应用安装。

优点：开箱即用，不需要给模块配作用域。
缺点：包体大（约 179 MB），内置的是搜狗 20.17.0 基线，无法跟随官方小版本更新；
与官方版数据不互通。

> 详细的方案对比、源码结构与构建步骤见 [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) 与
> [`work/enhancer/README.md`](work/enhancer/README.md)。

## 皮肤解锁

v1.3.7 起，两套方案都带皮肤解锁，实现放在
`work/enhancer/src/com/sogouenhance/skin/SkinUnlockHook.java`，随各自 DEX 打包。

参考实现是 LSPosed 模块 **SogouSkin**（作者 vhukze）：它先证明了 20.17.0 的付费态由客户端模型
字段决定，并给出了停服域名的替代地址。本项目的皮肤解锁沿用同一思路，在其基础上做了范围收敛。

- LSPosed 模块库：<https://modules.lsposed.org/module/io.github.vhukze.sogouskin>
- 仓库：<https://github.com/Xposed-Modules-Repo/io.github.vhukze.sogouskin>

| 注入点 | 本项目的处理 | 与 SogouSkin 的关系 |
|---|---|---|
| `SmartThemeSkinDetailActivity#T2` / `#E2`、`ThemePreviewActivity#L2` | `payment=1`、`vipOnly="0"`、`newVipType=0` | 同思路，同样在这三处置已购态 |
| `com.sogou.theme.network.b#e` | `download.sginput.qq.com` → `srv.android.shouji.sogou.com` | 同思路，域名重写 |
| `com.sogou.inputmethod.pay.e#d(midas.u)` | 仍需走支付时以结果码 0 回调并短路，不拉起收银台 | 本项目额外加的兜底 |

范围收敛：只对皮肤页（`com.sogou.theme.*`、`com.sogou.home.costume.*`）与皮肤 assetType
（2001/2012/2023/2027/2041/2042/6041/6042）生效，字体、表情、壁纸、会员、词库保持原流程。

真机验证（K90 Pro Max / HyperOS 4）：付费皮肤详情直接显示「已购买」，点「立即启用」后
`skindl.php` 请求被重写到可用域名，皮肤包下载、安装并自动应用。日志标签 `SogouSkin`。

## 版本历史

| 版本 | 日期 | 变更 |
|---|---|---|
| [v1.3.7](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.3.7) | 2026-11-19 | 方案 A / B 加入皮肤解锁：详情模型置已购 + 下载域名重写，付费皮肤可直接下载应用。 |
| [v1.3.6](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.3.6) | 2026-11-19 | 修复 K90 Pro Max 正常输入时最后一排按键离底栏过远的问题。 |
| [v1.3.5](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.3.5) | 2026-11-19 | 修复方案 A 和方案 B 的增强版号不一致。 |
| [v1.3.4](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.3.4) | 2026-11-19 | 修复键盘切换菜单首屏漏显第五项和当前输入法勾选的问题。 |
| [v1.3.3](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.3.3) | 2026-11-19 | 修复键盘静置时侧边光效被截断，以及拖动底部手柄后露白的问题。 |
| [v1.3.2](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.3.2) | 2026-11-19 | 拖动一侧手柄时固定另一侧边缘，统一预览和保存后的键盘位置。 |
| [v1.3.1](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.3.1) | 2026-11-19 | 对齐 K90 Pro Max 默认键盘尺寸，修复底栏图标遮挡和调节框越界。 |
| [v1.3.0](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.3.0) | 2026-11-19 | 方案 A 支持键盘弹出时隐藏手势白条，修复 HyperOS 4 底栏留白和 Android 17 增强设置入口异常。 |
| [v1.2.3](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.2.3) | 2026-10-21 | 修复底栏刷新卡死和方案 B 设置页校验失败。 |
| [v1.2.2](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.2.2) | 2026-11-19（归档） | 修复方案 A 切换皮肤后底栏颜色不刷新的问题。 |
| [v1.2.1](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.2.1) | 2026-10-21 | 修复方案 A 的桌面入口和任务栈。 |
| [v1.2.0](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.2.0) | 2026-10-21 | 底栏跟随当前皮肤配色，修复透明覆盖问题。 |
| [v1.1.0](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.1.0) | 2026-10-21 | 首个测试版，适配搜狗 20.17，提供全面屏底栏、去广告和方案 B 单 APK。 |

从 v1.3.5 起，GitHub 标签、附件名和两套方案的增强版本共用同一个版本号。旧包版本对应关系与校验值见 [版本与资产清单](docs/RELEASES.md)。

## 仓库结构

```
README.md                 本文件
AI-GENERATED.md           AI 产物声明
LICENSE                   我方代码的许可证（第三方组件不在此授权范围内）
docs/                     架构说明、交接文档、issue 工作流
  ARCHITECTURE.md         技术路线与模块结构
  RELEASES.md             版本与资产清单
  releasing/              Release 说明模板与资产校验清单
.scratch/sogou-enhancer/  issue 与 spec（见 docs/agents/issue-tracker.md）
work/enhancer/            增强模块源码与构建脚本（唯一可复现的代码资产）
  src/                    Java hook 源码
  companion-smali/        方案 A 首页 smali
  tests/                  配色行为自检
  build.py / package_b.py 构建入口
  research/               逆向研究笔记
AGENTS.md                 本仓库的 agent 协作约定
```

## 许可与免责

- 我方新写的代码以 **MIT** 发布，见 [LICENSE](LICENSE)。
- 搜狗输入法本体、用户提供的基线增强模块、NPatch 等**第三方组件不在授权范围内**，
  这里不重新授权，也不对第三方代码做任何主张。
- APK 仅供自己在真机上学习验证。重新分发第三方软件存在版权风险，请自行评估。
- 按现状提供，不保证可用性；刷机 / root 操作有变砖风险。

> ### 免责声明
>
> **本项目仅供个人学习和研究使用。** 禁止任何商业用途与盈利活动；不提供任何明示或暗示的担保；
> 使用、安装、修改或分发本项目的全部风险由使用者自行承担，作者与 AI 生成工具不承担任何责任。
> 本项目与搜狐 / 搜狗公司无任何关联，未获其授权或认可；使用者应自行确认行为符合当地法律法规
> 及相关平台条款。完整条款见 [AI-GENERATED.md · 免责声明](AI-GENERATED.md#免责声明--disclaimer)。

## 来源

- 官方下载：<https://shouji.sogou.com/index.php>
- 官方证书 SHA-256：`01cb5a64feb3f6169e9dbe9c4304b1a7fab12c92af6814dd5f9892aabc01f0f3`
