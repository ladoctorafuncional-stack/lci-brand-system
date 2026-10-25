"""Recetas de feed LCI (sistema de variación, oct 2026).

Regla: en una serie o carrusel NUNCA se repiten seguidas la misma receta, el mismo tratamiento de
foto ni la misma variante de logo. Lo único constante es la marca (Mencken + Poppins, paleta,
cápsula de contacto). Ver references/feed-instagram-lci.md §9.

Uso:
    import marca as M, recetas_feed as R
    uri = R.tratar(path, 'bw', crop=(x0,y0,x1,y1))
    html = R.r_centrado(fondo=M.foto(uri,'full'), ...)
"""
import io, base64
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import marca as M

W, H = 1080, 1350
STEEL = "#9fb2c6"      # azul acero (acento sobre oscuro)
CREAM = "#F1E6C8"      # crema de 'Thousand supplements'
GOLD = "#D2B58A"
NAVY = "#26313f"
AZUL_PAOLA = "#AFCAE4"   # azul claro de Paola en «The brain ages too» (medido 175,202,228): más vivo que #CAD3DD — usarlo en ALGUNAS piezas (acentos en cursiva sobre fondo oscuro)

# ───────── TRATAMIENTOS DE FOTO ─────────
def _arr(im): return np.asarray(im).astype(float) / 255.0
def _img(a): return Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
def _vignette(a, s=0.35):
    h, w = a.shape[:2]; y, x = np.ogrid[:h, :w]
    d = np.sqrt(((x - w / 2) / (w / 2)) ** 2 + ((y - h / 2) / (h / 2)) ** 2)
    return a * (1 - s * np.clip(d - 0.35, 0, 1))[..., None]

def tratar(path, modo, crop=None, q=90, blur=0):
    """modo: bw | ambar | calido | frio | azul | claro | natural. crop en fracciones (x0,y0,x1,y1). blur: desenfoque (px)
    para fondos cargados detrás de texto (receta R3 marco)."""
    im = Image.open(path).convert('RGB')
    if crop:
        w, h = im.size; im = im.crop((int(crop[0]*w), int(crop[1]*h), int(crop[2]*w), int(crop[3]*h)))
    a = _arr(im); L = (0.299*a[..., 0] + 0.587*a[..., 1] + 0.114*a[..., 2])[..., None]
    if modo == 'bw':        # B/N de alto contraste, negros profundos (Muscle Cells)
        g = np.clip((L - 0.08) * 1.35, 0, 1) ** 1.25
        a = _vignette(np.repeat(g, 3, 2), 0.45)
    elif modo == 'ambar':   # cálido sepia, como la corrección de 'Schedule'
        g = L ** 1.15
        sh = np.array([0.20, 0.13, 0.08]); hi = np.array([1.0, 0.90, 0.74])
        a = sh + (hi - sh) * g
        a = _vignette(a * 0.88, 0.40)
    elif modo == 'frio':    # frío desaturado (clínica)
        a = (0.25 * a + 0.75 * L) ** 1.35 * np.array([0.93, 0.98, 1.06]) * 0.80
    elif modo == 'azul':    # duotono navy→azul acero saturado (Brain/DNA)
        g = L ** 1.3
        sh = np.array([0.03, 0.06, 0.13]); hi = np.array([0.62, 0.78, 0.95])
        a = _vignette(sh + (hi - sh) * g, 0.35)
    elif modo == 'calido':  # Paola 'Schedule your longevity assessment': colores reales atenuados con
        # velo café translúcido (multiply ~0.55 cálido), más oscuro a la izquierda donde va el texto.
        h, w = a.shape[:2]; x = np.linspace(0, 1, w)[None, :, None]
        a = (0.75 * a + 0.25 * L) * np.array([0.50, 0.43, 0.34]) + np.array([0.03, 0.02, 0.01])
        a = a * (0.55 + 0.45 * np.clip(x / 0.75, 0, 1))
    elif modo == 'natural': # foto real de la clínica, colores verdaderos: solo pulido suave (sin efecto)
        a = np.clip((a - 0.5) * 1.06 + 0.5, 0, 1) * 0.97
    elif modo == 'claro':   # high-key luminoso azul pálido (Exosomes)
        g = 0.55 + 0.45 * L
        a = g * np.array([0.92, 0.96, 1.0]) + 0.04
    im = _img(a)
    if blur: im = im.filter(ImageFilter.GaussianBlur(blur))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

def recorte(path, max_h=1400, modo=None):
    """PNG con alfa (retrato sin fondo) → data-URI PNG, opcionalmente en B/N ('bw')."""
    im = Image.open(path).convert('RGBA'); im.thumbnail((max_h, max_h))
    if modo == 'calido':  # integra el recorte en un fondo cálido: baja contraste, tiñe medios/altas luces
        r, g, b, a = im.split(); rgb = np.asarray(Image.merge('RGB', (r, g, b))).astype(float) / 255
        rgb = 0.06 + 0.86 * rgb; rgb = rgb * np.array([1.0, 0.93, 0.84])
        im = Image.merge('RGBA', (*_img(rgb).split(), a))
    if modo == 'bw':
        r, g, b, a = im.split(); L = Image.merge('RGB', (r, g, b)).convert('L')
        L = ImageEnhance.Contrast(L).enhance(1.15); im = Image.merge('RGBA', (L, L, L, a))
    bb = io.BytesIO(); im.save(bb, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(bb.getvalue()).decode()

def movimiento(path, tinte='calido', crop=None, largo=0.12, ghost=0.06, q=90):
    """Efecto MOVIMIENTO (ref. aprobada oct 2026; misma familia que poster_reclaim_blur de Paola):
    barrido horizontal + doble exposición (fantasma desplazado) + tinte monocromo de marca.
    tinte: 'calido' (café-ámbar Paola) | 'azul' (navy-acero) | 'bw'. largo/ghost en fracción del ancho."""
    import cv2
    im = Image.open(path).convert('RGB')
    if crop:
        w, h = im.size; im = im.crop((int(crop[0]*w), int(crop[1]*h), int(crop[2]*w), int(crop[3]*h)))
    a = np.asarray(im).astype(np.float32) / 255; h, w = a.shape[:2]
    k = max(3, int(w * largo)); ker = np.zeros((k, k), np.float32); ker[k // 2, :] = 1.0 / k
    mb = cv2.filter2D(a, -1, ker)
    dx = int(w * ghost); sh = np.roll(a, -dx, axis=1)
    mb2 = cv2.filter2D(sh, -1, ker)
    out = 0.34 * a + 0.36 * mb + 0.30 * mb2         # nítido + barrido + fantasma barrido
    L = (0.299 * out[..., 0] + 0.587 * out[..., 1] + 0.114 * out[..., 2])[..., None]
    L = np.clip((L - 0.02) * 1.55, 0, 1) ** 0.95
    if tinte == 'calido':
        sh_, hi = np.array([0.16, 0.06, 0.03]), np.array([1.0, 0.74, 0.52])
    elif tinte == 'azul':
        sh_, hi = np.array([0.03, 0.05, 0.10]), np.array([0.70, 0.82, 0.96])
    else:
        sh_, hi = np.array([0.02, 0.02, 0.02]), np.array([0.96, 0.96, 0.96])
    out = _vignette(sh_ + (hi - sh_) * L, 0.25)
    b = io.BytesIO(); _img(out).save(b, 'JPEG', quality=q)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

def vidrio(path, crop=None, tinte=None, tiras=26, blur=26, q=90, w=None, h=None):
    """Efecto VIDRIO ESTRIADO / reeded glass (ref. 'Anatomy of a doctor's visit', oct 2026): la foto se ve a través de
    un vidrio de canales verticales — desenfoque fuerte + cada tira refracta (comprime y desplaza) su franja + brillo de
    borde por canal. Ideal para RECICLAR fotos ya usadas en portadas como fondo de interiores.
    tinte: None (color real) | 'calido' | 'azul' | 'bw'."""
    import cv2
    im = Image.open(path).convert('RGB')
    if crop:
        w, h = im.size; im = im.crop((int(crop[0]*w), int(crop[1]*h), int(crop[2]*w), int(crop[3]*h)))
    Wd, Hd = (w or W), (h or H)                                   # w/h: tamaño libre (bandas de documentos)
    im = im.resize((Wd, Hd), Image.LANCZOS)
    a = np.asarray(im).astype(np.float32) / 255
    a = cv2.GaussianBlur(a, (0, 0), blur)
    out = np.empty_like(a); sw = Wd / tiras; xs = np.arange(Wd)
    for i in range(tiras):
        x0, x1 = int(i * sw), int((i + 1) * sw)
        u = (xs[x0:x1] - x0) / max(1, x1 - x0 - 1)                      # 0..1 dentro del canal
        src = np.clip((x0 + (u - 0.5) * sw * 1.9 + sw * 0.35).astype(int), 0, Wd - 1)   # refracción
        out[:, x0:x1] = a[:, src]
        out[:, x0:x1] *= (0.90 + 0.16 * np.sin(np.pi * u))[None, :, None]           # volumen del canal
        out[:, x1 - 2:x1] = np.clip(out[:, x1 - 2:x1] * 1.18, 0, 1)                  # borde brillante
    if tinte:
        L = (0.299 * out[..., 0] + 0.587 * out[..., 1] + 0.114 * out[..., 2])[..., None]
        sh_, hi = {'calido': ([0.12, 0.07, 0.04], [1.0, 0.82, 0.64]), 'azul': ([0.03, 0.05, 0.10], [0.72, 0.84, 0.97]),
                   'bw': ([0.03, 0.03, 0.03], [0.95, 0.95, 0.95])}[tinte]
        out = np.array(sh_) + (np.array(hi) - np.array(sh_)) * L
    b = io.BytesIO(); _img(out).save(b, 'JPEG', quality=q)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

def pildora(palabra, color="#fff"):
    """Palabra resaltada dentro de una cápsula de contorno fino EN LÍNEA con el texto (ref. 'Most doctors only test TSH').
    Centrado óptico verificado midiendo píxeles: alto 1.02em, sin padding vertical, texto subido .06em (métricas Mencken)."""
    return (f'<span style="display:inline-flex;align-items:center;justify-content:center;border:1.6px solid {color};'
            f'border-radius:999px;padding:0 .34em;height:1.02em;line-height:1;margin:0 .06em;vertical-align:-.12em">'
            f'<span style="position:relative;top:-.13em">{palabra}</span></span>')

# ───────── FONDOS SIN FOTO (ref. feed aprobado por la Dra., oct 2026) ─────────
PALETAS_FONDO = {   # SOLO colores de marca: navy, azul acero, light blue, cream, gold
    'noche':  dict(base=(18, 26, 40),  blobs=[((0.25, 0.30), 0.55, (42, 54, 73)), ((0.80, 0.20), 0.45, (148, 180, 204)),
                                                ((0.70, 0.85), 0.50, (210, 181, 138)), ((0.10, 0.90), 0.40, (42, 54, 73))]),
    'acero':  dict(base=(30, 42, 60),  blobs=[((0.20, 0.15), 0.60, (148, 180, 204)), ((0.85, 0.60), 0.55, (202, 211, 221)),
                                                ((0.30, 0.90), 0.45, (42, 54, 73))]),
    'aurora': dict(base=(20, 28, 42),  blobs=[((0.15, 0.80), 0.55, (210, 181, 138)), ((0.70, 0.30), 0.60, (148, 180, 204)),
                                                ((0.95, 0.95), 0.40, (237, 229, 218))]),
    # Claras en LIGHT BLUE de marca (#CAD3DD) — para aclarar el feed (pedido de la Dra., 10-oct-2026)
    'cielo':  dict(base=(214, 222, 231), blobs=[((0.15, 0.15), 0.60, (244, 247, 250)), ((0.85, 0.70), 0.60, (176, 194, 212)),
                                                  ((0.30, 0.95), 0.45, (202, 211, 221))]),
    'cielo_crema': dict(base=(222, 228, 235), blobs=[((0.85, 0.15), 0.55, (237, 229, 218)), ((0.15, 0.75), 0.60, (190, 205, 220)),
                                                  ((0.60, 0.95), 0.40, (244, 247, 250))]),
    'niebla': dict(base=(238, 242, 246), blobs=[((0.20, 0.20), 0.60, (202, 211, 221)), ((0.85, 0.75), 0.55, (148, 180, 204)),
                                                  ((0.60, 0.10), 0.40, (255, 255, 255))]),
}
def gradiente(nombre='noche', grano=0.035, seed=1, w=1080, h=1350, q=92):
    """Fondo malla/degradé difuso (mesh gradient) con grano fino, solo colores de marca."""
    P = PALETAS_FONDO[nombre]; rng = np.random.default_rng(seed)
    y, x = np.mgrid[0:h, 0:w].astype(np.float32); x /= w; y /= h
    img = np.zeros((h, w, 3), np.float32) + np.array(P['base'], np.float32) / 255
    for (cx, cy), r, col in P['blobs']:
        m = np.exp(-(((x - cx) ** 2 + ((y - cy) * h / w) ** 2) / (2 * (r * 0.55) ** 2)))[..., None]
        img = img * (1 - 0.85 * m) + (np.array(col, np.float32) / 255) * 0.85 * m
    img += rng.normal(0, grano, (h, w, 1)).astype(np.float32)
    b = io.BytesIO(); _img(img).save(b, 'JPEG', quality=q)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

def bokeh(seed=3, w=1080, h=1350, q=90):
    """Fondo bokeh dorado/crema sobre navy-café (ref. 'Word of the Day')."""
    from PIL import ImageDraw
    rng = np.random.default_rng(seed)
    im = Image.new('RGB', (w, h), (22, 18, 16)); d = ImageDraw.Draw(im, 'RGBA')
    for _ in range(140):
        r = int(rng.uniform(4, 70)); cx, cy = rng.uniform(0, w), rng.uniform(0, h)
        col = [(210, 181, 138), (237, 229, 218), (180, 130, 70), (148, 180, 204)][rng.integers(0, 4)]
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col + (int(rng.uniform(40, 150)),))
    im = im.filter(ImageFilter.GaussianBlur(6))
    big = Image.new('RGB', (w, h), (0, 0, 0)); d2 = ImageDraw.Draw(big, 'RGBA')
    for _ in range(6):
        r = int(rng.uniform(150, 320)); cx, cy = rng.uniform(-100, w + 100), rng.uniform(-100, h + 100)
        d2.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(210, 160, 90, 255))
    big = big.filter(ImageFilter.GaussianBlur(90))
    a = np.clip(_arr(im) + 0.45 * _arr(big), 0, 1)
    b = io.BytesIO(); _img(a).save(b, 'JPEG', quality=q)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

