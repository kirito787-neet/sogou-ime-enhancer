package com.sogouenhance.bottom;

import android.os.Handler;
import android.os.Looper;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.ref.WeakReference;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XposedBridge;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;

/** Process-local HyperOS/MIUI integration. Does not change ROM or other IMEs. */
public final class BottomHook implements IXposedHookLoadPackage {
    private static final String MANAGER = "com.miui.inputmethod.InputMethodBottomManager";
    private static final Set<Method> HOOKS = Collections.synchronizedSet(new HashSet<Method>());
    private final ThreadLocal<Boolean> updating = new ThreadLocal<Boolean>();
    private WeakReference<Object> keyboardWindow = new WeakReference<Object>(null);
    private WeakReference<Object> bottomArea = new WeakReference<Object>(null);
    private WeakReference<Object> inputFrame = new WeakReference<Object>(null);
    private WeakReference<Object> normalKeyboard = new WeakReference<Object>(null);
    private int normalThemeBottomPadding;
    private Class<?> framework;
    private SkinPalette palette;
    private boolean refreshPending;
    private long refreshPendingAt;
    private Handler main;
    private String lastPalette;
    private boolean hyperOs4;
    private boolean gestureLayout;

    public void handleLoadPackage(LoadPackageParam p) {
        if (!"com.sohu.inputmethod.sogou".equals(p.packageName)
                && !"com.sohu.inputmethod.sogou.enhanced".equals(p.packageName)) return;
        try {
            Class<?> props = Class.forName("android.os.SystemProperties");
            Object supported = props.getMethod("get", String.class, String.class)
                    .invoke(null, "ro.miui.support_miui_ime_bottom", "0");
            if (!"1".equals(supported)) { log("SKIP ROM does not advertise MIUI bottom support"); return; }
            Class<?> injector;
            try { injector = Class.forName("android.inputmethodservice.InputMethodServiceInjector"); }
            catch (ClassNotFoundException absent) {
                injector = Class.forName("android.inputmethodservice.InputMethodServiceStubImpl");
            }
            framework = injector;
            hyperOs4 = Class.forName("android.os.Build$VERSION").getField("SDK_INT").getInt(null) >= 37;
            palette = new SkinPalette(p.classLoader);
            support(framework);
            disableXiaoAi(framework);
            hook(framework, "addMiuiBottomView", new XC_MethodHook() {
                protected void afterHookedMethod(MethodHookParam param) {
                    if (param.args.length == 7) {
                        inputFrame = new WeakReference<Object>(param.args[2]);
                        bottomArea = new WeakReference<Object>(param.args[4]);
                        rememberService(param.args[6]);
                    }
                    scheduleColor();
                }
            });
            hookResizeBounds(p.classLoader);
            if (hyperOs4 && "myron".equals(Class.forName("android.os.Build").getField("DEVICE").get(null))) {
                hookK90KeyboardSize(p.classLoader);
                hookK90ResizeGeometry(p.classLoader);
            }
            try {
                hook(Class.forName("com.android.internal.policy.PhoneWindow"), "setNavigationBarColor",
                        new XC_MethodHook() {
                            protected void beforeHookedMethod(MethodHookParam param) {
                                if (gestureLayout && keyboardWindow.get() == param.thisObject) param.args[0] = 0;
                            }

                            protected void afterHookedMethod(MethodHookParam param) {
                                if (Boolean.TRUE.equals(updating.get())) return;
                                rememberWindow(param.thisObject);
                                if (keyboardWindow.get() == param.thisObject) scheduleColor();
                            }
                        });
            } catch (Throwable error) { failure("navigation color", error); }
            try {
                hook(Class.forName("com.sohu.util.k", false, p.classLoader), "b", new XC_MethodHook() {
                    protected void afterHookedMethod(MethodHookParam param) {
                        if (param.args.length == 2) rememberWindow(param.args[1]);
                        scheduleColor();
                    }
                });
                Class<?> service = Class.forName("com.sohu.inputmethod.sogou.SogouIME", false, p.classLoader);
                for (String event : new String[] {"onWindowShown", "onStartInputView", "onConfigurationChanged"}) {
                    for (Class<?> type = service; type != null; type = type.getSuperclass()) {
                        boolean found = false;
                        for (Method m : type.getDeclaredMethods()) {
                            if (!m.getName().equals(event)) continue;
                            hookMethod(m, new XC_MethodHook() {
                                protected void afterHookedMethod(MethodHookParam param) {
                                    rememberService(param.thisObject);
                                    scheduleColor();
                                }
                            });
                            found = true;
                        }
                        if (found) break;
                    }
                }
            } catch (Throwable error) { failure("skin refresh callbacks", error); }
            filterListener(framework.getName() + "$MiuiSwitchInputMethodListener", p.classLoader);
            hook(Class.forName("android.inputmethodservice.InputMethodModuleManager"), "loadDex",
                    new XC_MethodHook() {
                        protected void beforeHookedMethod(MethodHookParam param) {
                            if (param.args.length != 2 || !(param.args[0] instanceof ClassLoader)
                                    || !(param.args[1] instanceof String)) return;
                            ClassLoader loader = (ClassLoader) param.args[0];
                            try {
                                try { Class.forName(MANAGER, false, loader); }
                                catch (ClassNotFoundException absent) {
                                    method(loader.getClass(), "addDexPath", String.class)
                                            .invoke(loader, param.args[1]);
                                }
                                plugin(loader);
                                // The original loadDex now sees the already-loaded class and returns normally.
                            } catch (Throwable error) { failure("loadDex; original retained", error); }
                        }
                        protected void afterHookedMethod(MethodHookParam param) {
                            if (param.args.length > 0 && param.args[0] instanceof ClassLoader) {
                                try { plugin((ClassLoader) param.args[0]); }
                                catch (Throwable error) { failure("plugin", error); }
                            }
                        }
                    });
            log("READY " + p.processName);
        } catch (Throwable error) { failure("initialization", error); }
    }

