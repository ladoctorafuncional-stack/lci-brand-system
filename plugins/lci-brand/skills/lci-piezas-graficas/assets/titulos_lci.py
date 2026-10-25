# -*- coding: utf-8 -*-
"""Biblioteca de diagramaciones de título LCI (oct 2026) — 8 estilos aportados por la Dra. + 3 variantes.
Uso: import marca as M; import titulos_lci as T; T.M=M; html=T.hd("Medir antes de","intervenir.",True,92,v="tagbox",tag="Cómo trabajamos")
Después de usar un estilo con filete/kicker propio, llamar T.consumir(inner) sobre el HTML de la página para
eliminar el filete (<div class="rl">) o el kicker (<p class="kk">) genérico que sobra (flags norl/nokk).
Estilos: panel, pills, tagbox, caps, vrule, glass, rulesub, bar + plain/marker (titular limpio, sin marcador), gold, block (barra que abraza). Regla: <=2 usos por estilo y nunca en páginas contiguas."""
import re as _re
M=None
NAVY='#2A3649';BLUE='#CAD3DD';GOLD='#D2B58A';MID='#5D768C'
_FLAG={'norl':False,'nokk':False}
# REGLAS DURAS (oct 2026, tras revisión del brochure por la Dra.):
#  · Titular = Mencken bold + acento Mencken Head itálico, MISMO tamaño, line-height 1.0 y CERO margen entre líneas
#    (una frase partida en dos líneas es UN bloque). Nunca cambiar de familia/peso a mitad de frase (p. ej. Poppins
#    bold → Poppins light): la jerarquía es recta/cursiva o color, no peso.
#  · Eyebrow en versalitas («Muscle Cells» de Paola): Poppins itálica light, ~0.40× la estrella, PEGADO (aire de tinta
#    ≈0.20× estrella) y justificado al ancho de la estrella.
#  · Resaltados: solo barras que ABRAZAN el texto (M.barra). Prohibidos subrayados/marcadores gruesos y cajas altas.
#  · Interlineado: ver references/estandar-visual-2026/INTERLINEADO-BLINDADO.md (M.ritmo).
_JUST='''<script>(function(){function f(){document.querySelectorAll('[data-just]').forEach(function(e){var t=document.getElementById(e.dataset.just);if(!t)return;
var r=document.createRange();r.selectNodeContents(t);var W=r.getBoundingClientRect().width;e.style.letterSpacing='0px';
var r2=document.createRange();r2.selectNodeContents(e);var w=r2.getBoundingClientRect().width;var n=Math.max(1,e.textContent.length-1);
var fs=parseFloat(getComputedStyle(e).fontSize);var ls=(W-w)/n;if(ls<0)ls=0;if(ls>0.35*fs){ls=0.2*fs;}e.style.letterSpacing=ls+'px';});}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){document.fonts.ready.then(f)});else document.fonts.ready.then(f);})();</script>'''
_N=[0]
def _tit(bold,acc,size,tx,ac,role):
    """Bloque titular estándar: bold + acento itálico, mismo tamaño, lh 1.0, sin aire entre líneas."""
    return (f'<div data-opt style="font-family:\'Mencken Std\',serif;font-weight:700;font-size:{size}px;line-height:1.0;color:{tx}">{bold}</div>'
            f'<div data-opt style="{M.it_css(role,size,ac)}line-height:1.04">{acc}</div>')
