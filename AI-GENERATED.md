# AI 产物声明 · AI-GENERATED NOTICE

## 一句话

**本仓库中的全部产物——代码、构建脚本、smali 补丁、文档、测试记录、发布说明、APK 二进制——均由 AI 生成或由 AI 在人工指令下修改。** 没有人工逐行编写或审计。

## 明细

| 产物类型 | 路径 | 生成方式 |
|---|---|---|
| Java hook 源码 | `work/enhancer/src/**` | AI 编写（基于对现有模块的反编译分析） |
| 方案 A 首页 smali | `work/enhancer/companion-smali/**` | AI 编写 |
| 构建脚本 | `work/enhancer/build.py`、`package_b.py`、`export*.py`、`manifest_view.py` | AI 编写 |
| 配色自检脚本 | `work/enhancer/tests/palette_check.py` | AI 编写 |
| 逆向研究笔记 | `work/enhancer/research/*.md` | AI 编写 |
| 文档 | `README.md`、`docs/**`、`.scratch/**`、`AGENTS.md` | AI 编写 |
| Release 说明 | `docs/releasing/**`、GitHub Releases 正文 | AI 编写 |
| APK 二进制 | GitHub Releases 附件 | AI 构建、AI 签名（测试证书）、AI 在真机上验证 |

## 不属于 AI 原创的部分

- **搜狗输入法本体**（`com.sohu.inputmethod.sogou`、`com.sohu.inputmethod.sogou.xiaomi`）：
  搜狐 / 搜狗公司的软件，本项目只做运行时 hook，不分发、不修改官方签名包。
- **用户提供的基线增强模块**（`搜狗输入法增强模块.apk`）：用户既有资产，AI 在其基础上增改。
- **第三方工具链**：apktool、jadx、NPatch、Android SDK build-tools、OpenJDK 等。
- **方案 B 单 APK**：它是搜狗 APK 的**共存重打包**，内部包含搜狗的原始代码与资源；
  AI 只改写了包名、签名与增强逻辑。它不是"纯 AI 软件"。

## 质量与责任

- AI 生成的代码**未经独立人工逐行审计**，可能存在错误、安全缺陷或遗漏。
- 真机验证只覆盖了文中所列的冒烟路径；标为"未验证"的场景（语音、完整登录、长时间稳定性、
  皮肤矩阵、无 root 设备、16KB 页设备）**没有经过测试**。
- 本项目是**个人学习记录**，不是产品，不提供任何担保。使用后果自负。

## 生成环境

- 生成时间：2026-10-19 ～ 2026-10-21
- 生成工具：DeepSeek Harness（DSH）智能体，模型 `deepseek-v4.1-flash`
- 交互方式：自然语言下达目标，AI 自主完成逆向分析、编码、构建、真机验证与文档
