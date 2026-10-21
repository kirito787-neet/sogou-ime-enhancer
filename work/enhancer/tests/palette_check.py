"""JVM behavior checks for skin resolution, alpha handling and contrast fallback."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'work/enhancer/tests'
JDK = ROOT/'work/tools/jdk/jdk-21.0.12.1+1/bin'
sources = {
    'test/State.java': '''package test;
public class State { public static int bg=0xffeeddcc, keyboard=0xffeeeeee, icon=0xff205080;
public static boolean defaults=false, special=false; }''',
    'android/content/Context.java': '''package android.content;
public class Context { public android.content.res.Resources getResources() { return new android.content.res.Resources(); } }''',
    'android/content/res/Resources.java': '''package android.content.res;
public class Resources { public static class Configuration { public int uiMode=16; }
public Configuration getConfiguration() { return new Configuration(); }
public int getColor(int id) { return 0xffedeff1; } }''',
    'com/sogou/theme/settings/a.java': '''package com.sogou.theme.settings;
public class a { public static a t() { return new a(); } public int f(int fallback) { return test.State.bg; } }''',
    'com/sohu/inputmethod/thememanager/h.java': '''package com.sohu.inputmethod.thememanager;
public class h { public static boolean f() { return test.State.defaults; } }''',
    'com/sogou/theme/impl/f.java': '''package com.sogou.theme.impl;
public class f { public static boolean m() { return test.State.special; } }''',
    'com/sohu/inputmethod/ui/s.java': '''package com.sohu.inputmethod.ui;
public class s { public static int c() { return test.State.keyboard; }
public static int g(android.content.Context c) { return test.State.keyboard; }
public static int h() { return test.State.icon; } }''',
    'com/sohu/inputmethod/ui/d.java': '''package com.sohu.inputmethod.ui;
public class d { public static int k(int color, boolean text) { return color; } }''',
    'com/sogouenhance/bottom/PaletteCheck.java': '''package com.sogouenhance.bottom;
public class PaletteCheck {
 private static int checks;
 private static void expect(boolean value, String message) { checks++; if (!value) throw new AssertionError(message); }
 public static void main(String[] args) throws Throwable {
  SkinPalette p=new SkinPalette(PaletteCheck.class.getClassLoader());
  Object context=new android.content.Context();
  int[] first=p.resolve(context);
  expect(first[0]==0xffeeddcc, "skin background must survive");
  expect(first[1]==0xff205080, "readable skin accent must survive");
  test.State.bg=0xff102030;
  int[] second=p.resolve(context);
  expect(second[0]==0xff102030, "skin changes must not use a cached palette");
  expect(SkinPalette.contrast(second[0],second[1])>=3, "dark-skin icon needs contrast");
  test.State.bg=0x80ff0000; test.State.keyboard=0xffffffff;
  expect(p.resolve(context)[0]==0xffff7f7f, "semi-transparent skin must composite over keyboard");
  test.State.bg=0; test.State.keyboard=0xff345678; test.State.icon=Integer.MAX_VALUE;
  int[] transparent=p.resolve(context);
  expect(transparent[0]==0xff345678, "transparent navigation must use skin background");
  expect(SkinPalette.contrast(transparent[0],transparent[1])>=3, "missing icon must be readable");
  test.State.defaults=true; test.State.bg=0xffff0000;
  expect(p.resolve(context)[0]==0xff345678, "default skin uses its native theme-color resolver");
  test.State.defaults=false; test.State.special=true;
  expect(p.resolve(context)[0]==0xff345678, "special skin uses native smart background");
  expect(Math.abs(SkinPalette.contrast(0xff000000,0xffffffff)-21)<0.001, "contrast reference");
  expect((p.resolve(context)[2]>>>24)==0x66, "pressed icon has intentional state alpha");
  System.out.println("PASS "+checks+" skin palette behavior checks");
 }
}'''
}
for name, source in sources.items():
    path=BASE/'fixtures'/name
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(source,encoding='utf-8')
out=BASE/'classes'
out.mkdir(exist_ok=True)
subprocess.run([str(JDK/'javac.exe'),'-encoding','UTF-8','-d',str(out),
    str(ROOT/'work/enhancer/src/com/sogouenhance/bottom/SkinPalette.java'),
    *map(str,(BASE/'fixtures').rglob('*.java'))],check=True)
subprocess.run([str(JDK/'java.exe'),'-cp',str(out),'com.sogouenhance.bottom.PaletteCheck'],check=True)
