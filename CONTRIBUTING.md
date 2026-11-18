# 参与方式

这是个人学习记录，**不接收功能请求**。可以提 issue 讨论技术点，但不保证响应。

## 动手前

1. 读 [README.md](README.md) 的「为什么不能改 APK 重签」——重签必定 `SIGSEGV`。
2. 读 [AI-GENERATED.md](AI-GENERATED.md)——这里的代码没有经过人工逐行审计。
3. 读 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) 理解模块结构。

## 本地开发

```bash
python work/enhancer/build.py --variant a   # 构建方案 A 模块
python work/enhancer/tests/palette_check.py # 配色行为自检
```

工具链（JDK 21、apktool、Android build-tools）不进仓库，见 `docs/ARCHITECTURE.md`。

## 版号与发布

版号采用「主版本.次版本.修订版本」。不兼容的大改动升主版本，能兼容现有用户的新功能升次版本，错误修复和维护升修订版本。升主版本或次版本时，后面的数字归零。

发布前更新 `work/enhancer/build.py` 中的共用增强版本和递增的 Android 模块版本代码，重新构建方案 A 和方案 B。GitHub 标签、附件名和增强版本使用同一个版号。在同一次提交中更新 README 的版本历史和 [版本与资产清单](docs/RELEASES.md)。

提交标题、发布标题和更新说明使用中文。提交标题示例为「修复：显示当前输入法」，发布标题用「v版本号 · 中文摘要」，发布正文写清变化和已验证的场景。

## issue

按 `AGENTS.md` 的约定：issue 是 `.scratch/<feature-slug>/issues/NN-slug.md` 的 markdown 文件，
`Status:` 行记录 triage 状态（`needs-triage` / `needs-info` / `ready-for-agent` / `ready-for-human` / `wontfix`）。
