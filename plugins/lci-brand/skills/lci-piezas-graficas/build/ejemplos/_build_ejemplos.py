# -*- coding: utf-8 -*-
"""Ejemplos de muestra para validar el motor de piezas LCI."""
import sys, os, io, base64
sys.path.insert(0, '/home/claude/lci-piezas-graficas/assets')
import marca as M
import lci_treat as T
from PIL import Image

IMG = '/home/claude/lci-piezas-graficas/assets/img-library'
OUT = '/home/claude/lci-piezas-graficas/build/ejemplos'
os.makedirs(OUT, exist_ok=True)

def cover(im, w, h):
    """Recorta tipo background-size:cover al aspecto del formato."""
    tr = w / h; ir = im.width / im.height
    if ir > tr:
        nw = int(im.height * tr); x = (im.width - nw)//2
        im = im.crop((x, 0, x+nw, im.height))
    else:
        nh = int(im.width / tr); y = (im.height - nh)//2
        im = im.crop((0, y, im.width, y+nh))
    return im.resize((w, h), Image.LANCZOS)

def datauri(im, q=84):
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

# ── foto tratada para hero de Story (tritone = mucho texto encima) ──
src = Image.open(f'{IMG}/hero_flatlay.png')
treated = T.treat(src, mode='tritone', vignette=0.22, contrast=0.14)
treated = cover(treated, 1080, 1920)
hero_uri = datauri(treated)

# 1) STORY editorial con foto
p1 = M.t_story(
    eyebrow_txt="LONGEVITY CLINICAL INSTITUTE",
    head="La comida es", head_it="información",
    head_b="para tus genes.",
    sub="Medicina funcional, regenerativa y de longevidad. "
        "Construimos tu salud desde la <span class='serif-it'>raíz celular</span>.",
    cta_txt="Agenda tu valoración",
    fondo=M.foto(hero_uri, veil="navy"),
)
open(f'{OUT}/01_story.html','w',encoding='utf-8').write(p1)

# 2) POST de dato clínico (gradiente navy firma)
p2 = M.t_dato(
    eyebrow_txt="POR QUÉ IMPORTA EL SUEÑO",
    numero="−40%", label="riesgo cardiometabólico con 7–8 h de sueño reparador",
    contexto="El sueño profundo regula el eje HPA, depura el cerebro vía sistema "
             "glinfático y reprograma tu metabolismo. <strong>No es descanso: es "
             "medicina regenerativa.</strong>",
    fondo=M.GRAD_NAVY, formato="post_v",
)
open(f'{OUT}/02_dato.html','w',encoding='utf-8').write(p2)

# 3) Pieza de CITA
p3 = M.t_cita(
    texto="La longevidad no se hereda:<br>se <span class='serif-it'>construye</span> "
          "cada día.",
    autor="DRA. CAROLINA RODRÍGUEZ · LCI",
    fondo=M.GRAD_NAVY_DEEP, formato="post_v",
)
open(f'{OUT}/03_cita.html','w',encoding='utf-8').write(p3)

print("HTML escritos en", OUT)