    private void hookResizeBounds(ClassLoader loader) {
        try {
            if (!hyperOs4) return;
            Class<?> resize = Class.forName("com.sohu.inputmethod.sogou.z0", false, loader);
            Class<?> ime = Class.forName("com.sohu.inputmethod.sogou.MainImeServiceDel", false, loader);
            Class<?> rect = Class.forName("android.graphics.Rect");
            Class<?> view = Class.forName("android.view.View");
            Method bounds = method(resize, "k", ime);
            Field bottom = rect.getField("bottom");
            Field top = rect.getField("top");
            Method visible = view.getMethod("isShown");
            Method location = view.getMethod("getLocationOnScreen", int[].class);

            // The overlay, bottom drag limit and saved inset share the keyboard edge.
            hookMethod(bounds, new XC_MethodHook() {
                protected void afterHookedMethod(MethodHookParam param) throws ReflectiveOperationException {
                    Object area = bottomArea.get();
                    Object frame = param.getResult();
                    if (area == null || frame == null || !(Boolean) visible.invoke(area)) return;
                    int[] position = new int[2];
                    location.invoke(area, position);
                    int areaTop = position[1];
                    if (areaTop > top.getInt(frame) && areaTop < bottom.getInt(frame)) {
                        bottom.setInt(frame, areaTop);
                    }
                }
            });
        } catch (ClassNotFoundException | NoSuchMethodException absent) {
            log("OPTIONAL keyboard resize callbacks are unavailable");
        } catch (Throwable error) { failure("keyboard resize", error); }
    }