# ───────── PIEZAS COMUNES ─────────
def _abs(x, y, html, extra=""):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;{extra}">{html}</div>'
def _lum_fondo(fondo, caja):
    """Luminancia media (0–1) del FONDO real en la caja (x0,y0,x1,y1) de la pieza. Lee la primera imagen data-URI del fondo
    (cover centrado). Devuelve None si el fondo no es una imagen."""
    import re, base64, io
    from PIL import Image
    mt = re.search(r"data:image/[a-z]+;base64,([A-Za-z0-9+/=]+)", fondo or "")
    if not mt: return None
    im = Image.open(io.BytesIO(base64.b64decode(mt.group(1)))).convert('L')
    s = max(W / im.width, H / im.height); im = im.resize((round(im.width*s), round(im.height*s)))
    ox, oy = (im.width - W)//2, (im.height - H)//2
    x0, y0, x1, y1 = [int(v) for v in caja]
    return sum(im.crop((x0+ox, y0+oy, x1+ox, y1+oy)).getdata()) / max(1, (x1-x0)*(y1-y0)) / 255

def _logo(kind, theme, pos, size=None, xl=None):
    """pos: tl | tr | tc | bl | bc. Tamaño por variante (principal 22%W; sello 150px; terciario 120px)."""
    h = size or {"principal": round(W*0.22/2.35), "sello": 150, "terciario": 118}[kind]   # principal 22 %W (la Dra., 10-oct-2026: un poquito más pequeño para que no choque con los textos)
    if theme == 'auto':   # se resuelve en _doc() según la luminancia real del fondo detrás del logo
        return f'§LOGOAUTO§{kind}§{pos}§{h}§{xl or ""}§'
    img = M.logo(kind, theme, h=h)
    y_top = M.margen(W, H)   # story también al margen de 108 px (la Dra., 11-oct-2026: el logo a 210 quedaba «demasiado abajo»)
    x_l = round(W*xl) if xl else M.margen(W, H)   # logo alineado al margen (10-oct-2026)   # logo dentro de la zona segura (10-oct-2026)
    if pos == "tl": return _abs(x_l, y_top, img)
    if pos == "tr": return f'<div style="position:absolute;right:{x_l}px;top:{y_top}px;">{img}</div>'
    if pos == "tc": return f'<div style="position:absolute;left:0;right:0;top:{y_top}px;display:flex;justify-content:center;">{img}</div>'
    if pos == "bl": return _abs(x_l, round(H*0.74), img)
    if pos == "bc": return f'<div style="position:absolute;left:0;right:0;top:{round(H*0.74)}px;display:flex;justify-content:center;">{img}</div>'
    raise ValueError(pos)
def _pill_web(x, w=None, y=None):
    """Cápsula SOLO-WEB dentro del vidrio (10-oct-2026). x = borde izquierdo del texto (dentro del vidrio)."""
    m = M.margen(W, H); y = H - round(m*1.2) if y is None else y
    return (f'<div data-rol="pie" style="position:absolute;left:{round(x)}px;top:{y}px;">{M.pill(solo_web=True)}</div>')
def _pill(light=False, top=None, vidrio=False):
    """Cápsula de contacto: dentro de los márgenes laterales (10 % del lado corto) y centrada en la banda del
    margen inferior — es lo único que vive fuera de la zona segura (guía de márgenes de la Dra., 10-oct-2026)."""
    m = M.margen(W, H); ph = 58
    y = round(H*top) if top else (H - round(m*1.2) if H < 1500 else H - 190)   # story: por encima de la barra de respuesta (250 px)   # misma altura que la cápsula de Paola en «Reclaim» (≈0.905 H), no pegada al borde
    vd = ('backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);background:rgba(20,26,37,.58);border-radius:20px;'
          if vidrio else '')   # cápsula sobre foto cargada: también lleva soporte de vidrio
    return (f'<div data-rol="pie" style="position:absolute;left:{m}px;right:{m}px;'
            f'top:{y}px;{vd}">{M.pill()}</div>')
def _lum_lin(L):   # luminancia relativa aproximada desde el gris 0–1
    return ((L + 0.055) / 1.055) ** 2.4 if L > 0.04045 else L / 12.92

def _resolver_logos(body, fondo):
    """Regla de la Dra. (10-oct-2026): el logo debe VERSE con claridad.
    1) Se mide el fondo real detrás del logo y se calcula el contraste del logo BLANCO y del logo NAVY.
    2) Si alguno llega a ≥ 4.5:1 se usa ese color.
    3) Si el fondo es de tono medio o cargado (madera iluminada, estantes) y NINGUNO llega, el logo blanco va sobre un
       SOPORTE: cápsula de vidrio esmerilado con tinte navy, ajustada al logo y alineada al margen."""
    import re
    def rep(mt):
        kind, pos, h, xl = mt.group(1), mt.group(2), int(mt.group(3)), (float(mt.group(4)) if mt.group(4) else None)
        w = round(h * (2.35 if kind == 'principal' else 1.0)); m = M.margen(W, H); y = m
        x = (W - m - w) if pos == 'tr' else (W - w)//2 if pos in ('tc', 'bc') else (round(W*xl) if xl else m)
        if pos in ('bl', 'bc'): y = round(H*0.74)
        L = _lum_fondo(fondo, (x, y, x + w, y + h))
        if L is None: return _logo(kind, 'blanco', pos, h, xl)
        lb = _lum_lin(L); cr_bl = 1.05 / (lb + 0.05); cr_nv = (lb + 0.05) / (0.032 + 0.05)
        # El color del logo DEPENDE DE LA PIEZA (fondo, foto, necesidad): no hay un color fijo. Se elige la variante de marca que
        # mejor contraste dé (blanco, navy…); si ninguna llega a 4.5:1 (tono medio, p. ej. madera iluminada), se baja la luz de
        # esa zona de la foto de forma natural y se usa el blanco.
        if max(cr_bl, cr_nv) >= 4.5:
            return _logo(kind, 'blanco' if cr_bl >= cr_nv else 'navy', pos, h, xl)
        # Soporte FOTOGRÁFICO (la Dra., 10-oct-2026: ni cápsula ni difuminado «exclusivo para el logo»): una caída de luz
        # NATURAL de la foto — viñeta amplia desde la esquina/borde donde está el logo, que abarca toda la parte alta de la
        # imagen, como si en esa zona la luz fuera más baja. Nunca una mancha local alrededor del logo.
        esq = '100% 0%' if pos == 'tr' else '0% 0%' if pos == 'tl' else '50% 0%'
        if pos in ('bl', 'bc'): esq = '0% 100%' if pos == 'bl' else '50% 100%'
        luz = (f'<div style="position:absolute;inset:0;pointer-events:none;background:'
               f'radial-gradient(150% 75% at {esq},rgba(10,13,20,.70) 0%,rgba(10,13,20,.36) 40%,rgba(10,13,20,0) 74%),'
               f'linear-gradient({"180deg" if pos in ("tr","tl","tc") else "0deg"},rgba(10,13,20,.22) 0%,rgba(10,13,20,0) 34%)"></div>')
        return luz + _logo(kind, 'blanco', pos, h, xl)
    return re.sub(r'§LOGOAUTO§(\w+)§(\w+)§(\d+)§([\d.]*)§', rep, body)

def _doc(body, fondo, light=False, soporte=None):
    body = _resolver_logos(body, fondo)
    if soporte: body = f'<!--SOPORTE:{soporte}-->' + body
    html = M.lienzo('story' if H > 1500 else 'carrusel', '<div style="position:absolute;inset:0;z-index:2;">' + body + '</div>',
                    fondo=fondo, theme='light' if light else 'navy')
    return html.replace("</head>", "<style>.pill{border-radius:20px;height:58px;padding:0 18px;}</style>" + M.OPTICA_JS + "</head>", 1)
def _fl(t):
    """Texto secundario fluido: quita los <br> manuales (al subir tamaños dejaban viudas) — el corte lo hace text-wrap:balance."""
    return t.replace('<br>', ' ') if isinstance(t, str) else t

def _veil(css): return f'<div style="position:absolute;inset:0;background:{css};"></div>'
POP = "font-family:Poppins,sans-serif;"
MEN = "font-family:'Mencken Std',serif;"

# ───────── RECETAS ─────────
VEIL_NAVY = "linear-gradient(0deg,rgba(25,34,46,.92) 0%,rgba(25,34,46,.45) 45%,rgba(25,34,46,0) 75%)"
VEIL_CAFE = "linear-gradient(0deg,rgba(28,19,11,.80) 0%,rgba(28,19,11,.35) 40%,rgba(28,19,11,0) 70%)"  # Schedule (Paola)

