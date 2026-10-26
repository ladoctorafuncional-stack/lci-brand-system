import os,shutil,glob
from PIL import Image,ImageDraw
cal=[('10-27','NA-perimenopausia',0), ('10-29', 'E01-vo2max', 0), ('10-31', 'PAOLA-thousand-supplements', 0), ('11-02', 'P28-just-tired', 0), ('11-04', 'N04-inside-lci', 0), ('11-06', 'P24-lpa', 0), ('11-08', 'PAOLA-exosomes', 0), ('11-10', 'NB-recuperacion', 0), ('11-12', 'P30-social-jetlag', 0), ('11-14', 'E02-antioxidants', 0), ('11-16', 'P31-quote', 0), ('11-18', 'NC-wearables', 0), ('11-20', 'P34-grip-strength', 0), ('11-22', 'P36-apob', 0), ('11-24', 'PAOLA-muscle-cells-timeline', 0), ('11-26', 'N05-patient-journey', 0), ('11-28', 'P29-4p', 0), ('11-30', 'PAOLA-schedule-assessment', 0), ('12-02', 'E03-sleep-regularity', 0), ('12-04', 'P41-testosterone', 0), ('12-06', 'P27-measured', 0), ('12-08', 'P37-one-measurement', 0), ('12-10', 'N06-functional-rigor', 0), ('12-12', 'N07-visit-medellin', 0), ('12-14', 'PAOLA-your-body-knows', 0), ('12-16', 'P33-word-sarcopenia', 0), ('12-18', 'P38-word-inflammaging', 0), ('12-20', 'P39-daily-steps', 0), ('12-22', 'N11-brainspan', 0), ('12-24', 'P40-inside-lci-2', 0), ('12-26', 'P35-microbiota', 0), ('12-28', 'N13-person-not-value', 0), ('12-30', 'P42-insulin-1921', 0), ('01-01', 'N09-healthspan', 0), ('01-03', 'P26-journey', 0)]
live=['Dra. Carolina (fijada)', 'Longevity, measured. (fijada)', 'Inside LCI (fijada)', 'Tiroides TSH', 'Your age on paper', 'Peso: where your fat is', 'Why I founded LCI', 'The brain ages too', 'We measure / Medimos', 'Healthspan (palabra)', 'Reclaim the energy']
PA=''
def src(lang,slug):
    for base in (f'out_{lang}',f'out_pend_{lang}'):
        if os.path.isdir(f'{base}/{slug}'): return sorted(glob.glob(f'{base}/{slug}/*.png'))
    return []
rows=[]
for lang in ('en','es'):
    root=f'FEED_LCI/{lang.upper()}'; shutil.rmtree(root,ignore_errors=True)
    covers=[]
    for i,(d,slug,note) in enumerate(cal,1):
        if slug:
            fs=src(lang,slug)
            if not fs: covers.append(None); continue
            dst=f'{root}/{i:02d}_{d}_{slug}'; os.makedirs(dst)
            for j,f in enumerate(fs,1): shutil.copy(f,f'{dst}/{j:02d}.png')
            covers.append(Image.open(fs[0]).convert('RGB'))
        else: covers.append(None)
    # grid: newest first, 3 cols
    w=360;h=450;order=list(range(len(cal)))[::-1]+[-(k+1) for k in range(len(live))]
    rowsN=(len(order)+2)//3
    G=Image.new('RGB',(3*w+8,rowsN*h+(rowsN)*4),(235,229,218)); dr=ImageDraw.Draw(G)
    for k,idx in enumerate(order):
        x=(k%3)*(w+4);y=(k//3)*(h+4)
        c=covers[idx] if idx>=0 else None
        if idx<0:
            dr.rectangle([x,y,x+w,y+h],fill=(93,118,140)); dr.text((x+14,y+14),'YA PUBLICADA: '+live[-idx-1],fill=(255,255,255)); continue
        if c: G.paste(c.resize((w,h)),(x,y))
        else:
            dr.rectangle([x,y,x+w,y+h],fill=(42,54,73)); dr.text((x+14,y+14),(cal[idx][2] or 'Paola: versión ES por subir'),fill=(210,181,138))
        dr.text((x+8,y+h-18),cal[idx][0].replace('-','/'),fill=(255,255,255))
    G.save(f'FEED_LCI/grid_{lang.upper()}.jpg',quality=85)
open('FEED_LCI/README.md','w').write("# Feed LCI 2026 — EN + ES\nOrden = calendario 13/oct → 1/ene. Carpetas NN_MM-DD_slug con láminas 01.png…\nCalendario reordenado desde 27/oct con lo que falta por publicar; las ya publicadas aparecen en gris-azul al final del grid.\nNB y NC: foto provisional del banco hasta tener las fotos Nano Banana #3 y #5.\n")
