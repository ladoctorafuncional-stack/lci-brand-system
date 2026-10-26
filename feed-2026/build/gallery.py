import os,re,glob,json,io,base64,shutil
from PIL import Image
SC='/tmp/claude-0/-home-user/509530f3-5d9a-5ff9-a427-b43b2f4fa3e1/scratchpad/feed-lci-2026.html'
REPO='/home/user/lci-brand-system/feed-2026'
ns={}; src=open('package.py').read()
exec(src.split("PA=''")[0].split("rows=[]")[0],ns)
cal,live=ns['cal'],ns['live']
for L in ('EN','ES'):
    shutil.rmtree(f'{REPO}/{L}',ignore_errors=True)
    for f in glob.glob(f'FEED_LCI/{L}/*/*.png'):
        p=f.split('/'); o=f'{REPO}/{L}/{p[-2]}/{p[-1][:-4]}.jpg'; os.makedirs(os.path.dirname(o),exist_ok=True)
        Image.open(f).convert('RGB').save(o,quality=80,optimize=True)
for g in ('grid_EN.jpg','grid_ES.jpg','README.md'): shutil.copy('FEED_LCI/'+g,REPO+'/'+g)
data={}
def thumb(f):
    im=Image.open(f).convert('RGB').resize((520,650),Image.LANCZOS); b=io.BytesIO(); im.save(b,'JPEG',quality=68,optimize=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
for L in ('EN','ES'):
    items=[]
    for i,(d,slug,note) in enumerate(cal,1):
        if slug:
            fs=sorted(glob.glob(f'FEED_LCI/{L}/{i:02d}_{d}_{slug}/*.png'))
            items.append({'d':d.replace('-','/'),'slug':slug,'files':[thumb(f) for f in fs]})
        else: items.append({'d':d.replace('-','/'),'slug':None,'note':note})
    data[L]={'items':items,'live':live}
h=open(SC).read()
h=re.sub(r"const D=.*?;\nlet L",lambda m:"const D="+json.dumps(data,ensure_ascii=False)+";\nlet L",h,flags=re.S)
open(SC,'w').write(h); print(len(h)/1e6)
