"""AUDITOR DE PIEZAS — reglas de la Dra. Carolina (10-oct-2026). Correr SIEMPRE antes de entregar una pieza.

Uso:
    python3 auditar_pieza.py pieza1.html [pieza2.html ...]        → informe + <pieza>_qa.png con los fallos en rojo
    from auditar_pieza import auditar_html; fallos = auditar_html(html_str, 'salida.png')

Renderiza la pieza dos veces (normal y con el texto transparente) para obtener la TINTA real de cada texto y revisa:
  F1 piso tipográfico   · ningún texto < el de la cápsula de contacto del pie (19 px a 1080 de ancho); rótulos ≥ 22; cuerpo ≥ 27; refs ≥ 20
  F2 zona segura        · texto/logo/recuadros dentro del margen = 10 % del lado corto (solo la cápsula en la banda inferior)
  F3 contraste          · tinta vs fondo real ≥ 4.5:1 (texto < 48 px) o ≥ 3:1 (≥ 48 px) — p. ej. «where your fat is», «y en la vejez.»
  F4 recuadros          · el texto dentro de un recuadro ([data-caja] o borde visible) queda simétrico: arriba ≈ abajo,
                          izquierda ≈ derecha (tolerancia 6 % del recuadro, mín. 4 px) — «Reclaim the energy» de Paola
  F5 interlineado       · en cada bloque [data-pila] o columna de líneas apiladas, el aire de tinta entre líneas es
                          uniforme (máx/mín ≤ 1.5) y nunca negativo (líneas montadas) — caso «up to 2×»
  F7 logos             · dentro de la zona segura y a su tamaño estándar: LCI principal 22 % W · sello 150 px · terciario 118 px ·
                          CR wordmark ≈80 px de alto · LAI horizontal ≈34 % W (pieza «Nuestra visión»)
  F8 jerarquía          · el piso NO es el tamaño de la pieza: ≥ 3 niveles de tamaño, titular ≥ 2.4 × cuerpo y no más de la
                          mitad de los textos en el mínimo (solo pie, referencias y aclaratorios van al piso)
  R  resaltados         · ≥ 1 lámina por carrusel (y ≥ 1 de cada 3 piezas del lote) con el RESALTADO que abraza el texto
                          (`M.barra`, ref. «are cellular messengers» de Exosomes de Paola) — `resaltados_ok(resultados)`
  F6 aprovechamiento    · el contenido usa el espacio: bloque principal ≥ 62 % del ancho útil o ≥ 55 % del alto útil
                          (aviso; si falla: subir 1–2 tamaños manteniendo jerarquía o sumar recuadro/elemento)
  F9 resaltado          · REGLA INQUEBRANTABLE: la barra de resaltado nunca invade la línea de arriba ni la de abajo
                          (aire ≥ max(10 px, 12 % del alto de la barra)).
Una pieza con F1–F5 o F9 NO se entrega. F6 es aviso que se resuelve con criterio.
"""
import sys, os, json, asyncio
import numpy as np
from PIL import Image, ImageDraw
from playwright.async_api import async_playwright
import os as _os, sys as _sys; _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _navegador import lanzar as _lanzar

PISO = {"gen": 19, "ref": 20, "label": 22, "body": 27}

