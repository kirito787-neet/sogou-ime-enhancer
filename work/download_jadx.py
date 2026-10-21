import requests,pathlib,zipfile,time
u='https://github.com/skylot/jadx/releases/download/v1.5.6/jadx-1.5.6.zip?download=1';p=pathlib.Path('work/tools/jadx-ready.zip')
for i in range(3):
 try:
  r=requests.get(u+'&attempt='+str(i),timeout=(10,20));r.raise_for_status();p.write_bytes(r.content)
  with zipfile.ZipFile(p) as z:z.extractall('work/tools/jadx-ready')
  print('jadx ready',len(r.content),flush=True);break
 except Exception as e:print(type(e).__name__,str(e)[:120],flush=True)