    private void hookK90ResizeGeometry(ClassLoader loader) {
        try {
            String root = "com.sogou.imskit.core.ui.keyboard.resize.";
            String host = "com.sohu.inputmethod.sogou.";
            Class<?> resize = Class.forName(host + "z0", false, loader);
            Class<?> callbacks = Class.forName(host + "y0", false, loader);
            Class<?> manager = Class.forName(root + "b", false, loader);
            Field instance = field(manager, "a");
            Method data = method(manager, "a");
            Method savedInset = method(data.getReturnType(), "g0");
            Class<?> metrics = Class.forName("com.sogou.theme.datacache.a", false, loader);
            Class<?> layout = Class.forName("com.sogou.core.ui.window.StyleConstraintLayout", false, loader);
            Class<?> view = Class.forName("android.view.View");
            Method getParent = view.getMethod("getParent");
            Method getParams = view.getMethod("getLayoutParams");
            Method getHeight = view.getMethod("getHeight");
            Method visible = view.getMethod("isShown");
            Method location = view.getMethod("getLocationInWindow", int[].class);
            Field gravity = Class.forName("android.widget.FrameLayout$LayoutParams").getField("gravity");
            Field margin = Class.forName("android.view.ViewGroup$MarginLayoutParams").getField("bottomMargin");
            Class<?> rect = Class.forName("android.graphics.Rect");
            Field top = rect.getField("top");
            Field bottom = rect.getField("bottom");
            java.lang.reflect.Constructor<?> copyRect = rect.getConstructor(rect);
            Class<?> presenter = Class.forName(root + "presenter.b", false, loader);
            Class<?> rules = Class.forName(root + "layout.limit.f", false, loader);
            Class<?> layoutProvider = Class.forName(host + "vpabridge.a", false, loader);
            // Resolve all signatures before installing the related hooks.
            Method limits = method(presenter, "j", rules, rect, layoutProvider);
            Method preview = method(resize, "p", Integer.TYPE, Integer.TYPE, Integer.TYPE, Integer.TYPE);
            Method currentRect = method(resize, "m");
            Method drag = method(callbacks, "b", rect, rect);
            Method measure = method(layout, "onMeasure", Integer.TYPE, Integer.TYPE);
            Method themeInset = method(metrics, "f");

            // The saved offset belongs below the keyboard. On this ROM Sogou passes it into
            // skin sizing, while Android still lays out the resulting view against the footer.
            hookMethod(themeInset, new XC_MethodHook() {
                protected void afterHookedMethod(MethodHookParam call) throws ReflectiveOperationException {
                    Object keyboard = normalKeyboard.get();
                    if (keyboard == null || k90PortraitWidth() <= 0
                            || getParent.invoke(keyboard) != inputFrame.get()) return;
                    int inset = (Integer) savedInset.invoke(data.invoke(instance.get(null)));
                    int padding = Math.max(0, (Integer) call.getResult() - Math.max(0, inset));
                    normalThemeBottomPadding = padding;
                    call.setResult(padding);
                }
            });
            hookMethod(measure, new XC_MethodHook() {
                protected void beforeHookedMethod(MethodHookParam call) throws ReflectiveOperationException {
                    Object keyboard = call.thisObject;
                    Object frame = inputFrame.get();
                    if (frame == null || getParent.invoke(keyboard) != frame) return;
                    Object params = getParams.invoke(keyboard);
                    if (params == null || !gravity.getDeclaringClass().isInstance(params)) return;
                    if ((gravity.getInt(params) & 0x70) != 0x50 || k90PortraitWidth() <= 0) {
                        if (normalKeyboard.get() == keyboard) {
                            margin.setInt(params, 0);
                            normalKeyboard.clear();
                        }
                        return;
                    }
                    normalKeyboard = new WeakReference<Object>(keyboard);
                    int inset = (Integer) savedInset.invoke(data.invoke(instance.get(null)));
                    margin.setInt(params, Math.max(0, inset));
                }
            });

            // The overlay shows the whole keyboard. Convert its bottom back to the
            // skin's logical edge only when passing a drag to Sogou's resize calculation.
            hookMethod(limits, new XC_MethodHook() {
                protected void beforeHookedMethod(MethodHookParam call) throws ReflectiveOperationException {
                    Object area = bottomArea.get();
                    if (normalKeyboard.get() == null || area == null || !(Boolean) visible.invoke(area)) return;
                    int[] position = new int[2];
                    location.invoke(area, position);
                    if (position[1] > top.getInt(call.args[1])) bottom.setInt(call.args[1], position[1]);
                }
            });
            hookMethod(preview, new XC_MethodHook() {
                protected void beforeHookedMethod(MethodHookParam call) throws ReflectiveOperationException {
                    Object keyboard = normalKeyboard.get();
                    if (keyboard == null || !(Boolean) visible.invoke(keyboard)) return;
                    int height = (Integer) getHeight.invoke(keyboard);
                    if (height > 0) call.args[3] = (Integer) call.args[1] + height;
                }
            });
            hookMethod(currentRect, new XC_MethodHook() {
                protected void afterHookedMethod(MethodHookParam call) throws ReflectiveOperationException {
                    Object keyboard = normalKeyboard.get();
                    Object result = call.getResult();
                    if (keyboard == null || result == null || !(Boolean) visible.invoke(keyboard)) return;
                    int height = (Integer) getHeight.invoke(keyboard);
                    if (height > 0) bottom.setInt(result, top.getInt(result) + height);
                }
            });
            hookMethod(drag, new XC_MethodHook() {
                protected void beforeHookedMethod(MethodHookParam call) throws ReflectiveOperationException {
                    if (normalKeyboard.get() == null || normalThemeBottomPadding <= 0) return;
                    for (int i = 0; i < call.args.length; i++) {
                        if (call.args[i] == null) continue;
                        Object logical = copyRect.newInstance(call.args[i]);
                        bottom.setInt(logical, bottom.getInt(logical) - normalThemeBottomPadding);
                        call.args[i] = logical;
                    }
                }
            });
        } catch (ClassNotFoundException | NoSuchMethodException absent) {
            log("OPTIONAL K90 resize geometry unavailable: " + absent);
        } catch (Throwable error) { failure("K90 resize geometry", error); }
    }

