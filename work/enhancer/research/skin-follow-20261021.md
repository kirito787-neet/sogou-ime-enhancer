# 底栏透明与随皮肤配色：只读研究

2026-10-21。用户要求：解释 A/B 透明原因，研究小米版随皮肤变化的原理与 A/B 可行性。
禁止卸载搜狗输入法小米版。此次没有对手机执行安装、卸载、切换皮肤、清数据或配置修改。
没有修改现有适配源码或重构建/替换交付 APK。

## 已确认：透明由当前适配实现强制产生

`src/com/sogouenhance/bottom/BottomHook.java`：

- 第 36 行把 `customizeBottomViewColor` 的背景参数改为 0。
- 第 48 行把 `PhoneWindow.setNavigationBarColor` 的颜色参数改为 0。
- 第 135 行再次调用 `customizeBottomViewColor(true, 0, foreground, pressed)`。

ARGB 的 `0x00000000` 是全透明。前景色只看系统 `uiMode`，未读取当前搜狗皮肤。
两方案使用同一 BottomHook，所以出现同样的结果。这不是系统接口只允许透明。

ROM 证据：`work/inventory/rom-phrase-bottom-disasm.txt:2076` 的
`InputMethodBottomManager.setBottomColor(ZIII)` 在自定义模式将第二个参数直接传给
`sBottomView.setBackgroundColor(int)`，后两个参数构造按钮的 ColorStateList。

## 已确认：小米版自己向系统提供配色

分析对象：项目根 `搜狗输入法小米.apk`。
SHA256：`1dba71c52a12bf773d5d78c50a414cbe45ed2a449bf86a19de6059eec20e763c`。
本次直接读取其 classes2.dex，确认含 `customizeBottomViewColor`、`getThemeColorInt`
及 `NavigationBar updateMiuiBottomColor: third` 的路径标记。
可读证据为现有 `work/xiaomi/` 反编译树，apktool.yml 指向此 APK。

核心类 `com.sogou.inputmethod.oem.xiaomi.screen.j`：

- `c()`（smali 第 202 行）：计算导航/底栏背景，处理系统皮肤、第三方皮肤等分支；
  第 429 行附近的第三方分支读取 theme settings 的颜色，再经过 UI 颜色转换。
- `u()`（第 1145 行）：计算底栏背景、正常图标色和按下图标色。
  第 1228 行第三方分支调用 `IOemAppService.getThemeColorInt()`，还检查图标与背景是否过近，
  必要时换成可读的深/浅色。随后反射调用 `customizeBottomViewColor(true, bg, icon, pressed)`。
- `v(Window)`（第 1462 行）：更新窗口导航栏；底栏启用时调用 `u()`。
- `window.b` 的窗口 Insets 回调会进入 `j.v(Window)`。
- `theme.i$a.onChange` 监听 `keyboard_skin_follow_system_enable` 并通知配色逻辑更新。

结论：系统提供绘制接口，小米版提供皮肤色和刷新时机；不是系统自动读取搜狗皮肤。

## 已确认：普通版有可复用的配色来源

`work/standard/smali_classes5/com/sohu/util/k.smali` 的 `b(Context, Window)`（第 99 行）：

- 区分浮动键盘、默认皮肤和第三方皮肤。
- 使用 `com.sohu.inputmethod.ui.s.c()/g(Context)`、`theme.settings.a.t().f(defaultColor)`
  等路径计算颜色，并经 `ui.d.k(color, false)` 转换。
- 第 269/373 行将结果传给 `Window.setNavigationBarColor`。
- `ui.s.c()` 进入 theme color engine；`ui.s.g(Context)` 查找皮肤 sid 对应颜色并处理叠色。
- 调用方包括 `input.lifecycle.v.i(ZZ)`、`input.keyboard.d.H(...)` 和其他输入法生命周期路径。

这条现成链路的输出正被当前 BottomHook 覆盖成 0。

## 可行性与下一步实现位置

A/B 均可增加随皮肤的底栏配色，同一份模块源码可以同时修正两方案。
本节为实施前研究；现已实现 1.2.0，新增 `SkinPalette.java` 并修改 `BottomHook.java`。
A 当前皮肤不透明、B 默认/霓虹实际换肤已验证，11 项配色行为检查通过。
完整证据及尚未覆盖的测试见 `../README.md` 和 `outputs/2026-10-21-skin-1.2.0/测试记录.json`。

具体实现应：

1. 移除三处无条件透明覆盖。
2. 复用普通版为当前键盘计算的颜色，桥接到 MIUI 底栏的三色接口。
3. 将桥接限定于输入法窗口，避免把设置页、登录页的 PhoneWindow 配色误用到键盘。
4. 保留皮肤的图标主色，并处理与背景过近时的对比度；无颜色资料时才使用深浅色兜底。
5. 覆盖底栏首次创建、切换皮肤、重新弹出键盘、系统深浅色、布局与浮动模式变化。
6. 以至少浅色、深色、彩色第三方皮肤验证 A/B，而不修改小米版安装与数据。

接口已证明能同步背景色与图标色；图片/渐变/动态皮肤的整张背景是否能连续延伸到底栏，
本轮证据不能证明。小米版此处调用的也是整数颜色接口，不应把颜色跟随直接等同于
任意背景图像的完整复刻。
