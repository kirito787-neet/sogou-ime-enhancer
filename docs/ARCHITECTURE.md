# 架构与技术路线

## 目标

在 Xiaomi HyperOS / MIUI 上让**官方普通版**搜狗输入法（`com.sohu.inputmethod.sogou`）
显示系统级「全面屏键盘优化」底栏，并去广告，且不改动官方 APK 的签名。

## 已排除的路线

| 路线 | 结论 | 原因 |
|---|---|---|
| 改 APK + 重签 | ⛔ 死路 | `libsogouime.so` 在 `+0xfd1a4` 校验签名，重签后 `SIGSEGV`。用"未改动官方包仅重签"做过对照实验，现象一致，证明是签名校验而不是我们的改动导致 |
| NPatch / LSPatch 把模块塞进搜狗包 | ⛔ 死路 | 同上，必然重签 |
| Zygisk 注入 | 🟡 可行但未采用 | 工作量大于 Xposed 路线 |

## 采用的路线

```
方案 A：官方 APK（零改动，官方签名）
          ↑ Xposed hook（LSPosed，作用域=官方包）
        sogou-enhancer 模块 APK
          └─ BottomHook：在输入法窗口里插入原生底栏
             SkinPalette：读取当前皮肤配色
             EmbeddedGuard：方案 B 内置场景下的防护

方案 B：单个 APK = 搜狗 20.17.0（NPatch 共存重打包，包名 .enhanced）
          └─ 内嵌同一个增强模块 + 设置页（classes8.dex）
```

### 关键类

| 类 | 作用 |
|---|---|
| `com.sogouenhance.HookEntry` | Xposed 入口，按目标包分发 |
| `com.sogouenhance.bottom.BottomHook` | 底栏创建 / 插入 / 显示隐藏，刷新任务投递到主线程 Handler（1.2.3 修复：原先投递到未 attach 的窗口视图会永久卡死） |
| `com.sogouenhance.bottom.SkinPalette` | 复用搜狗自身的 `theme.settings.a.t().f()`、`ui.s.c()/g()/h()`、`ui.d.k()` 读取皮肤底栏色与图标色，对比不足时降级为可读色 |
| `com.sogouenhance.bottom.EmbeddedGuard` | 方案 B 内嵌时防止外部重复加载 |
| `com.sogouenhance.AHomeActivity` | 方案 A 首页（官方搜狗 / 增强设置 / 系统输入法设置三个入口），`singleTask` |

## 构建

```bash
# 需要：JDK 21（work/tools/jdk）、apktool、Android build-tools
python work/enhancer/build.py --variant a      # 只构建方案 A 模块
python work/enhancer/build.py --variant both   # A + B 都构建
python work/enhancer/package_b.py              # 打方案 B 单 APK
python work/enhancer/export.py                 # 导出产物到 outputs/
```

构建过程：`javac` 编译 `src/` → 打包成 dex → 用 apktool 把 dex 塞进基线模块的
smali 树 → `aapt2` 打包 → `zipalign` → 测试证书签名 → 输出 `modules.json` / `single.json`
（含 SHA-256）。

## 证据

本仓库不存放大体积设备证据（截图 / logcat / 安装包）。真机验证记录摘要在各版本的
Release 说明与 `docs/RELEASES.md` 中；原始证据留在本地 `work/enhancer/device-*/`。