def r_poster(acento, bold, reg=None, tagline=None, lista=None, fondo=None, logo=("principal", "blanco", "tl"), Hs=74, veil=None, lado="izq", ajustar=False):
    """R1 'Reclaim': caja-acento + bold + regular + tagline + corchete. Texto abajo-izquierda, alineado al borde
    izquierdo de la cápsula de contacto (W*.075), pedido por la Dra. oct 2026."""
    fe = round(Hs*0.564); sp = lambda px: f'<div style="height:{round(px)}px"></div>'
    # Caja-acento: fondo CLARO translúcido (cream de marca) + texto navy de alto contraste (pedido de la Dra., oct 2026)
    # RECUADRO-acento (≠ resaltado): caja crema traslúcida con aire propio, aprobada por la Dra. ('Antioxidant pills').
    eb = (f'<div><span id="pbx" style="display:inline-block;background:rgba(237,229,218,.80);border:1px solid rgba(255,255,255,.55);border-radius:3px;'
          f'backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);padding:{round(fe*.18)}px {round(fe*.5)}px;line-height:1;">'
          f'<span style="{M.it_css("acento",fe,"#2A3649")}line-height:1;position:relative;top:-.12em;left:-.035em;">{acento}</span></span></div>')
    # Rev. 10-oct-2026 (la Dra.): recuadro + titular + regular como UN bloque apretado; luego respiro, filete fino
    # al ancho del bloque, respiro y tagline más grande (≥ 38 px).
    blk = eb + f'<div style="{MEN}color:#fff;font-weight:700;font-size:{Hs}px;line-height:.94;margin-top:{round(Hs*-0.29)}px"><span id="pbd" style="display:inline-block">{bold}</span></div>'
    if reg: blk += f'<div style="{MEN}color:#fff;font-weight:400;font-size:{round(Hs*.692)}px;line-height:1.04;margin-top:{round(Hs*.04)}px">{reg}</div>'
    if tagline: blk += (sp(Hs*.40) + '<div style="height:1.5px;background:rgba(255,255,255,.70)"></div>' + sp(Hs*.36)
                        + f'<div style="{POP}font-style:italic;font-weight:300;font-size:{round(Hs*.52)}px;line-height:1.36;color:{STEEL};text-wrap:balance">{_fl(tagline)}</div>')
    blk = f'<div style="display:inline-block;max-width:100%;text-align:inherit">{blk}</div>'
    if lista:
        its = "".join(f'<div style="{POP}font-style:italic;font-size:{round(Hs*.385)}px;color:#fff;margin:{round(Hs*.1)}px 0;line-height:1.2">{i}</div>' for i in lista)
        blk += sp(Hs*.52) + f'<div class="conx" style="grid-template-columns:46px 1fr;gap:0 28px;margin-left:{round(W*.14)}px;"><div class="ln"></div><div>{its}</div></div>'
    body = (_veil(veil or VEIL_NAVY)
            + (_logo(*logo) if logo else "") + f'<div style="position:absolute;left:{M.margen(W,H)}px;right:{M.margen(W,H)}px;bottom:{round(H*.155)}px;text-align:{"right" if lado=="der" else "left"}">{blk}</div>' + _pill())
    if ajustar:  # titular bold del MISMO ancho que la caja-acento (pedido de la Dra., oct 2026); mide glifos reales
        body += ('<script>document.fonts.ready.then(()=>{const b=document.getElementById("pbx"),t=document.getElementById("pbd");'
                 'for(let k=0;k<4;k++){const r=document.createRange();r.selectNodeContents(t);const tw=r.getBoundingClientRect().width;'
                 'const fs=parseFloat(getComputedStyle(t.parentElement).fontSize);t.parentElement.style.fontSize=(fs*b.getBoundingClientRect().width/tw)+"px";}});</script>')
    # Aire ÓPTICO recuadro→titular constante (0.18×Hs) midiendo la TINTA real de la primera línea del titular
    # (las ascendentes de «with», «the» suben más que una mayúscula: un margen fijo pegaba unos y separaba otros).
    body += ('<script>(function(){function fit(){var b=document.getElementById("pbx"),t=document.getElementById("pbd");if(!b||!t)return;'
             'var w=t.parentElement,cs=getComputedStyle(t),c=document.createElement("canvas").getContext("2d");'
             'c.font=cs.fontStyle+" "+cs.fontWeight+" "+cs.fontSize+" "+cs.fontFamily;'
             'var r=document.createRange(),n=t.firstChild;while(n&&n.nodeType!==3)n=n.firstChild;if(!n)return;'
             'var txt=n.textContent,top0=null,end=txt.length;for(var i=0;i<txt.length;i++){r.setStart(n,i);r.setEnd(n,i+1);var y=r.getBoundingClientRect().top;if(top0===null)top0=y;else if(y>top0+5){end=i;break;}}'
             'var first=txt.slice(0,end),m=c.measureText(first),mk=document.createElement("span");mk.style.cssText="display:inline-block;width:0;height:0;vertical-align:baseline";'
             't.insertBefore(mk,t.firstChild);var base=mk.getBoundingClientRect().top;mk.remove();'
             'var ink=base-m.actualBoundingBoxAscent,g=%d,d=(b.getBoundingClientRect().bottom+g)-ink;'
             'w.style.marginTop=(parseFloat(getComputedStyle(w).marginTop)+d)+"px";}'
             'if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fit);else fit();})();</script>') % round(min(Hs, 90)*.24)
    return _doc(body, fondo)

def r_centrado(pre, estrella, reg=None, nota=None, fondo=None, logo=("terciario", "auto", "tc"), color=CREAM, y=0.40, resaltar=False, light=False, velo=True):
    """R2 'Thousand supplements': todo centrado. Poppins light pequeño + ESTRELLA Mencken it 800 gigante
    crema + línea serif regular + nota entre paréntesis. Contraste de tamaños extremo."""
    if light: color = NAVY if color == CREAM else color
    c_pre, c_reg, c_not = ("#3a4352", NAVY, "#4f5a68") if light else ("#e9e4da", "#fff", "#d8d2c6")
    st = H > 1500   # historia: más aire entre bloques (Dra., 10-oct-2026: «los textos demasiado pegados»)
    g_est, g_reg, g_not, lh_reg, lh_not = (30, 62, 46, 1.16, 1.5) if st else (10, 44, 26, 1.05, 1.3)
    blk = (f'<div style="{POP}font-weight:300;font-size:40px;color:{c_pre};line-height:1.25;text-wrap:balance">{pre}</div>'
           + (f'<div style="margin-top:22px">{M.barra(estrella, 104, M.it_css("acento", 104, "#26313f"), fondo="rgba(202,211,221,.92)", alinear=False)}</div>' if resaltar else
              f'<div style="{M.it_css("hero_oscuro",132,color)}line-height:1.02;margin-top:{g_est}px">{estrella}</div>'))
    if reg: blk += f'<div style="{MEN}font-weight:400;font-size:56px;color:{c_reg};line-height:{lh_reg};margin-top:{g_reg}px;text-wrap:balance">{_fl(reg)}</div>'
    if nota: blk += f'<div style="{POP}font-weight:300;font-size:34px;color:{c_not};line-height:{lh_not};margin-top:{g_not}px;text-wrap:balance">{_fl(nota)}</div>'
    vl = "" if (light or not velo) else _veil("radial-gradient(85% 60% at 50% 45%,rgba(10,12,16,.68) 0%,rgba(10,12,16,.22) 72%),linear-gradient(0deg,rgba(10,12,16,.85) 0%,rgba(10,12,16,0) 30%)")
    body = (vl + (_logo(*logo) if logo else '') + f'<div data-pila="{"0.95" if st else "0.30"}" style="position:absolute;left:{M.margen(W,H)}px;right:{M.margen(W,H)}px;top:{round(H*y)}px;text-align:center">{blk}</div>' + _pill(light=light))
    return _doc(body, fondo, light=light)

def r_marco(bold, it, reg=None, lista=None, fondo=None, logo=("principal", "blanco", "tl")):
    """R3 'Brain': texto DENTRO de un marco de filete fino; bold blanco + it 800 azul acero + regular;
    conectores con nodos que salen del marco."""
    inner = (f'<div style="{MEN}font-weight:700;font-size:92px;color:#fff;line-height:.98">{bold}</div>'
             f'<div style="{M.it_css("hero_oscuro",92,STEEL)}line-height:1.0">{it}</div>')
    if reg: inner += f'<div style="{MEN}font-weight:400;font-size:52px;color:#fff;line-height:1.02;margin-top:18px">{reg}</div>'
    box = f'<div style="display:inline-block;border:1.5px solid rgba(159,178,198,.75);padding:44px 52px 46px 52px;background:rgba(9,14,24,.35)">{inner}</div>'
    lst = ""
    if lista:   # conector de Paola ('The brain ages too'): una rama por ítem, a la altura de su 1ª línea
        lst = f'<div style="margin-left:92px">{M.conector(lista, fs=27, color="#fff")}</div>'
    body = (_veil("linear-gradient(0deg,rgba(6,10,20,.85) 0%,rgba(6,10,20,.25) 40%,rgba(6,10,20,.10) 100%)")
            + (_logo(*logo) if logo else '') + f'<div style="position:absolute;left:{round(W*.10)}px;right:{round(W*.075)}px;top:{round(H*.30)}px">{box}{lst}</div>' + _pill())
    return _doc(body, fondo)

def r_derecha(bold, it, nota=None, bullets=None, fondo=None, logo=("sello", "claro", "tl"), fs=78, top=0.50):
    """R4 'DNA': bloque ALINEADO A LA DERECHA en la mitad inferior; bold blanco + it 800 azul acero;
    filete fino al ancho del bloque; viñetas estrella (SVG, nunca glifo ✦: no existe en Poppins/Mencken) doradas en versales Poppins it."""
    blk = (f'<div data-opt style="{MEN}font-weight:700;font-size:{fs}px;color:#fff;line-height:1.0">{bold}</div>'
           f'<div data-opt style="{M.it_css("hero_oscuro",fs,STEEL)}line-height:1.04">{it}</div>'
           f'<div style="height:1.5px;background:rgba(255,255,255,.85);margin:34px 0 26px"></div>')
    if nota: blk += f'<div style="{POP}font-style:italic;font-weight:300;font-size:37px;color:{STEEL};line-height:1.4;text-wrap:balance">{_fl(nota)}</div>'
    if bullets: blk += "".join(f'<div style="{POP}font-style:italic;font-size:28px;letter-spacing:.06em;color:#fff;margin:8px 0 0 34px;text-transform:uppercase"><span style="margin-right:14px"><svg width="16" height="16" viewBox="0 0 16 16" style="vertical-align:-1px"><path d="M8 0 L9.6 6.4 L16 8 L9.6 9.6 L8 16 L6.4 9.6 L0 8 L6.4 6.4 Z" fill="{GOLD}"/></svg></span>{b}</div>' for b in bullets)
    body = (_veil("linear-gradient(0deg,rgba(8,12,22,.9) 0%,rgba(8,12,22,.4) 45%,rgba(8,12,22,0) 70%)")
            + (_logo(*logo) if logo else '') + f'<div style="position:absolute;left:{round(W*.36)}px;right:{round(W*.09)}px;top:{round(H*top)}px">{blk}</div>' + _pill())
    return _doc(body, fondo)

def r_titulo_arriba(it1, it2=None, sub=None, fondo=None, logo=("principal", "gold", "bl"), color=CREAM, refs=None):
    """R5 'Schedule' (corrección cálida): titular Mencken it ARRIBA-izquierda en crema + sub Poppins it;
    logo ABAJO-izquierda sobre la cápsula. Composición invertida; velo arriba y abajo."""
    blk = f'<div style="{M.it_css("elegante",76,color)}line-height:1.06">{it1}</div>'
    if it2: blk += f'<div style="{M.it_css("elegante",76,color)}line-height:1.06">{it2}</div>'
    if sub: blk += f'<div style="{POP}font-style:italic;font-weight:300;font-size:41px;color:#f3ede2;line-height:1.3;margin-top:18px;text-wrap:balance">{_fl(sub)}</div>'
    body = (_veil("linear-gradient(180deg,rgba(30,20,12,.70) 0%,rgba(30,20,12,0) 35%,rgba(30,20,12,0) 55%,rgba(30,20,12,.85) 100%)")
            + f'<div style="position:absolute;left:{round(W*.11)}px;right:{round(W*.11)}px;top:{round(H*.085)}px">{blk}</div>'
            + (_logo(*logo) if logo else '') + (_refs(refs) if refs else "") + _pill())
    return _doc(body, fondo)

def r_claro(estrella, barra, cuerpo=None, fondo=None, logo=("principal", "navy", "tl"), fs=None):
    """R7 'Exosomes': fondo luminoso; estrella Mencken it navy (hero_claro) + sub-barra azul-gris que
    abraza el texto + cuerpo Poppins it navy."""
    # Escala revisada 10-oct-2026 (la Dra.: «textos demasiado pequeños»): estrella ≈170 px ajustada al ancho útil,
    # barra 60 px, cuerpo 42 px — la pieza debe LLENAR su zona, no flotar en blanco.
    import re as _re
    util = W - round(W*.118) - round(W*.12)
    fs = fs or int(min(170, util / (0.46 * max(1, len(_re.sub('<[^>]+>', '', estrella))))))
    fb = max(48, min(62, round(fs * .37)))
    blk = (f'<div style="{M.it_css("hero_claro",fs,NAVY)}line-height:1;position:relative;z-index:2">{estrella}</div>'
           f'<div style="margin:{M.aire_desc(estrella,fs,16)}px 0 0 0">' + M.barra(barra, fb, M.it_css("elegante", fb, NAVY), fondo="rgba(93,118,140,.46)") + '</div>')
    if cuerpo: blk += f'<div style="{POP}font-style:italic;font-size:42px;color:#3a4352;line-height:1.28;margin-top:36px;text-wrap:balance">{_fl(cuerpo)}</div>'
    body = (_veil("linear-gradient(90deg,rgba(236,241,246,.82) 0%,rgba(236,241,246,.45) 55%,rgba(236,241,246,0) 85%)")
            + (_logo(*logo) if logo else '') + f'<div style="position:absolute;left:{round(W*.118)}px;right:{round(W*.12)}px;top:{round(H*.33)}px">{blk}</div>' + _pill(light=True))
    return _doc(body, fondo, light=True)