    private void hookK90KeyboardSize(ClassLoader loader) {
        try {
            String resize = "com.sogou.imskit.core.ui.keyboard.resize.";
            String spec = "com.sohu.inputmethod.main.view.containerspec.";
            Class<?> resizeManager = Class.forName(resize + "b", false, loader);
            Field manager = field(resizeManager, "a");
            Method resizeData = method(resizeManager, "a");
            Method resizedKeyHeight = method(resizeData.getReturnType(), "v");
            Class<?> config = Class.forName(resize + "keyboard.config.a", false, loader);
            Class<?> configs = Class.forName(resize + "keyboard.config.b", false, loader);
            Method currentConfig = method(configs, "a", Boolean.TYPE);
            Field mode = field(config, "c");
            Field arrangement = field(config, "d");
            Class<?> candidate = Class.forName(spec + "CandidateBaseHeightProvider", false, loader);
            Class<?> specData = Class.forName(spec + "d", false, loader);
            Method copy = method(specData, "a");
            Method contentHeight = method(copy.getReturnType(), "x", Integer.TYPE);
            java.lang.reflect.Constructor<?> createSpec = specData.getDeclaredConstructor(copy.getReturnType());
            createSpec.setAccessible(true);
            Method sizeCandidate = method(Class.forName(spec + "h", false, loader), "b",
                    Class.forName(spec + "c", false, loader), specData);
            Class<?> themeMetrics = Class.forName("com.sogou.theme.datacache.a", false, loader);
            Method sizeKeys = method(themeMetrics, "j", Integer.TYPE);
            Method keyAreaInset = method(themeMetrics, "f");
            Method extraRow = method(candidate, "b");
            Method hasExtraRow = method(candidate, "f");
            ThreadLocal<Integer> defaultKeyHeight = new ThreadLocal<Integer>();

            // The bundled keyboard has a 140 px candidate strip and a 710 px key area
            // on the 1200 px-wide K90 Pro Max. Feed those defaults into Sogou's own layout
            // and let its normal resize calculation apply saved user adjustments.
            hookMethod(extraRow, new XC_MethodHook() {
                protected void afterHookedMethod(MethodHookParam param) throws ReflectiveOperationException {
                    if (k90PortraitWidth() > 0) param.setResult(0);
                }
            });
            hookMethod(hasExtraRow, new XC_MethodHook() {
                protected void afterHookedMethod(MethodHookParam param) throws ReflectiveOperationException {
                    if (k90PortraitWidth() > 0) param.setResult(false);
                }
            });
            hookMethod(sizeCandidate, new XC_MethodHook() {
                protected void beforeHookedMethod(MethodHookParam param) throws ReflectiveOperationException {
                    int width = k90PortraitWidth();
                    if (width <= 0) return;
                    Object active = currentConfig.invoke(null, false);
                    if (mode.getInt(active) != 0 || arrangement.getInt(active) != 0) return;
                    Object builder = copy.invoke(param.args[1]);
                    contentHeight.invoke(builder, Math.round(width * (140f / 1200)));
                    param.args[1] = createSpec.newInstance(builder);
                }
            });
            hookMethod(sizeKeys, new XC_MethodHook() {
                protected void beforeHookedMethod(MethodHookParam param) throws ReflectiveOperationException {
                    int width = k90PortraitWidth();
                    if (width <= 0 || (Integer) param.args[0] <= 0) return;
                    Object active = currentConfig.invoke(null, false);
                    if (mode.getInt(active) != 0 || arrangement.getInt(active) != 0) return;
                    int inset = (Integer) keyAreaInset.invoke(param.thisObject);
                    int height = Math.round(width * (710f / 1200)) - inset;
                    if (height <= 0) return;
                    param.args[0] = height;
                    defaultKeyHeight.set(height);
                }

                protected void afterHookedMethod(MethodHookParam param) throws ReflectiveOperationException {
                    Integer defaultHeight = defaultKeyHeight.get();
                    defaultKeyHeight.remove();
                    if (param.getThrowable() != null || defaultHeight == null) return;
                    Object data = resizeData.invoke(manager.get(null));
                    int height = (Integer) resizedKeyHeight.invoke(data);
                    param.setResult(height > 0 ? height : defaultHeight);
                }
            });
        } catch (ClassNotFoundException | NoSuchMethodException absent) {
            log("OPTIONAL K90 keyboard metrics are unavailable");
        } catch (Throwable error) { failure("K90 keyboard metrics", error); }
    }

