"""Auditoría OBLIGATORIA de fuentes antes de entregar cualquier pieza LCI.
Renderiza cada HTML en Chromium y pregunta al motor qué fuente REAL dibujó cada texto (CSS.getPlatformFontsForNode).
Solo se permiten Poppins y Mencken Std / Mencken Std Head. Cualquier otra (DejaVu, Liberation, Arial…) = glifo que la
marca no tiene (✦ ◂ ▸ ₂ &#8209; flechas, emojis…) → reemplazar por SVG o por la secuencia equivalente en fuente de marca
(p. ej. VO<span style='font-size:.62em;vertical-align:-.1em'>2</span>max, guion normal con white-space:nowrap).
Uso: python3 auditar_fuentes.py pieza1.html pieza2.html ...   (o importar auditar(lista_de_html_str))"""
import asyncio, sys
from playwright.async_api import async_playwright
import os as _os, sys as _sys; _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from _navegador import lanzar as _lanzar
JS = """() => { const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT); let n,i=0,o=[];
 while(n=w.nextNode()){ if(!n.textContent.trim()) continue; const e=n.parentElement;
 if(!e.hasAttribute('data-a')) e.setAttribute('data-a',i++); o.push([e.getAttribute('data-a'),n.textContent.trim().slice(0,50)]);} return o;}"""
async def _run(htmls):
    malos = []
    async with async_playwright() as p:
        b = await _lanzar(p); pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        cdp = await pg.context.new_cdp_session(pg); await cdp.send('DOM.enable'); await cdp.send('CSS.enable')
        for k, h in enumerate(htmls):
            await pg.set_content(h); await pg.wait_for_timeout(300)
            items = await pg.evaluate(JS); doc = await cdp.send('DOM.getDocument', {'depth': -1})
            for a, txt in items:
                r = await cdp.send('DOM.querySelector', {'nodeId': doc['root']['nodeId'], 'selector': f'[data-a="{a}"]'})
                if not r['nodeId']: continue
                pf = await cdp.send('CSS.getPlatformFontsForNode', {'nodeId': r['nodeId']})
                x = {f['familyName'] for f in pf['fonts'] if not f['familyName'].startswith(('Poppins', 'Mencken'))}
                if x: malos.append((k, txt, sorted(x)))
        await b.close()
    return malos
def auditar(htmls): return asyncio.run(_run(htmls))
if __name__ == '__main__':
    m = auditar([open(f).read() for f in sys.argv[1:]])
    for k, t, f in m: print(sys.argv[1:][k], '→', t, f)
    print('OK: solo fuentes de marca' if not m else f'{len(m)} textos con fuente NO permitida'); sys.exit(1 if m else 0)