def r_eyebrow_gigante(eyebrow, estrella, statement=None, cuerpo=None, fondo=None, logo=("sello", "claro", "tr"), ytop=0.22, color=STEEL):
    """R6 'Muscle Cells': eyebrow Poppins it versales (parte del titular, no rótulo de sección) +
    estrella Mencken it 800 gigante; statement con regla vertical abajo-izquierda."""
    top = (f'<div style="{POP}font-style:italic;font-weight:300;font-size:36px;letter-spacing:.12em;color:#f1ede6;text-transform:uppercase">{eyebrow}</div>'
           f'<div style="{M.it_css("hero_oscuro",116,color)}line-height:1;margin-top:6px">{estrella}</div>')
    st = ""
    if statement:
        st = (f'<div style="border-left:2px solid {STEEL};padding-left:24px">'
              f'<div style="{MEN}font-weight:700;font-size:44px;color:{STEEL};line-height:1.05">{statement}</div></div>')
        if cuerpo: st += f'<div style="{POP}font-style:italic;font-size:34px;color:#e6dfd3;line-height:1.35;margin:22px 0 0 26px;text-wrap:balance">{_fl(cuerpo)}</div>'
    body = (_veil("linear-gradient(0deg,rgba(8,8,10,.85) 0%,rgba(8,8,10,.2) 45%,rgba(8,8,10,.35) 100%)")
            + (_logo(*logo) if logo else '') + f'<div style="position:absolute;left:0;right:0;top:{round(H*ytop)}px;text-align:center">{top}</div>'
            + f'<div style="position:absolute;left:{round(W*.12)}px;right:{round(W*.35)}px;top:{round(H*.58)}px">{st}</div>' + _pill())
    return _doc(body, fondo)

def _refs(txt, light=False, left=None, right=None, bottom=None):
    """Referencias Vancouver al pie, DENTRO de la zona segura (Poppins 20px — nunca menor que la cápsula)."""
    c = "#3a4352" if light else "rgba(241,237,230,.88)"
    m = M.margen(W, H)
    left = m if left is None else left; right = m if right is None else right; bottom = (m + 14 if H < 1500 else 210) if bottom is None else bottom   # story: encima de la cápsula (que baja a H-190, 11-oct-2026: 1 cm más abajo)
    return (f'<div data-rol="ref" style="position:absolute;left:{left}px;right:{right}px;bottom:{bottom}px;'
            f'{POP}font-weight:300;font-size:22px;line-height:1.35;color:{c}">{txt}</div>')

COLW = 0.58   # ancho de la lámina vertical «tipo ducha»
def soporte(modo, H_=None):
    """SOPORTES DE LECTURA (regla de la Dra., 10-oct-2026): cuando el texto va sobre una foto cargada o clara, NO se baja
    el texto ni se oscurece toda la foto. Se le da un soporte de diseño:
      'mitad'   → panel de VIDRIO OPACO a media pieza (mitad inferior): blur + tinte navy, filo superior fino. El texto va encima.
      'mitad_sup' → igual, en la mitad superior.
      'columna_izq' / 'columna_der' → lámina de vidrio VERTICAL de alto completo, «tipo ducha» (58 % del ancho, estriado
                  muy fino, filo lateral); el texto va dentro de la columna, centrado en vertical.
      'vidrio'  → tarjeta de vidrio esmerilado ajustada al bloque de texto (se aplica como estilo del contenedor, ver r_natural).
      'velo'    → velo localizado detrás del bloque (degradado radial), para fotos medianamente cargadas.
    Además: resaltado que abraza el titular (`M.barra`) y cápsulas/recuadros (`M.caja`, pills) son soportes válidos."""
    Hh = H_ or H
    if modo in ('columna_izq', 'columna_der'):   # 'tipo ducha': lámina de vidrio VERTICAL de alto completo
        lado = 'left:0' if modo == 'columna_izq' else 'right:0'
        filo = 'border-right' if modo == 'columna_izq' else 'border-left'
        return (f'<div style="position:absolute;top:0;bottom:0;{lado};width:{round(W*COLW)}px;'
                f'backdrop-filter:blur(24px) saturate(.85);-webkit-backdrop-filter:blur(24px);'
                f'background:repeating-linear-gradient(90deg,rgba(255,255,255,.035) 0 2px,rgba(255,255,255,0) 2px 26px),'
                f'linear-gradient(180deg,rgba(26,33,46,.58),rgba(20,26,37,.74));{filo}:1.2px solid rgba(202,211,221,.38)"></div>')
    if modo in ('mitad', 'mitad_sup'):
        pos = f"top:{round(Hh*.5)}px;bottom:0" if modo == 'mitad' else f"top:0;bottom:{round(Hh*.5)}px"
        filo = 'border-top' if modo == 'mitad' else 'border-bottom'
        return (f'<div style="position:absolute;left:0;right:0;{pos};backdrop-filter:blur(26px) saturate(.85);-webkit-backdrop-filter:blur(26px);'
                f'background:linear-gradient(180deg,rgba(26,33,46,.62),rgba(20,26,37,.78));{filo}:1.2px solid rgba(202,211,221,.35)"></div>')
    return ""

VIDRIO_CSS = ("backdrop-filter:blur(22px) saturate(.9);-webkit-backdrop-filter:blur(22px);background:rgba(24,31,44,.68);"
              "border:1.2px solid rgba(202,211,221,.32);border-radius:22px;box-shadow:0 18px 40px rgba(0,0,0,.25);padding:44px 48px;")

def r_natural(bold, it=None, sub=None, fondo=None, logo=("principal", "blanco", "tl"), lado="izq", bottom=0.145, soporte_=None, resaltar=False, col=None, escala=1.0, acc_col="#dfe8f1", luz_sup=False):
    """soporte_: None | 'mitad' | 'vidrio' | 'velo' — ver soporte(). Si el auditor marca F3 sobre la foto, usar 'mitad' o 'vidrio'.
    col: ancho de la lámina vertical (fracción de W, def. 0.58). La Dra. (10-oct-2026): si la foto es protagonista, lámina
    más angosta (≈0.48) para aprovechar la foto; el titular se reduce en proporción para caber."""
    global COLW
    COLW = col or 0.58
    """R8 'Inside LCI' — foto REAL de la clínica a color (tratar 'natural'), sin efecto. Solo un velo
    bajo el texto (25% inferior) para leer. Titular más pequeño que en las piezas de concepto: la foto
    es la protagonista. lado: izq | der."""
    al = "left" if lado == "izq" else "right"
    fs = round(84 * min(1, (COLW - .12) / .46)) if soporte_ in ('columna_izq', 'columna_der') else 80 if soporte_ else 66   # con soporte el titular sube (jerarquía ≥ 2.4 × cuerpo)
    fs = round(fs * escala)
    # Regla de la Dra. (10-oct-2026): si el bloque lleva RESALTADO, el interlineado sube un poco para que la barra no
    # invada la línea de arriba ni la de abajo (aire ≈ 0.27 × fs antes de la barra; titular a 1.08).
    blk = f'<div style="{MEN}font-weight:700;font-size:{fs}px;color:#fff;line-height:{1.08 if (it and resaltar) else 1}">{bold}</div>'
    if it and resaltar:   # resaltado que ABRAZA la palabra gancho (ref. «are cellular messengers» de Exosomes, Paola)
        blk += f'<div style="margin-top:{round(fs*.27)}px">{M.barra(it, fs, M.it_css("acento", fs, "#26313f"), fondo="rgba(202,211,221,.92)", alinear=("der" if lado=="der" else True))}</div>'
    elif it: blk += f'<div style="{M.it_css("hero_oscuro",fs,acc_col)}line-height:1.05">{it}</div>'   # acc_col: variar color del acento (p. ej. azul claro #CAD3DD) — regla de color
    fsub = 38 if soporte_ in ("columna_izq", "columna_der") else 36 if soporte_ else 34
    fsub = max(30, round(fsub * (1 - (1 - escala) * .6)))   # escala<1: panel y texto más compactos (la Dra., 10-oct-2026)
    if sub: blk += f'<div style="{POP}font-style:italic;font-weight:300;font-size:{fsub}px;color:#f1ede6;line-height:1.35;margin-top:{22 if soporte_ else 14}px;text-wrap:balance;text-wrap:balance">{_fl(sub)}</div>'
    m = M.margen(W, H)
    if soporte_ == 'vidrio':
        caja = (f'<div data-caja style="display:inline-block;box-sizing:border-box;min-width:{round((W-2*m)*.66)}px;text-align:{al};{VIDRIO_CSS}">{blk}'   # ancho fijo mínimo: EN y ES idénticas
                f'<div data-rol="pie" style="margin-top:30px">{M.pill(solo_web=True)}</div></div>')
        cont = f'<div style="position:absolute;left:{m}px;right:{m}px;bottom:{m}px;text-align:{al}">{caja}</div>'
    else:
        if soporte_ in ('columna_izq', 'columna_der'):
            x0 = m if soporte_ == 'columna_izq' else W - round(W*COLW) + m*0.6
            cont = (f'<!--COL:{round(x0)}:{round(W*COLW - m*1.6)}--><div style="position:absolute;left:{round(x0)}px;width:{round(W*COLW - m*1.6)}px;top:{m}px;bottom:{m}px;display:flex;'
                    f'flex-direction:column;justify-content:center;text-align:left">{blk}</div>')
        elif soporte_ == 'recuadro':   # RECUADRO de Paola («The brain ages too»): filo claro fino de 1.2 px + relleno navy
            # translúcido que abraza el bloque (≈34 px de aire), sin desenfoque. Medido sobre el original (10-oct-2026).
            cont = (f'<div style="position:absolute;left:{m}px;right:{m}px;top:{round(H*.355)}px;text-align:{al}">'
                    f'<div data-caja style="display:inline-block;text-align:left;padding:34px 44px 30px 34px;'
                    f'border:1.2px solid rgba(202,211,221,.42);background:rgba(12,20,34,.46)">{blk}</div></div>')
        elif soporte_ == 'mitad':   # panel de vidrio AJUSTADO al texto (no tapa media foto si el texto es corto) — 10-oct-2026
            ytop_pill = H - round(m*1.2) if H < 1500 else H - 190
            cont = (f'<div style="position:absolute;left:0;right:0;bottom:0;padding:{round(m*0.62*escala)}px {m}px {H - ytop_pill + round(m*0.45*escala)}px;'
                    f'backdrop-filter:blur(26px) saturate(.85);-webkit-backdrop-filter:blur(26px);'
                    f'background:linear-gradient(180deg,rgba(26,33,46,.62),rgba(20,26,37,.78));border-top:1.2px solid rgba(202,211,221,.35);'
                    f'text-align:{al}">{blk}<!--REFS--></div>')
        else:
            cont = f'<div style="position:absolute;left:{m}px;right:{m}px;bottom:{round(H*bottom)}px;text-align:{al}">{blk}</div>'
    velo = (_veil("radial-gradient(70% 40% at 50% 85%,rgba(14,18,26,.70) 0%,rgba(14,18,26,0) 100%)") if soporte_ == 'velo'
            else _veil("linear-gradient(0deg,rgba(14,18,26,.80) 0%,rgba(14,18,26,.35) 24%,rgba(14,18,26,0) 42%)") if not soporte_ else "")
    if luz_sup:   # caída de luz AMPLIA y natural arriba para que el logo blanco se lea (nunca un difuminado solo alrededor del logo)
        velo += _veil("linear-gradient(180deg,rgba(14,18,26,.62) 0%,rgba(14,18,26,.30) 14%,rgba(14,18,26,0) 30%)")
    if logo and soporte_ in ('columna_izq', 'columna_der'):
        # Regla de la Dra. (10-oct-2026): con lámina de vidrio, el logo BLANCO va DENTRO del vidrio (arriba, alineado al texto).
        # Si el logo quedara fuera del vidrio sobre la foto, tendría que ir en color OSCURO (navy) y en zona limpia.
        # El logo SIEMPRE se alinea a un margen de la pieza (10-oct-2026): lámina izquierda → margen izquierdo;
        # lámina derecha → margen DERECHO (su borde derecho cae exactamente en W − margen).
        logo = (logo[0], 'blanco', 'tl' if soporte_ == 'columna_izq' else 'tr'); logo_html = _logo(*logo, xl=m / W)
    else:
        if logo and soporte_ and logo[1] == 'blanco': logo = (logo[0], 'auto', logo[2])   # logo fuera del vidrio → color según el fondo (un color explícito distinto de blanco se respeta)
        logo_html = (_logo(*logo) if logo else '') if logo else ""
    # Regla de la Dra. (10-oct-2026): con VIDRIO OPACO la cápsula va DENTRO del vidrio y lleva SOLO la página web.
    if soporte_ == 'mitad':
        # El panel cubre TODO el ancho → la cápsula COMPLETA (teléfono · @ · web) cabe dentro del vidrio (la Dra., 10-oct-2026)
        pie = _pill(vidrio=False)
    elif soporte_ in ('columna_izq', 'columna_der'):
        x0 = m if soporte_ == 'columna_izq' else W - round(W*COLW) + m*0.6
        pie = _pill_web(x0)
    elif soporte_ == 'vidrio':
        pie = ''   # va dentro de la tarjeta (ver caja)
    else:
        pie = _pill()
    body = (velo + (soporte(soporte_) if soporte_ != 'mitad' else '') + logo_html + cont + pie)
    return _doc(body, fondo, soporte=soporte_)

