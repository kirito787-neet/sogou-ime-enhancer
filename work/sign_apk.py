from pathlib import Path
import zipfile,subprocess,json,sys,hashlib
root=Path.cwd();work=root/'work';java=next((work/'tools/zulu-jre').glob('*/bin/java.exe'));m=json.loads((work/'signing/local-key.json').read_text());ks=work/'signing/local-test.p12'
source=Path(sys.argv[1]);dest=Path(sys.argv[2]);tag=dest.stem;staging=work/'signed'/tag;staging.mkdir(parents=True,exist_ok=True)
r=subprocess.run([str(java),'-Djava.io.tmpdir='+str(work/'tmp'),'-Duser.home='+str(work/'tool-home'),'-jar',str(work/'tools/signer.jar'),'-a',str(source.resolve()),'-o',str(staging),'--ks',str(ks),'--ksAlias',m['alias'],'--ksPass',m['password'],'--ksKeyPass',m['password']],capture_output=True,text=True,encoding='utf8',errors='replace')
(work/(tag+'-sign.log')).write_text(r.stdout+r.stderr,'utf8');assert r.returncode==0,r.stdout+r.stderr
signed=list(staging.glob('*-signed.apk'));assert len(signed)==1
assert 'signature verified' in r.stdout and 'zipalign verified' in r.stdout,r.stdout
dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(signed[0].read_bytes());print(dest,hashlib.sha256(dest.read_bytes()).hexdigest());print(r.stdout[-1100:])
