import requests,pathlib,time
u='https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.12.1%2B1/OpenJDK21U-jre_x64_windows_hotspot_21.0.12.1_1.zip'
p=pathlib.Path('work/tools/jre.zip');r=requests.get(u,timeout=(15,45),stream=True);r.raise_for_status();print(r.headers.get('content-length'),flush=True)
with p.open('wb') as f:
 for c in r.iter_content(65536):f.write(c)
print('jre downloaded',p.stat().st_size,flush=True)
import zipfile
with zipfile.ZipFile(p) as z:z.extractall('work/tools/jre')
