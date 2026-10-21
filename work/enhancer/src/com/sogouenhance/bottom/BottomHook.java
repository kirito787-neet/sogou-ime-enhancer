package com.sogouenhance.bottom;

import java.lang.reflect.Field;
import java.lang.reflect.Method;
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
            final Class<?> framework = injector;
            support(framework);
            disableXiaoAi(framework);
            hook(framework, "customizeBottomViewColor", new XC_MethodHook() {
                protected void beforeHookedMethod(MethodHookParam param) {
                    if (param.args.length == 4 && param.args[1] instanceof Integer) param.args[1] = 0;
                }
            });
            hook(framework, "addMiuiBottomView", new XC_MethodHook() {
                protected void afterHookedMethod(MethodHookParam param) {
                    try { color(framework); } catch (Throwable error) { failure("color", error); }
                }
            });
            try {
                hook(Class.forName("com.android.internal.policy.PhoneWindow"), "setNavigationBarColor",
                        new XC_MethodHook() {
                            protected void beforeHookedMethod(MethodHookParam param) {
                                if (param.args.length == 1) param.args[0] = 0;
                            }
                            protected void afterHookedMethod(MethodHookParam param) {
                                try { color(framework); } catch (Throwable error) { failure("window color", error); }
                            }
                        });
            } catch (Throwable error) { failure("navigation color", error); }
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

    private static void plugin(ClassLoader loader) throws Throwable {
        final Class<?> manager = Class.forName(MANAGER, false, loader);
        support(manager);
        disableXiaoAi(manager);
        filterListener(MANAGER + "$MiuiSwitchInputMethodListener", loader);
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

    private static void color(Class<?> owner) throws Throwable {
        Class<?> resources = Class.forName("android.content.res.Resources");
        Object system = resources.getMethod("getSystem").invoke(null);
        Object config = resources.getMethod("getConfiguration").invoke(system);
        boolean dark = (field(config.getClass(), "uiMode").getInt(config) & 48) == 32;
        int foreground = dark ? -657931 : -14671840;
        method(owner, "customizeBottomViewColor", Boolean.TYPE, Integer.TYPE, Integer.TYPE, Integer.TYPE)
                .invoke(null, true, 0, foreground, (foreground & 0xffffff) | 0x66000000);
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
