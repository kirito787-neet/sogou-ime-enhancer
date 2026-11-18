# Android 17 上方案 B 启动失败

Status: needs-triage

设备为 REDMI K90 Pro Max，运行 Android 17 和 HyperOS OS4.0.6.0.XPMCNXM。
原方案 B 1.2.3 冷启动时，输入法服务超过 20 秒仍未完成，系统记录 ANR。
主线程在 NPatch 原生加载路径等待动态链接器锁。

- NPatch 833 关闭可选重定向时，外层 APK 缺少宿主 DEX，启动报 `ClassNotFoundException`。
- 修复测试包的宿主 DEX 布局后，输入法可以显示键盘，但原生输入线程随后收到 `SIGSEGV`。
- NPatch 833 的集成配置和 [NPatch v1.1.0 (857)](https://github.com/7723mod/NPatch/releases/tag/v1.1.0) 的集成配置均在真机复现 `SIGSEGV`。新版候选包能显示键盘和底栏，输入法进程仍在数秒后重启。

B 候选均未通过验收。手机恢复测试前的 B 1.2.3 APK，默认输入法切回普通版搜狗（方案 A）。
验收需覆盖多次冷启动、正常输入和提交中文候选、内置设置读写及底栏。
