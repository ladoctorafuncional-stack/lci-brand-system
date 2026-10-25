#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar_pdf.py - Control de calidad OBLIGATORIO de todo PDF de LCI.

Reprueba (exit 1) si:
  1. Alguna pagina tiene contenido a menos de 10 mm de cualquier borde.
  2. Alguna pagina queda con un hueco final mayor al permitido (papel desperdiciado).

Uso:  python3 verificar_pdf.py archivo.pdf
      python3 verificar_pdf.py archivo.pdf --hueco 55

Solo la ultima pagina esta exenta de la regla del hueco (cierra el documento).
La PORTADA NO esta exenta: regla de la Dra. Rodriguez, el contenido empieza a
escribirse en el espacio en blanco de la pagina 1, debajo del hero.
"""
import sys, os, glob, subprocess, tempfile, shutil

DPI = 150
MM = DPI / 25.4
MARGEN_MIN_MM = 10.0
HUECO_MAX_MM = 70.0      # hueco final tolerado en una pagina intermedia (27% del alto util)
TOL_MM = 0.35            # tolerancia por redondeo de rasterizado a 150 dpi
UMBRAL_TINTA = 245       # < esto cuenta como tinta

def _paginas(pdf, tmp):
    subprocess.run(["pdftoppm", "-png", "-r", str(DPI), pdf, os.path.join(tmp, "p")],
                   check=True, capture_output=True)
    return sorted(glob.glob(os.path.join(tmp, "p-*.png")))

def _libre(px, w, h, lado):
    mmpx = 25.4 / DPI
    if lado in ("sup", "inf"):
        rng = range(h) if lado == "sup" else range(h - 1, -1, -1)
        for i, y in enumerate(rng):
            for x in range(0, w, 2):
                if px[x, y] < UMBRAL_TINTA:
                    return i * mmpx
        return h * mmpx
    rng = range(w) if lado == "izq" else range(w - 1, -1, -1)
    for i, x in enumerate(rng):
        for y in range(0, h, 2):
            if px[x, y] < UMBRAL_TINTA:
                return i * mmpx
    return w * mmpx


def _vacio_inf(px, w, h):
    """Hueco final REAL: filas del pie que no tienen contenido aunque esten pintadas
    de un fondo de color (p. ej. la seccion beige). Una fila vacia es la que cambia de
    tono 4 veces o menos (margen blanco | fondo | margen blanco). Texto, tarjetas y
    fotos producen muchas mas transiciones."""
    mmpx = 25.4 / DPI
    for i, y in enumerate(range(h - 1, -1, -1)):
        trans, prev = 0, px[0, y]
        for x in range(0, w, 2):
            q = px[x, y]
            if abs(q - prev) > 10:
                trans += 1; prev = q
                if trans > 4:
                    return i * mmpx
    return h * mmpx

def _cierra_con_banda(px, w, h, libre_inf_mm):
    """True si lo ultimo de la pagina es una banda a sangre (ocupa >90% del ancho).
    Esas paginas son separadores de capitulo por diseno, no papel desperdiciado."""
    ultimo = h - int(libre_inf_mm * MM) - 1
    mejor = 0.0
    for off_mm in range(3, 45, 2):          # barre la franja de 3 a 45 mm sobre el ultimo pixel
        y = ultimo - int(off_mm * MM)
        if y < 0:
            break
        con = sum(1 for x in range(0, w, 2) if px[x, y] < UMBRAL_TINTA)
        mejor = max(mejor, con / (w / 2))
    return mejor >= 0.85

def verificar(pdf, hueco_max=HUECO_MAX_MM):
    try:
        from PIL import Image
    except ImportError:
        print("FALTA Pillow: pip install pillow --break-system-packages"); return 2
    tmp = tempfile.mkdtemp()
    try:
        pgs = _paginas(pdf, tmp)
        n = len(pgs)
        fallos = []
        print(f"{os.path.basename(pdf)} - {n} paginas\n")
        print(f"{'pag':>4} {'sup':>7} {'inf':>7} {'izq':>7} {'der':>7}   estado")
        for i, f in enumerate(pgs, 1):
            im = Image.open(f).convert("L"); w, h = im.size; px = im.load()
            v = {l: _libre(px, w, h, l) for l in ("sup", "inf", "izq", "der")}
            malos = [l for l, mm in v.items() if mm < MARGEN_MIN_MM - TOL_MM]
            estado = ""
            if malos:
                fallos.append(f"pag {i}: contenido a menos de 10 mm del borde {', '.join(malos)}")
                estado = "MARGEN <10mm"
            # regla del hueco: exenta SOLO la ultima pagina (las bandas ya no eximen: 23/09/2026). Antes:
            # cierran con una banda decorativa a sangre completa (separador de capitulo)
            hueco = max(v["inf"], _vacio_inf(px, w, h))
            # la banda se busca justo encima del ULTIMO CONTENIDO real, no del borde:
            # un fondo beige vacio no es una banda decorativa.
            banda = _cierra_con_banda(px, w, h, hueco)
            if i < n and hueco > hueco_max:
                fallos.append(f"pag {i}: hueco final de {hueco:.0f} mm (maximo {hueco_max:.0f} mm)")
                estado = (estado + " ").strip() + f" HUECO {hueco:.0f}mm"
            print(f"{i:>4} {v['sup']:>7.2f} {v['inf']:>7.2f} {v['izq']:>7.2f} {v['der']:>7.2f}   {estado or 'ok'}")
        print()
        if fallos:
            print("PDF REPROBADO:")
            for x in fallos: print("  -", x)
            print("\nQue hacer: el texto debe fluir y llenar la pagina. Revisa que no haya")
            print("saltos de pagina forzados (.page-break) ni bloques sobredimensionados.")
            return 1
        print("PDF APROBADO: margenes de 10 mm en los cuatro bordes y sin paginas medio vacias.")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    hueco = HUECO_MAX_MM
    if "--hueco" in sys.argv:
        hueco = float(sys.argv[sys.argv.index("--hueco") + 1])
    sys.exit(verificar(sys.argv[1], hueco))
