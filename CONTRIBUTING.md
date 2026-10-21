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

## issue

按 `AGENTS.md` 的约定：issue 是 `.scratch/<feature-slug>/issues/NN-slug.md` 的 markdown 文件，
`Status:` 行记录 triage 状态（`needs-triage` / `needs-info` / `ready-for-agent` / `ready-for-human` / `wontfix`）。
