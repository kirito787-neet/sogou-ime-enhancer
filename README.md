# 搜狗输入法 · 全面屏键盘优化 + 去广告（AI 实验项目）

> ⚠️ **本项目全部代码、文档与构建脚本均由 AI（DeepSeek Harness 智能体）生成或修改。**
> 详见 [AI-GENERATED.md](AI-GENERATED.md)。这是个人技术学习记录，不是可商用产品。

在 **Xiaomi HyperOS / MIUI** 上，让**官方普通版**搜狗输入法获得系统级「全面屏键盘优化」底栏
（语音 / 语言 / 布局 / 收起），并顺带移除键盘广告，且与小米版共存。

| 项 | 状态 |
|---|---|
| 普通版搜狗显示原生「全面屏键盘优化」底栏 | ✅ 真机验证 |
| 去广告（键盘 / 互动 / 快捷栏 / 福利 / 开屏） | ✅ 真机验证 |
| 方案 A：官方包 + 独立增强模块（Xposed） | ✅ 已发布 v1.2.3 |
| 方案 B：内置增强的单 APK（独立包名共存） | ✅ 已发布 v1.2.3 |
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
3. LSPosed 里启用模块，**作用域只勾官方普通版搜狗**
4. 软重启输入法 / 设备

优点：官方包零改动、官方签名完整、跟随官方更新。
缺点：需要 root + LSPosed；是两个包。

### 方案 B · 内置增强单 APK

一个 APK，装完即用，**不需要** LSPosed 作用域，与官方普通版、小米版共存。

优点：开箱即用，不需要给模块配作用域。
缺点：包体大（约 179 MB），内置的是搜狗 20.17.0 基线，无法跟随官方小版本更新；
与官方版数据不互通。

> 详细的方案对比、源码结构与构建步骤见 [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) 与
> [`work/enhancer/README.md`](work/enhancer/README.md)。

## 版本历史

| 版本 | 日期 | 变更 |
|---|---|---|
| [v1.1.0](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.1.0) | 2026-10-21 | 首个测试版：20.17 方法改名适配 + MIUI 原生底栏 + 去广告 + 方案 B 单 APK |
| [v1.2.0](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.2.0) | 2026-10-21 | 底栏跟随皮肤配色（`SkinPalette`），移除 1.1.0 的错误透明覆盖 |
| [v1.2.1](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.2.1) | 2026-10-21 | 方案 A 入口与任务栈修缮（`AHomeActivity`），仅 A 有更新 |
| [v1.2.3](https://github.com/kirito787-neet/sogou-ime-enhancer/releases/tag/v1.2.3) | 2026-10-21 | 修复底栏刷新卡死（主线程 Handler + 3s 兜底）；修复方案 B 设置页 VerifyError |

每个版本的 APK 与校验值见对应的 GitHub Release；仓库内**不存放 APK 二进制**。

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

## 来源

- 官方下载：<https://shouji.sogou.com/index.php>
- 官方证书 SHA-256：`01cb5a64feb3f6169e9dbe9c4304b1a7fab12c92af6814dd5f9892aabc01f0f3`