def hd(bold,acc,light=False,size=86,v='marker',tag=None,tags=None):
    tx=NAVY if light else '#FFFFFF'; ac=MID if light else '#9fb2c6'
    ln=MID if light else 'rgba(202,211,221,.55)'
    role='hero_claro' if light else 'hero_oscuro'
    PO="font-family:'Poppins',sans-serif;"
    _FLAG['norl']=False; _FLAG['nokk']=False
    if v in ('marker','gold','plain'):   # titular limpio (sin marcador): el acento se distingue por cursiva + color
        col=GOLD if (v=='gold' and not light) else ac
        return _tit(bold,acc,size,tx,col,role) + M.OPTICA_JS
    if v=='block':   # acento dentro de barra sólida que ABRAZA el texto (sin caja alta)
        bg=NAVY if light else BLUE; fc='#EDE5DA' if light else NAVY
        return (f'<div data-opt style="font-family:\'Mencken Std\',serif;font-weight:700;font-size:{size}px;line-height:1.0;color:{tx};position:relative;z-index:2">{bold}</div>'
                f'<div style="margin:{M.aire_desc(bold,size,round(size*.06))}px 0 0 -{round(size*.12)}px">'
                + M.barra(acc,size,M.it_css("acento",size,fc),fondo=bg,pad_x=(.12,.18)) + '</div>' + M.OPTICA_JS)
    if v=='panel':   # ref 1 «The brain ages too»: titular en recuadro de filete fino
        _FLAG['norl']=True
        bg='rgba(255,255,255,.45)' if light else 'rgba(14,20,32,.42)'
        return (f'<div style="width:fit-content;align-self:flex-start;max-width:100%;border:1.6px solid {ln};padding:{round(size*.44)}px {round(size*.58)}px {round(size*.47)}px;background:{bg};box-shadow:0 14px 40px rgba(14,20,32,.18)">'
                + _tit(bold,acc,size,tx,ac,role) + f'</div><div style="width:1.5px;height:{round(size*.7)}px;background:{ln};margin:0 0 0 {round(size*.8)}px"></div>' + M.OPTICA_JS)
    if v=='pills':   # ref 2 «Healthspan»: término Poppins 700 (acento mismo tamaño en color) + píldoras + filete
        _FLAG['norl']=True
        pl=''.join(f'<span style="display:inline-block;border:1.4px solid {ln};border-radius:40px;padding:9px 28px;font-size:17px;letter-spacing:.2em;text-transform:uppercase;color:{tx};margin-right:16px">{t}</span>' for t in (tags or ()))
        return (f'<h1 style="{PO}font-weight:700;font-size:{round(size*.98)}px;line-height:1.0;letter-spacing:-.01em;margin:0;color:{tx}">{bold}<br><span style="color:{ac}">{acc}</span></h1>'
                f'<div style="margin:{round(size*.22)}px 0 {round(size*.5)}px">{pl}</div><div style="height:1.4px;background:{ln};width:100%;margin-bottom:{round(size*.35)}px"></div>')
    if v=='tagbox':  # ref 3 «Antioxidant pills» (Paola Reclaim): recuadro-acento + bold + regular de apoyo (ratios t_poster)
        _FLAG['nokk']=True
        tb='rgba(237,229,218,.80)' if not light else 'rgba(93,118,140,.24)'; fe=round(size*.564)
        return (f'<div style="align-self:flex-start;margin-bottom:{round(size*.10)}px"><span style="display:inline-block;background:{tb};padding:{round(fe*.18)}px {round(fe*.5)}px;line-height:1;border-radius:3px">'
                f'<span style="{M.it_css("acento",fe,NAVY)}line-height:1;position:relative;top:-.12em">{tag}</span></span></div>'
                f'<div data-opt style="font-family:\'Mencken Std\',serif;font-weight:700;font-size:{size}px;line-height:1.0;color:{tx}">{bold}</div>'
                f'<div data-opt style="font-family:\'Mencken Std\',serif;font-weight:400;font-size:{round(size*.692)}px;line-height:1.0;color:{tx};margin-top:{round(size*.22)}px">{acc}</div>' + M.OPTICA_JS)
    if v=='caps':    # ref 4 «Muscle Cells» (Paola, medido): eyebrow versal itálica PEGADO y justificado al ancho de la estrella
        st=round(size*1.55); eb=round(st*.40); _N[0]+=1; sid=f'st{_N[0]}'
        return (f'<div style="display:inline-block;align-self:flex-start">'
                f'<div data-just="{sid}" style="{PO}font-style:italic;font-weight:300;font-size:{eb}px;line-height:.78;text-transform:uppercase;color:{tx};white-space:nowrap">{bold}</div>'
                f'<div style="line-height:1;margin-top:{round(st*.20)-round(st*.205)}px"><span id="{sid}" style="{M.it_css(role,st,ac)}line-height:1;white-space:nowrap">{acc}</span></div></div>'
                + _JUST + M.OPTICA_JS)
    if v=='vrule':   # ref 5: filete vertical a la izquierda del titular
        return (f'<div style="border-left:3px solid {ln if light else BLUE};padding:{round(size*.06)}px 0 {round(size*.10)}px {round(size*.46)}px">'
                + _tit(bold,acc,size,tx,ac,role) + '</div>' + M.OPTICA_JS)
    if v=='glass':   # ref 6 «Gut bacteria»: tarjeta de vidrio; título Poppins + subtítulo (idea distinta) pegado
        bg='rgba(255,255,255,.5)' if light else 'rgba(202,211,221,.10)'
        _FLAG['norl']=True
        return (f'<div style="border:1.4px solid {ln};border-radius:22px;padding:44px 52px 48px;background:{bg};backdrop-filter:blur(10px);box-shadow:0 18px 50px rgba(14,20,32,.22)">'
                f'<h1 style="{PO}font-weight:600;font-size:{round(size*.86)}px;line-height:1.0;margin:0;color:{tx}">{bold}</h1>'
                f'<div style="{PO}font-weight:300;font-style:italic;font-size:{round(size*.45)}px;line-height:1.32;color:{ac};margin-top:{round(size*.14)}px">{acc}</div></div><div style="height:34px"></div>')
    if v=='rulesub': # ref 7 «What is social jet lag?»: titular + filete + texto (ratios de r_derecha)
        _FLAG['norl']=True
        return (f'<div data-opt style="font-family:\'Mencken Std\',serif;font-weight:700;font-size:{size}px;line-height:1.0;color:{tx}">{bold}</div>'
                f'<div style="height:1.5px;background:{ln};width:100%;margin:{round(size*.515)}px 0 {round(size*.394)}px"></div>'
                f'<div style="{PO}font-style:italic;font-weight:300;font-size:{round(size*.4545)}px;line-height:1.4;color:{ac}">{acc}</div>' + M.OPTICA_JS)
    if v=='bar':     # ref 8 «Exosomes» (Paola): estrella Mencken itálica + SUB-BARRA que ABRAZA el texto
        band='rgba(93,118,140,.46)' if light else 'rgba(202,211,221,.22)'
        st=round(size*1.18); fb=round(st*0.47)
        return (f'<div style="line-height:1.0;position:relative;z-index:2">{M.menc_it(bold,role,st,tx)}</div>'
                f'<div style="align-self:flex-start;margin:{M.aire_desc(bold,st,round(st*0.12))}px 0 0 -10px">'
                + M.barra(acc, fb, M.it_css("elegante", fb, tx), fondo=band) + '</div>')
    raise ValueError(v)

def consumir(inner):
    if _FLAG['nokk']: inner=_re.sub(r'<p class="kk"[^>]*>.*?</p>','',inner,count=1)
    if _FLAG['norl']: inner=inner.replace('<div class="rl"></div>','',1)
    _FLAG['norl']=False; _FLAG['nokk']=False
    return inner
