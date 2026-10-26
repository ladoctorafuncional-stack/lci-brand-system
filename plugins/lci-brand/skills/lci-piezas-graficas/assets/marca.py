# -*- coding: utf-8 -*-
"""
LCI · Motor de PIEZAS GRÁFICAS v2 — clon del estilo de Diana Paola Londoño (Ikigai).
Autocontenido: fuentes (fonts_brand.json) + logos oficiales (logos_brand.json) + paleta
del brandbook, todo base64. Render a PNG pixel-exacto vía scripts/render.py.
Lee references/marca-oficial/MANUAL-LCI.md para la doctrina de marca.

Uso:
    import sys; sys.path.insert(0,'.../assets'); import marca as M
    body = M.content(M.logo('principal','blanco') + ... )
    html = M.lienzo('story', body, fondo=M.GRAD_NAVY)
    open('out.html','w',encoding='utf-8').write(html)
    # render: python3 scripts/render.py out.html out.png story
O usar un template de alto nivel: M.t_poster(...), M.t_concepto(...), etc.
"""
import json, os, io, base64

_DIR = os.path.dirname(__file__)
F = json.load(open(os.path.join(_DIR, 'fonts_brand.json')))
LG = json.load(open(os.path.join(_DIR, 'logos_brand.json')))
import sys as _s; _s.path.insert(0,_DIR)
from reglas_lectura import REGLAS_JS, margen, MARGEN   # reglas de lectura y márgenes (10-oct-2026)

# ───────── FORMATOS (px) ─────────
PRESETS = {
    'brochure': (1240, 1754),   # A4 a 150 dpi (brochures/revistas, oct 2026)
    "story": (1080,1920), "reel": (1080,1920), "post": (1080,1080),
    "post_v": (1080,1350), "carrusel": (1080,1350), "infografia": (1080,1920),
    "flyer": (1240,1754), "flyer_hd": (2480,3508), "banner": (1200,630),
    "banner_v": (1080,1350), "email_sig": (1500,400), "carnet": (1000,1400),
    "story_hero": (1080,1755),   # story 2:3.25 (hero foto full-bleed, tipo 'DNA/heal')
    "poster_v": (1080,1620),     # afiche 2:3 (tipo 'Creatine timeline / Muscle Cells')
}

# ───────── FUENTES ─────────
def _face(k):
    f=F[k]
    return (f"@font-face{{font-family:'{f['family']}';font-style:{f['style']};"
            f"font-weight:{f['weight']};font-display:block;"
            f"src:url(data:{f['mime']};base64,{f['data']}) format('{f['fmt']}');}}")
def fonts_css(): return "\n".join(_face(k) for k in F)

# ───────── LOGOS ─────────
def _uri(key): return f"data:image/png;base64,{LG[key]['data']}"
def logo_uri(key): return _uri(key)

# recolorea una marca de un solo color (cutout navy transparente) a cualquier color
_recache={}
def mark_recolor(key, hexcolor):
    ck=(key,hexcolor)
    if ck in _recache: return _recache[ck]
    from PIL import Image
    im=Image.open(io.BytesIO(base64.b64decode(LG[key]['data']))).convert('RGBA')
    r,g,b=int(hexcolor[1:3],16),int(hexcolor[3:5],16),int(hexcolor[5:7],16)
    a=im.split()[3]
    solid=Image.new('RGBA',im.size,(r,g,b,0)); solid.putalpha(a)
    buf=io.BytesIO(); solid.save(buf,'PNG')
    uri="data:image/png;base64,"+base64.b64encode(buf.getvalue()).decode()
    _recache[ck]=uri; return uri

def logo(kind="principal", theme="blanco", h=None):
    """kind: principal|sello|terciario · theme: blanco|beige|gold|navy|fondo_oscuro|claro|dorado"""
    key=f"{kind}_{theme}"
    if key not in LG:  # fallbacks por nombre de color alterno
        alt={"gold":"dorado","dorado":"gold","blanco":"beige","claro":"beige"}.get(theme)
        key=f"{kind}_{alt}" if alt and f"{kind}_{alt}" in LG else key
    style=f'height:{h}px;' if h else ''
    return f'<img data-logo="{kind}" src="{_uri(key)}" style="{style}display:block;">'

def logo_cr(kind="wordmark", color=None, theme="claro", h=None):
    """Marca personal CR. kind: wordmark|sello. color=hex para recolorear (p.ej. beige sobre foto)."""
    key=f"cr_{kind}_{theme}"
    src = mark_recolor(f"cr_{kind}_claro", color) if color else _uri(key)
    style=f'height:{h}px;' if h else ''
    return f'<img data-logo="cr_{kind}" src="{src}" style="{style}display:block;">'

MEMBRETE = None
_mp=os.path.join(_DIR,'papeleria','membrete_lci.png')
if os.path.exists(_mp):
    MEMBRETE="data:image/png;base64,"+base64.b64encode(open(_mp,'rb').read()).decode()

# ───────── PALETA (brandbook) ─────────
PALETTE = """
:root{
  --navy:#2A3649; --navy-2:#222d3d; --navy-deep:#19222e; --navy-soft:#36445a;
  --blue:#CAD3DD; --blue-mid:#5D768C; --blue-deep:#9fb2c6;
  --gold:#D2B58A; --gold-deep:#b9966a; --gold-soft:#e3cdac;
  --cream:#EDE5DA; --beige:#f7f1e9; --paper:#fbf8f3; --ink:#2A3649; --white:#fff;
}
"""
GRAD_NAVY=("radial-gradient(120% 85% at 80% 8%, #33425a 0%, #2A3649 44%, #19222e 100%)")
GRAD_NAVY_DEEP=("radial-gradient(130% 100% at 50% 0%, #2f3d52 0%, #2A3649 38%, #19222e 100%)")
GRAD_CURSO=("radial-gradient(90% 70% at 35% 32%, #46659e 0%, #243a66 38%, #0e1830 100%)")
GRAD_CREAM="linear-gradient(160deg,#fbf8f3 0%, #efe5d6 100%)"
GRAD_BLUE="linear-gradient(160deg,#e7edf2 0%, #CAD3DD 120%)"
GRAD_GRIS="linear-gradient(150deg,#eceff2 0%, #b9c2cc 130%)"

def foto(uri, veil="navy", pos="center", zoom=1.0):
    veils={
      "navy":"linear-gradient(0deg, rgba(25,34,46,.94) 0%, rgba(25,34,46,.55) 42%, rgba(25,34,46,.12) 78%, rgba(25,34,46,.30) 100%)",
      "navy-side":"linear-gradient(96deg, rgba(25,34,46,.95) 0%, rgba(25,34,46,.74) 40%, rgba(25,34,46,.22) 78%, rgba(25,34,46,0) 100%)",
      "soft":"linear-gradient(0deg, rgba(25,34,46,.78) 0%, rgba(25,34,46,.10) 60%)",
      "full":"linear-gradient(0deg, rgba(25,34,46,.55), rgba(25,34,46,.55))",
      None:"linear-gradient(0deg, rgba(25,34,46,0), rgba(25,34,46,0))"}
    return f"{veils.get(veil,veils['navy'])}, url('{uri}')|cover|{pos}|{zoom}"

def bg_particulas(formato="story", top_rgb=(0x25,0x32,0x4a), bot_rgb=(0x12,0x19,0x24),
                  glow=True):
    """Fondo navy a sangre con la onda de partículas oficial (membrete) fundida arriba.
    Devuelve un data URI listo para fondo=... (ya viene oscuro; sin velo extra)."""
    from PIL import Image, ImageDraw, ImageFilter
    import numpy as np
    W,H=PRESETS[formato]
    top=np.array(top_rgb); bot=np.array(bot_rgb)
    g=np.zeros((H,W,3),np.uint8)
    for y in range(H):
        t=y/H; g[y,:]=(top*(1-t)+bot*t).astype(np.uint8)
    base=Image.fromarray(g)
    if glow:
        gl=Image.new('L',(W,H),0)
        ImageDraw.Draw(gl).ellipse([W*0.05,-H*0.16,W*0.95,H*0.32],fill=64)
        gl=gl.filter(ImageFilter.GaussianBlur(int(W*0.11)))
        base=Image.composite(Image.new('RGB',(W,H),(64,86,132)),base,gl)
    if MEMBRETE:
        band=Image.open(_mp).convert('RGBA').crop((0,0,980,272))
        bw=W; bh=int(band.height*bw/band.width); band=band.resize((bw,bh),Image.LANCZOS)
        m=Image.new('L',(bw,bh),0); dm=ImageDraw.Draw(m)
        for y in range(bh):
            a=255 if y<bh*0.5 else int(255*max(0,(1-(y-bh*0.5)/(bh*0.5))))
            dm.line([(0,y),(bw,y)],fill=a)
        band.putalpha(Image.composite(band.split()[3],Image.new('L',(bw,bh),0),m))
        base=base.convert('RGBA'); base.alpha_composite(band,(0,int(H*0.015))); base=base.convert('RGB')
    buf=io.BytesIO(); base.save(buf,'JPEG',quality=90)
    return "data:image/jpeg;base64,"+base64.b64encode(buf.getvalue()).decode()

