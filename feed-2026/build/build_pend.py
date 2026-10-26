import sys,asyncio,os
sys.path.insert(0,'/root/.claude/plugins/synced/d59b7fb3-87ca-4bdc-804b-1f33a38211ca_25d78cb2-7fe1-4243-bbc4-e095148a53fb/lci-brand/skills/lci-piezas-graficas/assets')
import marca as M, recetas_feed as R
from playwright.async_api import async_playwright
D='/home/user/feed-lci/D/'
P={'meas_w':'ChatGPT Image Sep 30, 2026, 12_14_10 chatgpt.png','meas_dna':'ChatGPT Image Sep 30, 2026, 12_25_45 AM.png',
   'desk':'ChatGPT Image Sep 30, 2026, 12_28_02 chatgpt.png','edan':'ChatGPT Image Sep 30, 2026, 12_32_45 chatgpt.png',
   'ther':'ChatGPT Image Sep 30, 2026, 12_38_03 AM.png','coffee':'ChatGPT Image Sep 29, 2026, 09_09_47 chatgpt.png',
   'recep':'ChatGPT Image Sep 29, 2026, 09_08_25 AM.png','inbody':'ChatGPT Image Sep 30, 2026, 12_13_09 AM.png',
   'night':'ChatGPT Image Sep 30, 2026, 12_55_26 AM.png','cons':'ChatGPT Image Sep 29, 2026, 08_47_22 AM.png',
   'chair':'ChatGPT Image Sep 29, 2026, 08_47_07 AM.png','hall':'Pasillo moderno con luces doradas chatgpt.png',
   'equip':'ChatGPT Image Sep 30, 2026, 12_34_38 AM.png',
   'p_sit':'Fotos y Logos Academia/Foto Carolina Sentada.png','p_bg':'Fotos y Logos Academia/foto Carolina fondo.png',
   'p_cut':'Fotos y Logos Academia/foto Carolina sin fondo.png',
   'mri':'Gemini_Generated_Image_4dgn7s4dgn7s4dgn.jpg','lab':'Gemini_Generated_Image_8wq5uk8wq5uk8wq5.jpg',
   'brain_w':'Gemini_Generated_Image_awffmiawffmiawff.jpg','brain_b':'Gemini_Generated_Image_g8hu0zg8hu0zg8hu.jpg',
   'face':'S03-precision-medicine.webp','n_rope':'nuevas/cuerda.png','n_cons':'nuevas/consultorio.png','n_age':'nuevas/edades.png','n_mus':'nuevas/musculo_d.png','n_dyn':'nuevas/dinamometro.png','n_doc':'nuevas/10.png','n_check':'nuevas/11.png','n_juice':'nuevas/12.png','n_juiced':'nuevas/12_d.png','n_juiceg':'nuevas/12_g.png','n_fit':'nuevas/13.png','n_fitd':'nuevas/13_dark.png','oxi':'oximetro.png','g_sofa':'gafas_sofa.png','g_det':'gafas_detalle.png','ph_edan':'IMG_20260929_195814.jpg.jpeg','vlab':'Gemini_Generated_Image_p084w0p084w0p084.png','ph_mask':'IMG_20260929_194625.jpg.jpeg','ph_room':'IMG_20260929_195540.jpg.jpeg','ph_chair':'IMG_20260929_194548.jpg.jpeg','hands':'Gemini_Generated_Image_5a9th85a9th85a9t.jpg','ibdisp':'Gemini_Generated_Image_9us0io9us0io9us0.jpg','brain_l':'Gemini_Generated_Image_vdh1j1vdh1j1vdh1.jpg','brain_h':'Gemini_Generated_Image_bg1cxmbg1cxmbg1c.jpg'}