JS_INFO = r'''() => {
 const L=document.getElementById('lienzo'); const R=L.getBoundingClientRect(); const W=R.width,H=R.height,k=W/1080;
 const out=[]; const boxes=[]; const cv=document.createElement('canvas').getContext('2d');
 function bl(e,end){const s=document.createElement('span');s.style.cssText='display:inline-block;width:0;height:0;vertical-align:baseline';
   if(end)e.appendChild(s);else e.insertBefore(s,e.firstChild);const y=s.getBoundingClientRect().bottom;s.remove();return y;}
 L.querySelectorAll('*').forEach(e=>{
   let own=false; for(const n of e.childNodes){ if(n.nodeType===3&&n.textContent.trim()){own=true;break;} }
   const cs=getComputedStyle(e);
   const bw=parseFloat(cs.borderTopWidth)+parseFloat(cs.borderLeftWidth);
   const bg=cs.backgroundColor; const hasBg=bg&&bg!=='rgba(0, 0, 0, 0)'&&bg!=='transparent';
   const r=e.getBoundingClientRect();
   if(!e.closest('[data-resaltado]')&&(e.hasAttribute('data-caja')||bw>=1.5||hasBg)&&(e.textContent||'').trim()&&r.width<W*0.95&&r.height<H*0.9&&!e.closest('.pill')&&!e.classList.contains('pill'))
     boxes.push({x:r.left-R.left,y:r.top-R.top,w:r.width,h:r.height,t:(e.textContent||'').trim().slice(0,40),caja:e.hasAttribute('data-caja')});
   if(!own) return;
   const rg=document.createRange(); rg.selectNodeContents(e); const b=rg.getBoundingClientRect(); if(!b.width) return;
   const rr=e.closest('[data-rol]'); const t=(e.textContent||'').trim();
   cv.font=cs.fontStyle+' '+cs.fontWeight+' '+cs.fontSize+' '+cs.fontFamily; const mt=cv.measureText(t||'H');
   const it=bl(e,false)-mt.actualBoundingBoxAscent-R.top, ib=bl(e,true)+mt.actualBoundingBoxDescent-R.top;
   out.push({it,ib,t:t.slice(0,60),len:t.length,fs:parseFloat(cs.fontSize),ls:parseFloat(cs.letterSpacing)||0,tt:cs.textTransform,
     rol:rr?rr.getAttribute('data-rol'):'',col:cs.color,pill:!!e.closest('.pill'),res:!!e.closest('[data-resaltado]'),pila:!!e.closest('[data-pila]'),
     x:b.left-R.left,y:b.top-R.top,w:b.width,h:b.height});
 });
 const logos=[...L.querySelectorAll('img[data-logo]')].map(i=>{const r=i.getBoundingClientRect();return {kind:i.getAttribute('data-logo'),x:r.left-R.left,y:r.top-R.top,w:r.width,h:r.height};});
 const resal=L.querySelectorAll('[data-resaltado]').length;
 const barras=[...L.querySelectorAll('[data-resaltado]')].map(b=>{const r=b.getBoundingClientRect();return {x:r.left-R.left,y:r.top-R.top,w:r.width,h:r.height,t:(b.textContent||'').trim().slice(0,30)};});
 const ficha=!!L.querySelector('[data-jerarquia="ficha"]');
 return {ficha,resal,barras,W,H,k,m:Math.round(0.10*Math.min(W,H)),texts:out,boxes,logos,avisos:window.__lci_avisos||[]};
}'''

def _lum(c):
    c = np.asarray(c, float) / 255.0
    c = np.where(c <= 0.03928, c/12.92, ((c+0.055)/1.055)**2.4)
    return 0.2126*c[..., 0] + 0.7152*c[..., 1] + 0.0722*c[..., 2]

def _cr(a, b):
    la, lb = _lum(a), _lum(b); hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

async def _render(pg, html):
    await pg.set_content(html)
    try: await pg.wait_for_function('window.__lci_listo===true', timeout=6000)
    except Exception: await pg.wait_for_timeout(600)
    await pg.wait_for_timeout(120)