# ───────── CSS DE COMPONENTES (literal; sin interpolación Python) ─────────
_CSS = r"""
*{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
html,body{background:#fff;}
.lienzo{position:relative;overflow:hidden;font-family:'Poppins',sans-serif;font-weight:300;
  color:#fff;-webkit-font-smoothing:antialiased;}
.lienzo *{line-height:1.5;}
.serif{font-family:'Mencken Std',serif;}
/* .serif-it y .dh .it = master 400 puro (base 'elegante'). Con it_css()/menc_it() se aplica el rol: 'hero_oscuro'(800) claro-sobre-oscuro · 'hero_claro'(400+2.2%) navy-sobre-claro · 'acento'(400+2.5%) cajas · 'elegante'(400+1%) sub-barras/secundarias. */
.serif-it{font-family:'Mencken Std Head','Mencken Std',serif;font-style:italic;font-weight:400;}
.bg{position:absolute;inset:0;background-size:cover;background-position:center;z-index:0;}
.lienzo img{align-self:flex-start;width:auto;max-width:100%;}
.content{position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;}

/* tipografía */
.eyebrow{font-size:18px;letter-spacing:.42em;text-transform:uppercase;color:var(--gold);font-weight:500;}
.eyebrow.blue{color:var(--blue);}
.kicker{font-size:15px;letter-spacing:.34em;text-transform:uppercase;color:var(--blue);font-weight:400;}
h1.dh{font-family:'Mencken Std',serif;font-weight:700;color:#fff;font-size:92px;line-height:1.03;letter-spacing:.004em;}
.dh .it{font-family:'Mencken Std Head','Mencken Std',serif;font-style:italic;font-weight:400;}
.dh .cream{color:var(--cream);} .dh .blue{color:var(--blue);} .dh .gold{color:var(--gold-soft);}
.dh .reg{font-weight:400;} .dh .navy{color:var(--navy);}
.subhead{font-weight:300;font-size:30px;color:var(--blue);line-height:1.45;}
.subhead.it{font-style:italic;font-family:'Poppins';}
.subhead .serif-it{color:#fff;}
.body{font-weight:300;font-size:25px;color:var(--blue);line-height:1.6;}
.body strong{color:#fff;font-weight:500;} .body.it{font-style:italic;}

/* hairline / reglas */
/* línea LIMPIA de marca (la Dra., 25-oct-2026: nada de destello/difuminado ni degradado de color) */
.hairline{height:1.5px;background:rgba(255,255,255,.72);border:0;opacity:1;}
.theme-light .hairline{background:rgba(42,54,73,.42);}
.rule-left{width:84px;height:2px;background:var(--gold);border:0;}
.rule-w{height:2px;background:#fff;border:0;opacity:.85;}

/* barra de resaltado (motivo firma) — azul / oro / gris */
.hl{background:rgba(202,211,221,.30);padding:.06em .34em;box-decoration-break:clone;-webkit-box-decoration-break:clone;}
.hl-gold{background:rgba(210,181,138,.42);}
.hl-mid{background:rgba(93,118,140,.45);}
.hl-grey{background:rgba(255,255,255,.16);}

/* caja de borde fino alrededor de línea-acento */
.h-box{display:inline-block;border:1.6px solid var(--blue-deep);border-radius:3px;padding:.05em .5em;}
.h-box.gold{border-color:var(--gold);}

/* caja de borde dorado (ofertas / CTA) */
.goldbox{border:1.5px solid var(--gold);border-radius:16px;padding:24px 30px;}
.framebox{border:1.4px solid rgba(202,211,221,.5);border-radius:6px;padding:22px 26px;}

/* conector vertical con nodos */
.conx{display:grid;grid-template-columns:46px 1fr;gap:0 26px;align-items:stretch;}
.conx .ln{position:relative;border-left:2px solid var(--blue-mid);margin:6px 0;}
.conx .ln::before,.conx .ln::after{content:"";position:absolute;left:-6px;width:11px;height:11px;border-radius:50%;background:var(--blue-mid);}
.conx .ln::before{top:-2px;} .conx .ln::after{bottom:-2px;}
.conx .it{font-size:25px;color:#fff;margin:10px 0;font-weight:300;}
.conx .it b{font-family:'Mencken Std Head',serif;font-style:italic;color:var(--gold-soft);font-weight:400;}

/* viñetas diamante doradas */
.bul{list-style:none;} .bul li{position:relative;padding-left:34px;margin:12px 0;font-size:25px;color:#fff;font-weight:300;}
.bul li::before{content:"";position:absolute;left:2px;top:.42em;width:12px;height:12px;background:var(--gold);transform:rotate(45deg);}
.bul.caps li{text-transform:uppercase;letter-spacing:.06em;font-style:italic;font-size:22px;}

/* lista check dorado + subrayado (estilo curso) */
.chk{list-style:none;} .chk li{position:relative;padding:12px 0 14px 46px;font-size:27px;color:#fff;border-bottom:1px solid rgba(210,181,138,.4);font-style:italic;}
.chk li::before{content:"\2713";position:absolute;left:6px;top:10px;color:var(--gold);font-weight:700;font-style:normal;}

/* chips (síntomas / keywords) */
.chips{display:flex;flex-wrap:wrap;gap:14px;}
.chip{background:rgba(93,118,140,.55);border-radius:7px;padding:12px 22px;font-size:24px;color:#fff;font-weight:300;}

/* dato grande */
.stat .n{font-family:'Mencken Std',serif;font-weight:800;font-size:140px;color:var(--gold-soft);line-height:.9;}
.stat .l{font-size:22px;color:var(--blue);margin-top:6px;}

/* bloque de fecha (eventos) */
.fecha .rl{font-size:18px;letter-spacing:.4em;text-transform:uppercase;color:var(--gold);text-align:center;}
.fecha .dt{font-size:40px;color:#fff;text-align:center;margin-top:8px;letter-spacing:.04em;
  border-top:1.4px solid var(--gold);border-bottom:1.4px solid var(--gold);padding:10px 0;}
.fecha .dt span{color:var(--gold-soft);margin:0 14px;}

/* bloque ubicación */
.ubic{display:grid;grid-template-columns:34px 1fr;gap:0 16px;align-items:start;font-style:italic;font-size:26px;color:#fff;}
.ubic .pin{width:28px;height:34px;}

/* pill de contacto */
.pill{display:flex;align-items:center;justify-content:center;gap:14px;border:1.6px solid rgba(202,211,221,.45);
  border-radius:60px;padding:15px 30px;font-size:19px;color:var(--blue);font-weight:300;white-space:nowrap;}
.pill.fill{background:rgba(255,255,255,.10);border-color:transparent;}
.pill .sep{width:1px;height:22px;background:rgba(202,211,221,.45);}
.pill .wa{width:30px;height:30px;border-radius:50%;border:1.4px solid var(--blue);display:inline-flex;align-items:center;justify-content:center;}
.pill .wa svg{width:17px;height:17px;fill:var(--blue);}

/* banda de contacto rellena (marca personal, 4 filas) */
.cband{display:flex;flex-direction:column;gap:14px;}
.cband .row{display:flex;align-items:center;gap:16px;font-size:26px;color:#fff;}
.cband .ic{width:34px;height:34px;color:var(--gold);flex-shrink:0;}

/* panel de foto vertical con marca de recorte */
.vpanel{position:relative;border:1px solid rgba(255,255,255,.5);overflow:hidden;}
.vpanel .cross{position:absolute;width:34px;height:34px;}
.vpanel .cross::before,.vpanel .cross::after{content:"";position:absolute;background:#fff;}
.vpanel .cross::before{left:50%;top:0;width:1.5px;height:100%;transform:translateX(-50%);}
.vpanel .cross::after{top:50%;left:0;height:1.5px;width:100%;transform:translateY(-50%);}

/* TEMA CLARO (sobre crema/gris/azul) — texto navy */
.theme-light{color:var(--navy);}
.theme-light h1.dh{color:var(--navy);} .theme-light .dh .it{color:var(--gold-deep);}
.theme-light .dh .blue{color:var(--blue-mid);} .theme-light .dh .cream{color:var(--gold-deep);}
.theme-light .subhead,.theme-light .body{color:#55617a;} .theme-light .body strong{color:var(--navy);}
.theme-light .eyebrow{color:var(--gold-deep);} .theme-light .kicker{color:var(--blue-mid);}
.theme-light .conx .it{color:var(--navy);} .theme-light .conx .ln,.theme-light .conx .ln::before,.theme-light .conx .ln::after{border-color:var(--blue-mid);background:var(--blue-mid);}
.theme-light .pill{border-color:rgba(42,54,73,.30);color:var(--blue-mid);}
.theme-light .pill .wa{border-color:var(--blue-mid);} .theme-light .pill .wa svg{fill:var(--blue-mid);}
.theme-light .pill .sep{background:rgba(42,54,73,.3);}
.theme-light .hl{background:rgba(93,118,140,.22);} .theme-light .chip{background:rgba(93,118,140,.30);color:var(--navy);}
.theme-light .h-box{border-color:var(--blue-mid);}
"""