F=lambda k,m,c=None,bl=0,pos='center': M.foto(R.tratar(D+P[k],m,crop=c,blur=bl),None,pos=pos)
def BR(k,m,c=None,f=1.4):
    import base64,io
    from PIL import Image,ImageEnhance
    u=R.tratar(D+P[k],m,crop=c); im=Image.open(io.BytesIO(base64.b64decode(u.split(',',1)[1])))
    im=ImageEnhance.Brightness(im).enhance(f); im=ImageEnhance.Contrast(im).enhance(0.95)
    b=io.BytesIO(); im.save(b,'JPEG',quality=90); return M.foto('data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode(),None)
GR=lambda n,s=1: R.gradiente(n,seed=s)
NAVY='#2A3649'
ICON='<circle cx="120" cy="120" r="104" fill="none" stroke="#D2B58A" stroke-width="2"/><circle cx="120" cy="120" r="80" fill="none" stroke="rgba(255,255,255,.45)" stroke-width="1.2"/><polyline points="30,124 78,124 94,92 112,158 130,70 146,124 210,124" fill="none" stroke="#fff" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>'
def PH(k,m='natural',c=None,f=1.0):
    import base64,io
    from PIL import Image,ImageOps,ImageEnhance
    im=ImageOps.exif_transpose(Image.open(D+P[k])).convert('RGB'); im.thumbnail((1600,1600))
    tmp='/tmp/_ph_'+k+'.jpg'; im.save(tmp,quality=92)
    u=R.tratar(tmp,m,crop=c)
    if f!=1.0:
        x=Image.open(io.BytesIO(base64.b64decode(u.split(',',1)[1]))); x=ImageEnhance.Brightness(x).enhance(f); b=io.BytesIO(); x.save(b,'JPEG',quality=90); u='data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
    return M.foto(u,None)
def FXB(tipo):
    """Fondos fx.py del catálogo de 38 (familias 13–26), recetas probadas del skill. Rotar: la Dra. exige usar TODAS las opciones."""
    import fx as _fx
    W_,H_=R.W,R.H
    if tipo=='galaxia': a=_fx.galaxia(W_,H_,2,'azul',3.2,(.80,.16))
    elif tipo=='galaxia_oro': a=_fx.galaxia(W_,H_,7,'oro',2.4,(.22,.10),1.4)
    elif tipo=='malla': a=_fx.malla(W_,H_,4,(.78,.18),inten=.5)
    elif tipo=='mesh_oscuro': a=_fx.mesh(W_,H_,[[_fx.DEEP,_fx.INK,_fx.NAVY],[_fx.INK,_fx.STEEL,_fx.SLATE],[_fx.NAVY,_fx.DEEP,_fx.INK],[_fx.STEEL*.8,_fx.NAVY,_fx.DEEP]],3,70)
    elif tipo=='mesh_claro': a=_fx.mesh(W_,H_,[[_fx.WHITE,_fx.ICE,_fx.BLUE],[_fx.ICE,_fx.SLATE*1.12,_fx.WHITE],[_fx.WHITE,_fx.BLUE,_fx.ICE],[_fx.BLUE,_fx.WHITE,_fx.SLATE*1.1]],2,60,.012)
    return M.foto(_fx.uri_img(a),None)
def VD(k,c=None,tinte=None):
    from PIL import Image,ImageOps
    im=ImageOps.exif_transpose(Image.open(D+P[k])).convert('RGB'); im.thumbnail((1600,1600)); tmp='/tmp/_vd_'+k+'.jpg'; im.save(tmp,quality=92)
    return R.vidrio(tmp,c,tinte)
CUT=lambda m=None: R.recorte(D+P['p_cut'],1400,m)
SQ=(0.1,0,0.9,1)  # 4:5 de un cuadrado
BOOK="Book your consultation —<br>link in bio."
ES=len(sys.argv)>1 and sys.argv[1]=='es'
if ES: M.IDIOMA='es'
t=(lambda en,es: es if ES else en)
POSTS={
'NB-recuperacion':[
 lambda: R.r_derecha(t("Back to training,","De vuelta a entrenar,"),t("with a plan.","con un plan."),
   t("Assessment, measurement and follow-up<br>for athletes returning from injury.","Valoración, medición y seguimiento<br>para deportistas que regresan de una lesión."),
   None,fondo=F('ph_room','frio',(0.05,0,0.95,1)),logo=("principal","blanco","tl"),fs=66,top=0.46),
],
'NC-wearables':[
 lambda: R.r_derecha(t("Your wearable has the data.","Tu wearable tiene los datos."),t("We give it context.","Nosotros, el contexto."),
   t("Smartwatch and ring data, read<br>alongside clinical-grade measurement.","Datos de tu reloj y anillo inteligente,<br>leídos junto a mediciones de grado clínico."),
   None,fondo=F('oxi','azul'),logo=("sello","claro","tl"),fs=64,top=0.44),
],
}
only=[]
async def main():
    async with async_playwright() as p:
        import _navegador; b=await _navegador.lanzar(p); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for k,sl in POSTS.items():
            if only and k not in only: continue
            L='es' if ES else 'en'; os.makedirs(f'out_pend_{L}/{k}',exist_ok=True)
            for i,f in enumerate(sl,1):
                await pg.set_content(f())
                try: await pg.wait_for_function('window.__lci_listo===true', timeout=6000)
                except Exception: await pg.wait_for_timeout(600)
                await pg.wait_for_timeout(120)
                await pg.locator('#lienzo').screenshot(path=f'out_pend_{L}/{k}/{k[:2]}-{i}.png')
            print(k,len(sl))
        await b.close()
asyncio.run(main())
