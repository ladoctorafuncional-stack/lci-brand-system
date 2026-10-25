import sys,asyncio,os
sys.path.insert(0,'/tmp/claude-0/-home-claude/935dcae0-16a1-5584-ae31-8a4dc5eb42f1/scratchpad/plug/lci-suite/skills/lci-piezas-graficas/assets')
import marca as M, recetas_feed as R
from playwright.async_api import async_playwright
D='/mnt/user-data/uploads/Downloads/'
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
POSTS={
'N02-founder':[
 lambda: R.r_retrato("Dr. Carolina","Rodríguez Morales","Founder &amp; Medical Director",retrato=CUT('calido'),fondo=F('cons','calido',(0.05,0,0.85,1),16),logo=("sello","claro","tl"),h=1080,x=0.40).replace('rgba(9,12,18','rgba(28,19,11'),
 lambda: R.r_derecha("The first physician","in Latin America","with the Advanced Functional Medicine<br>Clinician (AFMC) certification.",
                     ["Kharrazian Institute · USA","AFMC · CFMC"],fondo=F('mri','azul',SQ),logo=("principal","blanco","tl"),fs=64,top=0.42),
 lambda: R.r_poster("Training","International.",None,None,["United States — advanced postgraduate<br>training endorsed by NUHS","United Kingdom — CPD international<br>accreditation","MSc in Functional Immunology —<br>Cogence Immunology, USA"],
                    fondo=F('lab','frio',(0.22,0,0.78,1)),logo=("sello","claro","tr")),
 lambda: R.r_centrado("Innovation without evidence is","speculation.","Evidence without biological<br>individuality never reaches<br>excellence.","— Dr. Carolina Rodríguez Morales",
                      fondo=F('brain_b','azul',SQ,2),logo=("terciario","beige","tc"),y=0.33),
 lambda: R.r_titulo_arriba("Medicine with rigor.","Care with time.",BOOK,fondo=F('p_sit','calido',(0.08,0.02,0.98,1.0)),logo=("principal","gold","bl")),
],
'N03-we-measure':[
 lambda: R.r_eyebrow_gigante("We measure.","We don't guess.",None,None,fondo=F('mri','bw',SQ,2),logo=("sello","claro","tr"),ytop=0.68,color='#E3EBF3'),
 lambda: R.r_centrado("A first consultation of at least","two hours.","Measurements and a complete<br>medical assessment.",None,
                      fondo=F('ther','bw',(0.05,0.03,0.95,1)),logo=("terciario","beige","tc"),y=0.36),
 lambda: R.r_marco("Biomarkers that speak","before symptoms do.",None,["Functional · Epigenetic · Immunological","Metabolic · Neurocognitive"],
                   fondo=R.vidrio(D+P['meas_dna'],None,'azul'),logo=("principal","blanco","tl")),
 lambda: R.r_derecha("Processed <span style='white-space:nowrap'>in-house</span>,<br>in Colombia","and in U.S. labs.","Interpreted with our own clinical AI —<br>always reviewed by your physician.",None,
                     fondo=F('edan','azul',(0.05,0.02,0.95,0.92),3),fs=64,top=0.44,logo=("sello","claro","tl")),
 lambda: R.r_claro("Biological age","from several biological clocks","A preliminary estimate — and a<br>personalized therapeutic roadmap.",fondo=F('brain_w','claro',(0.22,0,1.0,1),0,'right'),logo=("principal","navy","tl")),
 lambda: R.r_titulo_arriba("Exact numbers,","not assumptions.",BOOK,fondo=F('chair','calido',(0.2,0.05,1,1)),logo=("principal","gold","bl")),
],
'N04-inside-lci':[
 lambda: R.r_natural("Inside","LCI.","Milla de Oro · El Poblado, Medellín",fondo=F('recep','natural'),logo=None),
 lambda: R.r_natural("Where we","measure.","Clinical-grade measurement, in one room.",fondo=F('meas_w','natural'),logo=("principal","blanco","tr"),lado="der"),
 lambda: R.r_natural("Where we","listen.","First consultations of at least two hours.",fondo=F('cons','natural'),logo=("sello","navy","tl")),
 lambda: R.r_natural("Where you","rest.","A calm room for in-clinic therapies.",fondo=F('ther','natural'),logo=("principal","blanco","tl"),lado="der"),
 lambda: R.r_natural("Designed for","unhurried medicine.","Come and see it — link in bio.",fondo=F('coffee','natural'),logo=("terciario","navy","tr")),
],
'N05-patient-journey':[
 lambda: R.r_centrado("Your patient journey","from first contact","to your plan.",None,fondo=F('n_cons','frio',(0,0.02,1,0.98)),logo=("terciario","beige","bc"),y=0.32),
 lambda: R.r_paso("01","Pre-consultation","Clinical history, measurements and<br>baseline data — collected before you<br>sit down with your doctor.",fondo=F('inbody','azul'),logo=("principal","blanco","tl"),lado="izq"),
 lambda: R.r_paso("02","The consultation","At least two hours: measurements and<br>a complete, unhurried medical assessment.",fondo=F('chair','ambar',(0.2,0.05,1,1)),logo=("sello","claro","tr"),lado="der"),
 lambda: R.r_paso("03","Precision diagnostics","The tests your case actually needs —<br>no more, no less.",fondo=GR('noche',12),logo=("principal","blanco","tl"),lado="izq"),
 lambda: R.r_paso("04","Your action plan","A personalized roadmap built around<br>what your case needs: nutrition, movement,<br>sleep, therapies and follow-up.",fondo=F('brain_h','claro',SQ),logo=("principal","navy","tr"),lado="der",light=True),
 lambda: R.r_paso("05","Follow-up","We re-measure, adjust and track<br>your progress over time.",fondo=F('meas_dna','frio'),logo=("sello","claro","tl"),lado="izq",cta="Book your consultation — link in bio."),
],
'N06-functional-rigor':[
 lambda: R.r_poster("Functional,","with rigor.","Held to medical standards.","Evidence first. Biology always.",None,fondo=F('equip','bw',(0.25,0,1,0.95)),logo=("principal","blanco","tl"),lado="der"),
 lambda: R.r_derecha("If the evidence calls for","a statin, I prescribe it.","If an infection needs antibiotics<br>or a hospital, that is the treatment.",None,
                     fondo=GR('acero',13),logo=("sello","claro","tl")),
 lambda: R.r_marco("I don't stop","psychiatric medication","to “go natural.”",["And I don't fill patients with supplements.","That is not good medicine."],
                   fondo=F('meas_w','bw',None,6),logo=("principal","blanco","tr")),
 lambda: R.r_centrado("Evidence first.","Biology always.",None,"— Dr. Carolina Rodríguez Morales",fondo=F('hall','frio',(0.15,0,0.85,1)),logo=("terciario","beige","bc"),y=0.40),
],
'N07-visit-medellin':[
 lambda: R.r_titulo_arriba("Your visit","to Medellín.","International patients.",fondo=BR('night','calido',(0.24,0,1,0.95),1.95),logo=("principal","gold","bl")).replace('rgba(30,20,12,.70) 0%','rgba(30,20,12,.55) 0%').replace('rgba(30,20,12,.85) 100%','rgba(30,20,12,.70) 100%'),
 lambda: R.r_poster("In-clinic protocols","Up to 10 days.","The length depends<br>on your protocol.",None,None,fondo=F('desk','calido'),logo=("principal","blanco","tl"),veil=R.VEIL_CAFE),
 lambda: R.r_derecha("Airport, hotel, transport —","arranged for you.","And our team stays in touch<br>throughout your stay.",None,fondo=F('hall','azul',(0.1,0,0.9,1)),logo=("sello","claro","tl")),
 lambda: R.r_claro("In your language.","English and Spanish","A bilingual medical and patient-care team,<br>from first message to follow-up.",fondo=F('recep','claro'),logo=("principal","navy","tl")),
 lambda: R.r_natural("Plan your","visit.","Message us — link in bio<br>Milla de Oro · El Poblado, Medellín",fondo=F('chair','natural'),logo=("terciario","navy","tr")),
],
'N09-healthspan':[
 lambda: R.r_eyebrow_gigante("Living longer is not","living well.",None,None,fondo=F('brain_b','bw',SQ,1),logo=("sello","claro","tr"),ytop=0.68),
 lambda: R.r_claro("Healthspan","the years lived in good health","Lifespan: how many years you live.<br>Healthspan: how many of those years<br>you live in good health.",fondo=F('brain_w','claro',(0.22,0,1.0,1),0,'right'),logo=("principal","navy","tl")),
 lambda: R.r_centrado("Across 183 countries, the gap averages","9.6 years","and it has widened<br>over two decades. [1]",None,fondo=FXB('mesh_claro'),logo=("terciario","navy","tc"),y=0.36,light=True),
 lambda: R.r_derecha("In the United States,","12.4 years.","The largest gap measured. [1]",None,fondo=F('night','azul',(0.25,0,0.98,0.82)),logo=("sello","claro","tl")),
 lambda: R.r_marco("Driven largely by","chronic disease.",None,["Non-communicable disease. [1,2]","That is where measurement and","early action matter most."],fondo=GR('acero',15),logo=("principal","blanco","tl")),
 lambda: R.r_titulo_arriba("Not only more years.","More healthy years.",None,fondo=F('cons','ambar',(0.3,0,1,0.9)),logo=("principal","gold","bl"),
          refs="[1] Garmany A, Terzic A. JAMA Netw Open. 2024;7(12):e2450241. doi:10.1001/jamanetworkopen.2024.50241<br>[2] Garmany A, Yamada S, Terzic A. NPJ Regen Med. 2021;6(1):57. doi:10.1038/s41536-021-00169-5"),
],
'E01-vo2max':[
 lambda: R.r_eyebrow_gigante("Not your weight. Not your cholesterol.","Your VO<span style='font-size:.62em;vertical-align:-.1em'>2</span>max.",None,None,fondo=F('face','bw',(0.38,0,0.83,1)),logo=("sello","claro","tl"),ytop=0.68,color='#E3EBF3'),
 lambda: R.r_claro("VO<span style='font-size:.62em;vertical-align:-.1em'>2</span>max","oxygen, under effort","How well your heart, lungs and muscles<br>take up and use oxygen during exercise.",fondo=GR('niebla',16),logo=("principal","navy","tl")),
 lambda: R.r_articulo("JAMA Network Open","2018 · 1(6):e183605","Association of Cardiorespiratory Fitness With Long-term Mortality Among Adults Undergoing Exercise Treadmill Testing",
          "Mandsager K, Harb S, Cremer P, Phelan D, Nissen SE, Jaber W",[("Design","Retrospective cohort, Cleveland Clinic"),("Participants","122,007 adults"),("Follow-up","Median 8.4 years")],
          "Low vs elite fitness: adjusted HR <b>5.04</b> for all-cause mortality.","10.1001/jamanetworkopen.2018.3605",fondo=F('meas_w','azul',None,8),logo=("principal","blanco","tl")),
 lambda: R.r_centrado("Low fitness vs elite:","5× mortality.","Comparable to, or greater than,<br>smoking or diabetes. [1]",None,fondo=M.foto(R.movimiento(D+P['face'],'azul',(0.30,0,0.78,1)),None),logo=("terciario","beige","tc"),y=0.36),
 lambda: R.r_derecha("The good news:","it's modifiable.","No upper limit of benefit was<br>observed in this cohort. [1]",None,fondo=GR('noche',17),logo=("sello","claro","tl"),fs=70),
 lambda: R.con_refs(R.r_titulo_arriba("Measure it.","Don't guess it.","Book your longevity assessment —<br>link in bio.",fondo=F('inbody','ambar'),logo=("principal","gold","bl")),
          "[1] Mandsager K, Harb S, Cremer P, Phelan D, Nissen SE, Jaber W. JAMA Netw Open. 2018;1(6):e183605. doi:10.1001/jamanetworkopen.2018.3605"),
],
'E02-antioxidants':[
 lambda: R.r_poster("Antioxidant pills","Do they slow aging?","The best evidence says otherwise.",None,None,fondo=F('meas_w','calido',(0,0,0.75,0.6)),logo=("principal","blanco","tl"),veil=R.VEIL_CAFE),
 lambda: R.r_marco("Why they became","so popular.","Oxidative damage is linked to aging.",["Hence the leap: “supplementing","antioxidants should protect us.”"],fondo=R.vidrio(D+P['meas_w'],None,None),logo=("sello","claro","tr")),
 lambda: R.r_articulo("Cochrane Database Syst Rev","2012 · CD007176","Antioxidant supplements for prevention of mortality in healthy participants and patients with various diseases",
          "Bjelakovic G, Nikolova D, Gluud LL, Simonetti RG, Gluud C",[("Design","Systematic review &amp; meta-analysis"),("Trials","78 randomized trials"),("Participants","296,707")],
          "No reduction in mortality. In low-bias trials, beta-carotene and vitamin E <b>increased</b> it.","10.1002/14651858.CD007176.pub2",fondo=F('coffee','azul',None,8),logo=("principal","blanco","tl")),
 lambda: R.r_centrado("78 trials · 296,707 people","No benefit","on mortality. Beta-carotene and<br>vitamin E were linked to higher<br>mortality. [1]",None,fondo=R.bokeh(19),logo=("terciario","beige","tc"),y=0.34),
 lambda: R.r_claro("From the bottle","to the plate","Vegetables, fruit, olive oil —<br>not isolated megadoses.",fondo=F('desk','claro'),logo=("principal","navy","tl")),
 lambda: R.con_refs(R.r_derecha("Supplement","with criteria.","Personalized and evidence-based.<br>Book your assessment — link in bio.",None,fondo=F('cons','azul',(0.3,0,1,0.9)),logo=("sello","claro","tl"),top=0.40),
          "[1] Bjelakovic G, Nikolova D, Gluud LL, Simonetti RG, Gluud C. Cochrane Database Syst Rev. 2012;(3):CD007176. doi:10.1002/14651858.CD007176.pub2"),
],
'E03-sleep-regularity':[
 lambda: R.r_centrado("It's not only how long you sleep.","It's when.","Consistent sleep and wake times<br>may matter more than your 8 hours.",None,fondo=F('ther','azul',(0.37,0,1,1)),logo=("sello","claro","bc",110),y=0.12),
 lambda: R.r_derecha("Regularity","over duration.","Your body runs on a circadian clock.<br>Shifting bed and wake times<br>every day disrupts it.",None,fondo=R.vidrio(D+P['ther'],None,'azul'),logo=("sello","claro","tl")),
 lambda: R.r_articulo("Sleep","2024 · 47(1):zsad253","Sleep regularity is a stronger predictor of mortality risk than sleep duration: a prospective cohort study",
          "Windred DP, Burns AC, Lane JM, Saxena R, Rutter MK, Cain SW, Phillips AJK",[("Design","Prospective cohort, UK Biobank"),("Participants","60,977 adults"),("Data","&gt;10 million hours of accelerometry")],
          "More regular sleep: <b>20–48%</b> lower all-cause mortality vs the least regular quintile.","10.1093/sleep/zsad253",fondo=F('ther','azul',None,8),logo=("principal","blanco","tl")),
 lambda: R.r_derecha("Lower all-cause mortality:","20–48%","with more regular sleep. [1]<br>Observational evidence: an association,<br>not proof of cause.",None,fondo=GR('aurora',21),logo=("sello","claro","tl"),top=0.44),
 lambda: R.r_paso("1","Start with one thing.","Wake up at the same time all 7 days —<br>weekends included — and get natural<br>light soon after.",fondo=F('recep','claro'),logo=("principal","navy","tr"),lado="der",light=True),
 lambda: R.con_refs(R.r_poster("At LCI","We look at the data.","Not at assumptions.","Book your longevity assessment — link in bio.",None,fondo=F('cons','calido',(0.3,0,1,0.9)),logo=("principal","blanco","tl"),veil=R.VEIL_CAFE),
          "[1] Windred DP, Burns AC, Lane JM, Saxena R, Rutter MK, Cain SW, Phillips AJK. Sleep. 2024;47(1):zsad253. doi:10.1093/sleep/zsad253"),
],
'E04-waist-bmi':[
 lambda: R.r_eyebrow_gigante("Your weight doesn't tell you","where your fat is.",None,None,fondo=F('meas_dna','azul'),logo=("sello","claro","tr")),
 lambda: R.r_claro("What BMI ignores","muscle vs. fat — and where","BMI only divides weight by height.<br>It can't tell muscle from fat,<br>or where fat is stored.",fondo=GR('niebla',22),logo=("principal","navy","tl")),
 lambda: R.r_articulo("N Engl J Med","2008 · 359(20):2105-20","General and abdominal adiposity and risk of death in Europe",
          "Pischon T, Boeing H, Hoffmann K, et al. (EPIC)",[("Design","Prospective cohort, 9 European countries"),("Participants","359,387 adults"),("Follow-up","Mean 9.7 years")],
          "Highest vs lowest waist quintile, adjusted for BMI: RR <b>2.05</b> (men) · <b>1.78</b> (women).","10.1056/NEJMoa0801891",fondo=F('inbody','azul',None,8),logo=("principal","blanco","tl")),
 lambda: R.r_centrado("Even after adjusting for BMI,","up to 2×","the risk of death with the<br>largest waist circumference. [1]",None,fondo=GR('aurora',23),logo=("terciario","beige","tc"),y=0.34),
 lambda: R.r_marco("That's why we","measure.","We don't estimate.",["Body composition and fat distribution —","not just the scale."],fondo=F('inbody','azul',None,4),logo=("sello","claro","tr")),
 lambda: R.con_refs(R.r_poster("Know your","real numbers.",None,"Book your body-composition assessment —<br>link in bio.",None,fondo=F('desk','natural'),logo=("principal","blanco","tr"),Hs=70),
          "[1] Pischon T, Boeing H, Hoffmann K, et al. N Engl J Med. 2008;359(20):2105-20. doi:10.1056/NEJMoa0801891"),
],
'N11-brainspan':[
 lambda: R.r_claro("Brainspan","as important as lifespan","We assess cognitive function with our<br>own neurocognitive tests — to act early.",fondo=F('brain_l','claro',(0.0,0.05,0.62,0.95)),logo=("principal","navy","tl")),
],
'N12-biological-age':[
 lambda: R.r_derecha("Your age on paper","is not your biological age.","We estimate it with several<br>biological clocks — and re-measure<br>it over time.",None,fondo=F('n_age','azul',(0,0,1,1)),logo=("sello","claro","tl"),fs=62),
],
'N13-person-not-value':[
 lambda: R.r_marco("Treat the person,","not the lab value.","Every number is read in context.",["Your history. Your biology.","Your goals."],fondo=F('ibdisp','azul',(0,0,1,0.88),11),logo=("principal","blanco","tl")),
],
'P24-lpa':[
 lambda: R.r_claro("Lp(a)","measure it once","A cholesterol particle largely<br>written in your genes.",fondo=F('lab','claro',(0.25,0,0.80,1)),logo=("principal","navy","tl")),
 lambda: R.r_centrado("Its level is","largely genetic","— and it is not part of<br>a standard cholesterol panel. [1]",None,fondo=FXB('galaxia'),logo=("terciario","beige","tc"),y=0.34),
 lambda: R.r_articulo("Eur Heart J","2022 · 43(39):3925-46","Lipoprotein(a) in atherosclerotic cardiovascular disease and aortic stenosis: a European Atherosclerosis Society consensus statement",
          "Kronenberg F, Mora S, Stroes ESG, et al.",[("Type","Consensus statement (EAS)"),("Evidence","Epidemiologic and genetic studies"),("Finding","Lp(a) is a causal risk factor")],
          "Recommendation: test Lp(a) <b>at least once</b> in adults.","10.1093/eurheartj/ehac361",fondo=GR('noche',31),logo=("principal","blanco","tl")),
 lambda: R.r_circulos("Measured <b>once</b>,<br>known for <b>life</b>.","The gap","A standard lipid panel does not<br>include Lp(a), so elevated levels<br>often go unnoticed.","The approach","Measure it at least once in<br>adulthood, as the EAS consensus<br>recommends. [1]",paso=(4,5),seccion="Lp(a)"),
 lambda: R.con_refs(R.r_titulo_arriba("Know your Lp(a).","Once.","Book your assessment —<br>link in bio.",fondo=M.foto(R.vidrio(D+P['cons'],(0.3,0,1,0.9),'calido'),None),logo=("principal","gold","bl")),
          "[1] Kronenberg F, Mora S, Stroes ESG, et al. Eur Heart J. 2022;43(39):3925-46. doi:10.1093/eurheartj/ehac361"),
],
'P25-word-healthspan':[
 lambda: R.r_palabra("Healthspan","noun",["Longevity","Prevention"],"The years of life lived in good health — free from chronic disease and disability.","Longevity medicine aims to extend healthspan, not only lifespan.",fondo=F('n_juiceg','natural',(0,0,1,1))),
],
'P26-journey':[
 lambda: R.r_centrado("Your longevity","journey.","Measure · Interpret ·<br>Personalize · Re-measure",None,fondo=F('n_check','calido',(0,0.37,1,1),5),logo=("terciario","beige","bc"),y=0.30),
 lambda: R.r_orbitas("Your longevity","journey.",[("Measure","Clinical-grade biomarkers<br>and body composition."),("Interpret","Your physician reads every<br>number in context."),("Personalize","A plan built around what<br>your case needs."),("Re-measure","We track your progress<br>over time.")],fondo=R.gradiente('noche')),
 lambda: R.r_centrado("It starts with","one measurement.","Book your consultation —<br>link in bio.",None,fondo=FXB('galaxia_oro'),logo=("terciario","beige","tc"),y=0.36),
],
'P27-measured':[
 lambda: R.r_poster("Measured,","not assumed.","Clinical-grade biomarkers.","Every number, read in context.",None,fondo=PH('oxi','azul',(0,0.02,1,1)),logo=("principal","blanco","tl")),
 lambda: R.r_red("Measured,","not assumed.",["Metabolic","Hormonal","Inflammatory","Neurocognitive","Epigenetic","Body composition"],fondo=R.gradiente('acero',seed=4)),
 lambda: R.r_cifras("How a first visit<br>works at LCI:",[("2+","hours for a first<br>consultation"),("3","places your samples<br>are processed: in-house,<br>Colombia, U.S."),("48","hours to receive your<br>orders and prescriptions")],rotulo="Longevity Clinical Institute",fondo=FXB('malla')),
],
'P28-just-tired':[
 lambda: R.r_icono(ICON,"You are not","“just tired.”","Fatigue has causes —<br>and many of them can be measured.",fondo=R.gradiente('aurora',seed=7)),
 lambda: R.r_derecha("Fatigue is a symptom,","not a diagnosis.","Thyroid function, iron, sleep,<br>glucose, hormones and mood<br>can all play a role.",None,fondo=FXB('mesh_oscuro'),logo=("sello","claro","tl"),fs=64),
 lambda: R.r_circulos("From <b>“normal labs”</b><br>to <b>real answers</b>.","The problem","“Your labs are normal.”<br>Yet you still feel<br>exhausted.","Our approach","A complete assessment that<br>looks for the cause —<br>and measures it.",paso=(3,4),seccion="Fatigue"),
 lambda: R.r_titulo_arriba("Find the cause.","Then treat it.","Book your consultation —<br>link in bio.",fondo=M.foto(R.vidrio(D+P['chair'],(0.2,0.05,1,1),'calido'),None),logo=("principal","gold","bl")),
],
'P29-4p':[
 lambda: R.r_titulo_arriba("4P","medicine.","Predictive · Preventive ·<br>Personalized · Participatory",fondo=F('n_doc','calido',(0,0,1,1)),logo=("principal","gold","bl")),
 lambda: R.r_orbitas("The medicine","of the 4Ps.",[("Predictive","We look for risk before<br>disease appears."),("Preventive","We act early, while<br>there is time."),("Personalized","Your plan follows<br>your biology."),("Participatory","You are part of every<br>decision.")],fondo=R.gradiente('aurora',seed=9)),
 lambda: R.con_refs(R.r_centrado("A framework described by","Leroy Hood","Systems biology · P4 medicine [1]",None,fondo=FXB('malla'),logo=("terciario","beige","tc"),y=0.36),
          "[1] Hood L. Systems biology and p4 medicine: past, present, and future. Rambam Maimonides Med J. 2013;4(2):e0012. doi:10.5041/RMMJ.10112"),
],
'P30-social-jetlag':[
 lambda: R.r_derecha("What is","social jet lag?","When your body clock and<br>your schedule don't match.",None,fondo=PH('g_sofa','azul',(0.10,0,0.90,1)),logo=("sello","claro","tl"),fs=66),
 lambda: R.r_claro("Social jet lag","biological vs. social time","The gap between when your body wants<br>to sleep and when your schedule makes<br>you sleep. [1]",fondo=R.gradiente('niebla',seed=5),logo=("principal","navy","tl")),
 lambda: R.r_articulo("Chronobiol Int","2006 · 23(1-2):497-509","Social jetlag: misalignment of biological and social time",
          "Wittmann M, Dinich J, Merrow M, Roenneberg T",[("Design","Questionnaire study (MCTQ)"),("Participants","501 volunteers"),("Measured","Chronotype, sleep, wellbeing")],
          "Late chronotypes showed the largest gap between work and free days — and sleep debt on workdays.","10.1080/07420520500545979",fondo=VD('g_det',(0.1,0,0.9,1),'azul'),logo=("principal","blanco","tl")),
 lambda: R.r_paso("1","Start with one thing.","Keep your weekend wake time<br>close to your weekday one.",fondo=R.gradiente('acero',seed=8),logo=("sello","claro","tr"),lado="der"),
 lambda: R.con_refs(R.r_titulo_arriba("Your clock","matters.","Book your consultation —<br>link in bio.",fondo=M.foto(R.vidrio(D+P['night'],(0.2,0,1,1),'calido'),None),logo=("principal","gold","bl")),
          "[1] Wittmann M, Dinich J, Merrow M, Roenneberg T. Chronobiol Int. 2006;23(1-2):497-509. doi:10.1080/07420520500545979"),
],
'P31-quote':[
 lambda: R.r_cita("Innovation without evidence is speculation. Evidence without biological individuality never reaches excellence.","Dr. Carolina Rodríguez Morales",fondo=VD('p_bg',(0,0.05,1,0.95),None)),
],
'P32-thyroid':[
 lambda: R.r_ondas("Is your thyroid<br>checked with "+R.pildora("TSH")+" alone?","A starting point,<br>not the whole story.",None,fondo=R.ondas(2,nivel=0.62),y=0.20),
 lambda: R.r_circulos("One marker,<br>or the <b>full picture</b>?","Screening","TSH is the usual first test<br>of thyroid function.","When symptoms persist","Free T4, free T3 and thyroid<br>antibodies, chosen according<br>to your case.",paso=(2,3),seccion="Thyroid"),
 lambda: R.r_centrado("Your symptoms","deserve context.","Book your consultation —<br>link in bio.",None,fondo=R.ondas(7,calor=False),logo=("terciario","beige","tc"),y=0.36),
],
'P33-word-sarcopenia':[
 lambda: R.r_palabra("Sarcopenia","noun",["Muscle","Healthy aging"],"A muscle disease marked by low muscle strength, confirmed by low muscle quantity or quality. [1]","It is common in older adults — but it can begin earlier in life. [1]",fondo=F('n_mus','bw',(0,0,1,1))),
 lambda: R.con_refs(R.r_centrado("Strength","comes first.","In the revised European consensus,<br>low muscle strength is the key<br>characteristic of sarcopenia. [1]",None,fondo=R.gradiente('acero',seed=12),logo=("terciario","beige","tc"),y=0.34),"[1] Cruz-Jentoft AJ, Bahat G, Bauer J, et al. Age Ageing. 2019;48(1):16-31. doi:10.1093/ageing/afy169"),
],
'P34-grip-strength':[
 lambda: R.r_dato("5 kg","lower grip strength was linked<br>to 16% higher risk of death<br>from any cause. [1]",fondo=R.movimiento(D+P['n_dyn'],'azul'),x=0.07,y=0.55,refs="[1] Leong DP, Teo KK, Rangarajan S, et al. Lancet. 2015;386(9990):266-73. doi:10.1016/S0140-6736(14)62000-6"),
 lambda: R.r_articulo("Lancet","2015 · 386(9990):266-73","Prognostic value of grip strength: findings from the Prospective Urban Rural Epidemiology (PURE) study",
          "Leong DP, Teo KK, Rangarajan S, et al.",[("Design","Prospective cohort, 17 countries"),("Participants","139,691 adults"),("Follow-up","Median 4.0 years")],
          "Grip strength predicted all-cause and cardiovascular death better than systolic blood pressure.","10.1016/S0140-6736(14)62000-6",fondo=R.gradiente('noche',seed=34),logo=("principal","blanco","tl")),
 lambda: R.r_paso("1","Strength is measurable.","Train it. Track it.<br>Your muscle is part of your longevity.",fondo=M.foto(R.vidrio(D+P['hands'],None,'calido'),None),logo=("sello","claro","tl"),lado="izq"),
],
'P35-microbiota':[
 lambda: R.con_refs(R.r_tarjeta_micro("Microbiology","Gut bacteria",["Single-celled microorganisms","Most of them live in the colon"],"A reference adult carries an estimated 38 trillion bacteria — about the same order as the number of human cells. [1]",fondo=R.bacterias(5)),"[1] Sender R, Fuchs S, Milo R. PLoS Biol. 2016;14(8):e1002533. doi:10.1371/journal.pbio.1002533"),
 lambda: R.con_refs(R.r_cifras("Revised estimates<br>for a reference<br>adult (70 kg):",[("38T","bacteria"),("30T","human cells"),("0.2","kg — total mass<br>of those bacteria")],rotulo=None,fondo=R.bacterias(9)),"[1] Sender R, Fuchs S, Milo R. PLoS Biol. 2016;14(8):e1002533. doi:10.1371/journal.pbio.1002533"),
 lambda: R.r_titulo_arriba("Your microbiome","is part of you.","Book your consultation —<br>link in bio.",fondo=M.foto(R.vidrio(D+P['lab'],(0.25,0,0.8,1),'azul'),None),logo=("principal","gold","bl")),
],
'P36-apob':[
 lambda: R.r_tarjeta_datos("Don't lose sight of","what's changing inside.","ApoB","92","mg/dL",[118,111,104,97,92],"Particles that can enter the artery wall — tracked over time.",fondo=PH('ph_edan','frio',(0.05,0,1,0.85))),
 lambda: R.con_refs(R.r_claro("ApoB","one particle, one molecule","Every atherogenic lipoprotein particle carries<br>one apoB molecule — so apoB reflects how<br>many of those particles you have. [1]",fondo=R.gradiente('niebla',seed=36),logo=("principal","navy","tl")),"[1] Sniderman AD, Thanassoulis G, Glavinovic T, et al. JAMA Cardiol. 2019;4(12):1287-95. doi:10.1001/jamacardio.2019.3780"),
 lambda: R.r_articulo("JAMA Cardiol","2019 · 4(12):1287-95","Apolipoprotein B particles and cardiovascular disease: a narrative review",
          "Sniderman AD, Thanassoulis G, Glavinovic T, et al.",[("Type","Narrative review"),("Focus","ApoB, LDL-C and non-HDL-C"),("Finding","ApoB unifies lipid risk markers")],
          "ApoB more accurately measures the atherogenic risk of apoB lipoproteins than LDL-C or non-HDL-C.","10.1001/jamacardio.2019.3780",fondo=R.vidrio(D+P['desk'],None,'azul'),logo=("principal","blanco","tl")),
 lambda: R.r_titulo_arriba("Count the particles.","Not only the cholesterol.","Book your assessment —<br>link in bio.",fondo=R.gradiente('noche',seed=37),logo=("principal","gold","bl")),
],
'P37-one-measurement':[
 lambda: R.r_nodo_luz("Precision starts with","one measurement.",None,fondo=F('coffee','frio',None,30)),
],
'P38-word-inflammaging':[
 lambda: R.r_palabra("Inflammaging","noun",["Aging","Inflammation"],"The chronic, low-grade rise in pro-inflammatory status that accompanies aging. [1]","A term coined by Franceschi and colleagues in 2000. [1]",fondo=R.gradiente('aurora',seed=38)),
 lambda: R.con_refs(R.r_red("Inflammaging","is measurable.",["Metabolic","Immune","Vascular","Brain","Muscle","Sleep"],centro="Inflammation",fondo=R.gradiente('noche',seed=39)),"[1] Franceschi C, Bonafè M, Valensin S, et al. Ann N Y Acad Sci. 2000;908:244-54. doi:10.1111/j.1749-6632.2000.tb06651.x"),
],
'P39-daily-steps':[
 lambda: R.con_refs(R.r_cifras("Daily steps and<br>mortality — 15<br>cohorts: [1]",[("6–8k","steps/day: where the<br>benefit levelled off<br>in adults 60+"),("8–10k","steps/day in adults<br>under 60"),("47k","adults followed for<br>a median 7.1 years")],rotulo=None,fondo=R.vidrio(D+P['hall'],(0.2,0,1,1),'calido')),"[1] Paluch AE, Bajpai S, Bassett DR, et al. Lancet Public Health. 2022;7(3):e219-28. doi:10.1016/S2468-2667(21)00302-9"),
 lambda: R.r_articulo("Lancet Public Health","2022 · 7(3):e219-28","Daily steps and all-cause mortality: a meta-analysis of 15 international cohorts",
          "Paluch AE, Bajpai S, Bassett DR, et al.",[("Design","Meta-analysis, participant-level data"),("Participants","47,471 adults"),("Follow-up","Median 7.1 years")],
          "More daily steps: progressively lower all-cause mortality, up to a level that varied by age.","10.1016/S2468-2667(21)00302-9",fondo=R.gradiente('acero',seed=40),logo=("principal","blanco","tl")),
 lambda: R.r_paso("1","Know your baseline.","Count your usual steps for a week<br>before you set a goal.",fondo=R.gradiente('niebla',seed=41),logo=("principal","navy","tl"),lado="izq",light=True),
],
'P40-inside-lci-2':[
 lambda: R.r_poster("Welcome to","LCI.","Milla de Oro · El Poblado, Medellín.",None,None,fondo=BR('hall','calido',(0.15,0,1,1),1.7),logo=("sello","claro","tr"),veil="linear-gradient(0deg,rgba(28,19,11,.66) 0%,rgba(28,19,11,.22) 38%,rgba(28,19,11,0) 62%)",ajustar=True),
 lambda: R.r_natural("Clinical-grade","measurement.","Every test, in context.",fondo=VD('inbody',(0.15,0.2,0.85,1),'azul'),logo=("sello","claro","tr")),
 lambda: R.r_natural("A space designed","around you.","Book your visit — link in bio.",fondo=F('cons','frio',(0.2,0,1,1)),logo=("principal","blanco","tl")),
],
'P41-testosterone':[
 lambda: R.r_cifra_titular("Testosterone","declines with age.","1.6","%","per year in total<br>testosterone —<br>men aged 40–70. [1]",None,fondo=F('n_rope','bw',(0,0,1,1)),logo=("principal","blanco","bl"),refs="[1] Feldman HA, Longcope C, Derby CA, et al. J Clin Endocrinol Metab. 2002;87(2):589-98. doi:10.1210/jcem.87.2.8201"),
 lambda: R.r_articulo("J Clin Endocrinol Metab","2002 · 87(2):589-98","Age trends in the level of serum testosterone and other hormones in middle-aged men: longitudinal results from the Massachusetts Male Aging Study",
          "Feldman HA, Longcope C, Derby CA, et al.",[("Design","Population-based longitudinal cohort"),("Participants","1,156 men followed 7–10 years"),("Finding","Bioavailable T fell 2–3% per year")],
          "Apparent good health added 10–15% to the level of several androgens.","10.1210/jcem.87.2.8201",fondo=R.gradiente('noche',seed=42),logo=("principal","blanco","tl")),
 lambda: R.con_refs(R.r_circulos("A diagnosis<br>needs <b>both</b>.","Symptoms","Signs and symptoms<br>consistent with low<br>testosterone.","Lab confirmation","Low morning, fasting total<br>testosterone — confirmed<br>on a repeat test. [2]",paso=(3,4),seccion="Testosterone"),"[2] Bhasin S, Brito JP, Cunningham GR, et al. J Clin Endocrinol Metab. 2018;103(5):1715-44. doi:10.1210/jc.2018-00229",light=True),
 lambda: R.con_refs(R.r_titulo_arriba("Measure it.","Don't guess.","Book your assessment —<br>link in bio.",fondo=FXB('mesh_oscuro'),logo=("principal","gold","bl")),"[1] Feldman HA, Longcope C, Derby CA, et al. J Clin Endocrinol Metab. 2002;87(2):589-98. doi:10.1210/jcem.87.2.8201<br>[2] Bhasin S, Brito JP, Cunningham GR, et al. J Clin Endocrinol Metab. 2018;103(5):1715-44. doi:10.1210/jc.2018-00229"),
],
'P42-insulin-1921':[
 lambda: R.r_eyebrow_gigante("Toronto, 1921.","A discovery made by measuring.",None,None,fondo=F('vlab','calido',(0.30,0,0.85,1)),logo=("sello","claro","tr"),ytop=0.66,color='#E3EBF3'),
 lambda: R.con_refs(R.r_centrado("In 1921, at the University of Toronto,","insulin","was extracted and tested —<br>first in animals, then in<br>people with diabetes. [1]",None,fondo=FXB('galaxia'),logo=("terciario","beige","tc"),y=0.32),"[1] Rosenfeld L. Insulin: discovery and controversy. Clin Chem. 2002;48(12):2270-88. PMID: 12446492"),
 lambda: R.con_refs(R.r_derecha("Behind the discovery:","accurate measurement.","Frequent, accurate blood sugar<br>testing in small samples helped<br>make it possible. [1]",None,fondo=R.gradiente('noche',seed=41),logo=("sello","claro","tl"),fs=64),"[1] Rosenfeld L. Insulin: discovery and controversy. Clin Chem. 2002;48(12):2270-88. PMID: 12446492"),
 lambda: R.con_refs(R.r_titulo_arriba("A century later,","we still measure first.","Book your assessment —<br>link in bio.",fondo=FXB('malla'),logo=("principal","gold","bl")),"[1] Rosenfeld L. Insulin: discovery and controversy. Clin Chem. 2002;48(12):2270-88. PMID: 12446492"),
],
'N10-reel-cover':[
 lambda: R.r_titulo_arriba("Why I founded","LCI.","Reel · 40 seconds",fondo=F('p_sit','bw',(0.04,0.0,0.96,0.92)),logo=("sello","claro","tr"),color="#ffffff"),
],
}
only=sys.argv[1:]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for k,sl in POSTS.items():
            if only and k not in only: continue
            os.makedirs(k,exist_ok=True)
            for i,f in enumerate(sl,1):
                await pg.set_content(f())
                try: await pg.wait_for_function('window.__lci_listo===true', timeout=6000)
                except Exception: await pg.wait_for_timeout(600)
                await pg.wait_for_timeout(120)
                await pg.locator('#lienzo').screenshot(path=f'{k}/{k[:3]}-{i}.png')
            print(k,len(sl))
        await b.close()
asyncio.run(main())