def base_css(w,h):
    return fonts_css()+PALETTE+f".lienzo{{width:{w}px;height:{h}px;}}\n"+_CSS

# ───────── HELPERS DE CONTENIDO ─────────
def eyebrow(t,blue=False): return f'<div class="eyebrow{" blue" if blue else ""}">{t}</div>'
def kicker(t): return f'<div class="kicker">{t}</div>'
def subhead(t,it=False): return f'<div class="subhead{" it" if it else ""}">{t}</div>'
def parrafo(t,it=False): return f'<div class="body{" it" if it else ""}">{t}</div>'
def hairline(): return '<hr class="hairline">'
def rule_left(): return '<hr class="rule-left">'
def hl(t,tone="blue"):
    c={"blue":"hl","gold":"hl hl-gold","mid":"hl hl-mid","grey":"hl hl-grey"}[tone]
    return f'<span class="{c}" data-resaltado>{t}</span>'
def caja(inner,gold=False): return f'<span class="h-box{" gold" if gold else ""}">{inner}</span>'

# ───────── MASTERS DE MENCKEN HEAD ITÁLICO — regla del ADN medida en 11 piezas de Paola ─────────
# Solo hay DOS dibujos embebidos de Mencken Std Head itálico: 400 (abierto, contraste suave) y
# 800 (contraste extremo grueso/fino). NUNCA pedir 700: no existe y el navegador salta al 800.
#  · 800 = PROTAGONISTA CLARO SOBRE OSCURO — la palabra estrella de la pieza en light-blue/crema/
#    blanco sobre foto o navy: 'Muscle Cells', 'longevidad.', 'Péptidos', 'ages too.', 'We know how
#    to activate it.', 'Thousand supplements', 'Some people in their 40s'. El contraste extremo
#    BRILLA sobre fondo oscuro y le da presencia frente a la foto.
#  · 400 (+ peso por text-stroke) = TODO LO DEMÁS:
#    a) protagonista NAVY SOBRE CLARO ('Exosomes', 'Your lab results…', 'Acompañándote'): el 800
#       quedaría como mancha negra; el 400 engrosado (~2.2% del cuerpo) da presencia con elegancia.
#    b) rol 'acento' (400 + 2.5%): acentos en CAJA ('Reclaim the energy', 'Los nuevos comienzos',
#       'something important') — medido: pesan casi como el protagonista claro, no son delicados.
#    c) rol 'elegante' (400 + 1%): sub-barras y líneas secundarias ('are cellular messengers',
#       'Schedule your longevity assessment', 'Beneficios físicos', 'Pronto…', 'Soon…'): voz de apoyo.
IT_ROLES={"hero_oscuro":(800,0.0),"hero_claro":(400,0.022),"acento":(400,0.025),"elegante":(400,0.010)}
def it_css(rol, fs, color):
    """CSS inline de Mencken Head itálico según ROL: hero_oscuro | hero_claro | acento | elegante. fs en px."""
    w,st=IT_ROLES[rol]
    stroke=f"-webkit-text-stroke:{fs*st:.2f}px {color};" if st>0 else ""
    return (f"font-family:'Mencken Std Head','Mencken Std',serif;font-style:italic;font-weight:{w};"
            f"{stroke}font-size:{fs}px;color:{color};")
def menc_it(txt, rol, fs, color, extra=""):
    """<span> Mencken Head itálico con el master correcto por rol: hero_oscuro | hero_claro | acento | elegante."""
    return f'<span style="{it_css(rol,fs,color)}{extra}">{txt}</span>'
def goldbox(inner): return f'<div class="goldbox">{inner}</div>'

def titular(spans, size=92):
    """spans: HTML ya compuesto con <span class='it/cream/blue/gold/reg/navy'>…</span>."""
    return f'<h1 class="dh" style="font-size:{size}px;">{spans}</h1>'

def conector(items):
    its="".join(f'<div class="it">{i}</div>' for i in items)
    return f'<div class="conx"><div class="ln"></div><div>{its}</div></div>'
def bullets(items,caps=False):
    its="".join(f'<li>{i}</li>' for i in items)
    return f'<ul class="bul{" caps" if caps else ""}">{its}</ul>'
def checklist(items):
    its="".join(f'<li>{i}</li>' for i in items)
    return f'<ul class="chk">{its}</ul>'
def chips(items):
    cs="".join(f'<span class="chip">{i}</span>' for i in items)
    return f'<div class="chips">{cs}</div>'
def stat(n,label): return f'<div class="stat"><div class="n">{n}</div><div class="l">{label}</div></div>'

def bloque_fecha(rotulo,fecha_html):
    return f'<div class="fecha"><div class="rl">{rotulo}</div><div class="dt">{fecha_html}</div></div>'
_PIN='<svg class="pin" viewBox="0 0 24 30" fill="none"><path d="M12 0C5.4 0 0 5.4 0 12c0 8 12 18 12 18s12-10 12-18C24 5.4 18.6 0 12 0z" fill="#D2B58A"/><circle cx="12" cy="12" r="5" fill="#19222e"/></svg>'
def bloque_ubicacion(html): return f'<div class="ubic">{_PIN}<div>{html}</div></div>'

