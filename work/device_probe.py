import subprocess,json,pathlib
ADB=r'C:\Program Files\Netease\MuMuPlayer\nx_main\adb.exe'
cmds={
 'props':['shell','getprop'],
 'standard_package':['shell','pm','path','com.sohu.inputmethod.sogou'],
 'xiaomi_package':['shell','pm','path','com.sohu.inputmethod.sogou.xiaomi'],
 'framework':['shell','ls','/system/framework'],
 'system_ext_framework':['shell','ls','/system_ext/framework'],
 'product_framework':['shell','ls','/product/framework'],
 'permissions':['shell','ls','/system/etc/permissions'],
}
root=pathlib.Path('work/device')
for name,args in cmds.items():
 r=subprocess.run([ADB,'-s','df043723',*args],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=30)
 (root/(name+'.txt')).write_text(r.stdout+r.stderr,'utf8')
 if name=='props':
  print(name,'\n'.join(x for x in r.stdout.splitlines() if any(k in x for k in ['ro.miui','ro.build.version','ro.product.model','ro.product.device','ro.product.cpu.abi'])))
 else:print(name,r.returncode,r.stdout[:7000],r.stderr)
