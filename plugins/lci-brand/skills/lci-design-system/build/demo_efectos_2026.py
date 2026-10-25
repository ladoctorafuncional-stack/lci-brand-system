# EJEMPLO de documento al estándar visual 2026 (efectos_lci). Las fotos (D=...) son de la sesión de oct-2026: reemplazar por las del caso.
import sys,asyncio
import os; A=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','assets')  # carpeta assets del skill
sys.path.insert(0,A)
import brand as B, efectos_lci as E
D='/mnt/user-data/uploads/Downloads/'
hero=E.hero(E.foto(D+'nuevas/consultorio.png','calido',crop=(0,0.05,1,0.95)),'Tu ruta en','LCI.','Guía del paciente · Longevity Clinical Institute',
            'De la primera consulta a tu plan personalizado.',B.LOGO_LEFT)
intro='<div class="section"><div class="sec-head"><div class="t">Cómo <span class="it">trabajamos</span></div></div>'
intro+=E.cifras([('2','h','Primera consulta de mínimo dos horas: mediciones y evaluación médica completa.'),
                 ('48','h','Tus órdenes de exámenes, listas en las 48 horas siguientes.'),
                 ('10','días','Protocolos en clínica de hasta ~10 días, según tu protocolo.')])
intro+=E.pasos([('Paso 01','Preconsulta','Historia clínica, mediciones y datos de base — antes de sentarte con tu médica.'),
                ('Paso 02','La consulta','Mínimo dos horas: mediciones y una evaluación médica completa, sin afanes.'),
                ('Paso 03','Diagnóstico de precisión','Los exámenes que tu caso realmente necesita — ni más, ni menos.'),
                ('Paso 04','Tu plan de acción','Nutrición, movimiento, sueño, terapias y seguimiento según lo que tu caso necesita.')])
intro+='</div>'
band=E.banda(E.vidrio(D+'ChatGPT Image Sep 30, 2026, 12_34_38 AM.png','azul',w=1800,h=520),'La medicina se creó','para la enfermedad.','Nosotros empezamos antes: medición de grado clínico, números exactos, no suposiciones.')
circ='<div class="section">'+E.circulos('Antes','Esperar a que aparezcan los síntomas para tratar la enfermedad.','En LCI','Medir antes, entender tu biología y actuar a tiempo.')+'</div>'
dark=('<section class="fx-band" style="background-image:url(\''+E.ondas(w=1800,h=600,nivel=0.42)+'\')"><div>'+
      E.tarjeta('<div style="font-family:Mencken Std,serif;font-weight:700;font-size:1.5rem">Seguimiento</div><p style="font-family:Poppins;font-weight:300;margin:6px 0 0">Volvemos a medir, ajustamos y acompañamos tu progreso en el tiempo.</p>',oscuro=True)+'</div></section>')
body='<div class="wrap">'+hero+intro+band+circ+dark+B.footer()+'</div>'
html=B.html_doc('Demo estándar 2026',body).replace('</style>',E.css()+'</style>',1)
open('demo.html','w').write(html)
from playwright.async_api import async_playwright
async def m():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':900,'height':1200})
        await pg.set_content(html); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(600)
        await pg.screenshot(path='demo.png',full_page=True); await b.close()
asyncio.run(m())