    private int k90PortraitWidth() throws ReflectiveOperationException {
        Object window = keyboardWindow.get();
        if (window == null) return 0;
        Object context = method(window.getClass(), "getContext").invoke(window);
        Object resources = method(context.getClass(), "getResources").invoke(context);
        Object config = method(resources.getClass(), "getConfiguration").invoke(resources);
        if (config.getClass().getField("orientation").getInt(config) != 1) return 0;
        Object metrics = method(resources.getClass(), "getDisplayMetrics").invoke(resources);
        return metrics.getClass().getField("widthPixels").getInt(metrics);
    }

    private static void plugin(ClassLoader loader) throws Throwable {
        final Class<?> manager = Class.forName(MANAGER, false, loader);
        support(manager);
        disableXiaoAi(manager);
        filterListener(MANAGER + "$MiuiSwitchInputMethodListener", loader);
        repairBottomMargins(manager, loader);
        hook(manager, "getSupportIme", new XC_MethodHook() {
            protected void beforeHookedMethod(MethodHookParam param) {
                try {
                    Object helper = field(manager, "sBottomViewHelper").get(null);
                    if (helper == null) return;
                    Object imm = field(helper.getClass(), "mImm").get(helper);
                    if (imm == null) return;
                    Object enabled = method(imm.getClass(), "getEnabledInputMethodList").invoke(imm);
                    if (enabled != null) param.setResult(enabled);
                } catch (Throwable error) { failure("enabled IMEs; original retained", error); }
            }
        });
    }