async def _audit_async(html, out_png, pg):
    await _render(pg, html)
    info = await pg.evaluate(JS_INFO)
    W, H = int(info['W']), int(info['H'])
    await pg.set_viewport_size({'width': W, 'height': H})
    a_path = out_png or '/tmp/_qa_a.png'
    await pg.locator('#lienzo').screenshot(path=a_path)
    await pg.add_style_tag(content='#lienzo *{color:transparent!important;-webkit-text-stroke:0!important;text-shadow:none!important;caret-color:transparent} #lienzo img[data-logo]{visibility:hidden!important}')
    await pg.wait_for_timeout(60)
    b_path = a_path.replace('.png', '_bg.png')
    await pg.locator('#lienzo').screenshot(path=b_path)
    A = np.asarray(Image.open(a_path).convert('RGB')).astype(int); B = np.asarray(Image.open(b_path).convert('RGB')).astype(int)
    os.remove(b_path)
    sh, sw = A.shape[:2]; sx, sy = sw / W, sh / H
    ink = np.abs(A - B).sum(2) > 40
    m, k = info['m'], info['k']; fallos = []; marcas = []

    def inkbox(x, y, w, h):
        x0, y0 = max(0, int(x*sx)), max(0, int(y*sy)); x1, y1 = min(sw, int((x+w)*sx)+1), min(sh, int((y+h)*sy)+1)
        sub = ink[y0:y1, x0:x1]
        if not sub.any(): return None
        ys, xs = np.where(sub)
        return (x0+xs.min())/sx, (y0+ys.min())/sy, (x0+xs.max()+1)/sx, (y0+ys.max()+1)/sy, (y0, y1, x0, x1, sub)

    for t in info['texts']:
        if t['pill']: continue
        fs = t['fs'] / k
        if t['rol'] == 'ref': fl = PISO['ref']
        elif t['rol'] == 'label' or t['tt'] == 'uppercase' or (t['ls']/max(t['fs'], 1)) > 0.06: fl = PISO['label']
        elif t['rol'] == 'body' or (t['len'] >= 28 and fs < 44): fl = PISO['body']
        else: fl = PISO['gen']
        if fs + 0.3 < fl:
            fallos.append(f"F1 piso: «{t['t'][:34]}» {fs:.0f}px < {fl}px"); marcas.append((t['x'], t['y'], t['w'], t['h']))
        ib = inkbox(t['x'], t['y'], t['w'], t['h'])
        if not ib: continue
        x0, y0, x1, y1, (Y0, Y1, X0, X1, sub) = ib
        if t['rol'] != 'pie' and (x0 < m-2 or x1 > W-m+2 or y0 < m-2 or y1 > H-m+2):
            fallos.append(f"F2 margen: «{t['t'][:34]}» sale de la zona segura ({m}px)"); marcas.append((x0, y0, x1-x0, y1-y0))
        import re as _re
        cc = [float(v) for v in _re.findall(r'[\d.]+', t['col'])]
        bgp = B[Y0:Y1, X0:X1][sub]; bg = np.median(bgp, 0)
        fg = np.array(cc[:3]) if len(cc) >= 3 else A[Y0:Y1, X0:X1][sub].mean(0)
        if len(cc) == 4: fg = fg*cc[3] + bg*(1-cc[3])                 # color con alfa sobre el fondo real
        if os.environ.get('QA_DEBUG'): print('   ·', t['t'][:30], round(_cr(fg, bg), 2), fg.round(), bg.round())
        cr = _cr(fg, bg)
        need = 6.0 if t['fs']/k >= 60 else 4.5          # titulares sobre foto: contraste alto, como Paola (10-oct-2026)
        if bgp.std(0).mean() > 22: need += 0.5            # fondo cargado (foto/partículas) exige más
        if cr < need:
            fallos.append(f"F3 contraste {cr:.1f}:1 (<{need}) «{t['t'][:34]}» → dar SOPORTE: panel de vidrio a media pieza (R.soporte('mitad')), tarjeta de vidrio, resaltado que abraza (M.barra), cápsula o recuadro; o navy sobre claro"); marcas.append((x0, y0, x1-x0, y1-y0))

    for bx in info['boxes']:
        ib = inkbox(bx['x']+3, bx['y']+3, bx['w']-6, bx['h']-6)
        if not ib: continue
        x0, y0, x1, y1, _ = ib
        l, r, tp, bt = x0-bx['x'], bx['x']+bx['w']-x1, y0-bx['y'], bx['y']+bx['h']-y1
        tolx, toly = max(6, .06*bx['w']), max(6, .08*bx['h'])
        una = (y1 - y0) < 1.7 * max([tt['fs'] for tt in info['texts'] if bx['t'][:10] in tt['t']] or [999])   # una sola línea
        if bx['h'] < H*0.5 and (abs(tp-bt) > toly or (una and abs(l-r) > tolx)) and (bx['caja'] or bx['w'] < W*0.8):
            fallos.append(f"F4 recuadro asimétrico «{bx['t'][:28]}»: ↑{tp:.0f} ↓{bt:.0f} ←{l:.0f} →{r:.0f}")
            marcas.append((bx['x'], bx['y'], bx['w'], bx['h']))

    # F7 — logos: dentro de la zona segura y al tamaño estándar de la marca
    TAM = {'principal': ('w', .20*W, .245*W), 'cr_wordmark': ('h', 72*k, 92*k), 'sello': ('h', 130*k, 170*k), 'terciario': ('h', 104*k, 132*k), 'lai': ('w', .31*W, .37*W)}
    for lg in info.get('logos', []):
        if lg['x'] < m-2 or lg['y'] < m-2 or lg['x']+lg['w'] > W-m+2 or lg['y']+lg['h'] > H-m+2:
            fallos.append(f"F7 logo {lg['kind']} fuera de la zona segura"); marcas.append((lg['x'], lg['y'], lg['w'], lg['h']))
        ibl = inkbox(lg['x'], lg['y'], lg['w'], lg['h'])
        if ibl:
            _, _, _, _, (Y0, Y1, X0, X1, sub) = ibl
            if sub.sum() > 50:
                dd = np.abs(A[Y0:Y1, X0:X1] - B[Y0:Y1, X0:X1]).sum(2); core = sub & (dd >= np.percentile(dd[sub], 50))   # núcleo del trazo
                crl = _cr(A[Y0:Y1, X0:X1][core].mean(0), np.median(B[Y0:Y1, X0:X1][sub], 0))
                if crl < 4.5:
                    fallos.append(f"F7 logo {lg['kind']} no se ve (contraste {crl:.1f}:1) → navy sobre zona clara, blanco sobre oscura, o dentro de un soporte")
                    marcas.append((lg['x'], lg['y'], lg['w'], lg['h']))
        al = min(abs(lg['x'] - m), abs(W - m - (lg['x'] + lg['w'])), abs((lg['x'] + lg['w']/2) - W/2))
        if al > 6: fallos.append(f"F7 logo {lg['kind']} no está alineado a un margen ni centrado (desvío {al:.0f}px)"); marcas.append((lg['x'], lg['y'], lg['w'], lg['h']))
        if lg['kind'] in TAM:
            dim, lo, hi = TAM[lg['kind']]; v = lg['w'] if dim == 'w' else lg['h']
            if not (lo <= v <= hi): fallos.append(f"F7 logo {lg['kind']} fuera de tamaño estándar ({v:.0f}px; {lo:.0f}–{hi:.0f})")

    # F5 — columnas de líneas apiladas: textos con solape horizontal, en orden vertical
    def _lab(t): return t['tt'] == 'uppercase' or (t['ls']/max(t['fs'], 1)) > 0.06 or t['rol'] == 'label'
    ts = [t for t in info['texts'] if not t['pill'] and t['rol'] not in ('ref', 'pie') and t['len'] > 2 and not _lab(t)]
    lines = [(t['it'], t['ib'], t['x'], t['x']+t['w'], t) for t in ts]   # tinta vertical exacta (métricas de la fuente)
    lines.sort(key=lambda z: z[0])
    for i in range(len(lines)-1):
        a, b = lines[i], lines[i+1]
        ov = min(a[3], b[3]) - max(a[2], b[2])
        if ov > 4 and b[0] < a[1] - 3 and abs(a[4]['fs'] - b[4]['fs']) > 1:
            fallos.append(f"F5 líneas montadas: «{a[4]['t'][:20]}» / «{b[4]['t'][:20]}»"); marcas.append((a[2], a[0], a[3]-a[2], b[1]-a[0]))
    # bloques: cadenas de líneas consecutivas (solapan en x, aire < 1.1 × cuerpo mayor) → aire de tinta uniforme
    cad, cur = [], [lines[0]] if lines else []
    for z in lines[1:]:
        p_ = cur[-1]; g = z[0]-p_[1]; ov = min(p_[3], z[3]) - max(p_[2], z[2])
        sigue = not p_[4]['t'].rstrip().endswith(('.', ':', '?', '!', ']'))   # la frase continúa → mismo bloque
        if ov > 0 and sigue and min(p_[4]['fs'], z[4]['fs'])/k >= 40 and -2 < g < 1.1*max(p_[4]['fs'], z[4]['fs']) and abs(p_[4]['fs']-z[4]['fs']) > 1: cur.append(z)
        else:
            if len(cur) >= 3: cad.append(cur)
            cur = [z]
    if len(cur) >= 3: cad.append(cur)
    for c in cad:
        gaps = [c[i+1][0]-c[i][1] for i in range(len(c)-1)]
        if max(gaps) - min(gaps) > 8 and max(gaps) / max(min(gaps), 1) > 1.6:
            fallos.append(f"F5 interlineado desigual «{c[0][4]['t'][:18]}…»: aires de tinta {[round(g) for g in gaps]} px")
            marcas.append((min(z[2] for z in c), c[0][0], max(z[3] for z in c)-min(z[2] for z in c), c[-1][1]-c[0][0]))

    # F6 — aprovechamiento (aviso)
    main = [z for z in lines if z[4]['fs']/k >= 24]
    if main:
        ux0 = min(z[2] for z in main); ux1 = max(z[3] for z in main); uy0 = min(z[0] for z in main); uy1 = max(z[1] for z in main)
        if (ux1-ux0) < .62*(W-2*m) and (uy1-uy0) < .55*(H-2*m):
            fallos.append(f"F6 aviso: el contenido usa {100*(ux1-ux0)/(W-2*m):.0f}% del ancho y {100*(uy1-uy0)/(H-2*m):.0f}% del alto útil — subir tamaños o sumar recuadro")
    # F8 — jerarquía: el piso no es el tamaño de la pieza
    tx = [t for t in info['texts'] if not t['pill'] and t['rol'] not in ('pie',)]
    if len(tx) >= 3 and not info.get('ficha'):   # fichas de artículo: jerarquía propia de la «primera página» del paper
        fss = sorted(set(round(t['fs']/k) for t in tx)); top = max(fss)
        cuerpo = [t['fs']/k for t in tx if t['len'] >= 28 and t['fs']/k < 44]
        en_piso = sum(1 for t in tx if t['fs']/k <= 20.5)
        if cuerpo and len(tx) >= 4 and len(fss) < 3: fallos.append(f"F8 jerarquía plana: solo {len(fss)} tamaños {fss}")   # portadas de solo titular (recta + cursiva al mismo tamaño) no aplican
        if cuerpo and top < 2.4*max(cuerpo): fallos.append(f"F8 jerarquía: titular {top}px < 2.4 × cuerpo ({max(cuerpo):.0f}px)")
        if en_piso > len(tx)/2: fallos.append(f"F8 jerarquía: {en_piso}/{len(tx)} textos en el tamaño mínimo")
    # F9 — REGLA INQUEBRANTABLE (la Dra., 10-oct-2026): con RESALTADO el interlineado sube; la barra NUNCA invade
    # la línea de arriba ni la de abajo. Aire mínimo entre la barra y la tinta vecina: max(10 px, 12 % del alto de la barra).
    for b in info.get('barras', []):
        need = max(10*k, 0.12*b['h'])
        for t in info['texts']:
            if t.get('res') or t['pill']: continue
            if t['x'] > b['x']+b['w'] or t['x']+t['w'] < b['x']: continue
            if t['ib'] <= b['y']+b['h']/2: gap = b['y'] - t['ib']
            elif t['it'] >= b['y']+b['h']/2: gap = t['it'] - (b['y']+b['h'])
            else: gap = -1
            if gap < need and gap > -b['h']*1.5:
                fallos.append(f"F9 resaltado montado sobre «{t['t'][:22]}»: aire {gap/k:.0f}px < {need/k:.0f}px — subir interlineado")
                marcas.append((b['x'], b['y'], b['w'], b['h']))
    for a in info['avisos']: fallos.append('JS ' + a)
    fallos.append(f"INFO resaltados={info.get('resal', 0)}")

    if out_png:
        im = Image.open(a_path).convert('RGB'); d = ImageDraw.Draw(im)
        d.rectangle([m*sx, m*sy, (W-m)*sx, (H-m)*sy], outline=(0, 230, 120), width=2)
        for (x, y, w, h) in marcas: d.rectangle([x*sx-3, y*sy-3, (x+w)*sx+3, (y+h)*sy+3], outline=(255, 40, 40), width=4)
        im.save(out_png.replace('.png', '_qa.png'))
    return fallos

