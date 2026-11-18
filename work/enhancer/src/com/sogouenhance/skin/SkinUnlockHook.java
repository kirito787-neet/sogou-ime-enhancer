package com.sogouenhance.skin;

import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XposedBridge;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;

/**
 * Skin entitlement for the 20.17.0 (2620) code base.
 *
 * Three touch points, all client-local:
 *
 * 1. Paid state. SmartThemeSkinDetailActivity#T2 / #E2 bind the detail model to
 *    the page; the shop decides "owned" from fields on that model. Forcing
 *    payment=1, vipOnly="0", newVipType=0 makes the store hand out the package
 *    instead of opening the cashier.
 *
 * 2. Purchase safety net. If a purchase path still starts, pay.e#d(u) is the
 *    single funnel (i.h / i.j both create pay.e and call it). For a skin page it
 *    answers callback code 0 - the Midas success value - and skips the original,
 *    so no order is created and no WeChat/Midas cashier is opened.
 *
 * 3. Download host. 20.17.0 still points at download.sginput.qq.com, which now
 *    answers 404; the same interface is served by srv.android.shouji.sogou.com.
 *    com.sogou.theme.network.b#e builds the GET request, so the host is rewritten
 *    before the request is created.
 *
 * Scope: skin pages only (com.sogou.theme.*, com.sogou.home.costume.*) plus the
 * skin asset types 2001/2012/2041/2042/2023/2027/6041/6042, so fonts, emoji,
 * wallpapers, VIP and phrases keep the stock behaviour.
 */
public final class SkinUnlockHook implements IXposedHookLoadPackage {
    private static final String[] SKIN_ACTIVITY_PREFIXES = {"com.sogou.theme.", "com.sogou.home.costume."};
    private static final Set<String> SKIN_ASSET_TYPES = Collections.unmodifiableSet(new HashSet<String>(
            Arrays.asList("2001", "2012", "2023", "2027", "2041", "2042", "6041", "6042")));
    private static final Set<String> GRANTED = Collections.synchronizedSet(new HashSet<String>());

    private static final String DEAD_HOST = "download.sginput.qq.com";
    private static final String LIVE_HOST = "srv.android.shouji.sogou.com";

    private static Method assetTypeOf;
    private static Method assetIdOf;
    private static Method firstProductOf;
    private static Method coordinatorOf;   // pay.e#a() -> pay.d
    private static Method activityOf;      // pay.d#a() -> Activity
    private static Field payInfoOf;
    private static Field paymentOf;
    private static Field vipOnlyOf;
    private static Field newVipTypeOf;

    public void handleLoadPackage(LoadPackageParam p) {
        if (!"com.sohu.inputmethod.sogou".equals(p.packageName)
                && !"com.sohu.inputmethod.sogou.enhanced".equals(p.packageName)) return;
        try {
            Class<?> model = Class.forName("com.sogou.home.theme.bean.SmartThemeDetailModel", false, p.classLoader);
            paymentOf = model.getField("payment");
            vipOnlyOf = model.getField("vipOnly");
            newVipTypeOf = model.getField("newVipType");
            hookDetailState(p.classLoader);

            Class<?> product = Class.forName("com.sogou.bu.basic.pay.ProductWithPrice", false, p.classLoader);
            assetTypeOf = product.getMethod("getAssetType");
            assetIdOf = product.getMethod("getAssetId");
            hookMethod(product.getMethod("getPayStatus"), new XC_MethodHook() {
                protected void afterHookedMethod(MethodHookParam param) {
                    String id = assetId(param.thisObject);
                    if (id == null || !GRANTED.contains(id)) return;
                    param.setResult("1");
                }
            });
            log("hook getPayStatus ok");

            Class<?> payInfo = Class.forName("com.sogou.bu.basic.pay.PayInfoBean", false, p.classLoader);
            firstProductOf = payInfo.getMethod("getFirstProduct");
            Class<?> coordinator = Class.forName("com.sogou.inputmethod.pay.e", false, p.classLoader);
            payInfoOf = coordinator.getDeclaredField("b");
            payInfoOf.setAccessible(true);
            coordinatorOf = coordinator.getMethod("a");
            Class<?> request = Class.forName("com.sogou.inputmethod.pay.d", false, p.classLoader);
            activityOf = request.getMethod("a");
            Class<?> callback = Class.forName("com.sogou.inputmethod.pay.midas.u", false, p.classLoader);
            hookMethod(coordinator.getDeclaredMethod("d", callback), new XC_MethodHook() {
                protected void beforeHookedMethod(MethodHookParam param) {
                    try {
                        Object info = payInfoOf.get(param.thisObject);
                        if (info == null) return;
                        Object product = firstProductOf.invoke(info);
                        String activity = activityName(param.thisObject);
                        if (!isSkinActivity(activity) && !isSkinProduct(product)) return;
                        Object target = param.args[0];
                        if (target == null) return;
                        // Same contract as the native success path: code 0 means paid.
                        Method success = target.getClass().getMethod("a", Integer.TYPE, String.class);
                        success.invoke(target, 0, "");
                        String id = assetId(product);
                        if (id != null) GRANTED.add(id);
                        log("PAY-BYPASS type=" + assetType(product) + " id=" + id + " activity=" + activity);
                        param.setResult(null);
                    } catch (Throwable error) {
                        log("PAY-BYPASS failed: " + error);
                    }
                }
            });
            log("hook pay coordinator ok");

            hookDownloadHost(p.classLoader);
        } catch (Throwable error) {
            log("install failed: " + error);
        }
    }