_WA=('<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15l-1.4 5 5.1-1.3A10 10 0 1 0 12 2zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8 8 0 1 1 12 20zm4.5-5.9c-.2-.1-1.4-.7-1.6-.8-.2-.1-.4-.1-.5.1l-.7.9c-.1.2-.3.2-.5.1a6.5 6.5 0 0 1-3.2-2.8c-.1-.2 0-.4.1-.5l.4-.5c.1-.2.1-.3 0-.5l-.7-1.7c-.2-.4-.4-.4-.5-.4h-.5c-.2 0-.5.1-.7.3a3 3 0 0 0-.9 2.2c0 1.3 1 2.6 1.1 2.8.1.2 1.9 3 4.7 4.1 1.7.6 1.9.4 2.2.4.4 0 1.3-.5 1.5-1 .2-.5.2-1 .1-1z"/></svg>')
# Teléfono por IDIOMA de la pieza (regla de la Dra., oct-2026):
#   inglés  -> (+57) 300 002 71 15   ·   español -> (+57) 301 512 39 91
TEL={"en":"(+57) 300 002 71 15","es":"(+57) 301 512 39 91"}
IG={"en":"@longevityclinicalinstitute","es":"@institutoclinicodelongevidad"}   # Instagram por idioma (oct 2026)
IDIOMA="en"   # el feed LCI es en inglés; las piezas en español deben poner M.IDIOMA="es"
def pill(institucional=True, fill=False, idioma=None, solo_web=False):
    """solo_web=True (regla de la Dra., 10-oct-2026): en piezas con VIDRIO OPACO la cápsula va DENTRO del vidrio y lleva
    SOLO la página web de la clínica — así ningún elemento se sale del vidrio."""
    tel=TEL[idioma or IDIOMA]; ig=IG[idioma or IDIOMA]
    if solo_web:
        web='longevityclinicalinstitute.com' if institucional else 'longevitymedicaldoctor.com'
        return f'<div class="pill pill-web{" fill" if fill else ""}" style="display:inline-flex;width:auto;justify-content:center;padding:0 30px"><span>{web}</span></div>'
    if institucional:
        cells=[f'<span class="wa">{_WA}</span><span>{tel}</span>',
               f'<span>{ig}</span>','<span>longevityclinicalinstitute.com</span>']
    else:
        cells=[f'<span class="wa">{_WA}</span><span>{tel}</span>',
               '<span>@longevitymedicaldoctor</span>','<span>longevitymedicaldoctor.com</span>']
    inner='<span class="sep"></span>'.join(cells)
    return f'<div class="pill{" fill" if fill else ""}">{inner}</div>'

# ───────── ENSAMBLADOR ─────────
def _bg(fondo):
    if fondo is None: fondo=GRAD_NAVY
    if "|cover|" in fondo:
        css,size,pos,zoom=fondo.split("|")
        sc=f"transform:scale({zoom});" if float(zoom)!=1.0 else ""
        return f'<div class="bg" style="background-image:{css};background-size:{size};background-position:{pos};{sc}"></div>'
    if fondo.startswith('data:') or fondo.startswith('url('):
        url=fondo if fondo.startswith('url(') else f"url('{fondo}')"
        return f'<div class="bg" style="background-image:{url};background-size:cover;background-position:center;"></div>'
    return f'<div class="bg" style="background:{fondo};"></div>'

def lienzo(formato, body, fondo=None, theme="navy"):
    if formato not in PRESETS: raise ValueError(f"Formato '{formato}' no existe: {list(PRESETS)}")
    w,h=PRESETS[formato]
    tc=" theme-light" if theme=="light" else ""
    return (f'<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">'
            f'<title>LCI {formato}</title><style>{base_css(w,h)}</style>{REGLAS_JS}</head>'
            f'<body><div class="lienzo{tc}" id="lienzo">{_bg(fondo)}{body}</div></body></html>')

def content(inner, pad="104px", justify="space-between", align="stretch", gap="0"):
    return (f'<div class="content" style="padding:{pad};justify-content:{justify};'
            f'align-items:{align};gap:{gap};">{inner}</div>')

# ───────── TEMPLATES DE ALTO NIVEL (salen siempre con el estilo Paola) ─────────

OPTICA_JS = '''<script>/* ALINEACIÓN ÓPTICA LCI (oct 2026): la TINTA de la primera letra de cada línea [data-opt] cae exactamente en el borde
del bloque (corrige el colgado de itálicas como la «j» y el sangrado de «¿», «¡», comillas). Así ES = EN. */
(function(){function f(){var c=document.createElement('canvas').getContext('2d');
document.querySelectorAll('[data-opt]').forEach(function(e){var t=(e.textContent||'').replace(/^\s+/,'');if(!t)return;
var s=getComputedStyle(e);c.font=s.fontStyle+' '+s.fontWeight+' '+s.fontSize+' '+s.fontFamily;
var m=c.measureText(t[0]);var d=m.actualBoundingBoxLeft;if(Math.abs(d)>0.4)e.style.marginLeft=d.toFixed(1)+'px';});}
function g(){if(document.fonts&&document.fonts.ready)document.fonts.ready.then(f);else f();}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',g);else g();})();</script>'''


# ───────── CONECTOR DE NODOS «Paola» (medido en 'The brain ages too', oct 2026) ─────────
# Cada ítem tiene SU rama horizontal, que sale de la línea vertical con un punto en la unión y llega a la altura
# del CENTRO DE LA X-HEIGHT de la PRIMERA línea del ítem. El texto arranca a 0.68em del final de la rama, en una
# columna angosta (~11em) que parte en 2–3 líneas. La vertical baja desde el bloque de arriba hasta la última rama.
# Medidas (cuerpo 25px): rama 3.9em · aire rama→texto 0.68em · interlínea 1.28 · aire entre ítems 1.2em · punto 7px.
# Prohibido: ítems en una sola línea larga lejos de sus ramas, o ramas que no coinciden con la primera línea.
def conector(items, fs=26, color="#fff", linea="rgba(159,178,198,.85)", arriba_em=2.9, col_em=11.5, it=True, peso=400,
             rama_em=3.9, gap_em=0.68, lh=1.28, entre_em=1.2):
    """Conector de nodos de Paola. items = textos (con <br> si se quiere fijar el corte). arriba_em = del borde superior
    del bloque (p. ej. base del marco) a la PRIMERA rama. Verificado ±1px contra 'The brain ages too'."""
    yb = 0.62*lh   # rama = centro de la x-height de la 1ª línea (0.62 de su caja), en em
    rows = ""
    for i, t in enumerate(items):
        pt = round(fs*(arriba_em - yb)) if i == 0 else round(fs*entre_em)
        y = f"calc({pt}px + {yb:.3f}em)"
        seg = f'<div style="position:absolute;left:0;top:0;height:{y};border-left:1.5px solid {linea}"></div>'
        if i < len(items) - 1:   # la vertical continúa hasta el siguiente ítem
            seg += f'<div style="position:absolute;left:0;top:{y};bottom:0;border-left:1.5px solid {linea}"></div>'
        seg += f'<div style="position:absolute;left:0;top:{y};width:{rama_em}em;border-top:1.5px solid {linea}"></div>'
        seg += (f'<div style="position:absolute;left:-3.5px;top:calc({pt}px + {yb:.3f}em - 3px);width:7px;height:7px;'
                f'border-radius:50%;background:{linea}"></div>')
        txt = (f'<div style="font-family:Poppins,sans-serif;font-style:{"italic" if it else "normal"};font-weight:{peso};'
               f'line-height:{lh};color:{color};max-width:{col_em}em">{t}</div>')
        rows += f'<div style="position:relative;padding-top:{pt}px;padding-left:{rama_em+gap_em:.2f}em">{seg}{txt}</div>'
    return f'<div data-escala style="font-size:{fs}px">{rows}</div>'

# ───────── INTERLINEADO BLINDADO (regla oct-2026; ver references/estandar-visual-2026/INTERLINEADO-BLINDADO.md) ─────────
def ritmo(fs_titular, fs_cuerpo):
    """Devuelve las medidas aprobadas (px y line-heights) para un bloque titular + cuerpo. Nunca interlinear a ojo."""
    T, c = float(fs_titular), float(fs_cuerpo)
    return dict(
        lh_titular=1.0, lh_estrella=0.98, lh_regular_apoyo=1.05,
        lh_parrafo=1.40, lh_parrafo_italica=1.32, lh_rotulo=1.0,
        titular_lineas=0,                       # entre líneas de un mismo titular
        estrella_a_apoyo=round(T*0.11),         # 'Thousand / supplements' -> 'to improve'
        eyebrow_a_titular=round(T*0.08),        # 'Timeline of creatine in' -> 'Muscle Cells'
        estrella_a_barra=round(T*0.20),         # 'Exosomes' -> sub-barra (sumar aire_desc si hay descendentes)
        titular_a_parrafo=round(c*1.35),        # sin filete
        titular_a_filete=round(c*1.2), filete_a_parrafo=round(c*0.9),
        rotulo_a_termino=None,                  # = 1.0 x fs del rótulo (calcular con su tamaño)
        termino_a_etiquetas=round(T*0.22),
        etiquetas_a_filete=round(c*1.5),
        parrafo_a_parrafo=round(c*0.8),
        seccion_a_seccion=round(c*2.75),
    )

