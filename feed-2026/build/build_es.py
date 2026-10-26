import sys,asyncio,os
sys.path.insert(0,'/root/.claude/plugins/synced/d59b7fb3-87ca-4bdc-804b-1f33a38211ca_25d78cb2-7fe1-4243-bbc4-e095148a53fb/lci-brand/skills/lci-piezas-graficas/assets')
import marca as M, recetas_feed as R
M.IDIOMA='es'
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
BOOK='Agenda tu consulta —<br>link en la bio.'
POSTS={
'N02-founder':[
 lambda: R.r_retrato('Dra. Carolina',"Rodríguez Morales",'Fundadora y Directora Médica',retrato=CUT('calido'),fondo=F('cons','calido',(0.05,0,0.85,1),16),logo=("sello","claro","tl"),h=1080,x=0.40).replace('rgba(9,12,18','rgba(28,19,11'),
 lambda: R.r_derecha('La primera médica','en Latinoamérica','con la certificación Advanced Functional<br>Medicine Clinician (AFMC).',
                     ['Kharrazian Institute · EE. UU.',"AFMC · CFMC"],fondo=F('mri','azul',SQ),logo=("principal","blanco","tl"),fs=64,top=0.42),
 lambda: R.r_poster('Formación','Internacional.',None,None,['Estados Unidos — formación avanzada de<br>posgrado avalada por NUHS','Reino Unido — acreditación<br>internacional CPD','MSc en Inmunología Funcional —<br>Cogence Immunology, EE. UU.'],
                    fondo=F('lab','frio',(0.22,0,0.78,1)),logo=("sello","claro","tr")),
 lambda: R.r_centrado('La innovación sin evidencia es','especulación.','La evidencia sin individualidad<br>biológica nunca alcanza<br>la excelencia.','— Dra. Carolina Rodríguez Morales',
                      fondo=F('brain_b','azul',SQ,2),logo=("terciario","beige","tc"),y=0.33),
 lambda: R.r_titulo_arriba('Medicina con rigor.','Atención con tiempo.',BOOK,fondo=F('p_sit','calido',(0.08,0.02,0.98,1.0)),logo=("principal","gold","bl")),
],
'N03-we-measure':[
 lambda: R.r_eyebrow_gigante('Medimos.','No adivinamos.',None,None,fondo=F('mri','bw',SQ,2),logo=("sello","claro","tr"),ytop=0.68,color='#E3EBF3'),
 lambda: R.r_centrado('Una primera consulta de al menos','dos horas.','Mediciones y una evaluación<br>médica completa.',None,
                      fondo=F('ther','bw',(0.05,0.03,0.95,1)),logo=("terciario","beige","tc"),y=0.36),
 lambda: R.r_marco('Biomarcadores que hablan','antes que los síntomas.',None,['Funcionales · Epigenéticos · Inmunológicos','Metabólicos · Neurocognitivos'],
                   fondo=R.vidrio(D+P['meas_dna'],None,'azul'),logo=("principal","blanco","tl")),
 lambda: R.r_derecha("Procesadas <span style='white-space:nowrap'>in house</span>,<br>en Colombia",'y en laboratorios de EE. UU.','Interpretadas con nuestra IA clínica propia —<br>siempre revisadas por tu médico.',None,
                     fondo=F('edan','azul',(0.05,0.02,0.95,0.92),3),fs=64,top=0.44,logo=("sello","claro","tl")),
 lambda: R.r_claro('Edad biológica','a partir de varios relojes biológicos','Una estimación preliminar — y una hoja<br>de ruta terapéutica personalizada.',fondo=F('brain_w','claro',(0.22,0,1.0,1),0,'right'),logo=("principal","navy","tl")),
 lambda: R.r_titulo_arriba('Números exactos,','no suposiciones.',BOOK,fondo=F('chair','calido',(0.2,0.05,1,1)),logo=("principal","gold","bl")),
],
'N04-inside-lci':[
 lambda: R.r_natural('Dentro de',"LCI.","Milla de Oro · El Poblado, Medellín",fondo=F('recep','natural'),logo=None),
 lambda: R.r_natural('Donde','medimos.','Medición de grado clínico, en una sola sala.',fondo=F('meas_w','natural'),logo=("principal","blanco","tr"),lado="der"),
 lambda: R.r_natural('Donde','escuchamos.','Primeras consultas de al menos dos horas.',fondo=F('cons','natural'),logo=("sello","navy","tl")),
 lambda: R.r_natural('Donde tú','descansas.','Una sala tranquila para las terapias en la clínica.',fondo=F('ther','natural'),logo=("principal","blanco","tl"),lado="der"),
 lambda: R.r_natural('Diseñada para','una medicina sin prisa.','Ven a conocerla — link en la bio.',fondo=F('coffee','natural'),logo=("terciario","navy","tr")),
],
'N05-patient-journey':[
 lambda: R.r_centrado('Tu recorrido como paciente','desde el primer contacto','hasta tu plan.',None,fondo=F('n_cons','frio',(0,0.02,1,0.98)),logo=("terciario","beige","bc"),y=0.32),
 lambda: R.r_paso("01",'Preconsulta','Historia clínica, mediciones y datos<br>basales — recopilados antes de que<br>te sientes con tu médico.',fondo=F('inbody','azul'),logo=("principal","blanco","tl"),lado="izq"),
 lambda: R.r_paso("02",'La consulta','Al menos dos horas: mediciones y<br>una evaluación médica completa, sin prisa.',fondo=F('chair','ambar',(0.2,0.05,1,1)),logo=("sello","claro","tr"),lado="der"),
 lambda: R.r_paso("03",'Diagnóstico de precisión','Las pruebas que tu caso realmente necesita —<br>ni más, ni menos.',fondo=GR('noche',12),logo=("principal","blanco","tl"),lado="izq"),
 lambda: R.r_paso("04",'Tu plan de acción','Una hoja de ruta personalizada según lo que<br>tu caso necesita: nutrición, movimiento,<br>sueño, terapias y seguimiento.',fondo=F('brain_h','claro',SQ),logo=("principal","navy","tr"),lado="der",light=True),
 lambda: R.r_paso("05",'Seguimiento','Volvemos a medir, ajustamos y seguimos<br>tu progreso en el tiempo.',fondo=F('meas_dna','frio'),logo=("sello","claro","tl"),lado="izq",cta='Agenda tu consulta — link en la bio.'),
],
'N06-functional-rigor':[
 lambda: R.r_poster('Funcional,','con rigor.','Bajo estándares médicos.','Primero la evidencia. Siempre la biología.',None,fondo=F('equip','bw',(0.25,0,1,0.95)),logo=("principal","blanco","tl"),lado="der"),
 lambda: R.r_derecha('Si la evidencia indica','una estatina, la formulo.','Si una infección requiere antibióticos<br>u hospitalización, ese es el tratamiento.',None,
                     fondo=GR('acero',13),logo=("sello","claro","tl")),
 lambda: R.r_marco('No suspendo','medicación psiquiátrica','para «volverme natural».',['Y no lleno a mis pacientes de suplementos.','Eso no es buena medicina.'],
                   fondo=F('meas_w','bw',None,6),logo=("principal","blanco","tr")),
 lambda: R.r_centrado('Primero la evidencia.','Siempre la biología.',None,'— Dra. Carolina Rodríguez Morales',fondo=F('hall','frio',(0.15,0,0.85,1)),logo=("terciario","beige","bc"),y=0.40),
],
'N07-visit-medellin':[
 lambda: R.r_titulo_arriba('Tu visita','a Medellín.','Pacientes internacionales.',fondo=BR('night','calido',(0.24,0,1,0.95),1.95),logo=("principal","gold","bl")).replace('rgba(30,20,12,.70) 0%','rgba(30,20,12,.55) 0%').replace('rgba(30,20,12,.85) 100%','rgba(30,20,12,.70) 100%'),
 lambda: R.r_poster('Protocolos en la clínica','Hasta 10 días.','La duración depende<br>de tu protocolo.',None,None,fondo=F('desk','calido'),logo=("principal","blanco","tl"),veil=R.VEIL_CAFE),
 lambda: R.r_derecha('Aeropuerto, hotel, transporte —','organizados para ti.','Y nuestro equipo está pendiente<br>durante toda tu estadía.',None,fondo=F('hall','azul',(0.1,0,0.9,1)),logo=("sello","claro","tl")),
 lambda: R.r_claro('En tu idioma.','Inglés y español','Un equipo médico y de atención al paciente bilingüe,<br>desde el primer mensaje hasta el seguimiento.',fondo=F('recep','claro'),logo=("principal","navy","tl")),
 lambda: R.r_natural('Planea tu','visita.','Escríbenos — link en la bio<br>Milla de Oro · El Poblado, Medellín',fondo=F('chair','natural'),logo=("terciario","navy","tr")),
],
'N09-healthspan':[
 lambda: R.r_eyebrow_gigante('Vivir más no es','vivir bien.',None,None,fondo=F('brain_b','bw',SQ,1),logo=("sello","claro","tr"),ytop=0.68),
 lambda: R.r_claro("Healthspan",'los años vividos con buena salud','Lifespan: cuántos años vives.<br>Healthspan: cuántos de esos años<br>los vives con buena salud.',fondo=F('brain_w','claro',(0.22,0,1.0,1),0,'right'),logo=("principal","navy","tl")),
 lambda: R.r_centrado('En 183 países, la brecha promedia','9,6 años','y se ha ampliado<br>en dos décadas. [1]',None,fondo=FXB('mesh_claro'),logo=("terciario","navy","tc"),y=0.36,light=True),
 lambda: R.r_derecha('En Estados Unidos,','12,4 años.','La mayor brecha medida. [1]',None,fondo=F('night','azul',(0.25,0,0.98,0.82)),logo=("sello","claro","tl")),
 lambda: R.r_marco('Impulsada en gran parte por','enfermedad crónica.',None,['Enfermedad no transmisible. [1,2]','Ahí es donde la medición y','la acción temprana importan más.'],fondo=GR('acero',15),logo=("principal","blanco","tl")),
 lambda: R.r_titulo_arriba('No solo más años.','Más años saludables.',None,fondo=F('cons','ambar',(0.3,0,1,0.9)),logo=("principal","gold","bl"),
          refs="[1] Garmany A, Terzic A. JAMA Netw Open. 2024;7(12):e2450241. doi:10.1001/jamanetworkopen.2024.50241<br>[2] Garmany A, Yamada S, Terzic A. NPJ Regen Med. 2021;6(1):57. doi:10.1038/s41536-021-00169-5"),
],
'E01-vo2max':[
 lambda: R.r_eyebrow_gigante('No tu peso. No tu colesterol.',"Tu VO<span style='font-size:.62em;vertical-align:-.1em'>2</span>max.",None,None,fondo=F('face','bw',(0.38,0,0.83,1)),logo=("sello","claro","tl"),ytop=0.68,color='#E3EBF3'),
 lambda: R.r_claro("VO<span style='font-size:.62em;vertical-align:-.1em'>2</span>max",'oxígeno, bajo esfuerzo','Qué tan bien tu corazón, pulmones y músculos<br>captan y usan el oxígeno durante el ejercicio.',fondo=GR('niebla',16),logo=("principal","navy","tl")),
 lambda: R.r_articulo("JAMA Network Open","2018 · 1(6):e183605","Association of Cardiorespiratory Fitness With Long-term Mortality Among Adults Undergoing Exercise Treadmill Testing",
          "Mandsager K, Harb S, Cremer P, Phelan D, Nissen SE, Jaber W",[('Diseño','Cohorte retrospectiva, Cleveland Clinic'),('Participantes','122.007 adultos'),('Seguimiento','Mediana 8,4 años')],
          'Capacidad baja vs élite: HR ajustado <b>5,04</b> para mortalidad por todas las causas.',"10.1001/jamanetworkopen.2018.3605",fondo=F('meas_w','azul',None,8),logo=("principal","blanco","tl")),
 lambda: R.r_centrado('Capacidad baja vs élite:','5× la mortalidad.','Comparable o mayor que<br>el tabaquismo o la diabetes. [1]',None,fondo=M.foto(R.movimiento(D+P['face'],'azul',(0.30,0,0.78,1)),None),logo=("terciario","beige","tc"),y=0.36),
 lambda: R.r_derecha('La buena noticia:','es modificable.','No se observó un límite superior<br>de beneficio en esta cohorte. [1]',None,fondo=GR('noche',17),logo=("sello","claro","tl"),fs=70),
 lambda: R.con_refs(R.r_titulo_arriba('Mídelo.','No lo adivines.','Agenda tu valoración de longevidad —<br>link en la bio.',fondo=F('inbody','ambar'),logo=("principal","gold","bl")),
          "[1] Mandsager K, Harb S, Cremer P, Phelan D, Nissen SE, Jaber W. JAMA Netw Open. 2018;1(6):e183605. doi:10.1001/jamanetworkopen.2018.3605"),
],
'E02-antioxidants':[
 lambda: R.r_poster('Pastillas antioxidantes','¿Frenan el envejecimiento?','La mejor evidencia dice que no.',None,None,fondo=F('meas_w','calido',(0,0,0.75,0.6)),logo=("principal","blanco","tl"),veil=R.VEIL_CAFE),
 lambda: R.r_marco('Por qué se volvieron','tan populares.','El daño oxidativo se asocia con el envejecimiento.',['De ahí el salto: «suplementar','antioxidantes debería protegernos».'],fondo=R.vidrio(D+P['meas_w'],None,None),logo=("sello","claro","tr")),
 lambda: R.r_articulo("Cochrane Database Syst Rev","2012 · CD007176","Antioxidant supplements for prevention of mortality in healthy participants and patients with various diseases",
          "Bjelakovic G, Nikolova D, Gluud LL, Simonetti RG, Gluud C",[('Diseño','Revisión sistemática y metaanálisis'),('Ensayos','78 ensayos aleatorizados'),('Participantes',"296,707")],
          'Sin reducción de la mortalidad. En ensayos con bajo riesgo de sesgo, el betacaroteno y la vitamina E la <b>aumentaron</b>.',"10.1002/14651858.CD007176.pub2",fondo=F('coffee','azul',None,8),logo=("principal","blanco","tl")),
 lambda: R.r_centrado('78 ensayos · 296.707 personas','Sin beneficio','en mortalidad. El betacaroteno y la<br>vitamina E se asociaron con mayor<br>mortalidad. [1]',None,fondo=R.bokeh(19),logo=("terciario","beige","tc"),y=0.34),
 lambda: R.r_claro('Del frasco','al plato','Verduras, fruta, aceite de oliva —<br>no megadosis aisladas.',fondo=F('desk','claro'),logo=("principal","navy","tl")),
 lambda: R.con_refs(R.r_derecha('Suplementa','con criterio.','Personalizado y basado en evidencia.<br>Agenda tu valoración — link en la bio.',None,fondo=F('cons','azul',(0.3,0,1,0.9)),logo=("sello","claro","tl"),top=0.40),
          "[1] Bjelakovic G, Nikolova D, Gluud LL, Simonetti RG, Gluud C. Cochrane Database Syst Rev. 2012;(3):CD007176. doi:10.1002/14651858.CD007176.pub2"),
],
'E03-sleep-regularity':[
 lambda: R.r_centrado('No es solo cuánto duermes.','Es cuándo.','Horarios constantes para dormir y despertar<br>pueden importar más que tus 8 horas.',None,fondo=F('ther','azul',(0.37,0,1,1)),logo=("sello","claro","bc",110),y=0.12),
 lambda: R.r_derecha('Regularidad','sobre duración.','Tu cuerpo funciona con un reloj circadiano.<br>Cambiar a diario la hora de acostarte<br>y de despertar lo altera.',None,fondo=R.vidrio(D+P['ther'],None,'azul'),logo=("sello","claro","tl")),
 lambda: R.r_articulo("Sleep","2024 · 47(1):zsad253","Sleep regularity is a stronger predictor of mortality risk than sleep duration: a prospective cohort study",
          "Windred DP, Burns AC, Lane JM, Saxena R, Rutter MK, Cain SW, Phillips AJK",[('Diseño','Cohorte prospectiva, UK Biobank'),('Participantes','60.977 adultos'),('Datos','&gt;10 millones de horas de acelerometría')],
          'Sueño más regular: mortalidad por todas las causas <b>20–48%</b> menor vs el quintil menos regular.',"10.1093/sleep/zsad253",fondo=F('ther','azul',None,8),logo=("principal","blanco","tl")),
 lambda: R.r_derecha('Menor mortalidad por todas las causas:',"20–48%",'con un sueño más regular. [1]<br>Evidencia observacional: una asociación,<br>no una prueba de causa.',None,fondo=GR('aurora',21),logo=("sello","claro","tl"),top=0.44),
 lambda: R.r_paso("1",'Empieza por una cosa.','Despierta a la misma hora los 7 días —<br>fines de semana incluidos — y recibe<br>luz natural poco después.',fondo=F('recep','claro'),logo=("principal","navy","tr"),lado="der",light=True),
 lambda: R.con_refs(R.r_poster('En LCI','Miramos los datos.','No las suposiciones.','Agenda tu valoración de longevidad — link en la bio.',None,fondo=F('cons','calido',(0.3,0,1,0.9)),logo=("principal","blanco","tl"),veil=R.VEIL_CAFE),
          "[1] Windred DP, Burns AC, Lane JM, Saxena R, Rutter MK, Cain SW, Phillips AJK. Sleep. 2024;47(1):zsad253. doi:10.1093/sleep/zsad253"),
],
'E04-waist-bmi':[
 lambda: R.r_eyebrow_gigante('Tu peso no te dice','dónde está tu grasa.',None,None,fondo=F('meas_dna','azul'),logo=("sello","claro","tr")),
 lambda: R.r_claro('Lo que el IMC ignora','músculo vs. grasa — y dónde','El IMC solo divide el peso por la estatura.<br>No distingue músculo de grasa,<br>ni dónde se almacena la grasa.',fondo=GR('niebla',22),logo=("principal","navy","tl")),
 lambda: R.r_articulo("N Engl J Med","2008 · 359(20):2105-20","General and abdominal adiposity and risk of death in Europe",
          "Pischon T, Boeing H, Hoffmann K, et al. (EPIC)",[('Diseño','Cohorte prospectiva, 9 países europeos'),('Participantes','359.387 adultos'),('Seguimiento','Media 9,7 años')],
          'Mayor vs menor quintil de cintura, ajustado por IMC: RR <b>2,05</b> (hombres) · <b>1,78</b> (mujeres).',"10.1056/NEJMoa0801891",fondo=F('inbody','azul',None,8),logo=("principal","blanco","tl")),
 lambda: R.r_centrado('Aun ajustando por IMC,','hasta 2×','el riesgo de muerte con la mayor<br>circunferencia de cintura. [1]',None,fondo=GR('aurora',23),logo=("terciario","beige","tc"),y=0.34),
 lambda: R.r_marco('Por eso','medimos.','No estimamos.',['Composición corporal y distribución de grasa —','no solo la báscula.'],fondo=F('inbody','azul',None,4),logo=("sello","claro","tr")),
 lambda: R.con_refs(R.r_poster('Conoce tus','números reales.',None,'Agenda tu valoración de composición corporal —<br>link en la bio.',None,fondo=F('desk','natural'),logo=("principal","blanco","tr"),Hs=70),
          "[1] Pischon T, Boeing H, Hoffmann K, et al. N Engl J Med. 2008;359(20):2105-20. doi:10.1056/NEJMoa0801891"),
],
'N11-brainspan':[
 lambda: R.r_claro("Brainspan",'tan importante como los años de vida','Evaluamos la función cognitiva con nuestras<br>propias pruebas neurocognitivas — para actuar temprano.',fondo=F('brain_l','claro',(0.0,0.05,0.62,0.95)),logo=("principal","navy","tl")),
],
'N12-biological-age':[
 lambda: R.r_derecha('Tu edad en papel','no es tu edad biológica.','La estimamos con varios relojes<br>biológicos — y la volvemos a medir<br>con el tiempo.',None,fondo=F('n_age','azul',(0,0,1,1)),logo=("sello","claro","tl"),fs=62),
],
'N13-person-not-value':[
 lambda: R.r_marco('Trata a la persona,','no el valor de laboratorio.','Cada número se lee en contexto.',['Tu historia. Tu biología.','Tus metas.'],fondo=F('ibdisp','azul',(0,0,1,0.88),11),logo=("principal","blanco","tl")),
],
'P24-lpa':[
 lambda: R.r_claro("Lp(a)",'mídela una vez','Una partícula de colesterol<br>en gran parte escrita en tus genes.',fondo=F('lab','claro',(0.25,0,0.80,1)),logo=("principal","navy","tl")),
 lambda: R.r_centrado('Su nivel es','en gran parte genético','— y no forma parte de un<br>perfil lipídico estándar. [1]',None,fondo=FXB('galaxia'),logo=("terciario","beige","tc"),y=0.34),
 lambda: R.r_articulo("Eur Heart J","2022 · 43(39):3925-46","Lipoprotein(a) in atherosclerotic cardiovascular disease and aortic stenosis: a European Atherosclerosis Society consensus statement",
          "Kronenberg F, Mora S, Stroes ESG, et al.",[('Tipo','Consenso (EAS)'),('Evidencia','Estudios epidemiológicos y genéticos'),('Hallazgo','La Lp(a) es un factor de riesgo causal')],
          'Recomendación: medir la Lp(a) <b>al menos una vez</b> en adultos.',"10.1093/eurheartj/ehac361",fondo=GR('noche',31),logo=("principal","blanco","tl")),
 lambda: R.r_circulos('Medida <b>una vez</b>,<br>conocida de <b>por vida</b>.','La brecha','Un perfil lipídico estándar no incluye<br>la Lp(a), por eso los niveles elevados<br>suelen pasar inadvertidos.','El enfoque','Mídela al menos una vez en la<br>adultez, como recomienda el<br>consenso de la EAS. [1]',paso=(4,5),seccion="Lp(a)"),
 lambda: R.con_refs(R.r_titulo_arriba('Conoce tu Lp(a).','Una vez.','Agenda tu valoración —<br>link en la bio.',fondo=M.foto(R.vidrio(D+P['cons'],(0.3,0,1,0.9),'calido'),None),logo=("principal","gold","bl")),
          "[1] Kronenberg F, Mora S, Stroes ESG, et al. Eur Heart J. 2022;43(39):3925-46. doi:10.1093/eurheartj/ehac361"),
],
'P25-word-healthspan':[
 lambda: R.r_palabra("Healthspan",'sustantivo',['Longevidad','Prevención'],'Los años de vida vividos con buena salud — sin enfermedad crónica ni discapacidad.','La medicina de longevidad busca extender el healthspan, no solo la esperanza de vida.',fondo=F('n_juiceg','natural',(0,0,1,1))),
],
'P26-journey':[
 lambda: R.r_centrado('Tu viaje','de longevidad.','Medir · Interpretar ·<br>Personalizar · Volver a medir',None,fondo=F('n_check','calido',(0,0.37,1,1),5),logo=("terciario","beige","bc"),y=0.30),
 lambda: R.r_orbitas('Tu viaje','de longevidad.',[('Medir','Biomarcadores de grado clínico<br>y composición corporal.'),('Interpretar','Tu médico lee cada<br>número en contexto.'),('Personalizar','Un plan construido según lo que<br>tu caso necesita.'),('Volver a medir','Seguimos tu progreso<br>en el tiempo.')],fondo=R.gradiente('noche')),
 lambda: R.r_centrado('Todo empieza con','una medición.','Agenda tu consulta —<br>link en la bio.',None,fondo=FXB('galaxia_oro'),logo=("terciario","beige","tc"),y=0.36),
],
'P27-measured':[
 lambda: R.r_poster('Medido,','no supuesto.','Biomarcadores de grado clínico.','Cada número, leído en contexto.',None,fondo=PH('oxi','azul',(0,0.02,1,1)),logo=("principal","blanco","tl")),
 lambda: R.r_red('Medido,','no supuesto.',['Metabólico','Hormonal','Inflamatorio','Neurocognitivo','Epigenético','Composición corporal'],fondo=R.gradiente('acero',seed=4)),
 lambda: R.r_cifras('Cómo funciona una<br>primera visita en LCI:',[("2+",'horas para una<br>primera consulta'),("3",'lugares donde se procesan<br>tus muestras: in house,<br>Colombia, EE. UU.'),("48",'horas para recibir tus<br>órdenes y fórmulas')],rotulo="Longevity Clinical Institute",fondo=FXB('malla')),
],
'P28-just-tired':[
 lambda: R.r_icono(ICON,'No es','«solo cansancio».','La fatiga tiene causas —<br>y muchas se pueden medir.',fondo=R.gradiente('aurora',seed=7)),
 lambda: R.r_derecha('La fatiga es un síntoma,','no un diagnóstico.','La función tiroidea, el hierro, el sueño,<br>la glucosa, las hormonas y el ánimo<br>pueden influir.',None,fondo=FXB('mesh_oscuro'),logo=("sello","claro","tl"),fs=64),
 lambda: R.r_circulos('Del <b>«todo normal»</b><br>a <b>respuestas reales</b>.','El problema','«Tus laboratorios son normales».<br>Y aun así sigues<br>sin energía.','Nuestro enfoque','Una evaluación completa que<br>busca la causa —<br>y la mide.',paso=(3,4),seccion='Fatiga'),
 lambda: R.r_titulo_arriba('Encuentra la causa.','Luego, trátala.','Agenda tu consulta —<br>link en la bio.',fondo=M.foto(R.vidrio(D+P['chair'],(0.2,0.05,1,1),'calido'),None),logo=("principal","gold","bl")),
],
'P29-4p':[
 lambda: R.r_titulo_arriba("4P",'medicina.','Predictiva · Preventiva ·<br>Personalizada · Participativa',fondo=F('n_doc','calido',(0,0,1,1)),logo=("principal","gold","bl")),
 lambda: R.r_orbitas('La medicina','de las 4P.',[('Predictiva','Buscamos el riesgo antes de<br>que aparezca la enfermedad.'),('Preventiva','Actuamos temprano, mientras<br>hay tiempo.'),('Personalizada','Tu plan sigue<br>tu biología.'),('Participativa','Eres parte de cada<br>decisión.')],fondo=R.gradiente('aurora',seed=9)),
 lambda: R.con_refs(R.r_centrado('Un marco descrito por',"Leroy Hood",'Biología de sistemas · Medicina P4 [1]',None,fondo=FXB('malla'),logo=("terciario","beige","tc"),y=0.36),
          "[1] Hood L. Systems biology and p4 medicine: past, present, and future. Rambam Maimonides Med J. 2013;4(2):e0012. doi:10.5041/RMMJ.10112"),
],
'P30-social-jetlag':[
 lambda: R.r_derecha('¿Qué es el','jet lag social?','Cuando tu reloj biológico y<br>tu horario no coinciden.',None,fondo=PH('g_sofa','azul',(0.10,0,0.90,1)),logo=("sello","claro","tl"),fs=66),
 lambda: R.r_claro('Jet lag social','tiempo biológico vs. tiempo social','La brecha entre cuándo tu cuerpo quiere<br>dormir y cuándo tu horario te hace<br>dormir. [1]',fondo=R.gradiente('niebla',seed=5),logo=("principal","navy","tl")),
 lambda: R.r_articulo("Chronobiol Int","2006 · 23(1-2):497-509","Social jetlag: misalignment of biological and social time",
          "Wittmann M, Dinich J, Merrow M, Roenneberg T",[('Diseño','Estudio con cuestionario (MCTQ)'),('Participantes','501 voluntarios'),('Medido','Cronotipo, sueño, bienestar')],
          'Los cronotipos tardíos mostraron la mayor brecha entre días laborales y libres — y deuda de sueño en días laborales.',"10.1080/07420520500545979",fondo=VD('g_det',(0.1,0,0.9,1),'azul'),logo=("principal","blanco","tl")),
 lambda: R.r_paso("1",'Empieza por una cosa.','Mantén tu hora de despertar del fin de semana<br>cerca de la de entre semana.',fondo=R.gradiente('acero',seed=8),logo=("sello","claro","tr"),lado="der"),
 lambda: R.con_refs(R.r_titulo_arriba('Tu reloj','importa.','Agenda tu consulta —<br>link en la bio.',fondo=M.foto(R.vidrio(D+P['night'],(0.2,0,1,1),'calido'),None),logo=("principal","gold","bl")),
          "[1] Wittmann M, Dinich J, Merrow M, Roenneberg T. Chronobiol Int. 2006;23(1-2):497-509. doi:10.1080/07420520500545979"),
],
'P31-quote':[
 lambda: R.r_cita('La innovación sin evidencia es especulación. La evidencia sin individualidad biológica nunca alcanza la excelencia.','Dra. Carolina Rodríguez Morales',fondo=VD('p_bg',(0,0.05,1,0.95),None)),
],
'P32-thyroid':[
 lambda: R.r_ondas('¿Tu tiroides se evalúa<br>solo con '+R.pildora("TSH")+'?','Un punto de partida,<br>no toda la historia.',None,fondo=R.ondas(2,nivel=0.62),y=0.20),
 lambda: R.r_circulos('¿Un solo marcador,<br>o el <b>panorama completo</b>?','Tamizaje','La TSH suele ser la primera<br>prueba de función tiroidea.','Cuando persisten los síntomas','T4 libre, T3 libre y anticuerpos<br>tiroideos, elegidos según<br>tu caso.',paso=(2,3),seccion='Tiroides'),
 lambda: R.r_centrado('Tus síntomas','merecen contexto.','Agenda tu consulta —<br>link en la bio.',None,fondo=R.ondas(7,calor=False),logo=("terciario","beige","tc"),y=0.36),
],
'P33-word-sarcopenia':[
 lambda: R.r_palabra("Sarcopenia",'sustantivo',['Músculo','Envejecimiento saludable'],'Enfermedad muscular caracterizada por baja fuerza muscular, confirmada por baja cantidad o calidad muscular. [1]','Es común en adultos mayores — pero puede comenzar antes en la vida. [1]',fondo=F('n_mus','bw',(0,0,1,1))),
 lambda: R.con_refs(R.r_centrado('Fuerza','primero.','En el consenso europeo revisado,<br>la baja fuerza muscular es la<br>característica clave de la sarcopenia. [1]',None,fondo=R.gradiente('acero',seed=12),logo=("terciario","beige","tc"),y=0.34),"[1] Cruz-Jentoft AJ, Bahat G, Bauer J, et al. Age Ageing. 2019;48(1):16-31. doi:10.1093/ageing/afy169"),
],
'P34-grip-strength':[
 lambda: R.r_dato("5 kg",'una menor fuerza de prensión se<br>asoció con un 16% más de riesgo<br>de muerte por cualquier causa. [1]',fondo=R.movimiento(D+P['n_dyn'],'azul'),x=0.07,y=0.55,refs="[1] Leong DP, Teo KK, Rangarajan S, et al. Lancet. 2015;386(9990):266-73. doi:10.1016/S0140-6736(14)62000-6"),
 lambda: R.r_articulo("Lancet","2015 · 386(9990):266-73","Prognostic value of grip strength: findings from the Prospective Urban Rural Epidemiology (PURE) study",
          "Leong DP, Teo KK, Rangarajan S, et al.",[('Diseño','Cohorte prospectiva, 17 países'),('Participantes','139.691 adultos'),('Seguimiento','Mediana 4,0 años')],
          'La fuerza de prensión predijo la muerte por todas las causas y la cardiovascular mejor que la presión arterial sistólica.',"10.1016/S0140-6736(14)62000-6",fondo=R.gradiente('noche',seed=34),logo=("principal","blanco","tl")),
 lambda: R.r_paso("1",'La fuerza se mide.','Entrénala. Mídela.<br>Tu músculo es parte de tu longevidad.',fondo=M.foto(R.vidrio(D+P['hands'],None,'calido'),None),logo=("sello","claro","tl"),lado="izq"),
],
'P35-microbiota':[
 lambda: R.con_refs(R.r_tarjeta_micro('Microbiología','Bacterias intestinales',['Microorganismos unicelulares','La mayoría vive en el colon'],'Un adulto de referencia alberga unos 38 billones de bacterias — del mismo orden que el número de células humanas. [1]',fondo=R.bacterias(5)),"[1] Sender R, Fuchs S, Milo R. PLoS Biol. 2016;14(8):e1002533. doi:10.1371/journal.pbio.1002533"),
 lambda: R.con_refs(R.r_cifras('Estimaciones revisadas<br>para un adulto<br>de referencia (70 kg):',[("38T",'bacterias'),("30T",'células humanas'),("0.2",'kg — masa total<br>de esas bacterias')],rotulo=None,fondo=R.bacterias(9)),"[1] Sender R, Fuchs S, Milo R. PLoS Biol. 2016;14(8):e1002533. doi:10.1371/journal.pbio.1002533"),
 lambda: R.r_titulo_arriba('Tu microbioma','es parte de ti.','Agenda tu consulta —<br>link en la bio.',fondo=M.foto(R.vidrio(D+P['lab'],(0.25,0,0.8,1),'azul'),None),logo=("principal","gold","bl")),
],
'P36-apob':[
 lambda: R.r_tarjeta_datos('No pierdas de vista','lo que cambia por dentro.',"ApoB","92","mg/dL",[118,111,104,97,92],'Partículas que pueden entrar en la pared arterial — seguidas en el tiempo.',fondo=PH('ph_edan','frio',(0.05,0,1,0.85))),
 lambda: R.con_refs(R.r_claro("ApoB",'una partícula, una molécula','Cada partícula de lipoproteína aterogénica<br>lleva una molécula de apoB — así que la apoB<br>refleja cuántas de esas partículas tienes. [1]',fondo=R.gradiente('niebla',seed=36),logo=("principal","navy","tl")),"[1] Sniderman AD, Thanassoulis G, Glavinovic T, et al. JAMA Cardiol. 2019;4(12):1287-95. doi:10.1001/jamacardio.2019.3780"),
 lambda: R.r_articulo("JAMA Cardiol","2019 · 4(12):1287-95","Apolipoprotein B particles and cardiovascular disease: a narrative review",
          "Sniderman AD, Thanassoulis G, Glavinovic T, et al.",[('Tipo','Revisión narrativa'),('Enfoque','ApoB, LDL-C y no-HDL-C'),('Hallazgo','La apoB unifica los marcadores de riesgo lipídico')],
          'La apoB mide con mayor precisión el riesgo aterogénico de las lipoproteínas con apoB que el LDL-C o el no-HDL-C.',"10.1001/jamacardio.2019.3780",fondo=R.vidrio(D+P['desk'],None,'azul'),logo=("principal","blanco","tl")),
 lambda: R.r_titulo_arriba('Cuenta las partículas.','No solo el colesterol.','Agenda tu valoración —<br>link en la bio.',fondo=R.gradiente('noche',seed=37),logo=("principal","gold","bl")),
],
'P37-one-measurement':[
 lambda: R.r_nodo_luz('La precisión empieza con','una medición.',None,fondo=F('coffee','frio',None,30)),
],
'P38-word-inflammaging':[
 lambda: R.r_palabra("Inflammaging",'sustantivo',['Envejecimiento','Inflamación'],'El aumento crónico, de bajo grado, del estado proinflamatorio que acompaña al envejecimiento. [1]','Término acuñado por Franceschi y colaboradores en 2000. [1]',fondo=R.gradiente('aurora',seed=38)),
 lambda: R.con_refs(R.r_red("Inflammaging",'se puede medir.',['Metabólico','Inmune','Vascular','Cerebro','Músculo',"Sueño"],centro='Inflamación',fondo=R.gradiente('noche',seed=39)),"[1] Franceschi C, Bonafè M, Valensin S, et al. Ann N Y Acad Sci. 2000;908:244-54. doi:10.1111/j.1749-6632.2000.tb06651.x"),
],
'P39-daily-steps':[
 lambda: R.con_refs(R.r_cifras('Pasos diarios y<br>mortalidad — 15<br>cohortes: [1]',[("6–8k",'pasos/día: donde el<br>beneficio se estabilizó<br>en adultos de 60+'),("8–10k",'pasos/día en adultos<br>menores de 60'),("47k",'adultos seguidos<br>durante una mediana<br>de 7,1 años')],rotulo=None,fondo=R.vidrio(D+P['hall'],(0.2,0,1,1),'calido')),"[1] Paluch AE, Bajpai S, Bassett DR, et al. Lancet Public Health. 2022;7(3):e219-28. doi:10.1016/S2468-2667(21)00302-9"),
 lambda: R.r_articulo("Lancet Public Health","2022 · 7(3):e219-28","Daily steps and all-cause mortality: a meta-analysis of 15 international cohorts",
          "Paluch AE, Bajpai S, Bassett DR, et al.",[('Diseño','Metaanálisis, datos por participante'),('Participantes','47.471 adultos'),('Seguimiento','Mediana 7,1 años')],
          'Más pasos diarios: menor mortalidad por todas las causas de forma progresiva, hasta un nivel que varió según la edad.',"10.1016/S2468-2667(21)00302-9",fondo=R.gradiente('acero',seed=40),logo=("principal","blanco","tl")),
 lambda: R.r_paso("1",'Conoce tu línea de base.','Cuenta tus pasos habituales durante una semana<br>antes de fijar una meta.',fondo=R.gradiente('niebla',seed=41),logo=("principal","navy","tl"),lado="izq",light=True),
],
'P40-inside-lci-2':[
 lambda: R.r_poster('Bienvenidos a',"LCI.","Milla de Oro · El Poblado, Medellín.",None,None,fondo=BR('hall','calido',(0.15,0,1,1),1.7),logo=("sello","claro","tr"),veil="linear-gradient(0deg,rgba(28,19,11,.66) 0%,rgba(28,19,11,.22) 38%,rgba(28,19,11,0) 62%)",ajustar=True),
 lambda: R.r_natural('Medición','de grado clínico.','Cada prueba, en contexto.',fondo=VD('inbody',(0.15,0.2,0.85,1),'azul'),logo=("sello","claro","tr")),
 lambda: R.r_natural('Un espacio','pensado para ti.','Agenda tu visita — link en la bio.',fondo=F('cons','frio',(0.2,0,1,1)),logo=("principal","blanco","tl")),
],
'P41-testosterone':[
 lambda: R.r_cifra_titular('Testosterona','disminuye con la edad.',"1.6","%",'por año en la testosterona<br>total — hombres de<br>40 a 70 años. [1]',None,fondo=F('n_rope','bw',(0,0,1,1)),logo=("principal","blanco","bl"),refs="[1] Feldman HA, Longcope C, Derby CA, et al. J Clin Endocrinol Metab. 2002;87(2):589-98. doi:10.1210/jcem.87.2.8201"),
 lambda: R.r_articulo("J Clin Endocrinol Metab","2002 · 87(2):589-98","Age trends in the level of serum testosterone and other hormones in middle-aged men: longitudinal results from the Massachusetts Male Aging Study",
          "Feldman HA, Longcope C, Derby CA, et al.",[('Diseño','Cohorte longitudinal poblacional'),('Participantes','1.156 hombres seguidos 7–10 años'),('Hallazgo','La T biodisponible cayó 2–3% por año')],
          'La buena salud aparente sumó 10–15% al nivel de varios andrógenos.',"10.1210/jcem.87.2.8201",fondo=R.gradiente('noche',seed=42),logo=("principal","blanco","tl")),
 lambda: R.con_refs(R.r_circulos('Un diagnóstico<br>necesita <b>ambos</b>.','Síntomas','Signos y síntomas<br>compatibles con<br>testosterona baja.','Confirmación de laboratorio','Testosterona total baja, matutina<br>y en ayunas — confirmada<br>en una prueba repetida. [2]',paso=(3,4),seccion='Testosterona'),"[2] Bhasin S, Brito JP, Cunningham GR, et al. J Clin Endocrinol Metab. 2018;103(5):1715-44. doi:10.1210/jc.2018-00229",light=True),
 lambda: R.con_refs(R.r_titulo_arriba('Mídelo.','No adivines.','Agenda tu valoración —<br>link en la bio.',fondo=FXB('mesh_oscuro'),logo=("principal","gold","bl")),"[1] Feldman HA, Longcope C, Derby CA, et al. J Clin Endocrinol Metab. 2002;87(2):589-98. doi:10.1210/jcem.87.2.8201<br>[2] Bhasin S, Brito JP, Cunningham GR, et al. J Clin Endocrinol Metab. 2018;103(5):1715-44. doi:10.1210/jc.2018-00229"),
],
'P42-insulin-1921':[
 lambda: R.r_eyebrow_gigante('Toronto, 1921.','Un descubrimiento hecho al medir.',None,None,fondo=F('vlab','calido',(0.30,0,0.85,1)),logo=("sello","claro","tr"),ytop=0.66,color='#E3EBF3'),
 lambda: R.con_refs(R.r_centrado('En 1921, en la Universidad de Toronto,','la insulina','fue extraída y probada —<br>primero en animales, luego en<br>personas con diabetes. [1]',None,fondo=FXB('galaxia'),logo=("terciario","beige","tc"),y=0.32),"[1] Rosenfeld L. Insulin: discovery and controversy. Clin Chem. 2002;48(12):2270-88. PMID: 12446492"),
 lambda: R.con_refs(R.r_derecha('Detrás del descubrimiento:','la medición precisa.','Las mediciones frecuentes y precisas<br>de glucosa en muestras pequeñas<br>ayudaron a hacerlo posible. [1]',None,fondo=R.gradiente('noche',seed=41),logo=("sello","claro","tl"),fs=64),"[1] Rosenfeld L. Insulin: discovery and controversy. Clin Chem. 2002;48(12):2270-88. PMID: 12446492"),
 lambda: R.con_refs(R.r_titulo_arriba('Un siglo después,','seguimos midiendo primero.','Agenda tu valoración —<br>link en la bio.',fondo=FXB('malla'),logo=("principal","gold","bl")),"[1] Rosenfeld L. Insulin: discovery and controversy. Clin Chem. 2002;48(12):2270-88. PMID: 12446492"),
],
'N10-reel-cover':[
 lambda: R.r_titulo_arriba('Por qué fundé',"LCI.",'Reel · 40 segundos',fondo=F('p_sit','bw',(0.04,0.0,0.96,0.92)),logo=("sello","claro","tr"),color="#ffffff"),
],
}
only=sys.argv[1:]
async def main():
    async with async_playwright() as p:
        import _navegador; b=await _navegador.lanzar(p); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for k,sl in POSTS.items():
            if only and k not in only: continue
            os.makedirs('out_es/'+k,exist_ok=True)
            for i,f in enumerate(sl,1):
                await pg.set_content(f())
                try: await pg.wait_for_function('window.__lci_listo===true', timeout=6000)
                except Exception: await pg.wait_for_timeout(600)
                await pg.wait_for_timeout(120)
                await pg.locator('#lienzo').screenshot(path=f'out_es/{k}/{k[:3]}-{i}.png')
            print(k,len(sl))
        await b.close()
asyncio.run(main())
