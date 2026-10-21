# 微信输入法修改版.apk 的「全面屏键盘优化」适配是怎么做的

分析对象：`C:\Users\Kirito787\Documents\AI\DSH\sougou\微信输入法修改版.apk`（175,983,806 B，3463 条目）
分析时间：本次会话；REA 在本会话不可用（paged namespace 为空），改用本地 jadx 1.5.6 + zulu-jre 21 手工完成同等分析。

## 一、结论先行

这个包**没有修改微信输入法自身的代码**来实现底栏适配。它是一个用 **NPatch（LSPatch 的分支）打的补丁包**，
里面塞进了用户自己的 Xposed 模块 **com.xposed.wetypehook**，全面屏底栏的适配**全部**发生在那个模块里。

证据（zip 条目）：

- `assets/npatch/config.json`
- `assets/npatch/loader.bin`
- `assets/npatch/so/arm64-v8a/libnpatch.so`、`assets/npatch/so/x86_64/libnpatch.so`
- `assets/npatch/modules/com.xposed.wetypehook.apk`

`assets/npatch/config.json` 原文：

```json
{"appComponentFactory":"androidx.core.app.CoreComponentFactory","debuggable":false,"injectProvider":false,
 "lspConfig":{"API_CODE":101,"CORE_VERSION_CODE":3049,"CORE_VERSION_NAME":"2.0","VERSION_CODE":639,"VERSION_NAME":"1.0.5","sigBypassLevel":0},
 "managerPackageName":"top.nkbe.npatch","newPackage":"com.monet.inputmethod.hyper","outputLog":true,
 "overrideVersionCode":false,"sigBypassLevel":0,"useManager":false,"useMicroG":false}
```

反向证据：把包内 5 个 dex（classes.dex 8,060,276 / classes2 8,368,996 / classes3 8,530,860 / classes4 1,029,428 / classes5 2,124）
整体做过字符串扫描，`InputMethodServiceInjector`、`sImeSupport`、`sImeMinVersionSupport`、`InputMethodBottomManager`、
`InputMethodModuleManager`、`LSPass`、`de.robv.android.xposed`、`XposedBridge` **一个都没有出现**。
所以微信输入法自己的代码是干净的，MIUI 适配完全由模块注入。

## 二、包内模块是什么

已抽出到 `work/wxime/npatch-wetypehook.apk`（2,604,886 B，sha256 `5aacd7b2ef23e9ce6cf057b267dec75c4efa3fea042803a9d2a98cccacf1fb84`），
它**不是**本机保存的 `work/dsh/wetypehook.apk`（4,973,489 B，sha256 `025d3a75fbe503981e96d9120b2fb46b999297d7657fcf390f7d3975f37f1940`）。

- 48 个条目，`classes.dex` 1,997,272 B
- **legacy Xposed API**（不是 libxposed 102）：`assets/xposed_init` = `com.xposed.wetypehook.MainHook`
- 没有 `META-INF/xposed/` 目录
- 入口类实现 `IXposedHookLoadPackage` + `IXposedHookZygoteInit`

反编译产物：`work/wxime/jadx-embedded/sources/`（2261 个 .java），核心逻辑全在
`work/wxime/jadx-embedded/sources/com/xposed/wetypehook/MainHook.java`（1505 行）。

## 三、底栏适配的完整机制（MainHook.java 行号为反编译产物行号）

### 0. 总开关
`handleLoadPackage`（行 401）先读系统属性：

- 行 407：`ro.miui.support_miui_ime_bottom`，默认 `"0"`
- 行 415：`boolean zI = "1".equals(prop)`，为 true 才算这台机器支持 MIUI 全面屏底栏
- 行 416-419：非 `android` 进程（即 IME 进程）走 `q(loadPackageParam, zI)`；`android`（system_server）另走一支

### 1. 竖旗：把 `sIsImeSupport` 置 1
行 110-124：

```java
public static void h(Class cls) {
    qh1.b(cls, "sIsImeSupport").set(null, 1);   // 静态字段写 1
    fv.B("Success:Hook field sIsImeSupport");
}
```

作用对象有两处：`android.inputmethodservice.InputMethodServiceInjector`（不存在时退化为
`android.inputmethodservice.InputMethodServiceStubImpl`，行 463-466），以及 `com.miui.inputmethod.InputMethodBottomManager`（行 535）。
这是告诉 framework「本 IME 支持 MIUI 底栏」的原始开关。

### 2. 让 framework 真的去画底栏：hook `addMiuiBottomView` / `customizeBottomViewColor`
行 459-524，`m(boolean z)`：

- 行 491：找 `InputMethodServiceInjector` 里名为 `customizeBottomViewColor` 的方法并挂 hook
- 行 504-513：找 `addMiuiBottomView` 并挂 hook
- 行 479-481：同时 hook `com.android.internal.policy.PhoneWindow` 上的一个方法（取窗口层级用）

hook 回调 `yc0.k()`（`work/wxime/jadx-embedded/sources/miuiime/yc0.java`）只是在事件里回调
`MainHook.b(cls, z)`，而 `b`（行 235-249）最终通过反射调用静态方法
`customizeBottomViewColor(boolean, int, int, int)`：

```java
// 行 237-239（z=true 时）
int i = (Resources.getSystem().getConfiguration().uiMode & 48) == 32 ? -657931 : -14671840; // 深/浅色
Object[] objArr = {Boolean.TRUE, 0, i, Color.argb(md0.u(102,0,255), ...)};
qh1.a(cls, "customizeBottomViewColor", true, objArr).invoke(null, Arrays.copyOf(objArr, 4));
```

即：**替 IME 声明底栏配色/尺寸参数**，让 framework 按第三方 IME 的样子画出一条匹配的底栏。

