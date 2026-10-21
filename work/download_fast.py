import requests,pathlib,concurrent.futures,time,zipfile
root=pathlib.Path('work/tools');jobs=[('apktool-fast.jar','https://github.com/iBotPeaches/Apktool/releases/download/v3.0.3/apktool_3.0.3.jar',15478013),('jre-fast.zip','https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.12.1%2B1/OpenJDK21U-jre_x64_windows_hotspot_21.0.12.1_1.zip',48999141),('jadx-fast.zip','https://github.com/skylot/jadx/releases/download/v1.5.6/jadx-1.5.6.zip',72646741)]
def download(job):
 name,url,size=job;parts=root/(name+'.parts');parts.mkdir(exist_ok=True);step=1024*1024
 def part(i):
  start=i*step;end=min(size,start+step)-1;p=parts/str(i)
  if p.exists() and p.stat().st_size==end-start+1:return
  for attempt in range(3):
   try:
    r=requests.get(url,headers={'Range':f'bytes={start}-{end}'},stream=True,timeout=(15,45));r.raise_for_status()
    if r.status_code!=206 or not r.headers.get('Content-Range','').startswith(f'bytes {start}-'):raise ValueError('range mismatch '+str(r.headers))
    with p.open('wb') as f:
     for c in r.iter_content(65536):f.write(c)
    if p.stat().st_size!=end-start+1:raise ValueError('bad size')
    return
   except Exception:
    if attempt==2:raise
 with concurrent.futures.ThreadPoolExecutor(max_workers=16) as ex:list(ex.map(part,range((size+step-1)//step)))
 with (root/name).open('wb') as f:
  for i in range((size+step-1)//step):f.write((parts/str(i)).read_bytes())
 print(name,'done',size,flush=True)
 if name.endswith('.zip'):
  with zipfile.ZipFile(root/name) as z:z.extractall(root/name[:-4])
for j in jobs:download(j)