# ───────── BARRA / CAJA DE RESALTADO QUE ABRAZA EL TEXTO (regla oct-2026, medida en Paola) ─────────
# Medido en 'are cellular messengers' (poster_reclaim_face): la barra va EXACTAMENTE de la punta de los
# ascendentes a la base de los descendentes — sin aire vertical — y ~0.45em/0.55em de aire lateral.
# Caja con BORDE ('Reclaim the energy'): ~0.11em de aire vertical. Prohibido el resaltado "alto"
# (padding vertical grande / line-height 1 + padding): la Dra. lo rechazó ("supremamente altos").
# Métricas Mencken Std Head itálico (400/800), medidas en Chrome a line-height 1:
#   punta ascendente 0.205em · base descendente 1.14em  → alto de tinta 0.935em.
_MENC_ASC, _MENC_DESC = 0.205, 1.14
def aire_desc(txt, fs, base=6):
    """Aire entre una palabra estrella y la barra de debajo: si la estrella tiene descendentes (p, g, y, paréntesis…)
    la barra baja lo justo para que el descendente NO toque el texto de la barra (regla oct-2026, caso 'Lp(a)')."""
    import re
    plano = re.sub(r'<[^>]+>', '', txt)
    return base + (round(fs*0.16) if any(c in plano for c in 'gjpqyQ(),;') else 0)


# REGLA DE RESALTADOS POR TINTA (la Dra., 10-oct-2026). Tras cargar fuentes, cada barra de relleno se recalcula midiendo
# la tinta REAL del texto (canvas actualBoundingBox):
#   · MISMO aire arriba y abajo de la tinta (round(0.09·fs)+2 px; ~8 px a 62 px — ni al ras ni exagerado) — sin reservar descendentes que la palabra no tiene.
#   · izq: la primera letra arranca en la vertical de la primera letra del titular de arriba; poco azul al comienzo
#     (0.16 em) que sobresale a la izquierda; cola 0.30 em + 2 px a la derecha.
#   · der: ESPEJO — la última letra/punto cierra en la vertical de la última letra del titular; la barra sobresale a la
#     DERECHA (0.16 em + 2 px); 0.30 em de azul al comienzo.
#   · c (bloque centrado): 0.40 em a cada lado.
_BARRA_JS = ("<script>if(!document.__bfix){document.__bfix=1;(function(){function fx(){var cv=document.createElement('canvas'),"
 "x=cv.getContext('2d');function fnt(e){var c=getComputedStyle(e);return c.fontStyle+' '+c.fontWeight+' '+c.fontSize+' '+c.fontFamily;}"
 "function inks(e,first){var t=(e.innerText||'').split('\\n').map(function(z){return z.trim();}).filter(Boolean);if(!t.length)return 0;"
 "var w=first?t[0]:t[t.length-1];var tn=e;var it=e.querySelectorAll('*');for(var i=0;i<it.length;i++){if((it[i].innerText||'').trim())tn=it[i];if(first)break;}"
 "x.font=fnt(first?e:tn);var ch=first?w.charAt(0):w.charAt(w.length-1),m=x.measureText(ch);return first?-m.actualBoundingBoxLeft:(m.width-m.actualBoundingBoxRight);}"
 "document.querySelectorAll('[data-resaltado][data-al]').forEach(function(b){var t=b.firstElementChild;if(!t)return;var c=getComputedStyle(t),fs=parseFloat(c.fontSize);"
 "x.font=fnt(t);var m=x.measureText(t.textContent),A=m.actualBoundingBoxAscent,D=m.actualBoundingBoxDescent,L=m.actualBoundingBoxLeft,R=m.actualBoundingBoxRight,"
 "fA=m.fontBoundingBoxAscent,fD=m.fontBoundingBoxDescent,al=b.getAttribute('data-al'),pv=Math.round(fs*.09)+2,"
 "pl=fs*(al=='izq'?.16:al=='der'?.30:.40),pr=fs*(al=='izq'?.30:al=='der'?.16:.40)+(al=='c'?0:2),base=fA;"
 "b.style.padding='0';b.style.position='relative';b.style.width=(pl+L+R+pr)+'px';b.style.height=(A+D+2*pv)+'px';"
 "t.style.lineHeight='normal';t.style.position='absolute';t.style.left=(pl+L)+'px';t.style.top=(pv+A-base)+'px';"
 "var ref=b.parentElement&&b.parentElement.previousElementSibling;"
 "if(al=='izq'){b.style.marginLeft=(-pl+(ref?inks(ref,true):0))+'px';}"
 "else if(al=='der'){b.style.marginRight=(-pr+(ref?inks(ref,false):0))+'px';}});}"
 "if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fx);else fx();})();}</script>")

def barra(txt, fs, css, fondo=None, borde=None, radio=3, pad_x=None, extra="", ident=None, alinear=True):
    """Span de resaltado que ABRAZA el texto. css = estilo de la fuente (p. ej. it_css('elegante',fs,color)).
    fondo: color de relleno (barra) · borde: 'Npx solid color' (caja). Devuelve inline-block."""
    pv = 0.11 if borde else 0.02
    h = (_MENC_DESC - _MENC_ASC) + 2*pv
    up = _MENC_ASC - pv
    # La Dra. (10-oct-2026): la barra deja AL MENOS 2 px arriba y abajo de la tinta (las letras no quedan al ras del borde).
    # REGLA (la Dra., 10-oct-2026, «Del frasco / al plato»): en TODA barra de relleno alineada a la izquierda, la TINTA del
    # texto resaltado arranca en la misma vertical que el titular/filete de arriba: poco azul al comienzo (0.16em) y la
    # barra sobresale ese mismo tanto hacia la izquierda (margin-left negativo). Aplica a TODOS los resaltados;
    # alinear=False solo en bloques CENTRADOS (padding simétrico). Los recuadros con borde no cambian.
    #   alinear='der' (texto alineado a la derecha): ESPEJO — la última letra y el punto CIERRAN en la vertical de la última
    #   letra del titular de arriba («medimos.» bajo la «e» de «Donde») y la barra sobresale un poco a la DERECHA.
    if pad_x is None:
        pad_x = ((.30, .16) if alinear == 'der' else (.16, .30)) if (alinear and fondo and not borde) else (.45, .55)
    if alinear and fondo and not borde:
        extra = (f"margin-right:calc(-{pad_x[1]}em - 2px);" if alinear == 'der' else f"margin-left:-{pad_x[0]}em;") + extra
    av = 0 if borde else 2   # px extra arriba y abajo (solo barras de relleno; los recuadros conservan su aire)
    st = (f"display:inline-block;box-sizing:border-box;height:calc({h:.3f}em + {2*av}px);font-size:{fs}px;line-height:1;"
          f"padding:0 calc({pad_x[1]}em + 2px) 0 {pad_x[0]}em;overflow:visible;vertical-align:top;")   # +2 px de barra DESPUÉS del final del texto (la Dra., 10-oct-2026)
    if fondo: st += f"background:{fondo};"
    if borde: st += f"border:{borde};border-radius:{radio}px;"
    idattr = f' id="{ident}"' if ident else ''
    if fondo and not borde:   # barra de relleno → ajuste por TINTA medida (ver _BARRA_JS)
        idattr += f' data-al="{"der" if alinear == "der" else "izq" if alinear else "c"}"'
        extra += ""
    js = _BARRA_JS if (fondo and not borde) else ""
    return js + (f'<span{idattr} data-resaltado style="{st}{extra}"><span style="{css}font-size:{fs}px;line-height:1;position:relative;'
            f'top:calc(-{up:.3f}em + {av}px);display:inline-block;white-space:nowrap">{txt}</span></span>')