### 3. 把 MIUI 底栏类塞进 IME 的 classloader：hook `InputMethodModuleManager.loadDex`
行 323-376，`f(boolean z)`：hook 后 `methodHookParam.setResult(null)` **直接吞掉原逻辑**（行 352），然后：

- 行 344：`Class.forName("com.miui.inputmethod.InputMethodBottomManager", true, classLoader)`（IME 的 plugin classloader）
- 行 348-350：**加载不到就 `addDexPath(classLoader, dexPath)`**，手工把 MIUI 底栏 dex 挂进 IME 的 classloader
- 行 351：`mainHook.n(classLoader, z)`，接着挂 `InputMethodBottomManager`

第三方 IME 原本拿不到 MIUI 这套底栏类，这一步是硬把门打开的。

### 4. 改白名单：hook `InputMethodBottomManager.getSupportIme()`
行 526-556 挂 hook，替换体在 `miuiime/l.java` **case 16（行 471-484）**：

```java
Object obj3 = qh1.b((Class) this.e, "sBottomViewHelper").get(null);   // InputMethodBottomManager.sBottomViewHelper
Object obj4 = qh1.b(obj3.getClass(), "mImm").get(obj3);               // 里面的 InputMethodManager
return ((InputMethodManager) obj4).getEnabledInputMethodList();       // 所有已启用 IME 都算“支持”
```

这是整个适配的**核心**：MIUI 原本按自己的白名单（小米版搜狗、讯飞小米版、百度 input_mi……）决定谁有底栏，
这里直接把判断改成「只要已启用就有」。

### 5. 防止被踢出列表：hook `deleteNotSupportIme`
行 278-321 `e(String, ClassLoader)`：在 `InputMethodBottomManager$MiuiSwitchInputMethodListener` 上找名为
`deleteNotSupportIme` 的方法，用 `XC_MethodReplacement.returnConstant(null)` 替换（行 310）。
行 528 调用点。即：MIUI 想把「不支持」的 IME 从底栏候选里删掉时，这里让它什么都不做。

### 6. 顺手关掉小爱
行 378-399：`isXiaoAiEnable` 返回 `false`。

### 7. 哪些包跳过第 2 步
行 75：

```java
public final Set a = fv.L("com.iflytek.inputmethod.miui", "com.sohu.inputmethod.sogou.xiaomi",
                          "com.baidu.input_mi", "com.miui.catcherpatch", "com.xiaomi.type");
```

行 1493-1503 的分流：

```java
if (z) {                              // ro.miui.support_miui_ime_bottom == "1"
    boolean zContains = mainHook.a.contains(str);   // str = 当前包名
    boolean z2 = !zContains;
    if (!zContains) mainHook.m(zI);                 // 不在集合里 → 才做 Injector 定制
    mainHook.e("...InputMethodServiceInjector$MiuiSwitchInputMethodListener", loader);
    mainHook.f(z2);                                 // 不在集合里 → z2=true，n() 里会额外竖旗
}
```

**原生就有 MIUI 支持的包（小米版搜狗在内）跳过第 2 步；第三方包（普通版搜狗、微信输入法）走完整改造。**

### 8. 微信输入法专属部分（和底栏无关）
行 601 起 `q()` 里 `com.monet.inputmethod.hyper` 分支只做外观：字体替换（`Typeface.createFromAsset`）、
窗口模糊（`updateFullscreenMode` / `onComputeInsets` / `onWindowHidden` / `hideWindow` / `onDestroy`，行 1440-1456）、
渐变背景、圆角等。**删掉这些不影响底栏适配。**

## 四、对搜狗任务的直接含义

1. 这套方案是**纯 Xposed 层**，不碰目标 APK 一个字节 → **不会触发 `libsogouime.so` 的签名自校验**（那个 +0xfd1a4 SIGSEGV 是重签才有的）。
2. 普通版搜狗 `com.sohu.inputmethod.sogou` **不在**行 75 的集合里，正好走完整改造路径 —— 这正是需求 1 要的效果。
3. 本机已有的 `work/dsh/wetypehook.apk`（libxposed API 102 版）字符串里有同一批 hook 点
   （`InputMethodServiceInjector`、`sIsImeSupport`、`InputMethodModuleManager.loadDex`、`InputMethodBottomManager`、
   `deleteNotSupportIme`、`sBottomViewHelper`），说明两个 build 是同一套逻辑，只是 API 代际不同。
4. 因此「把 `com.sohu.inputmethod.sogou` 加进 LSPosed 作用域」不是碰运气 —— 机制上它就该生效。
5. **NPatch/LSPatch 路线（把这个包的做法照搬到搜狗）不可行**：它要往目标 APK 里塞东西并重签，正好踩反篡改死路。

## 五、当前阻碍

设备现在**没有 root**（ZygiskNext 装完重启后 KernelSU 没挂载 su）：`su -c id` → `su: inaccessible or not found`，
`ps -A | grep -E "lspd|zygiskd|ksud"` 为空。LSPosed 因此不工作，第 4 点的验证要等 root 恢复后才能做。

## 六、关键文件位置

- 原始包：`C:\Users\Kirito787\Documents\AI\DSH\sougou\微信输入法修改版.apk`
- 抽出的模块：`work/wxime/npatch-wetypehook.apk`
- 模块 dex：`work/wxime/wetypehook-embedded.dex`
- 反编译源码：`work/wxime/jadx-embedded/sources/`
- 核心类：`work/wxime/jadx-embedded/sources/com/xposed/wetypehook/MainHook.java`
- 关键 lambda：`work/wxime/jadx-embedded/sources/miuiime/l.java`（case 16）、`miuiime/yc0.java`