    /** Forces the "owned" state on the detail model that the store binds to the page. */
    private static void hookDetailState(ClassLoader cl) throws Throwable {
        Class<?> model = Class.forName("com.sogou.home.theme.bean.SmartThemeDetailModel", false, cl);
        Class<?> detail = Class.forName("com.sogou.theme.SmartThemeSkinDetailActivity", false, cl);
        for (final String name : new String[] {"T2", "E2"}) {
            final Method m = detail.getDeclaredMethod(name, model);
            hookMethod(m, new XC_MethodHook() {
                protected void beforeHookedMethod(MethodHookParam param) {
                    try { markOwned(param.args[0]); }
                    catch (Throwable error) { log("markOwned failed in " + name + ": " + error); }
                }
            });
        }
        Class<?> preview = Class.forName("com.sogou.theme.ThemePreviewActivity", false, cl);
        Class<?> item = Class.forName("com.sohu.inputmethod.publish.ThemePreviewItem", false, cl);
        hookMethod(preview.getDeclaredMethod("L2", item), new XC_MethodHook() {
            protected void beforeHookedMethod(MethodHookParam param) {
                try {
                    Object value = param.args[0];
                    for (Field f : value.getClass().getDeclaredFields()) {
                        if (f.getType() != Class.forName("com.sogou.home.theme.bean.SmartThemeDetailModel")) continue;
                        f.setAccessible(true);
                        markOwned(f.get(value));
                    }
                } catch (Throwable ignored) { }
            }
        });
        log("hook detail state ok");
    }

    private static void markOwned(Object model) throws IllegalAccessException {
        if (model == null) return;
        paymentOf.setInt(model, 1);
        vipOnlyOf.set(model, "0");
        newVipTypeOf.setInt(model, 0);
    }

    /** 20.17.0 still requests the dead host; the same endpoint lives on the other one. */
    private static void hookDownloadHost(ClassLoader cl) throws Throwable {
        Class<?> network = Class.forName("com.sogou.theme.network.b", false, cl);
        Class<?> callback = Class.forName("com.home.common.g", false, cl);
        hookMethod(network.getDeclaredMethod("e", String.class, String.class, Integer.TYPE, callback),
                new XC_MethodHook() {
            protected void beforeHookedMethod(MethodHookParam param) {
                Object url = param.args[0];
                if (!(url instanceof String)) return;
                String value = (String) url;
                if (!value.contains(DEAD_HOST)) return;
                String fixed = value.replace(DEAD_HOST, LIVE_HOST);
                param.args[0] = fixed;
                log("DL-HOST " + value + " -> " + fixed);
            }
        });
        log("hook download host ok");
    }

    private static String activityName(Object coordinator) {
        try {
            Object request = coordinatorOf.invoke(coordinator);
            Object activity = activityOf.invoke(request);
            return activity == null ? null : activity.getClass().getName();
        } catch (Throwable ignored) {
            return null;
        }
    }

    private static boolean isSkinActivity(String activity) {
        if (activity == null) return false;
        for (String prefix : SKIN_ACTIVITY_PREFIXES) if (activity.startsWith(prefix)) return true;
        return false;
    }

    private static boolean isSkinProduct(Object product) {
        if (product == null || assetTypeOf == null) return false;
        try {
            return SKIN_ASSET_TYPES.contains((String) assetTypeOf.invoke(product));
        } catch (Throwable ignored) {
            return false;
        }
    }

    private static String assetType(Object product) {
        try { return String.valueOf(assetTypeOf.invoke(product)); } catch (Throwable ignored) { return "?"; }
    }

    private static String assetId(Object product) {
        if (product == null || assetIdOf == null) return null;
        try { return (String) assetIdOf.invoke(product); } catch (Throwable ignored) { return null; }
    }

    private static void hookMethod(Method m, XC_MethodHook callback) throws Throwable {
        m.setAccessible(true);
        XposedBridge.hookMethod(m, callback);
    }

    private static void log(String text) { XposedBridge.log("[SogouSkin] " + text); }
}