    private static void repairBottomMargins(Class<?> manager, ClassLoader loader) {
        try {
            Class<?> version = Class.forName("android.os.Build$VERSION");
            if (version.getField("SDK_INT").getInt(null) < 37) return;
            Class<?> util = Class.forName("com.miui.inputmethod.InputMethodUtil", false, loader);
            Method updateOverlap = method(util, "updateBottomMargin", Integer.TYPE);
            Method applyMargin = method(manager, "updateBottomMarginReal", Integer.TYPE);
            // HyperOS 4 uses MATCH_PARENT as a pixel height when calculating the overlap.
            // Clamp its negative overlap and the corresponding positive layout margin.
            hookMethod(updateOverlap, new XC_MethodHook() {
                protected void beforeHookedMethod(MethodHookParam param) {
                    if ((Integer) param.args[0] < 0) param.args[0] = 0;
                }
            });
            hookMethod(applyMargin, new XC_MethodHook() {
                protected void beforeHookedMethod(MethodHookParam param) {
                    if ((Integer) param.args[0] > 0) param.args[0] = 0;
                }
            });
        } catch (ClassNotFoundException | NoSuchMethodException absent) {
            log("OPTIONAL bottom margin layout is unavailable");
        } catch (Throwable error) { failure("bottom margin", error); }
    }

    private static void support(Class<?> owner) throws Throwable {
        Field flag = field(owner, "sIsImeSupport");
        flag.setInt(null, 1);
    }

    private static void filterListener(String name, ClassLoader loader) {
        try {
            hook(Class.forName(name, false, loader), "deleteNotSupportIme", new XC_MethodHook() {
                protected void beforeHookedMethod(MethodHookParam param) { param.setResult(null); }
            });
        } catch (ClassNotFoundException absent) { log("OPTIONAL absent " + name); }
        catch (Throwable error) { failure(name, error); }
    }

    private static void disableXiaoAi(Class<?> owner) {
        try {
            for (Method m : owner.getDeclaredMethods()) {
                if (m.getName().equals("isXiaoAiEnable") && m.getReturnType() == Boolean.TYPE) {
                    hookMethod(m, new XC_MethodHook() {
                        protected void beforeHookedMethod(MethodHookParam param) { param.setResult(false); }
                    });
                }
            }
        } catch (Throwable error) { failure("optional XiaoAi", error); }
    }

    private void rememberService(Object service) {
        try {
            Object dialog = method(service.getClass(), "getWindow").invoke(service);
            if (dialog == null) return;
            Object window = method(dialog.getClass(), "getWindow").invoke(dialog);
            rememberWindow(window);
            if (hyperOs4 && window != null && keyboardWindow.get() == window) {
                gestureLayout = fitGestureNavigation(window);
            }
        } catch (Throwable error) { failure("input window", error); }
    }

    private static boolean fitGestureNavigation(Object window) throws ReflectiveOperationException {
        Object context = window.getClass().getMethod("getContext").invoke(window);
        Object resolver = context.getClass().getMethod("getContentResolver").invoke(context);
        Class<?> settings = Class.forName("android.provider.Settings$Global");
        Method getInt = settings.getMethod("getInt", Class.forName("android.content.ContentResolver"),
                String.class, Integer.TYPE);
        boolean gestures = (Integer) getInt.invoke(null, resolver, "force_fsg_nav_bar", 0) != 0;
        // Let the IME content reach the same bottom edge as HyperOS's bundled keyboard.
        // SystemUI still owns the gesture input region.
        window.getClass().getMethod("setDecorFitsSystemWindows", Boolean.TYPE).invoke(window, !gestures);
        if (gestures) {
            window.getClass().getMethod("setNavigationBarContrastEnforced", Boolean.TYPE).invoke(window, false);
        }
        return gestures;
    }

