package com.sogouenhance.bottom;

import java.lang.reflect.Method;
import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XposedBridge;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;

/** Embedded variant only. Keeps the known first-install JNI abort out of startup. */
public final class EmbeddedGuard implements IXposedHookLoadPackage {
    public void handleLoadPackage(LoadPackageParam p) {
        if (!"com.sohu.inputmethod.sogou".equals(p.packageName)
                && !"com.sohu.inputmethod.sogou.enhanced".equals(p.packageName)) return;
        try {
            Method lookup = Class.forName("android.content.res.Resources").getDeclaredMethod(
                    "getIdentifier", String.class, String.class, String.class);
            XposedBridge.hookMethod(lookup, new XC_MethodHook() {
                protected void beforeHookedMethod(MethodHookParam param) {
                    if ("com.sohu.inputmethod.sogou.enhanced".equals(param.args[2])) {
                        param.args[2] = "com.sohu.inputmethod.sogou";
                    }
                    if (param.args[0] instanceof String) {
                        String name = (String) param.args[0];
                        if (name.startsWith("com.sohu.inputmethod.sogou.enhanced:")) {
                            param.args[0] = "com.sohu.inputmethod.sogou:" + name.substring(name.indexOf(':')+1);
                        }
                    }
                }
            });
            XposedBridge.log("[SogouEmbedded] resource package lookup compatibility installed");
        } catch (Throwable error) { XposedBridge.log("[SogouEmbedded] resource hook failed: " + error); }
        for (String name : new String[] {"IMECoreInterface", "IMENativeInterface"}) {
            try {
                Class<?> owner = Class.forName("com.sogou.core.input.chinese.engine.engine." + name,
                        false, p.classLoader);
                Method m = owner.getDeclaredMethod("setFirstInstallTime", Long.TYPE);
                if (m.getReturnType() != Boolean.TYPE) throw new NoSuchMethodException("return type");
                XposedBridge.hookMethod(m, new XC_MethodHook() {
                    protected void beforeHookedMethod(MethodHookParam param) {
                        param.setResult(true);
                        XposedBridge.log("[SogouEmbedded] first-install guard HIT");
                    }
                });
                XposedBridge.log("[SogouEmbedded] guard installed " + name);
            } catch (Throwable error) { XposedBridge.log("[SogouEmbedded] guard failed " + name + ": " + error); }
        }
    }
}