def t_poster(eyebrow_box, head_bold, head_reg=None, tagline=None, lista=None,
             fondo=None, formato="post_v", theme="navy", logo_theme="blanco", contacto=True, H=78,
             logo_pos="right"):
    """Póster 'Reclaim' — SISTEMA TIPOGRÁFICO MEDIDO del banner original de Paola.
    NO inventar tamaños ni espacios: todo va en RATIOS de H (cuerpo del titular bold, def. 78px).
      · Acento = Mencken Std Head italic rol 'acento' (master 400 + trazo 2.5%, regla de masters) en caja
        que ABRAZA el texto: 0.564·H · azul-medio #9fb2c6.
        Caja: padding 0.14·fe vertical / 0.50·fe horizontal (fe = cuerpo del acento) + nudge en em
        (top/left) para CENTRAR la tinta perfecta en AMBOS ejes — el bearing itálico la descentra.
      · Titular = 2 líneas Mencken Std: bold = H (grande) + regular = 0.69·H (más pequeña).
        Interlínea bold→regular = 0.22·H con line-height 1.0 (punto medio, no pegado).
      · Tagline = POPPINS itálica 300 = 0.42·H · azul-medio.  (NO serif.)
      · Lista  = POPPINS itálica 400 = 0.38·H · blanca, con conector de nodos.  (NO serif.)
      · Ritmo de bloques (aire): acento→titular 0.10·H (apretado) · titular→tagline 0.74·H ·
        tagline→lista 0.59·H · lista→pill 0.92·H.
      · LOGO ARRIBA por CRITERIO DE CONTRASTE (logo_pos: 'right' por defecto, porque bg_particulas
        carga arriba-izq.; va donde el fondo esté limpio/oscuro, nunca sobre partículas/luz). El
        bloque de texto + pill quedan anclados abajo (justify flex-start + flex spacer); fondo respira.
    Cambiar H reescala TODO manteniendo las proporciones. Márgenes del lienzo = content() (104px)."""
    acc = "#9fb2c6"  # azul-medio legible sobre navy (blue-deep)
    def _sp(px): return '<div style="height:%dpx;"></div>' % round(px)
    # CRITERIO DE CONTRASTE: colocar el logo donde el fondo está limpio/oscuro, NO sobre el área
    # cargada de partículas/luz. Con bg_particulas (partículas arriba-izq.) -> logo a la DERECHA.
    _lp = {"left":"flex-start","center":"center","right":"flex-end"}.get(logo_pos, "flex-end")
    top = ('<div style="display:flex;justify-content:%s;">%s</div>'
           % (_lp, logo("principal", logo_theme, h=round(H*1.0))))
    # Acento en caja: padding en px derivado del cuerpo (no em heredado) + line-height:1 +
    # micro-nudge para CENTRAR la tinta simétrica (como Paola: ~igual aire arriba/abajo).
    _fe = round(H*0.564)
    eb = ('<div style="align-self:flex-start;">'
          '<span style="display:inline-block;border:1.6px solid var(--blue-deep);border-radius:3px;'
          'padding:%dpx %dpx;line-height:1;">'
          '<span style="%sline-height:1;position:relative;'
          'top:-.17em;left:-.035em;">%s</span></span></div>'
          % (round(_fe*0.14), round(_fe*0.50), it_css("acento",_fe,acc), eyebrow_box))
    hd = '<h1 class="dh" style="margin:0;letter-spacing:.002em;">'
    hd += '<div style="font-size:%dpx;font-weight:700;line-height:1.0;">%s</div>' % (round(H), head_bold)
    if head_reg:
        hd += ('<div style="font-size:%dpx;font-weight:400;line-height:1.0;margin-top:%dpx;">%s</div>'
               % (round(H*0.692), round(H*0.22), head_reg))
    hd += '</h1>'
    block = eb + _sp(H*0.10) + hd
    if tagline:
        block += _sp(H*0.74) + ('<div style="font-family:\'Poppins\',sans-serif;font-style:italic;'
            'font-weight:300;font-size:%dpx;line-height:1.42;color:%s;">%s</div>'
            % (round(H*0.423), acc, tagline))
    if lista:
        its = "".join('<div style="font-family:\'Poppins\',sans-serif;font-style:italic;font-weight:400;'
                      'font-size:%dpx;color:#fff;margin:%dpx 0;line-height:1.2;">%s</div>'
                      % (round(H*0.385), round(H*0.10), i) for i in lista)
        block += _sp(H*0.59) + ('<div class="conx" style="grid-template-columns:46px 1fr;gap:0 28px;">'
                 '<div class="ln"></div><div>%s</div></div>' % its)
    # Logo ARRIBA del lienzo; el bloque de texto + pill quedan anclados abajo (fondo respira en medio).
    inner = top + '<div style="flex:1;"></div>' + block
    if contacto:
        inner += _sp(H*0.92) + pill()
    return lienzo(formato, content(inner, justify="flex-start"), fondo=fondo, theme=theme)

def t_concepto(term, term_it=None, bar=None, body=None, fondo=None, formato="post_v",
               theme="navy", logo_theme="blanco", logo_pos="top", contacto=True):
    """Concepto 'Exosomes': término Mencken display + barra-acento + cuerpo. Claro u oscuro."""
    lg=logo("principal",logo_theme,h=64)
    spans=f'<span class="it">{term}</span>'
    blk=titular(spans, size=104)
    if bar:
        _bar = "<span class='serif' style='font-size:34px;'>%s</span>" % bar
        blk += '<div style="margin-top:6px;">%s</div>' % hl(_bar, "mid")
    if body: blk+='<div style="height:24px;"></div>'+parrafo(body,it=True)
    inner=(lg+f'<div style="margin-top:120px;max-width:62%;">{blk}</div>'
           +(f'<div style="margin-top:auto;">{pill()}</div>' if contacto else ''))
    return lienzo(formato, content(inner), fondo=fondo, theme=theme)

def t_concepto_hero(term, bar, body=None, fondo=None, formato="poster_v", theme="light",
                    logo_pos="left"):
    """Concepto 'Exosomes' — POSICIÓN ABSOLUTA por RATIO MEDIDO del original de Paola (tema claro).
      · Logo principal arriba (navy en claro / blanco en oscuro): top 0.114·H · left 0.133·W · alto 0.067·H.
        `logo_pos`='left'|'right' por CRITERIO DE CONTRASTE (donde el fondo esté limpio).
      · term = palabra estrella Mencken Head itálico 0.094·W, top 0.379·H, left 0.118·W. MASTER por regla:
        tema claro (navy sobre claro) -> rol 'hero_claro' (400 + trazo 2.2%); tema oscuro -> 'hero_oscuro' (800).
      · bar = sub-barra que ABRAZA el texto: fondo azul-gris rgba(93,118,140,.46), top 0.440·H (pegada a la
        base del término), left 0.108·W, padding 0.005·H / 0.020·W; texto Mencken itálico 0.041·W rol
        'elegante' (400 + trazo 1%) — medido: 'are cellular messengers' es delicado, NO grueso.
      · body = Poppins itálica 400 · 0.033·W · interlínea 1.25 · top 0.503·H · left 0.132·W · tinta #3a4352
        (claro) / #eef1f4 (oscuro). Admite <br>.
      · pill institucional en 0.93·H. Fondo por defecto GRAD_BLUE (claro) / GRAD_NAVY_DEEP (oscuro); la
        foto tratada va vía `fondo` (zona derecha libre para la imagen)."""
    w,h=PRESETS[formato]; Y=lambda r:round(h*r); X=lambda r:round(w*r)
    light=(theme=="light")
    navy="#26313f"; term_col=navy if light else "#a7c0d6"
    body_col="#3a4352" if light else "#eef1f4"
    barfill="rgba(93,118,140,.46)" if light else "rgba(202,211,221,.22)"
    lg_theme="navy" if light else "blanco"
    lx=X(0.133) if logo_pos=="left" else None
    logo_html=('<div style="position:absolute;top:%dpx;%s">%s</div>'
        %(Y(0.114), (f"left:{lx}px;" if lx is not None else f"right:{X(0.133)}px;"), logo("principal",lg_theme,h=Y(0.067))))
    rol_term="hero_claro" if light else "hero_oscuro"
    term_html=('<div style="position:absolute;top:%dpx;left:%dpx;line-height:1;z-index:2;%s">%s</div>'
        %(Y(0.379),X(0.118),it_css(rol_term,X(0.094),term_col),term))
    bar_html=('<div style="position:absolute;top:%dpx;left:%dpx;">%s</div>'
        %(Y(0.440)+aire_desc(term,X(0.094),0),X(0.118),barra(bar,X(0.041),it_css("elegante",X(0.041),term_col),fondo=barfill)))
    body_html=''
    if body:
        body_html=('<div style="position:absolute;top:%dpx;left:%dpx;font-family:\'Poppins\',sans-serif;'
            'font-style:italic;font-weight:400;font-size:%dpx;line-height:1.25;color:%s;">%s</div>'
            %(Y(0.503),X(0.132),X(0.033),body_col,body))
    cap='<div style="position:absolute;top:%dpx;left:104px;right:104px;">%s</div>'%(Y(0.93),pill())
    inner='<div style="position:absolute;inset:0;z-index:2;">%s</div>'%(logo_html+term_html+bar_html+body_html+cap)
    bg=fondo if fondo is not None else (GRAD_BLUE if light else GRAD_NAVY_DEEP)
    return lienzo(formato, inner, fondo=bg, theme=theme)