def r_retrato(bold, it=None, sub=None, retrato=None, fondo=None, logo=("sello", "claro", "tl"), h=1010, x=0.40):
    """R9 'Founder' — retrato recortado (PNG con alfa) sobre fondo oscuro; texto a la izquierda a media
    altura; el retrato entra por la derecha y se apoya sobre la cápsula. retrato = data-URI con alfa."""
    blk = f'<div style="{MEN}font-weight:700;font-size:80px;color:#fff;line-height:1">{bold}</div>'
    if it: blk += f'<div style="{M.it_css("hero_oscuro",80,STEEL)}line-height:1.04">{it}</div>'
    if sub: blk += f'<div style="height:1.5px;width:120px;background:{GOLD};margin:28px 0 22px"></div><div style="{POP}font-style:italic;font-weight:300;font-size:37px;color:#e9e4da;line-height:1.35;text-wrap:balance">{_fl(sub)}</div>'
    img = (f'<img src="{retrato}" style="position:absolute;left:{round(W*x)}px;bottom:0;height:{h}px;filter:drop-shadow(-18px 10px 40px rgba(0,0,0,.55));">'
           if retrato else "")
    body = (img + _veil("linear-gradient(0deg,rgba(9,12,18,.92) 0%,rgba(9,12,18,.55) 14%,rgba(9,12,18,0) 30%),linear-gradient(90deg,rgba(9,12,18,.85) 0%,rgba(9,12,18,.35) 40%,rgba(9,12,18,0) 60%)")
            + (_logo(*logo) if logo else '') + f'<div style="position:absolute;left:{round(W*.11)}px;width:{round(W*.48)}px;top:{round(H*.40)}px">{blk}</div>' + _pill())
    return _doc(body, fondo or "linear-gradient(160deg,#2a3649 0%,#141b26 55%,#0b0f16 100%)")

def r_paso(num, titulo, cuerpo=None, fondo=None, logo=("principal", "blanco", "tl"), lado="izq", light=False, cta=None, numc=None):
    """R10 'Journey' — número GIGANTE Mencken it 800 (crema/acero) + titular bold + cuerpo Poppins it.
    lado izq: número arriba-derecha, texto abajo-izquierda · lado der: número arriba-izquierda, texto
    abajo-derecha (alinear a la derecha). light=True para fondo claro (texto navy)."""
    tc, nc, bc = (NAVY, "#5d768c", "#3a4352") if light else ("#fff", CREAM, "#e9e4da")
    nc = numc or nc   # número sobre zona clara de la foto → navy (contraste)
    al = "left" if lado == "izq" else "right"
    numpos = f"right:{round(W*.09)}px" if lado == "izq" else f"left:{round(W*.09)}px"
    blk = f'<div style="{MEN}font-weight:700;font-size:84px;color:{tc};line-height:1.02">{titulo}</div>'
    if cuerpo: blk += f'<div style="{POP}font-style:italic;font-weight:300;font-size:40px;color:{bc};line-height:1.38;margin-top:20px;text-wrap:balance">{_fl(cuerpo)}</div>'
    if cta: blk += f'<div style="{POP}font-style:italic;font-weight:400;font-size:34px;color:{STEEL if not light else NAVY};margin-top:26px">{cta}</div>'
    veil = ("linear-gradient(0deg,rgba(236,241,246,.92) 0%,rgba(236,241,246,.55) 35%,rgba(236,241,246,0) 60%)" if light else
            "linear-gradient(0deg,rgba(8,12,20,.92) 0%,rgba(8,12,20,.5) 38%,rgba(8,12,20,.05) 65%,rgba(8,12,20,.35) 100%)")
    body = (_veil(veil) + (_logo(*logo) if logo else '')
            + f'<div style="position:absolute;{numpos};top:{round(H*.05)}px;{M.it_css("hero_oscuro" if not light else "hero_claro",300,nc)}line-height:1">{num}</div>'
            + f'<div style="position:absolute;left:{round(W*.11)}px;right:{round(W*.11)}px;bottom:{round(H*.15)}px;text-align:{al}">{blk}</div>' + _pill(light=light))
    return _doc(body, fondo, light=light)

def r_articulo(journal, meta, titulo, autores, filas, clave, doi, fondo=None, logo=("sello", "claro", "tl"), acento="The study"):
    """R11 'Artículo' — la "foto del artículo" para carruseles de evidencia: ficha tipo primera página
    de paper (papel blanco, sombra) sobre foto oscura difuminada. NO reproduce figuras del artículo
    (derechos): solo cita + diseño + n + hallazgo clave + DOI. filas = [(etiqueta, valor), ...]."""
    rows = "".join(f'<div style="display:flex;gap:18px;padding:12px 0;border-top:1px solid #e3e6ea">'
                   f'<div style="{POP}font-size:20px;letter-spacing:.14em;text-transform:uppercase;color:#4f5a68;width:205px;flex:none;padding-top:5px">{a}</div>'
                   f'<div style="{POP}font-size:28px;color:#2a3649;line-height:1.3">{b}</div></div>' for a, b in filas)
    card = (f'<div data-jerarquia="ficha" style="background:#fbfaf7;border-radius:6px;box-shadow:0 30px 70px rgba(0,0,0,.55),0 4px 14px rgba(0,0,0,.35);padding:50px 52px 44px">'
            f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid #2a3649;padding-bottom:12px">'
            f'<div style="{POP}font-weight:600;font-size:24px;letter-spacing:.16em;text-transform:uppercase;color:#2a3649">{journal}</div>'
            f'<div style="{POP}font-size:22px;color:#4f5a68">{meta}</div></div>'
            f'<div style="{MEN}font-weight:700;font-size:48px;line-height:1.1;color:#1f2836;margin:26px 0 16px">{titulo}</div>'
            f'<div style="{POP}font-style:italic;font-weight:300;font-size:25px;color:#5d6b7a;margin-bottom:22px">{autores}</div>'
            f'{rows}'
            f'<div style="margin-top:20px;width:fit-content;background:#eef2f6;border-left:3px solid {STEEL};padding:16px 24px 24px;{MEN}font-size:33px;line-height:1.28;color:#1f2836">{clave}</div>'
            f'<div style="{POP}font-size:21px;color:#4f5a68;margin-top:18px">doi:{doi}</div></div>')
    eb = (f'<div style="margin-bottom:22px"><span style="display:inline-block;border:1.6px solid {STEEL};border-radius:3px;padding:6px 20px;line-height:1">'
          f'<span style="{M.it_css("acento",40,STEEL)}line-height:1;position:relative;top:{"-.17em" if any(ch in acento for ch in "gjpqy") else "-.08em"}">{acento}</span></span></div>')
    body = (_veil("rgba(9,12,18,.62)") + (_logo(*logo) if logo else '')
            + f'<div style="position:absolute;left:{round(W*.075)}px;right:{round(W*.075)}px;top:{round(H*.20)}px">{eb}{card}</div>' + _pill())
    return _doc(body, fondo)

def con_refs(html, txt, light=False):
    """Añade referencias Vancouver al pie de cualquier receta (sobre la cápsula)."""
    if '<!--REFS-->' in html:   # panel de vidrio a todo el ancho: las referencias van DENTRO del panel, bajo el texto
        c = "#3a4352" if light else "rgba(241,237,230,.88)"
        return html.replace('<!--REFS-->', f'<div data-rol="ref" style="{POP}font-weight:300;font-size:20px;line-height:1.35;color:{c};margin-top:26px;text-align:left">{txt}</div>', 1)
    i = html.rindex('</div></div></body>')
    import re
    m = M.margen(W, H); kw = {}
    if 'pill-web' in html:   # cápsula solo-web dentro del vidrio → las referencias van ENCIMA de ella, sin tocarla
        kw['bottom'] = (round(m*1.2) + 22) if H < 1500 else 210
        mc = re.search(r'<!--COL:(\d+):(\d+)-->', html)
        if mc: kw['left'] = int(mc.group(1)); kw['right'] = W - int(mc.group(1)) - int(mc.group(2))   # dentro de la lámina
    return html[:i] + _refs(txt, light, **kw) + html[i:]

def r_dato(numero, texto, fondo=None, logo=("sello", "claro", "tl"), x=0.56, y=0.55, refs=None, light=False):
    """R12 'Dato en movimiento' — cifra grande Poppins Light (no Mencken) + 3 líneas cortas Poppins Light, sobre foto
    con efecto `movimiento()`. Cifra SIEMPRE con fuente verificada [n] y referencia al pie (con_refs)."""
    blk = (f'<div style="{POP}font-weight:300;font-size:260px;letter-spacing:-.04em;line-height:.9;color:{NAVY if light else "#fff"}">{numero}</div>'
           f'<div style="{POP}font-weight:300;font-size:42px;line-height:1.24;color:{"#2f3a4b" if light else "#fff"};margin-top:62px;text-wrap:balance">{_fl(texto)}</div>')
    body = ((_veil("linear-gradient(0deg,rgba(236,241,246,.97) 0%,rgba(236,241,246,.92) 38%,rgba(236,241,246,.55) 58%,rgba(236,241,246,0) 82%)") if light else _veil("linear-gradient(0deg,rgba(10,8,8,.55) 0%,rgba(10,8,8,0) 30%)")) + (_logo(*logo) if logo else '')
            + f'<div style="position:absolute;left:{round(W*x)}px;right:{round(W*.06)}px;top:{round(H*y)}px">{blk}</div>' + _pill(light=light))
    html = _doc(body, fondo, light=light)
    return con_refs(html, refs, light=light) if refs else html

def _svg(inner, w=W, h=H):
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;inset:0" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'

def r_palabra(termino, tipo, etiquetas, definicion, nota=None, fondo=None, logo=("sello", "claro", "tr"), light=False):
    C1, C2, CL = (NAVY, "#3a4352", "rgba(42,54,73,.45)") if light else ("#fff", "#f1ede6", "rgba(255,255,255,.45)")
    """R13 'Word of the Day' — término Poppins 600 grande + clase gramatical + píldoras de categoría (contorno fino) +
    definición Poppins Light. Fondo SIN foto: `bokeh()` o `gradiente()`."""
    pills = "".join(f'<span style="display:inline-block;border:1.4px solid {CL if light else "rgba(255,255,255,.75)"};border-radius:999px;padding:8px 24px;margin-right:14px;{POP}font-size:23px;letter-spacing:.14em;color:{C1};text-transform:uppercase">{e}</span>' for e in etiquetas)
    blk = (f'<div style="{POP}font-weight:300;font-size:32px;color:{C2};margin-bottom:26px">{"Palabra del día" if M.IDIOMA=="es" else "Word of the day"}</div>'
           f'<div style="display:flex;flex-wrap:wrap;align-items:baseline;gap:14px 18px"><span style="{POP}font-weight:600;font-size:{min(132, int(W*.78/(.60*len(termino))))}px;letter-spacing:-.02em;color:{C1};line-height:1">{termino}</span>'
           f'<span style="{POP}font-style:italic;font-weight:300;font-size:32px;color:{C2}">{tipo}</span></div>'
           f'<div style="margin-top:22px">{pills}</div>'
           f'<div style="height:1px;background:{CL};margin:48px 0 30px"></div>'
           f'<div style="{POP}font-weight:300;font-size:42px;line-height:1.34;color:{C1};text-wrap:balance">{_fl(definicion)}</div>')
    if nota: blk += f'<div style="{POP}font-weight:300;font-size:36px;line-height:1.36;color:{C2};margin-top:24px;text-wrap:balance">{_fl(nota)}</div>'
    body = ("" if light else _veil("linear-gradient(0deg,rgba(12,10,9,.55) 0%,rgba(12,10,9,.15) 50%,rgba(12,10,9,.35) 100%)")) + (_logo(*logo)
            + f'<div style="position:absolute;left:{round(W*.11)}px;right:{round(W*.11)}px;top:{round(H*.24)}px">{blk}</div>' + _pill(light=light))
    return _doc(body, fondo or bokeh(), light=light)

