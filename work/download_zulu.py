import requests,pathlib,zipfile
p=pathlib.Path('work/tools/zulu-jre.zip');u='https://cdn.azul.com/zulu/bin/zulu21.52.203-ca-jre21.0.12.1-win_x64.zip'
r=requests.get(u,timeout=(15,30),stream=True);r.raise_for_status();print(r.headers.get('content-length'),flush=True)
with p.open('wb') as f:
 for c in r.iter_content(65536):f.write(c)
print('downloaded',p.stat().st_size,flush=True)
with zipfile.ZipFile(p) as z:z.extractall('work/tools/zulu-jre')
