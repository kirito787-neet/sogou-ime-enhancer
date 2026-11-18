package com.sogouenhance.bottom;

import de.robv.android.xposed.IXposedHookLoadPackage;
import de.robv.android.xposed.XC_MethodHook;
import de.robv.android.xposed.XposedBridge;
import de.robv.android.xposed.callbacks.XC_LoadPackage.LoadPackageParam;
import java.lang.reflect.Method;
import java.util.Collections;
import java.util.Set;
import java.util.WeakHashMap;

/** Suppresses only the gesture handle drawing while the phone's IME is visible. */
public final class GestureHandleHook implements IXposedHookLoadPackage {
    private static final String SYSTEM_UI = "com.android.systemui";
    private static final String HANDLE = SYSTEM_UI + ".navigationbar.gestural.NavigationHandle";
    private static final int DEFAULT_DISPLAY = 0;

    // NavigationBar callbacks and view drawing both run on SystemUI's main thread.
    private final Set<Object> handles = Collections.newSetFromMap(new WeakHashMap<Object, Boolean>());
    private boolean imeVisible;

    @Override
    public void handleLoadPackage(LoadPackageParam param) {
        if (!SYSTEM_UI.equals(param.packageName) || !SYSTEM_UI.equals(param.processName)) return;
        try {
            ClassLoader loader = param.classLoader;
            Class<?> handle = Class.forName(HANDLE, false, loader);
            Class<?> canvas = Class.forName("android.graphics.Canvas");
            Class<?> navBar = Class.forName(SYSTEM_UI + ".navigationbar.views.NavigationBar", false, loader);
            Method imeStatus = navBar.getDeclaredMethod("setImeWindowStatus",
                    Integer.TYPE, Integer.TYPE, Integer.TYPE, Boolean.TYPE);
            Method onDraw = handle.getDeclaredMethod("onDraw", canvas);
            Method getDisplay = handle.getMethod("getDisplay");
            Method invalidate = handle.getMethod("invalidate");
            Method displayId = Class.forName("android.view.Display").getMethod("getDisplayId");
            int visibleFlag = Class.forName("android.inputmethodservice.InputMethodService")
                    .getField("IME_VISIBLE").getInt(null);

            XC_MethodHook hideDrawing = new XC_MethodHook() {
                @Override
                protected void beforeHookedMethod(MethodHookParam call) throws ReflectiveOperationException {
                    Object view = call.thisObject;
                    Object display = getDisplay.invoke(view);
                    if (display == null || (Integer) displayId.invoke(display) != DEFAULT_DISPLAY) return;
                    handles.add(view);
                    if (imeVisible) call.setResult(null);
                }
            };
            XposedBridge.hookMethod(onDraw, hideDrawing);
            try {
                Class<?> rotatedHandle = Class.forName(
                        SYSTEM_UI + ".navigationbar.gestural.QuickswitchOrientedNavHandle", false, loader);
                XposedBridge.hookMethod(rotatedHandle.getDeclaredMethod("onDraw", canvas), hideDrawing);
            } catch (ClassNotFoundException | NoSuchMethodException absent) {
                // Some builds share the regular drawing method for both orientations.
            }
            XposedBridge.hookMethod(imeStatus, new XC_MethodHook() {
                @Override
                protected void afterHookedMethod(MethodHookParam call) throws ReflectiveOperationException {
                    if ((Integer) call.args[0] != DEFAULT_DISPLAY) return;
                    boolean visible = ((Integer) call.args[1] & visibleFlag) != 0;
                    if (imeVisible == visible) return;
                    imeVisible = visible;
                    for (Object view : handles) invalidate.invoke(view);
                }
            });
            XposedBridge.log("[SogouGestureHandle] READY");
        } catch (Throwable error) {
            XposedBridge.log("[SogouGestureHandle] Unavailable: " + error);
        }
    }
}