def r_orbitas(titulo, it, pasos, fondo=None, logo=("sello", "claro", "tl"), light=False):
    """R14 'Journey en órbitas' — arcos/círculos finos concéntricos con nodos y rótulos (ref. 'Your longevity journey').
    pasos = [(etiqueta, texto corto), ...] (3–4). Fondo `gradiente()`."""
    c = NAVY if light else "#fff"; sc = "rgba(42,54,73,.5)" if light else "rgba(255,255,255,.5)"
    import math
    cx, cy = -W * 0.10, H * 1.30; n = len(pasos)
    pts = [(W * 0.30, H * (0.40 + 0.12 * i)) for i in range(n)]
    g = ""; labs = ""
    for k, (x, y) in enumerate(pts):   # cada órbita llega hasta su nodo (no cruza los rótulos)
        r = math.hypot(x - cx, y - cy)
        g += (f'<clipPath id="o{k}"><rect x="0" y="0" width="{x:.0f}" height="{H}"/></clipPath>'
              f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="none" stroke="{sc}" stroke-width="1.4" clip-path="url(#o{k})"/>')
    for (et, tx), (x, y) in zip(pasos, pts):
        g += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="8" fill="{c}"/><circle cx="{x:.0f}" cy="{y:.0f}" r="17" fill="none" stroke="{sc}"/>'
        labs += (f'<div style="position:absolute;left:{x+34:.0f}px;top:{y-17:.0f}px;width:{W*0.95-x-34:.0f}px">'
                 f'<div style="{POP}font-weight:600;font-size:34px;color:{c}">{et}</div>'
                 f'<div style="{POP}font-weight:300;font-size:26px;line-height:1.32;color:{c};opacity:.92;margin-top:4px">{tx}</div></div>')
    head = (f'<div style="{MEN}font-weight:400;font-size:64px;line-height:1;color:{c}">{titulo}</div>'
            f'<div style="{M.it_css("hero_oscuro" if not light else "hero_claro",64,STEEL if not light else "#5d768c")}line-height:1.05">{it}</div>')
    body = (_svg(g) + (_logo(*logo) if logo else '') + f'<div style="position:absolute;left:{round(W*.11)}px;right:{round(W*.11)}px;top:{round(H*.16)}px;text-align:right">{head}</div>'
            + labs + _pill(light=light))
    return _doc(body, fondo or gradiente('noche'), light=light)

def r_red(titulo, it, nodos, centro="You", fondo=None, logo=("principal", "blanco", "tl")):
    """R15 'Red de nodos' — diagrama de líneas finas: nodo central + satélites con rótulos (ref. iconografía lineal del
    feed de referencia). nodos = lista de 4–7 rótulos cortos. Fondo `gradiente()`."""
    import math
    cx, cy, R = W * 0.5, H * 0.60, 300
    g = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="rgba(255,255,255,.28)" stroke-width="1.2"/>'
    g += f'<circle cx="{cx}" cy="{cy}" r="78" fill="none" stroke="{GOLD}" stroke-width="1.6"/>'
    labs = f'<div style="position:absolute;left:{cx-78:.0f}px;top:{cy-18:.0f}px;width:156px;text-align:center;{MEN}font-style:italic;font-size:38px;color:#fff">{centro}</div>'
    n = len(nodos)
    for i, t in enumerate(nodos):
        a = -math.pi / 2 + i * 2 * math.pi / n; x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        g += f'<line x1="{cx+78*math.cos(a):.0f}" y1="{cy+78*math.sin(a):.0f}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(255,255,255,.45)" stroke-width="1.2"/>'
        g += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="8" fill="#fff"/><circle cx="{x:.0f}" cy="{y:.0f}" r="16" fill="none" stroke="rgba(255,255,255,.5)"/>'
        al = "left" if math.cos(a) > 0.2 else ("right" if math.cos(a) < -0.2 else "center")
        lx = x + 28 if al == "left" else (x - 268 if al == "right" else x - 170)
        ly = y - 14 if al != "center" else (y - 30 if math.sin(a) < 0 else y + 26)
        tf = "transform:translateY(-100%);" if (al == "center" and math.sin(a) < 0) else ""   # rótulo superior: crece hacia arriba, nunca pisa el nodo
        labs += f'<div style="position:absolute;left:{lx:.0f}px;top:{ly:.0f}px;width:{340 if al == "center" else 240}px;{tf}text-align:{al};{POP}font-weight:300;font-size:26px;color:#fff">{t}</div>'
    head = (f'<div style="{MEN}font-weight:700;font-size:70px;line-height:1;color:#fff">{titulo}</div>'
            f'<div style="{M.it_css("hero_oscuro",70,STEEL)}line-height:1.05">{it}</div>')
    body = (_svg(g) + (_logo(*logo) if logo else '') + f'<div style="position:absolute;left:{round(W*.11)}px;right:{round(W*.11)}px;top:{round(H*.17)}px">{head}</div>' + labs + _pill())
    return _doc(body, fondo or gradiente('acero'))

def r_icono(icono_svg, titulo, it, sub=None, fondo=None, logo=("principal", "blanco", "tl")):
    """R16 'Statement con ícono' — ícono/marca lineal grande centrado arriba + titular centrado (ref. 'You are not low
    energy'). icono_svg = contenido SVG en caja 240×240 (trazo fino blanco/dorado)."""
    ic = f'<svg width="240" height="240" viewBox="0 0 240 240" style="display:block;margin:0 auto">{icono_svg}</svg>'
    blk = (ic + f'<div style="{MEN}font-weight:400;font-size:76px;line-height:1.02;color:#fff;margin-top:56px">{titulo}</div>'
           f'<div style="{M.it_css("hero_oscuro",76,CREAM)}line-height:1.05">{it}</div>')
    if sub: blk += f'<div style="{POP}font-weight:300;font-size:36px;line-height:1.4;color:#f1ede6;margin-top:26px;text-wrap:balance">{_fl(sub)}</div>'
    body = (_logo(*logo) + f'<div style="position:absolute;left:{round(W*.1)}px;right:{round(W*.1)}px;top:{round(H*.22)}px;text-align:center">{blk}</div>' + _pill())
    return _doc(body, fondo or gradiente('aurora'))

def r_portada_limpia(bold, it=None, sub=None, fondo=None, logo=("sello", "claro", "tr"), y=0.58, size=118,
                     light=False, acento=None, veil=True, align="left"):
    """R17 'Portada limpia' — idea de qura.health (foto a sangre, UN concepto grande, sin cajas ni listas) PERO en el
    lenguaje de LCI/Paola: titular recto en Mencken Std BOLD + acento en Mencken Head ITÁLICO del MISMO tamaño (nunca
    Poppins Light gigante), subtítulo corto Poppins Light, velo navy de Paola detrás del bloque de texto. La foto SIEMPRE
    lleva tratamiento de marca (`tratar`: bw/azul/frio/calido/ambar/claro) y recorte de detalle, sin objetos cotidianos
    legibles (cartas de café, cables, letreros, pantallas). Aprobado/corregido por la Dra. oct 2026."""
    tc = NAVY if light else "#fff"
    ac = acento or ("#5f7f9c" if light else CREAM)
    blk = f'<div style="{MEN}font-weight:700;font-size:{size}px;line-height:1.0;letter-spacing:.004em;color:{tc}">{bold}</div>'
    if it: blk += f'<div style="{M.it_css("hero_claro" if light else "hero_oscuro", size, ac)}line-height:1.05">{it}</div>'
    if sub: blk += f'<div style="{POP}font-weight:300;font-size:37px;line-height:1.38;color:{tc};margin-top:26px;text-wrap:balance">{_fl(sub)}</div>'
    v = ("linear-gradient(0deg,rgba(236,241,246,.80) 0%,rgba(236,241,246,.35) 38%,rgba(236,241,246,0) 62%)" if light
         else VEIL_NAVY)
    if y < 0.4 and not light:
        v = "linear-gradient(180deg,rgba(25,34,46,.88) 0%,rgba(25,34,46,.40) 40%,rgba(25,34,46,0) 65%)"
    body = ((_veil(v) if veil else "") + (_logo(*logo) if logo else "")
            + f'<div style="position:absolute;left:{round(W*.09)}px;right:{round(W*.09)}px;top:{round(H*y)}px;text-align:{align}">{blk}</div>'
            + _pill(light=light))
    return _doc(body, fondo, light=light)

def r_cita(cita, autor, fondo=None, logo=("sello", "claro", "tl")):
    """R18 'Cita' (ref. qura.health): comillas grandes de marca, cita en Poppins Light/Mencken it. sobre foto MUY
    desenfocada. Solo citas reales y atribuidas (frase de la Dra., publicaciones). NUNCA testimonios inventados."""
    q = f'<span style="{MEN}font-size:150px;line-height:.5;color:{GOLD}">“</span>'
    blk = (q + f'<div style="{POP}font-weight:300;font-size:46px;line-height:1.3;color:#fff;margin-top:20px">{cita}</div>'
           f'<div style="{M.it_css("elegante",34,CREAM)}margin-top:34px">— {autor}</div>')
    body = (_veil("rgba(10,12,16,.38)") + (_logo(*logo) if logo else '')
            + f'<div style="position:absolute;left:{round(W*.13)}px;right:{round(W*.13)}px;top:{round(H*.30)}px">{blk}</div>' + _pill())
    return _doc(body, fondo)

def r_cifras(intro, cifras, rotulo=None, fondo=None, logo=None, refs=None):
    """R19 'Cifras en columna' (ref. 'Anatomy of a doctor's visit'): intro Poppins a la izquierda arriba + 2–3 cifras
    gigantes Poppins Light apiladas a la derecha, cada una con su rótulo corto; rótulo de sección en versalitas mínimas
    abajo-izquierda. Fondo ideal: `vidrio()`. cifras = [(numero, texto), ...]. Cifras SIEMPRE verificadas."""
    m = M.margen(W, H)
    col = "".join(f'<div style="margin-bottom:30px"><div style="{POP}font-weight:300;font-size:132px;letter-spacing:-.05em;line-height:.9;color:#fff">{n}</div>'
                  f'<div style="{POP}font-weight:400;font-size:31px;line-height:1.22;color:#fff;margin-top:10px;text-wrap:balance">{_fl(t)}</div></div>' for n, t in cifras)
    body = (_veil("rgba(10,12,16,.18)") + (_logo(*logo) if logo else "")
            + f'<div style="position:absolute;left:{m}px;width:{round(W*.36)}px;top:{m}px;{POP}font-weight:400;font-size:50px;line-height:1.08;letter-spacing:-.02em;color:#fff">{intro}</div>'
            + f'<div style="position:absolute;left:{round(W*.50)}px;right:{m}px;top:{m}px;text-align:right">{col}</div>'
            + (f'<div style="position:absolute;left:{m}px;top:{round(H*.86)}px;{POP}font-weight:500;font-size:19px;letter-spacing:.08em;text-transform:uppercase;color:#fff">{rotulo}</div>' if rotulo else "")
            + _pill())
    html = _doc(body, fondo)
    return con_refs(html, refs) if refs else html

def r_circulos(titulo_html, a_tit, a_txt, b_tit, b_txt, paso=None, seccion=None, fondo=None, logo=("principal", "navy", "tl")):
    """R20 'Dos círculos' (ref. 'Problems met with solutions', oct 2026): fondo claro limpio (blanco/niebla, nunca beige
    plano), círculo NAVY sólido (A, ej. problema/convencional) que se cruza con círculo BLANCO con degradé suave (B, ej.
    solución/LCI). Titular Poppins Light con palabras clave en Poppins 600. paso=(n, total) dibuja la barra de progreso."""
    import math
    # Geometría revisada (10-oct-2026): círculos más grandes y cada texto en la media luna LIBRE de su círculo
    # (nunca sobre la intersección); cuerpo ≥ 27 px, titular 66 px a todo el ancho útil (jerarquía ≥ 2.4 × cuerpo).
    cA = (W * .36, H * .575); cB = (W * .64, H * .668); r = W * .29
    svg = (f'<defs><radialGradient id="gB" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#ffffff"/>'
           f'<stop offset=".75" stop-color="#f3f5f8"/><stop offset="1" stop-color="#d9e0e8"/></radialGradient>'
           f'<linearGradient id="sh" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2A3649" stop-opacity=".55"/>'
           f'<stop offset=".5" stop-color="#2A3649" stop-opacity="0"/></linearGradient></defs>'
           f'<circle cx="{cA[0]:.0f}" cy="{cA[1]:.0f}" r="{r:.0f}" fill="#1f2836"/>'
           f'<circle cx="{cB[0]:.0f}" cy="{cB[1]:.0f}" r="{r:.0f}" fill="url(#gB)"/>'
           f'<circle cx="{cB[0]:.0f}" cy="{cB[1]:.0f}" r="{r:.0f}" fill="url(#sh)"/>')
    def txt(c, t, x, col, sub, lado):
        x0 = c[0] - r*.80 if lado == 'A' else c[0] - r*.18
        y0 = c[1] - r*.58 if lado == 'A' else c[1] - r*.24
        x = x.replace('<br>', ' ')
        return (f'<div style="position:absolute;left:{x0:.0f}px;top:{y0:.0f}px;width:{r*(.80 if lado == "A" else .85):.0f}px">'
                f'<div style="{POP}font-weight:600;font-size:36px;line-height:1.1;color:{col}">{t}</div>'
                f'<div style="{POP}font-weight:300;font-size:29px;line-height:1.3;color:{sub};margin-top:12px">{x}</div></div>')
    prog = ""
    if paso:
        n, tot = paso
        prog = (f'<div style="position:absolute;right:{M.margen(W,H)}px;top:{M.margen(W,H)+18}px;display:flex;align-items:center;gap:14px;{POP}font-size:17px;color:#5d6b7a">'
                f'<span>{n:02d}</span><span style="width:150px;height:2px;background:#dfe5ec;position:relative"><span style="position:absolute;left:0;top:0;height:2px;width:{150*n/tot:.0f}px;background:{GOLD}"></span></span><span>{tot:02d}</span></div>')
    sec = (f'<div style="position:absolute;right:{M.margen(W,H)}px;top:{M.margen(W,H)+62}px;{POP}font-size:22px;color:#4f5a68">'
           f'<svg width="9" height="12" viewBox="0 0 9 12" style="vertical-align:0"><path d="M9 0 L0 6 L9 12 Z" fill="{GOLD}"/></svg>&nbsp; {seccion} &nbsp;<svg width="9" height="12" viewBox="0 0 9 12" style="vertical-align:0"><path d="M0 0 L9 6 L0 12 Z" fill="{GOLD}"/></svg></div>') if seccion else ""
    body = (_svg(svg) + (_logo(*logo) if logo else '') + prog + sec
            + f'<div style="position:absolute;left:{M.margen(W,H)}px;right:{M.margen(W,H)}px;top:{round(H*.20)}px;{POP}font-weight:300;font-size:70px;line-height:1.06;letter-spacing:-.01em;color:{NAVY};text-wrap:balance">{titulo_html.replace("<br>"," ")}</div>'
            + txt(cA, a_tit, a_txt, "#fff", "rgba(255,255,255,.88)", 'A') + txt(cB, b_tit, b_txt, NAVY, "#3f4a5a", 'B')
            + _pill(light=True))
    return _doc(body, fondo or "linear-gradient(180deg,#fbfcfd 0%,#eef2f6 100%)", light=True)

# ───────── EFECTOS Y RECETAS NUEVAS (oct 2026, 2ª tanda) ─────────
def _uri(a, q=90):
    b = io.BytesIO(); _img(a).save(b, 'JPEG', quality=q)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

def ondas(seed=2, periodo=9, w=1080, h=1350, calor=True, q=92, nivel=0.50):
    """Fondo 'ondas 3D estriadas' (ref. TSH): navy profundo, relieve de costillas verticales finas que siguen una cresta
    ondulada, iluminación acero y un destello GOLD (nunca rojo) en la cresta. Solo colores de marca."""
    rng = np.random.default_rng(seed)
    y, x = np.mgrid[0:h, 0:w].astype(np.float32)
    ph = rng.uniform(0, 6.28, 3)
    cresta = h * (nivel + 0.10*np.sin(x/w*5.2+ph[0]) + 0.05*np.sin(x/w*11+ph[1]) + 0.03*np.sin(x/w*19+ph[2]))
    d = (y - cresta) / h
    env = np.where(d < 0, np.exp(-(d/0.05)**2), np.exp(-(d/0.30)**2))           # borde nítido arriba, cae suave
    rib = 0.5 + 0.5*np.cos(2*np.pi*x/periodo); rib = rib**3
    fall = np.exp(-np.clip(d, 0, None)/0.18)
    lum = env * (0.18 + 0.82*rib) * (0.35 + 0.65*fall)
    base = np.array([18, 25, 36], np.float32)/255
    steel = np.array([148, 180, 204], np.float32)/255
    gold = np.array([210, 181, 138], np.float32)/255
    img = base + (steel - base)*lum[..., None]*0.95
    if calor:
        hx = w*(0.35 + 0.3*rng.uniform()); hy = np.interp(hx, x[0], cresta[0])
        g = np.exp(-(((x-hx)/(w*.16))**2 + ((y-hy)/(h*.10))**2)) * (0.25 + 0.75*rib) * (d > -0.02)
        img = img*(1-0.7*g[..., None]) + gold*0.95*g[..., None]
    img = img * (0.75 + 0.25*(1 - y/h))[..., None]
    img += rng.normal(0, 0.012, (h, w, 1)).astype(np.float32)
    return _uri(img, q)

def bacterias(seed=5, n=46, w=1080, h=1350, q=90):
    """Fondo 'microscopía' generado (ilustrativo, sin licencias de terceros): bacilos 3D con profundidad de campo,
    en azul acero/teal sobre navy. Para R23 `r_tarjeta_micro`."""
    from PIL import ImageDraw
    rng = np.random.default_rng(seed)
    out = np.zeros((h, w, 3), np.float32) + np.array([10, 24, 34], np.float32)/255
    capas = sorted([rng.uniform(0, 1) for _ in range(n)])
    for z in capas:                                   # z: 0 lejos (borroso, oscuro) → 1 cerca (nítido)
        L = rng.uniform(170, 330)*(0.6+0.7*z); R = L*rng.uniform(.16, .22); ang = rng.uniform(0, 180)
        cx, cy = rng.uniform(-80, w+80), rng.uniform(-80, h+80)
        S = int(L+2*R+40); m = Image.new('L', (S, S), 0); hl = Image.new('L', (S, S), 0)
        ImageDraw.Draw(m).rounded_rectangle((S/2-L/2-R, S/2-R, S/2+L/2+R, S/2+R), radius=R, fill=255)
        ImageDraw.Draw(hl).rounded_rectangle((S/2-L/2-R*.4, S/2-R*.75, S/2+L/2-R*.2, S/2-R*.15), radius=R*.4, fill=255)
        m = m.rotate(ang, resample=Image.BICUBIC); hl = hl.rotate(ang, resample=Image.BICUBIC)
        bl = abs(z-0.72)*26
        m = m.filter(ImageFilter.GaussianBlur(bl+1.5)); hl = hl.filter(ImageFilter.GaussianBlur(bl+R*.35))
        x0, y0 = int(cx-S/2), int(cy-S/2)
        xs, ys = max(0, x0), max(0, y0); xe, ye = min(w, x0+S), min(h, y0+S)
        if xe <= xs or ye <= ys: continue
        ma = np.asarray(m, np.float32)[ys-y0:ye-y0, xs-x0:xe-x0, None]/255
        ha = np.asarray(hl, np.float32)[ys-y0:ye-y0, xs-x0:xe-x0, None]/255
        col = np.array([40, 96, 120], np.float32)/255*(0.45+0.6*z)
        hi = np.array([150, 196, 214], np.float32)/255
        reg = out[ys:ye, xs:xe]
        reg[:] = reg*(1-ma) + col*ma
        reg[:] = reg + hi*ha*(0.25+0.45*z)*ma
    yy, xx = np.mgrid[0:h, 0:w]; v = 1 - 0.45*np.clip(np.hypot((xx-w/2)/(w/2), (yy-h/2)/(h/2))-0.4, 0, 1)
    out *= v[..., None]
    return _uri(out, q)

def r_tarjeta_micro(rotulo, termino, vinetas, texto, fondo=None, logo=("sello", "claro", "tl"), y=0.36, refs=None):
    """R21 'Tarjeta de microscopía' (ref. Bacteria): imagen macro/microscopía + tarjeta translúcida navy con filete fino
    (vidrio SUTIL, excepción documentada a la regla no-glassmorphism): rótulo versalitas, término Poppins 500, viñetas
    cortas y definición Poppins Light. Fondo: `bacterias()` o foto con licencia."""
    li = "".join(f'<div style="display:flex;gap:12px;margin-top:6px"><span style="color:{GOLD}">•</span><span>{v}</span></div>' for v in vinetas)
    card = (f'<div style="background:rgba(16,30,42,.42);border:1px solid rgba(202,211,221,.38);border-radius:22px;'
            f'backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);padding:44px 52px;box-shadow:0 30px 80px rgba(0,0,0,.35)">'
            f'<div style="{POP}font-weight:500;font-size:20px;letter-spacing:.22em;text-transform:uppercase;color:#CAD3DD">{rotulo}</div>'
            f'<div style="{POP}font-weight:500;font-size:72px;letter-spacing:-.02em;color:#fff;margin-top:10px;line-height:1.05">{termino}</div>'
            f'<div style="{POP}font-weight:300;font-size:30px;line-height:1.4;color:#e8eef3;margin-top:22px">{li}</div>'
            f'<div style="height:1px;background:rgba(202,211,221,.35);margin:30px 0 24px"></div>'
            f'<div style="{POP}font-weight:300;font-size:30px;line-height:1.45;color:#fff;text-wrap:balance">{_fl(texto)}</div></div>')
    body = (_veil("rgba(8,14,20,.18)") + (_logo(*logo) if logo else '')
            + f'<div style="position:absolute;left:{round(W*.10)}px;right:{round(W*.10)}px;top:{round(H*y)}px">{card}</div>' + _pill())
    html = _doc(body, fondo)
    return con_refs(html, refs) if refs else html

def r_nodo_luz(titulo, it=None, sub=None, fondo=None, logo=("principal", "blanco", "tc"), cy=0.33):
    """R22 'Nodo luminoso' (ref. dedo con nodo): foto MUY desenfocada fría + anillo luminoso con halo y una línea
    vertical fina que baja al titular centrado (Poppins Light + Mencken it.)."""
    x = W/2; y = H*cy; r = 46
    svg = (f'<defs><radialGradient id="hal"><stop offset="0" stop-color="#ffffff" stop-opacity=".55"/>'
           f'<stop offset=".35" stop-color="#CAD3DD" stop-opacity=".22"/><stop offset="1" stop-color="#CAD3DD" stop-opacity="0"/></radialGradient>'
           f'<linearGradient id="ln" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>'
           f'<circle cx="{x}" cy="{y}" r="{r*4.2}" fill="url(#hal)"/>'
           f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#fff" stroke-width="2.4"/>'
           f'<circle cx="{x}" cy="{y}" r="{r*.62}" fill="none" stroke="{GOLD}" stroke-width="1.4" stroke-opacity=".9"/>'
           f'<circle cx="{x}" cy="{y}" r="5" fill="#fff"/>'
           f'<rect x="{x-0.75}" y="{y+r+10}" width="1.5" height="{H*.17}" fill="url(#ln)"/>')
    blk = f'<div style="{POP}font-weight:300;font-size:64px;letter-spacing:-.02em;line-height:1.1;color:#fff">{titulo}'
    if it: blk += f'<br><span style="{M.it_css("hero_oscuro",60,CREAM)}">{it}</span>'
    blk += '</div>'
    if sub: blk += f'<div style="{POP}font-weight:300;font-size:34px;line-height:1.4;color:#e6ecf2;margin-top:22px;text-wrap:balance">{_fl(sub)}</div>'
    body = (_veil("rgba(14,22,32,.30)") + _svg(svg) + (_logo(*logo) if logo else '')
            + f'<div style="position:absolute;left:{round(W*.10)}px;right:{round(W*.10)}px;top:{round(H*(cy+.25))}px;text-align:center">{blk}</div>' + _pill())
    return _doc(body, fondo)

def r_tarjeta_datos(titular, it, marcador, valor, unidad, serie, nota, fondo=None, logo=("sello", "claro", "tr"),
                    etiqueta="Illustrative example"):
    """R23 'Tarjeta de datos' (ref. Function Health): titular Mencken arriba + tarjeta navy translúcida sutil con UN
    biomarcador, valor, unidad y minigráfica de tendencia. SIEMPRE con `etiqueta` 'Illustrative example' (o datos
    agregados reales con fuente). NUNCA datos de un paciente."""
    xs = np.linspace(0, 520, len(serie)); lo, hi = min(serie), max(serie); rg = (hi-lo) or 1
    ys = [110 - (v-lo)/rg*90 for v in serie]
    pts = " ".join(f"{a:.0f},{b:.0f}" for a, b in zip(xs, ys))
    dots = "".join(f'<circle cx="{a:.0f}" cy="{b:.0f}" r="5" fill="{GOLD if i==len(xs)-1 else "#CAD3DD"}"/>' for i, (a, b) in enumerate(zip(xs, ys)))
    spark = (f'<svg width="540" height="130" viewBox="-10 0 540 130"><polyline points="{pts}" fill="none" stroke="#CAD3DD" '
             f'stroke-width="2.4" stroke-linejoin="round"/>{dots}</svg>')
    card = (f'<div style="background:rgba(22,32,46,.48);border:1px solid rgba(202,211,221,.35);border-radius:24px;'
            f'backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);padding:38px 46px">'
            f'<div style="display:flex;justify-content:space-between;align-items:center">'
            f'<span style="{POP}font-weight:500;font-size:30px;color:#fff">{marcador}</span>'
            f'<span style="border:1.2px solid rgba(255,255,255,.6);border-radius:999px;padding:5px 16px;{POP}font-size:19px;letter-spacing:.12em;text-transform:uppercase;color:#fff">{etiqueta}</span></div>'
            f'<div style="display:flex;align-items:baseline;gap:12px;margin-top:14px"><span style="{POP}font-weight:300;font-size:110px;letter-spacing:-.04em;line-height:1;color:#fff">{valor}</span>'
            f'<span style="{POP}font-weight:300;font-size:30px;color:#CAD3DD">{unidad}</span></div>'
            f'<div style="margin-top:16px">{spark}</div>'
            f'<div style="{POP}font-weight:300;font-size:26px;line-height:1.4;color:#e6ecf2;margin-top:10px;text-wrap:balance">{_fl(nota)}</div></div>')
    head = (f'<div style="{M.it_css("hero_oscuro",74,"#fff")}line-height:1.05">{titular}</div>'
            + (f'<div style="{M.it_css("hero_oscuro",74,CREAM)}line-height:1.05">{it}</div>' if it else ""))
    body = (_veil("linear-gradient(180deg,rgba(12,16,22,.55) 0%,rgba(12,16,22,.05) 40%,rgba(12,16,22,.45) 100%)") + (_logo(*logo) if logo else '')
            + f'<div style="position:absolute;left:{round(W*.09)}px;right:{round(W*.12)}px;top:{round(H*.215)}px">{head}</div>'
            + f'<div style="position:absolute;left:{round(W*.09)}px;right:{round(W*.09)}px;top:{round(H*.47)}px">{card}</div>' + _pill())
    return _doc(body, fondo)

def r_ondas(titulo, acento=None, sub=None, fondo=None, logo=("sello", "claro", "tl"), fs=64, y=0.17):
    """R24 'Ondas + píldora' (ref. TSH), corregido por la Dra. (oct 2026): UN solo bloque jerarquizado arriba, sobre la
    zona oscura, nunca partir la frase entre arriba y abajo. Titular Mencken BOLD con la palabra clave en `pildora()`,
    acento Mencken Head ITÁLICO cream del mismo tamaño, subtítulo opcional Poppins Light. Las ondas quedan libres abajo."""
    blk = f'<div style="{MEN}font-weight:700;font-size:{fs}px;line-height:1.12;color:#fff">{titulo}</div>'
    if acento: blk += f'<div style="{M.it_css("hero_oscuro", fs, CREAM)}line-height:1.12;margin-top:6px">{acento}</div>'
    if sub: blk += f'<div style="{POP}font-weight:300;font-size:34px;line-height:1.45;color:#dfe6ee;margin-top:28px;text-wrap:balance">{_fl(sub)}</div>'
    body = (_logo(*logo)
            + f'<div style="position:absolute;left:{round(W*.133)}px;right:{round(W*.10)}px;top:{round(H*y)}px">{blk}</div>' + _pill())
    return _doc(body, fondo)

def r_cifra_titular(bold, acento, numero, unidad, texto, nota=None, fondo=None, logo=("sello", "claro", "tr"), refs=None):
    """R25 'Titular + cifra gigante' (ref. 'Testosterone levels naturally decline', oct 2026) en lenguaje LCI: titular
    Mencken BOLD + acento Mencken Head ITÁLICO (mismo tamaño), cifra Poppins Light gigante con su unidad en superíndice
    y 3 líneas cortas a la derecha, nota inferior Poppins Light. Todo a la izquierda sobre la zona limpia de la foto.
    Cifra SIEMPRE con fuente verificada [n] y con_refs."""
    x = round(W*.11)
    head = (f'<div style="{MEN}font-weight:700;font-size:70px;line-height:1.06;color:#fff">{bold}</div>'
            f'<div style="{M.it_css("hero_oscuro",70,CREAM)}line-height:1.06">{acento}</div>')
    cif = (f'<div style="display:flex;align-items:flex-start;gap:14px">'
           f'<div style="{POP}font-weight:300;font-size:230px;letter-spacing:-.05em;line-height:.82;color:#fff">{numero}</div>'
           f'<div style="padding-top:8px;{POP}font-weight:300;font-size:84px;line-height:.9;color:#fff">{unidad}</div></div>'
           f'<div style="height:1.5px;width:{round(W*.36)}px;background:rgba(255,255,255,.7);margin:40px 0 28px"></div>'
           f'<div style="{POP}font-weight:300;font-size:36px;line-height:1.3;color:#fff;max-width:{round(W*.40)}px;text-wrap:balance">{_fl(texto)}</div>')
    body = (_veil("linear-gradient(90deg,rgba(12,14,18,.70) 0%,rgba(12,14,18,.45) 42%,rgba(12,14,18,0) 70%)") + (_logo(*logo) if logo else '')
            + f'<div style="position:absolute;left:{x}px;right:{round(W*.08)}px;top:{round(H*.15)}px">{head}</div>'
            + f'<div style="position:absolute;left:{x}px;right:{round(W*.50)}px;top:{round(H*.355)}px">{cif}</div>'
            + (f'<div style="position:absolute;left:{x}px;right:{round(W*.30)}px;top:{round(H*.735)}px;{POP}font-weight:300;font-size:37px;line-height:1.35;color:#fff;text-wrap:balance">{_fl(nota)}</div>' if nota else "")
            + _pill())
    html = _doc(body, fondo)
    return con_refs(html, refs) if refs else html

RECETAS = {"R1": r_poster, "R2": r_centrado, "R3": r_marco, "R4": r_derecha,
           "R5": r_titulo_arriba, "R6": r_eyebrow_gigante, "R7": r_claro,
           "R8": r_natural, "R9": r_retrato, "R10": r_paso, "R11": r_articulo, "R12": r_dato, "R13": r_palabra, "R14": r_orbitas, "R15": r_red, "R16": r_icono, "R17": r_portada_limpia, "R18": r_cita, "R19": r_cifras, "R20": r_circulos, "R21": r_tarjeta_micro, "R22": r_nodo_luz, "R23": r_tarjeta_datos, "R24": r_ondas, "R25": r_cifra_titular}

def r_panel_claro(bold, acc, cuerpo, fondo, lado="der", logo=("principal", "navy", "tl")):
    """Panel de vidrio CREMA arriba con texto NAVY sobre foto clara (aprobado por la Dra., «Del frasco / al plato»,
    10-oct-2026). Titular bold + acento con resaltado azul claro + filete dorado + cuerpo Poppins itálica. lado="der":
    texto al margen derecho (logo se queda arriba a la izquierda). El panel se extiende 60 px fuera del lienzo para que el
    desenfoque no deje ver el borde de la foto. Cápsula sobre caída de luz oscura abajo. Usarlo como ACENTO del feed
    (comida, estilo de vida), nunca dos seguidas."""
    m = M.margen(W, H); X = 60; al = "right" if lado == "der" else "left"
    blk = (f'<div style="text-align:{al}">'
           f'<div style="{MEN}font-weight:700;font-size:84px;line-height:1.02;color:{NAVY}">{bold}</div>'
           f'<div style="margin-top:{round(84*.27)}px">{M.barra(acc, 84, M.it_css("acento", 84, NAVY), fondo="rgba(202,211,221,.95)", alinear=("der" if lado == "der" else True))}</div>'
           f'<div style="width:120px;height:4px;background:#C9A570;margin:34px {"0 26px auto" if lado == "der" else "0 26px 0"}"></div>'
           f'<div style="{POP}font-style:italic;font-weight:300;font-size:36px;line-height:1.3;color:#3a4352;{"" if lado == "der" else "margin-left:-4px"}">{cuerpo}</div></div>')
    panel = (f'<div style="position:absolute;left:-{X}px;right:-{X}px;top:-{X}px;padding:{(m+150 if H < 1500 else 300)+X}px {m+X}px {round(m*0.62)}px;'   # story: el logo baja a 210 px → el titular arranca debajo
             f'backdrop-filter:blur(22px);-webkit-backdrop-filter:blur(22px);'
             f'background:linear-gradient(180deg,rgba(241,236,228,.90),rgba(237,229,218,.84));border-bottom:1.2px solid rgba(210,181,138,.6)">{blk}</div>')
    body = (_veil("linear-gradient(0deg,rgba(14,18,26,.84) 0%,rgba(14,18,26,.45) 12%,rgba(14,18,26,0) 26%)") + panel + (_logo(*logo) if logo else '') + _pill())
    return _doc(body, fondo, soporte='panel_claro')


# ───────── AUDITOR DE TANDA (la Dra., 11-oct-2026: «¿por qué sigues haciendo todas las fotos con el mismo efecto?») ─────────
SOPORTES_FOTO = ('mitad', 'vidrio', 'columna_izq', 'columna_der', 'recuadro', 'panel_claro', 'velo')
def auditar_soportes(secuencias):
    """secuencias: {perfil: [(nombre, html), ...]} en ORDEN de publicación. Falla (AssertionError) si un soporte de foto
    se repite en dos piezas SEGUIDAS del mismo perfil, si un perfil usa el mismo soporte más de 2 veces en la tanda, o si
    la lámina «ducha» (columna_*) aparece más de 1 vez. Se llama SIEMPRE antes de entregar una tanda."""
    import re, collections
    errores = []
    for perfil, piezas in secuencias.items():
        sops = []
        for nombre, html in piezas:
            m_ = re.search(r'<!--SOPORTE:(\w+)-->', html); sops.append((nombre, m_.group(1) if m_ else None))
        for (a, sa), (b, sb) in zip(sops, sops[1:]):
            if sa and sa == sb: errores.append(f'{perfil}: «{sa}» seguido en {a} y {b}')
        cnt = collections.Counter(s_ for _, s_ in sops if s_)
        for s_, n in cnt.items():
            lim = 1 if s_.startswith('columna') else 2
            if n > lim: errores.append(f'{perfil}: «{s_}» {n} veces (máx. {lim})')
    assert not errores, 'VARIEDAD DE SOPORTES — corregir antes de entregar:\n  ' + '\n  '.join(errores)
    return True
