# fondos nuevos LCI: mesh gradient, galaxia/nebulosa, malla triangulada. Solo colores de marca.
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
from scipy.ndimage import map_coordinates, gaussian_filter
from scipy.spatial import Delaunay
def hx(h): h=h.lstrip('#'); return np.array([int(h[i:i+2],16) for i in (0,2,4)])/255.
NAVY,INK,DEEP,STEEL,SLATE,BLUE,ICE,WHITE,GOLD=map(hx,['#2A3649','#141C2A','#0E1522','#5D768C','#9FB2C6','#CAD3DD','#E6ECF2','#F7F9FB','#D2B58A'])
def _rs(a,W,H): 
    im=Image.fromarray((np.clip(a,0,1)*255).astype(np.uint8)); return np.asarray(im.resize((W,H),Image.BICUBIC)).astype(float)/255.
def fbm(W,H,rng,oct=5,base=3,pers=.5):
    out=np.zeros((H,W)); amp=1; tot=0
    for o in range(oct):
        n=base*2**o; a=rng.random((max(2,int(n*H/W))+2,n+2))
        out+=amp*_rs(a,W,H)[:,:,0] if _rs(a,W,H).ndim==3 else amp*_rs(a,W,H)
        tot+=amp; amp*=pers
    out/=tot; return (out-out.min())/(out.max()-out.min())
def grano(a,rng,g=.02):
    n=rng.normal(0,g,a.shape[:2])[:,:,None]; return a+n
def mesh(W,H,grid,seed=1,warp=140,g=.018):
    rng=np.random.default_rng(seed); g_=np.array([[hx(c) if isinstance(c,str) else c for c in row] for row in grid])
    r,c,_=g_.shape
    big=np.stack([_rs(g_[:,:,k],W,H) if False else np.asarray(Image.fromarray((g_[:,:,k]*255).astype(np.uint8)).resize((W,H),Image.BICUBIC)).astype(float)/255. for k in range(3)],-1)
    yy,xx=np.mgrid[0:H,0:W].astype(float)
    dx=(fbm(W,H,rng,2,2)-.5)*warp*2; dy=(fbm(W,H,rng,2,2)-.5)*warp*2
    out=np.stack([map_coordinates(big[:,:,k],[np.clip(yy+dy,0,H-1),np.clip(xx+dx,0,W-1)],order=1,mode='nearest') for k in range(3)],-1)
    return grano(out,rng,g)
def estrellas(W,H,rng,n=420,glow=1.0):
    lay=np.zeros((H,W))
    xs=rng.integers(0,W,n); ys=rng.integers(0,H,n); br=rng.power(.35,n)**3
    for x,y,b in zip(xs,ys,br): lay[y,x]=max(lay[y,x],b)
    core=lay.copy(); h1=gaussian_filter(lay,1.1)*7*glow; h2=gaussian_filter(lay,5)*40*glow
    return np.clip(core*1.0+h1+h2,0,1)
def galaxia(W,H,seed=1,tono='azul',giro=3.2,centro=(.62,.38),estr=1.0):
    rng=np.random.default_rng(seed)
    yy,xx=np.mgrid[0:H,0:W].astype(float); cx,cy=centro[0]*W,centro[1]*H
    x=(xx-cx)/W; y=(yy-cy)/W; r=np.sqrt(x*x+y*y)+1e-6; th=np.arctan2(y,x)+giro*np.log(r*6+1)
    xr=r*np.cos(th)*W+W/2; yr=r*np.sin(th)*W+H/2
    n1=fbm(W,H,rng,6,3); n2=fbm(W,H,rng,5,5)
    def samp(a): return map_coordinates(a,[np.clip(yr,0,H-1),np.clip(xr,0,W-1)],order=1,mode='mirror')
    neb=samp(n1)*.65+samp(n2)*.35
    neb=np.clip((neb-.38)*2.3,0,1)**1.4
    core=np.exp(-(r/ .28)**2)
    dens=np.clip(neb*(.45+1.1*core),0,1)
    base=INK[None,None,:]*(1-yy[:,:,None]/H*.5)+DEEP[None,None,:]*(yy[:,:,None]/H*.5)
    pal=[(0,INK),(.35,NAVY),(.7,STEEL),(1,BLUE)]
    col=np.zeros((H,W,3))
    for (a,ca),(b,cb) in zip(pal[:-1],pal[1:]):
        m=(dens>=a)&(dens<=b); t=((dens-a)/(b-a))[m][:,None]; col[m]=ca*(1-t)+cb*t
    col=col*dens[:,:,None]*1.15+base*(1-dens[:,:,None]*.7)
    if tono=='oro': col+=GOLD[None,None,:]*(core**2*dens*.35)[:,:,None]
    st=estrellas(W,H,rng,int(520*estr))
    col=col+st[:,:,None]*np.array([.85,.9,1.0])
    vig=1-.35*((xx/W-.5)**2+(yy/H-.5)**2)*2.2
    return grano(col*vig[:,:,None],rng,.016)
def malla(W,H,seed=1,focal=(.7,.3),nx=9,ny=13,claro=False,fondo=None,inten=1.0):
    rng=np.random.default_rng(seed)
    if fondo is None: fondo=mesh(W,H,[[DEEP,NAVY,STEEL*.7],[INK,NAVY*1.1,NAVY],[DEEP,INK,NAVY]],seed,100)
    S=2; im=Image.new('RGBA',(W*S,H*S),(0,0,0,0)); d=ImageDraw.Draw(im)
    pts=[]
    for j in range(ny+1):
        for i in range(nx+1):
            pts.append(((i+.5*(j%2)+rng.uniform(-.38,.38))/nx*W*1.05-W*.03,(j+rng.uniform(-.38,.38))/ny*H*1.04-H*.02))
    pts=np.array(pts); tri=Delaunay(pts); fx,fy=focal[0]*W,focal[1]*H
    col=(202,211,221) if not claro else (42,54,73)
    seen=set()
    for s in tri.simplices:
        for a,b in ((s[0],s[1]),(s[1],s[2]),(s[2],s[0])):
            k=(min(a,b),max(a,b))
            if k in seen: continue
            seen.add(k); m=(pts[a]+pts[b])/2; dist=np.hypot(m[0]-fx,m[1]-fy)/np.hypot(W,H)
            al=int(255*np.clip((.34*np.exp(-(dist/.42)**2)+.05)*inten,0,.4))
            d.line([tuple(pts[a]*S),tuple(pts[b]*S)],fill=col+(al,),width=2)
    for p in pts:
        dist=np.hypot(p[0]-fx,p[1]-fy)/np.hypot(W,H); al=int(255*np.clip((.9*np.exp(-(dist/.36)**2)+.12)*inten,0,1)); r=int((3+5*np.exp(-(dist/.3)**2))*(.5+.5*inten))
        d.ellipse([p[0]*S-r,p[1]*S-r,p[0]*S+r,p[1]*S+r],fill=col+(al,))
    im=im.resize((W,H),Image.LANCZOS); a=np.asarray(im).astype(float)/255.
    glow=gaussian_filter(a[:,:,3],7)[:,:,None]*1.6
    base=fondo; rgb=a[:,:,:3]
    out=base*(1-a[:,:,3:4])+rgb*a[:,:,3:4]+glow*np.array(col)/255.*.5
    return np.clip(out,0,1)
def uri_img(a,q=88):
    import io,base64
    b=io.BytesIO(); Image.fromarray((np.clip(a,0,1)*255).astype(np.uint8)).save(b,'JPEG',quality=q)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
