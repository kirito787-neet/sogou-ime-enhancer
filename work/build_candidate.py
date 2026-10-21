from pathlib import Path
import hashlib,json,re,zipfile,subprocess,secrets
root=Path.cwd();out=root/'outputs';out.mkdir(exist_ok=True);work=root/'work';sign=work/'signing';sign.mkdir(exist_ok=True)
source=root/'搜狗输入法.apk';dex=work/'ads/classes3.dex';unsigned=work/'sogou-ad-switches-unsigned.apk'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='df10256e9228e9ed3831be4278a7b9046dd16b0e045d68dee8baafa2491c1574'
assert hashlib.sha256(dex.read_bytes()).hexdigest()=='9c8860775d6a5a24997183c662562bdd4fdfe159790e278dde6ef02b2fc5ffff'
with zipfile.ZipFile(source) as src,zipfile.ZipFile(unsigned,'w') as dst:
 dst.comment=src.comment
 for item in src.infolist():
  if re.match(r'^META-INF/(?:[^/]+\.(?:SF|RSA|DSA|EC)|MANIFEST\.MF)$',item.filename,re.I):continue
  dst.writestr(item,dex.read_bytes() if item.filename=='classes3.dex' else src.read(item.filename))
java=next((work/'tools/zulu-jre').glob('*/bin/java.exe'));keytool=java.with_name('keytool.exe');meta=sign/'local-key.json';ks=sign/'local-test.p12'
if not meta.exists():meta.write_text(json.dumps({'alias':'sogou-local-test','password':secrets.token_urlsafe(24)}),'utf8')
m=json.loads(meta.read_text());props=['-Djava.io.tmpdir='+str(work/'tmp'),'-Duser.home='+str(work/'tool-home')]
if not ks.exists():
 r=subprocess.run([str(keytool),*['-J'+x for x in props],'-genkeypair','-alias',m['alias'],'-keyalg','RSA','-keysize','2048','-validity','3650','-dname','CN=Local Sogou Test Build','-storetype','PKCS12','-keystore',str(ks),'-storepass',m['password'],'-keypass',m['password']],capture_output=True,text=True,encoding='utf8',errors='replace')
 assert r.returncode==0,r.stderr
r=subprocess.run([str(java),*props,'-jar',str(work/'tools/signer.jar'),'-a',str(unsigned),'-o',str(work/'signed'), '--ks',str(ks),'--ksAlias',m['alias'],'--ksPass',m['password'],'--ksKeyPass',m['password']],capture_output=True,text=True,encoding='utf8',errors='replace')
(work/'candidate-signature.log').write_text(r.stdout+r.stderr,'utf8');print(r.stdout[-2500:]);assert r.returncode==0,r.stderr
signed=next((work/'signed').glob('*-signed.apk'));target=out/'sogou-20.17-ad-switches-TEST.apk';target.write_bytes(signed.read_bytes())
with zipfile.ZipFile(source) as a,zipfile.ZipFile(target) as b:
 names=[n for n in a.namelist() if not re.match(r'^META-INF/(?:[^/]+\.(?:SF|RSA|DSA|EC)|MANIFEST\.MF)$',n,re.I)]
 changes=[n for n in names if a.read(n)!=b.read(n)]
 assert changes==['classes3.dex'],changes
report={'apk':target.name,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'changed_payloads':changes,'original_apk_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'signature':'local test certificate, not official','runtime':'not yet tested','full_miui_integration':'not implemented in this ad-only candidate'}
(out/'candidate-validation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),'utf8');print(json.dumps(report,indent=2))
