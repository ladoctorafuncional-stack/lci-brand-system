import os, sys; sys.path.insert(0,'/mnt/skills/user/lci-design-system/assets')
import lci_treat as T
from PIL import Image
import base64, io

U='/mnt/user-data/uploads/'
def emb(fn, mode, W, q=82, **kw):
    im=Image.open(U+fn)
    t=T.treat(im, mode=mode, **kw)
    w,h=t.size; t=t.resize((W,int(h*W/w)), Image.LANCZOS)
    b=io.BytesIO(); t.convert('RGB').save(b,'JPEG',quality=q,optimize=True)
    return base64.b64encode(b.getvalue()).decode()

assets={
 'hero':  emb('1782128440758_image.png','grade',1500, vignette=0.22, contrast=0.12),
 'band':  emb('1782128542676_image.png','grade',1400, vignette=0.16),
 'market':emb('1782129009343_image.png','grade',1400, vignette=0.18),
}
import json
json.dump(assets, open('embeds.json','w'))
for k,v in assets.items(): print(k, round(len(v)/1024), 'KB b64')
