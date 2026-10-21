import requests,concurrent.futures,pathlib,hashlib,zipfile
root=pathlib.Path('work/tools')
jobs=[('apktool.jar','https://github.com/iBotPeaches/Apktool/releases/download/v3.0.3/apktool_3.0.3.jar'),('jadx.zip','https://github.com/skylot/jadx/releases/download/v1.5.6/jadx-1.5.6.zip'),('signer.jar','https://github.com/patrickfav/uber-apk-signer/releases/download/v1.3.0/uber-apk-signer-1.3.0.jar'),('jdk.zip','https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.12.1%2B1/OpenJDK21U-jdk_x64_windows_hotspot_21.0.12.1_1.zip')]
def get(job):
 name,url=job;p=root/name
 if not p.exists():
  r=requests.get(url,timeout=(20,90),stream=True);r.raise_for_status()
  with p.open('wb') as f:
   for chunk in r.iter_content(1024*1024):f.write(chunk)
 print(name,p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest(),flush=True)
 if name in ['jdk.zip','jadx.zip']:
  out=root/name[:-4];out.mkdir(exist_ok=True)
  with zipfile.ZipFile(p) as z:z.extractall(out)
 return name
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(get,jobs))
