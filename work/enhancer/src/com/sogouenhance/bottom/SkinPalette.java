package com.sogouenhance.bottom;

import java.lang.reflect.Field;
import java.lang.reflect.Method;

/** Reads Sogou 2620's own skin values; no pixel sampling or global ROM changes. */
final class SkinPalette {
    private final ClassLoader loader;

    SkinPalette(ClassLoader loader) { this.loader = loader; }

    int[] resolve(Object context) throws Throwable {
        Object resources = call(context, "getResources");
        Object configuration = call(resources, "getConfiguration");
        Field mode = configuration.getClass().getField("uiMode");
        boolean dark = (mode.getInt(configuration) & 48) == 32;
        int fallback = dark ? 0xff222222 : 0xffedeff1;
        // Match the app's default navigation-bar resource rather than a fixed light-only color.
        try { fallback = (Integer) call(resources, "getColor", new Class<?>[] {Integer.TYPE}, 0x7f06048c); }
        catch (Throwable unavailable) { /* fallback for a future app version */ }

        Object settings = invoke("com.sogou.theme.settings.a", "t");
        int background = (Integer) call(settings, "f", new Class<?>[] {Integer.TYPE}, fallback);
        Class<?> contextType = Class.forName("android.content.Context");
        if (Boolean.TRUE.equals(invoke("com.sohu.inputmethod.thememanager.h", "f"))) {
            background = (Integer) invoke("com.sohu.inputmethod.ui.s", "c");
        } else if (Boolean.TRUE.equals(invoke("com.sogou.theme.impl.f", "m"))) {
            background = (Integer) invoke("com.sohu.inputmethod.ui.s", "g",
                    new Class<?>[] {contextType}, context);
        }
        // Apply the same dark-mode/skin color conversion used by the input method itself.
        background = (Integer) invoke("com.sohu.inputmethod.ui.d", "k",
                new Class<?>[] {Integer.TYPE, Boolean.TYPE}, background, false);
        if ((background >>> 24) < 255) {
            int keyboardBackground;
            try { keyboardBackground = (Integer) invoke("com.sohu.inputmethod.ui.s", "g",
                    new Class<?>[] {contextType}, context); }
            catch (Throwable unavailable) { keyboardBackground = fallback; }
            background = composite(background, composite(keyboardBackground, fallback));
        }
        int icon;
        try { icon = (Integer) invoke("com.sohu.inputmethod.ui.s", "h"); }
        catch (Throwable unavailable) { icon = 0; }
        // h() can return a sentinel if a skin does not declare an icon/text color.
        if (icon == Integer.MAX_VALUE || icon == Integer.MIN_VALUE || (icon >>> 24) == 0) {
            icon = readable(background);
        } else {
            icon = (Integer) invoke("com.sohu.inputmethod.ui.d", "k",
                    new Class<?>[] {Integer.TYPE, Boolean.TYPE}, icon | 0xff000000, false);
            if (contrast(background, icon) < 3.0) icon = readable(background);
        }
        return new int[] {background | 0xff000000, icon | 0xff000000,
                (icon & 0xffffff) | 0x66000000};
    }

    private Object invoke(String name, String method) throws Throwable {
        return invoke(name, method, new Class<?>[0]);
    }

    private Object invoke(String name, String method, Class<?>[] args, Object... values) throws Throwable {
        return Class.forName(name, true, loader).getDeclaredMethod(method, args).invoke(null, values);
    }

    private static Object call(Object owner, String name) throws Throwable {
        return call(owner, name, new Class<?>[0]);
    }

    private static Object call(Object owner, String name, Class<?>[] types, Object... values) throws Throwable {
        Method method = owner.getClass().getMethod(name, types);
        method.setAccessible(true);
        return method.invoke(owner, values);
    }

    static int composite(int color, int background) {
        int alpha = color >>> 24;
        int red = (((color >>> 16) & 255) * alpha + ((background >>> 16) & 255) * (255-alpha) + 127) / 255;
        int green = (((color >>> 8) & 255) * alpha + ((background >>> 8) & 255) * (255-alpha) + 127) / 255;
        int blue = ((color & 255) * alpha + (background & 255) * (255-alpha) + 127) / 255;
        return 0xff000000 | (red << 16) | (green << 8) | blue;
    }

    static int readable(int background) {
        return contrast(background, 0xfff5f5f5) > contrast(background, 0xff202020)
                ? 0xfff5f5f5 : 0xff202020;
    }

    static double contrast(int first, int second) {
        double a = luminance(first), b = luminance(second);
        return (Math.max(a, b)+0.05) / (Math.min(a, b)+0.05);
    }

    private static double luminance(int color) {
        return 0.2126 * linear((color >>> 16) & 255)
                + 0.7152 * linear((color >>> 8) & 255) + 0.0722 * linear(color & 255);
    }

    private static double linear(int value) {
        double normalized = value / 255.0;
        return normalized <= 0.04045 ? normalized/12.92 : Math.pow((normalized+0.055)/1.055, 2.4);
    }
}