    private void rememberWindow(Object window) {
        if (window == null) return;
        try {
            Object attrs = method(window.getClass(), "getAttributes").invoke(window);
            // Never let a settings/login Activity's navigation bar recolor the keyboard.
            int type = field(attrs.getClass(), "type").getInt(attrs);
            if (type == 2011) keyboardWindow = new WeakReference<Object>(window);
        } catch (Throwable error) { failure("window type", error); }
    }

    private Handler main() {
        if (main == null) main = new Handler(Looper.getMainLooper());
        return main;
    }

    private synchronized void scheduleColor() {
        final Object window = keyboardWindow.get();
        // A dropped post would otherwise wedge refreshPending forever and mute every later refresh.
        boolean pending = refreshPending && System.currentTimeMillis() - refreshPendingAt < 3000;
        if (window == null || pending || Boolean.TRUE.equals(updating.get())) {
            return;
        }
        try {
            refreshPending = true;
            refreshPendingAt = System.currentTimeMillis();
            boolean posted = main().post(new Runnable() {
                public void run() {
                    synchronized (BottomHook.this) { refreshPending = false; }
                    if (keyboardWindow.get() != window) { scheduleColor(); return; }
                    updating.set(true);
                    try {
                        Object context = method(window.getClass(), "getContext").invoke(window);
                        int[] colors = palette.resolve(context);
                        method(framework, "customizeBottomViewColor", Boolean.TYPE, Integer.TYPE, Integer.TYPE, Integer.TYPE)
                                .invoke(null, true, colors[0], colors[1], colors[2]);
                        method(window.getClass(), "setNavigationBarColor", Integer.TYPE).invoke(window, colors[0]);
                        String value = String.format("bg=#%08x icon=#%08x pressed=#%08x", colors[0], colors[1], colors[2]);
                        if (!value.equals(lastPalette)) { lastPalette = value; log("SKIN " + value); }
                    } catch (Throwable error) { failure("skin palette", error); }
                    finally { updating.remove(); }
                }
            });
            if (!posted) refreshPending = false;
        } catch (Throwable error) { refreshPending = false; failure("post skin refresh", error); }
    }

    private static void hook(Class<?> owner, String name, XC_MethodHook callback) throws Throwable {
        int found = 0;
        for (Method m : owner.getDeclaredMethods()) {
            if (m.getName().equals(name)) { hookMethod(m, callback); found++; }
        }
        if (found == 0) throw new NoSuchMethodException(owner.getName() + "#" + name);
    }

    private static void hookMethod(Method m, XC_MethodHook callback) throws Throwable {
        if (!HOOKS.add(m)) return;
        try { m.setAccessible(true); XposedBridge.hookMethod(m, callback); log("HOOK " + m); }
        catch (Throwable error) { HOOKS.remove(m); throw error; }
    }

    private static Field field(Class<?> owner, String name) throws NoSuchFieldException {
        for (Class<?> c = owner; c != null; c = c.getSuperclass()) {
            try { Field f = c.getDeclaredField(name); f.setAccessible(true); return f; }
            catch (NoSuchFieldException absent) { /* search parent */ }
        }
        throw new NoSuchFieldException(owner.getName() + "#" + name);
    }

    private static Method method(Class<?> owner, String name, Class<?>... args) throws NoSuchMethodException {
        for (Class<?> c = owner; c != null; c = c.getSuperclass()) {
            try { Method m = c.getDeclaredMethod(name, args); m.setAccessible(true); return m; }
            catch (NoSuchMethodException absent) { /* search parent */ }
        }
        throw new NoSuchMethodException(owner.getName() + "#" + name);
    }

    private static void failure(String action, Throwable error) { log("FAIL " + action + ": " + error); }
    private static void log(String text) { XposedBridge.log("[SogouBottom] " + text); }
}
