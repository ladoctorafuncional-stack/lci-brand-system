# EJEMPLO: diagramaciones de revista en documentos (E.linea, E.recuadro, E.marco, E.barra). Fotos de oct-2026: reemplazar.
import sys,asyncio,os
import os; sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','assets'))
import brand as B, efectos_lci as E
D='/mnt/user-data/uploads/Downloads/'
bg1=E.foto(D+'gafas_sofa.png','azul'); bg2=E.microscopia(w=1800,h=800); bg3=E.foto(D+'Gemini_Generated_Image_g8hu0zg8hu0zg8hu.jpg','azul')
sec=lambda bg,html:f'<section class="fx-band" style="background-image:url(\'{bg}\');min-height:340px"><div style="max-width:640px">{html}</div></section>'
body='<div class="wrap">'+sec(bg1,E.linea('¿Qué es el','jet lag social?','Cuando tu reloj biológico y tu horario no coinciden.'))+\
 sec(bg2,E.recuadro('Microbiología','Bacterias intestinales',['Microorganismos unicelulares','La mayoría vive en el colon'],'Ejemplo de texto de cierre con referencia.','[1]'))+\
 sec(bg3,E.marco('El cerebro','también envejece.','Ahora se puede reprogramar.',['Mejorar la conectividad neuronal.','Optimizar memoria, foco y equilibrio emocional.']))+\
 '<div class="section">'+E.barra('medirla una vez',30)+'</div></div>'
html=B.html_doc('demo2',body).replace('</style>',E.css()+'</style>',1); open('demo2.html','w').write(html)
from playwright.async_api import async_playwright
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':900,'height':1000})
        await pg.set_content(html); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(500)
        await pg.screenshot(path='demo2.png',full_page=True); await b.close()
asyncio.run(m())