def t_story(eyebrow_txt, head_spans, sub=None, cta_pill=True, fondo=None, formato="story",
            theme="navy", sello="principal", sello_theme="blanco"):
    """Story editorial: sello/wordmark arriba · titular display abajo · pill."""
    # Logo al estándar de marca (la Dra., 25-oct-2026: en historias quedaba muy pequeño): principal ~22% del ancho.
    top=logo(sello,sello_theme,h=120 if sello!='principal' else 108)
    blk=eyebrow(eyebrow_txt)+'<div style="height:22px;"></div>'+titular(head_spans,size=86)
    if sub: blk+='<div style="height:24px;"></div>'+subhead(sub)
    blk+='<div style="height:38px;"></div>'+hairline()
    inner=(top+f'<div style="margin-top:auto;">{blk}</div>'
           +(f'<div style="margin-top:48px;">{pill()}</div>' if cta_pill else ''))
    return lienzo(formato, content(inner, pad="108px"), fondo=fondo, theme=theme)

def t_seal_hero(head_reg, head_it, lista=None, fondo=None, formato="story_hero",
                theme="navy", sello_theme="claro", acc="#9aacbb", pill_radius=16):
    """Story hero 'DNA/heal' — POSICIÓN ABSOLUTA por RATIO MEDIDO del original de Paola (sin flex).
    Cada elemento se ancla a su fracción exacta del lienzo; cambiar el preset reescala todo igual.
      · Sello CENTRADO (cx 0.46·W) · alto 0.135·H · top 0.076·H.
      · Titular en DOS estilos de la MISMA tipografía Mencken y MISMO tamaño (0.056·W): línea 1
        RECTA (Mencken Std BOLD 700, blanca) arriba, línea 2 CURSIVA (Mencken Head italic MASTER 800
        = rol 'hero_oscuro', azul acc) abajo — medido: 'We know how to activate it.' es 800 porque es
        protagonista claro sobre oscuro. La jerarquía es recta vs cursiva. Interlínea 1.18.
        Recto top 0.603·H · cursiva top 0.677·H · ambos left 0.345·W.
      · Hairline blanca fina en 0.776·H, de x 0.317·W a 0.917·W (ancho 0.60·W).
      · Lista mayúscula Poppins itálica (0.024·W) con viñeta estrella dorada (&#10022;), interlínea
        apretada; top 0.803·H, left 0.355·W.
      · Cápsula = RECTÁNGULO redondeado (radio 16px, no píldora), top 0.895·H, márgenes 104px.
      · Fondo por defecto navy casi negro (GRAD_NAVY_DEEP); la foto tratada (lci_treat) va detrás.
    head_reg/head_it admiten <br>. Devuelve HTML listo para render.py."""
    w,h=PRESETS[formato]
    Y=lambda r: round(h*r); X=lambda r: round(w*r); F=X(0.056)  # cuerpo titular medido del original
    seal=('<div style="position:absolute;top:%dpx;left:46%%;transform:translateX(-50%%);">%s</div>'
          % (Y(0.076), logo("sello",sello_theme,h=Y(0.135))))
    # Titular = grupo anclado arriba (recto) que FLUYE a la cursiva: nunca se solapan y el
    # cap-top de la 1a linea cae en ~0.603H. Gap recto->cursiva 0.012H (medido).
    head=('<div style="position:absolute;top:%dpx;left:%dpx;">'
          '<div style="font-family:\'Mencken Std\',serif;font-weight:700;font-size:%dpx;'
          'line-height:1.0;color:#fff;">%s</div>'
          '<div style="height:%dpx;"></div>'
          '<div style="%sline-height:1.08;">%s</div>'
          '</div>') % (Y(0.598), X(0.345), F, head_reg, Y(0.012), it_css("hero_oscuro",F,acc), head_it)
    hair=('<div style="position:absolute;top:%dpx;left:%dpx;width:%dpx;height:1.6px;'
          'background:rgba(255,255,255,.85);"></div>' % (Y(0.776),X(0.317),X(0.60)))
    lst=''
    if lista:
        rows=''.join(('<div style="display:flex;align-items:baseline;gap:16px;margin:%dpx 0;">'
              '<span style="color:var(--gold);font-size:%dpx;line-height:1;">&#10022;</span>'
              '<span style="font-family:\'Poppins\',sans-serif;font-style:italic;font-weight:400;'
              'font-size:%dpx;letter-spacing:.05em;color:#fff;line-height:1.15;">%s</span></div>'
              % (Y(0.0015), X(0.026), X(0.024), t)) for t in lista)
        lst='<div style="position:absolute;top:%dpx;left:%dpx;">%s</div>' % (Y(0.803),X(0.355),rows)
    cap='<div style="position:absolute;top:%dpx;left:104px;right:104px;">%s</div>' % (Y(0.895), pill())
    body='<div style="position:absolute;inset:0;z-index:2;">%s</div>' % (seal+head+hair+lst+cap)
    html=lienzo(formato, body, fondo=(fondo if fondo is not None else GRAD_NAVY_DEEP), theme=theme)
    return html.replace("</head>", "<style>.pill{border-radius:%dpx;}</style></head>" % pill_radius, 1)