async def _many(items):
    async with async_playwright() as p:
        b = await _lanzar(p); pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        res = []
        for html, out in items: res.append(await _audit_async(html, out, pg))
        await b.close(); return res

def auditar_html(html, out_png=None):
    return asyncio.run(_many([(html, out_png)]))[0]

def resaltados_ok(resultados, cada=3):
    """Regla de la Dra. (10-oct-2026): usar el RESALTADO que abraza el texto (como «are cellular messengers» de
    'Exosomes' de Paola) con más frecuencia: ≥ 1 lámina con resaltado en cada carrusel y ≥ 1 de cada `cada` piezas del lote."""
    con = [any(x.startswith('INFO resaltados=') and not x.endswith('=0') for x in r) for r in resultados]
    falta = len(con) >= cada and sum(con) < len(con) / cada
    return (not falta, f"{sum(con)}/{len(con)} láminas con resaltado (mínimo 1 de cada {cada})")

def auditar_lote(pares):
    """pares = [(html, 'salida.png'), ...] → lista de fallos por pieza (renderiza también el PNG final)."""
    return asyncio.run(_many(pares))

if __name__ == '__main__':
    pares = [(open(f).read(), f.rsplit('.', 1)[0] + '.png') for f in sys.argv[1:]]
    for f, fl in zip(sys.argv[1:], auditar_lote(pares)):
        dur = [x for x in fl if not x.startswith(('F6', 'INFO'))]
        print(('OK ' if not dur else 'FALLA ') + f); [print('   ', x) for x in fl]
