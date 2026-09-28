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

# ───────── FORMATOS (px) ─────────
PRESETS = {
    "story": (1080,1920), "reel": (1080,1920), "post": (1080,1080),
    "post_v": (1080,1350), "carrusel": (1080,1350), "infografia": (1080,1920),
    "flyer": (1240,1754), "flyer_hd": (2480,3508), "banner": (1200,630),
    "banner_v": (1080,1350), "email_sig": (1500,400), "carnet": (1000,1400),
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
    return f'<img src="{_uri(key)}" style="{style}display:block;">'

def logo_cr(kind="wordmark", color=None, theme="claro", h=None):
    """Marca personal CR. kind: wordmark|sello. color=hex para recolorear (p.ej. beige sobre foto)."""
    key=f"cr_{kind}_{theme}"
    src = mark_recolor(f"cr_{kind}_claro", color) if color else _uri(key)
    style=f'height:{h}px;' if h else ''
    return f'<img src="{src}" style="{style}display:block;">'

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
.hairline{height:2px;background:linear-gradient(90deg,transparent,var(--gold),transparent);border:0;opacity:.8;}
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
.pill{display:flex;align-items:center;justify-content:center;gap:20px;border:1.6px solid rgba(202,211,221,.45);
  border-radius:60px;padding:16px 30px;font-size:21px;color:var(--blue);font-weight:300;}
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
    return f'<span class="{c}">{t}</span>'
def caja(inner,gold=False): return f'<span class="h-box{" gold" if gold else ""}">{inner}</span>'
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
def pill(institucional=True, fill=False):
    if institucional:
        cells=[f'<span class="wa">{_WA}</span><span>(+57) 301 512 39 91</span>',
               '<span>@longevityclinicalinstitute</span>','<span>longevityclinicalinstitute.com</span>']
    else:
        cells=[f'<span class="wa">{_WA}</span><span>(+57) 301 512 39 91</span>',
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
            f'<title>LCI {formato}</title><style>{base_css(w,h)}</style></head>'
            f'<body><div class="lienzo{tc}" id="lienzo">{_bg(fondo)}{body}</div></body></html>')

def content(inner, pad="104px", justify="space-between", align="stretch", gap="0"):
    return (f'<div class="content" style="padding:{pad};justify-content:{justify};'
            f'align-items:{align};gap:{gap};">{inner}</div>')

# ───────── TEMPLATES DE ALTO NIVEL (salen siempre con el estilo Paola) ─────────
def t_poster(eyebrow_box, head_bold, head_reg=None, tagline=None, lista=None,
             fondo=None, formato="post_v", theme="navy", logo_theme="blanco", contacto=True):
    """Póster 'Reclaim': wordmark · caja-acento + titular bold + reg · tagline · conector·lista · pill."""
    top=logo("principal",logo_theme,h=70)
    block=f'<div style="margin-bottom:18px;">{caja(f"<span class=\'serif-it blue\'>{eyebrow_box}</span>")}</div>'
    spans=f'<span class="reg">{head_bold}</span>'
    if head_reg: spans+=f'<br><span class="reg" style="font-weight:400;">{head_reg}</span>'
    block+=titular(spans, size=78)
    if tagline: block+='<div style="height:30px;"></div>'+subhead(tagline,it=True)
    if lista: block+='<div style="height:30px;"></div>'+conector(lista)
    inner=(top+f'<div style="margin-top:auto;">{block}</div>'
           +(f'<div style="margin-top:46px;">{pill()}</div>' if contacto else ''))
    return lienzo(formato, content(inner), fondo=fondo, theme=theme)

def t_concepto(term, term_it=None, bar=None, body=None, fondo=None, formato="post_v",
               theme="navy", logo_theme="blanco", logo_pos="top", contacto=True):
    """Concepto 'Exosomes': término Mencken display + barra-acento + cuerpo. Claro u oscuro."""
    lg=logo("principal",logo_theme,h=64)
    spans=f'<span class="it">{term}</span>'
    blk=titular(spans, size=104)
    if bar: blk+=f'<div style="margin-top:6px;">{hl(f"<span class=\'serif\' style=\'font-size:34px;\'>{bar}</span>","mid")}</div>'
    if body: blk+='<div style="height:24px;"></div>'+parrafo(body,it=True)
    inner=(lg+f'<div style="margin-top:120px;max-width:62%;">{blk}</div>'
           +(f'<div style="margin-top:auto;">{pill()}</div>' if contacto else ''))
    return lienzo(formato, content(inner), fondo=fondo, theme=theme)

def t_story(eyebrow_txt, head_spans, sub=None, cta_pill=True, fondo=None, formato="story",
            theme="navy", sello="principal", sello_theme="blanco"):
    """Story editorial: sello/wordmark arriba · titular display abajo · pill."""
    top=logo(sello,sello_theme,h=120 if sello!='principal' else 70)
    blk=eyebrow(eyebrow_txt)+'<div style="height:22px;"></div>'+titular(head_spans,size=86)
    if sub: blk+='<div style="height:24px;"></div>'+subhead(sub)
    blk+='<div style="height:38px;"></div>'+hairline()
    inner=(top+f'<div style="margin-top:auto;">{blk}</div>'
           +(f'<div style="margin-top:48px;">{pill()}</div>' if cta_pill else ''))
    return lienzo(formato, content(inner), fondo=fondo, theme=theme)

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