def t_timeline(eyebrow, head, marks, statement, body=None, unit="YEARS",
               fondo=None, formato="poster_v", theme="navy",
               cream="#c9bda8", lblue="#a7c0d6", stmt="#cbd6e0", sello_theme="claro"):
    """Afiche 'Creatine timeline / Muscle Cells' — TODO en RATIOS MEDIDOS del original de Paola.
    CRITERIO DE COLUMNA (exigido por la Dra.): el eyebrow, la fila de gotas, la línea punteada y la
    unidad quedan JUSTIFICADOS al ancho exacto del TITULAR ('head'). Se logra sin medir: la columna
    es un `inline-block` que se ajusta a su hijo más ancho (el titular); los demás van a width:100%.
      · eyebrow = POPPINS ITÁLICA (no recto) mayúscula, justificada de borde a borde (text-align-last
        justify) sobre la columna · crema. (Medido: original inclinado, mismo ancho que el titular.)
      · head = Mencken Std Head itálico 800 · 0.098·W · light-blue. DEFINE el ancho de la columna.
      · Timeline de gotas: `marks`=[(label, nivel 0..1)]. Gotas justificadas (space-between): la 1a en
        el borde izq, la última en el derecho. LÍQUIDO CLARO que BAJA con el nivel (medido: líquido
        brillante ~80, aire oscuro ~30) → el nivel se LEE sobre el navy. Línea punteada al ancho de
        la columna + unidad ('YEARS') centrada, Poppins 600 tracking .34em.
      · statement = barra-acento izquierda + jerarquía por TAMAÑO: líneas superiores Mencken bold
        0.032·W (stmt) y PALABRA ESTRELLA abajo en Mencken Head itálico 800 0.052·W (light-blue) ≈2×.
        `statement`=(html_superior_con_<br>, palabra_estrella).
      · body = [(negrita, resto)] en Poppins itálica (negrita 700 + resto 400), tops 0.675 y 0.746.
      · Sello claro 0.11·H en 0.63·W/0.775·H · pill institucional en 0.93·H.
      · Fondo por defecto GRAD_NAVY_DEEP; la foto tratada (lci_treat) va detrás vía `fondo`.
    Ritmo vertical (aire entre bloques) medido y fijo en ratios de H. Cambiar el preset reescala todo."""
    w,h=PRESETS[formato]; Y=lambda r:round(h*r); X=lambda r:round(w*r)
    LX=X(0.22); SX=X(0.185); HEADF=X(0.098); EYEF=X(0.030); DW=X(0.05)
    def drop(f):  # f=1 llena (líquido claro), 0 vacía -> nivel que baja con la edad
        fillh=44*f; ytop=52-fillh; DP="M20 3 C20 3 5 25 5 37 A15 15 0 0 0 35 37 C35 25 20 3 20 3 Z"; i=int(f*1000)
        return ('<svg width="%d" height="%d" viewBox="0 0 40 56">'
          '<defs><clipPath id="c%d"><path d="%s"/></clipPath></defs>'
          '<path d="%s" fill="rgba(180,196,214,.09)"/>'
          '<rect x="0" y="%.1f" width="40" height="%.1f" fill="rgba(200,215,231,.62)" clip-path="url(#c%d)"/>'
          '<rect x="0" y="%.1f" width="40" height="1.5" fill="rgba(232,240,248,.9)" clip-path="url(#c%d)"/>'
          '<ellipse cx="14" cy="25" rx="2.6" ry="5" fill="rgba(255,255,255,.55)"/>'
          '<path d="%s" fill="none" stroke="#dbe3ea" stroke-width="1.7"/></svg>'
          )%(DW,DW*56//40,i,DP,DP,ytop,fillh,i,ytop,i,DP)
    cells=''.join('<div style="display:flex;flex-direction:column;align-items:center;">%s'
        '<div style="font-family:\'Poppins\',sans-serif;font-weight:400;font-size:%dpx;color:%s;'
        'margin-top:8px;">%s</div></div>'%(drop(lv),X(0.024),cream,lb) for lb,lv in marks)
    # COLUMNA: inline-block => ancho = hijo más ancho (el titular). Los demás llenan al 100%.
    # eyebrow: tracking UNIFORME calibrada al ancho del titular en el render (JS), NO justify por
    # palabras (que deja huecos desiguales). Fallback .16em centrado si no corre JS.
    col=('<div style="position:absolute;top:%dpx;left:%dpx;display:inline-block;">'%(Y(0.252),LX)
      +'<div style="width:100%%;text-align:center;line-height:1;"><span id="tl-eye" '
       'style="display:inline-block;white-space:nowrap;font-family:\'Poppins\',sans-serif;'
       'font-style:italic;font-weight:400;font-size:%dpx;letter-spacing:.16em;color:%s;">%s</span></div>'
       %(EYEF,cream,eyebrow)
      +'<div id="tl-head" style="margin-top:%dpx;font-family:\'Mencken Std Head\',\'Mencken Std\',serif;'
       'font-style:italic;font-weight:800;font-size:%dpx;line-height:1;color:%s;white-space:nowrap;">%s</div>'
       %(Y(0.004),HEADF,lblue,head)
      +'<div style="display:flex;justify-content:space-between;align-items:flex-end;width:100%%;'
       'margin-top:%dpx;">%s</div>'%(Y(0.050),cells)
      +'<div style="border-top:1.5px dashed rgba(255,255,255,.5);width:100%%;margin-top:%dpx;"></div>'%Y(0.014)
      +'<div style="text-align:center;width:100%%;font-family:\'Poppins\',sans-serif;font-weight:600;'
       'letter-spacing:.34em;font-size:%dpx;color:#fff;margin-top:%dpx;">%s</div>'%(X(0.024),Y(0.028),unit)
      +'</div>')
    # calibra la tracking del eyebrow para que su ancho = ancho del titular (tracking uniforme)
    col+=('<script>window.addEventListener("load",function(){'
          'var h=document.getElementById("tl-head"),e=document.getElementById("tl-eye");'
          'if(h&&e){var t=h.getBoundingClientRect().width;e.style.letterSpacing="0px";'
          'var w0=e.getBoundingClientRect().width,n=(e.textContent||"").length;'
          'if(n>0){var a=(t-w0)/n;if(a<0)a=0;e.style.letterSpacing=a+"px";}}});</script>')
    st_top,st_star=statement
    stmt_html=('<div style="position:absolute;top:%dpx;left:%dpx;border-left:2.5px solid %s;'
       'padding-left:%dpx;">'%(Y(0.575),SX,lblue,X(0.022))
      +'<div style="font-family:\'Mencken Std\',serif;font-weight:700;font-size:%dpx;line-height:0.98;'
       'color:%s;">%s</div>'%(X(0.032),stmt,st_top)
      +'<div style="font-family:\'Mencken Std Head\',\'Mencken Std\',serif;font-style:italic;'
       'font-weight:800;font-size:%dpx;line-height:0.92;color:%s;margin-top:%dpx;">%s</div>'
       %(X(0.052),lblue,Y(0.005),st_star)+'</div>')
    bod=''
    if body:
        tops=[0.675,0.746]
        for k,(strong,rest) in enumerate(body):
            ty=Y(tops[k]) if k<len(tops) else Y(0.675+0.071*k)
            bod+=('<div style="position:absolute;top:%dpx;left:%dpx;">'%(ty,SX+X(0.022))
              +'<div style="font-family:\'Poppins\',sans-serif;font-style:italic;font-weight:700;'
               'font-size:%dpx;line-height:1.15;color:#fff;">%s</div>'%(X(0.026),strong)
              +'<div style="font-family:\'Poppins\',sans-serif;font-style:italic;font-weight:400;'
               'font-size:%dpx;line-height:1.18;color:#eef1f4;">%s</div>'%(X(0.026),rest)+'</div>')
    sello=('<div style="position:absolute;top:%dpx;left:%dpx;">%s</div>'
           %(Y(0.775),X(0.63),logo("sello",sello_theme,h=Y(0.11))))
    cap='<div style="position:absolute;top:%dpx;left:104px;right:104px;">%s</div>'%(Y(0.93),pill())
    body_html='<div style="position:absolute;inset:0;z-index:2;">%s</div>'%(col+stmt_html+bod+sello+cap)
    return lienzo(formato, body_html, fondo=(fondo if fondo is not None else GRAD_NAVY_DEEP), theme=theme)

def t_curso(eyebrow_txt, term, term2=None, bar=None, sub=None, oferta=None,
            precio=None, formato="post", logo_theme="blanco"):
    """Curso de péptidos — fondo azul eléctrico radial + oro para precio/oferta."""
    blk=''
    if eyebrow_txt: blk+=hl(f'<span class="serif" style="font-size:32px;">{eyebrow_txt}</span>',"mid")+'<br>'
    spans=f'<span class="it cream">{term}</span>'
    if term2: spans+=f'<br><span class="it cream">{term2}</span>'
    blk+=titular(spans,size=110)
    if sub: blk+='<div style="height:18px;"></div>'+subhead(sub,it=True)
    if oferta: blk+='<div style="height:26px;"></div>'+goldbox(f'<div class="body" style="color:#fff;">{oferta}</div>')
    if precio: blk+=('<div style="height:24px;"></div><div style="display:inline-block;background:var(--navy-deep);'
                     'padding:12px 26px;border-radius:8px;"><span class="serif" style="font-size:46px;color:var(--gold-soft);font-weight:800;">'
                     f'{precio}</span></div>')
    foot=f'<div style="margin-top:auto;">{logo("principal",logo_theme,h=70)}</div>'
    return lienzo(formato, content(blk+foot), fondo=GRAD_CURSO, theme="navy")

def t_cita(texto, autor=None, fondo=None, formato="post_v", theme="navy"):
    q='<div style="font-family:\'Mencken Std Head\',serif;font-style:italic;font-size:170px;color:var(--gold-soft);line-height:.5;opacity:.6;">“</div>'
    cuerpo=f'<div class="serif" style="font-size:62px;line-height:1.18;color:#fff;text-align:center;font-weight:700;">{texto}</div>'
    firma=''
    if autor: firma=f'<div style="height:30px;"></div>{rule_left()}<div class="kicker" style="margin-top:20px;text-align:center;">{autor}</div>'
    inner=(f'<div style="margin:auto 0;text-align:center;display:flex;flex-direction:column;align-items:center;">{q}'
           f'<div style="height:16px;"></div>{cuerpo}{firma}</div>'
           f'<div style="display:flex;justify-content:center;">{logo("principal","blanco",h=56)}</div>')
    return lienzo(formato, content(inner), fondo=fondo, theme=theme)

if __name__=="__main__":
    print("marca.py v2 OK ·",len(F),"fuentes ·",len(LG),"logos ·",list(PRESETS))
