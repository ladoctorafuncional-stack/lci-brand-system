# -*- coding: utf-8 -*-
"""
Pipeline de tratamiento de imagen — Longevity Clinical Institute.
Convierte cualquier foto licenciada en parte de la familia visual LCI.

Tratamientos:
  - 'grade'    : color-grade de marca (recomendado para COMIDA: la mantiene apetitosa
                 pero unifica hacia la paleta). Desatura suave + lavado duotono leve.
  - 'tritone'  : gradient-map firma navy→gold→cream (para texturas, abstractos, heroes
                 con mucho texto encima). Look editorial fuerte.
  - 'duo'      : duotono navy→cream de dos tonos (minimalista).
Extras: grano de película sutil, viñeta navy, y overlay de gradiente para zona de texto.
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# ---- Paleta de marca ----
NAVY      = (42, 54, 73)     # #2A3649
NAVY_DEEP = (25, 34, 46)     # #19222E
GOLD      = (210, 181, 138)  # #D2B58A
GOLD_DEEP = (185, 150, 106)
CREAM     = (237, 229, 218)  # #EDE5DA
BLUE      = (202, 211, 221)  # #CAD3DD

def _lut_from_stops(stops):
    """stops: lista de (pos0..1, (r,g,b)) -> LUT 256x3."""
    pos = np.array([s[0] for s in stops])
    cols = np.array([s[1] for s in stops], dtype=float)
    x = np.linspace(0, 1, 256)
    lut = np.zeros((256, 3))
    for c in range(3):
        lut[:, c] = np.interp(x, pos, cols[:, c])
    return lut

# Gradient-map firma: sombras navy, mids puente cálido (evita verde lodoso), altas gold→cream
_TRITONE = _lut_from_stops([
    (0.00, NAVY_DEEP),
    (0.28, NAVY),
    (0.52, (104, 100, 102)),   # puente taupe neutro-cálido
    (0.70, GOLD_DEEP),
    (0.86, GOLD),
    (1.00, CREAM),
])
_DUO = _lut_from_stops([
    (0.00, NAVY_DEEP),
    (0.35, NAVY),
    (1.00, CREAM),
])

def _luma(arr):
    return (0.2126*arr[:,:,0] + 0.7152*arr[:,:,1] + 0.0722*arr[:,:,2])

def _apply_lut(gray, lut):
    idx = np.clip(gray, 0, 255).astype(int)
    return lut[idx]  # HxWx3

def _scurve(arr, amount=0.12):
    """S-curve suave de contraste sobre [0,1]."""
    x = arr/255.0
    y = x + amount*np.sin((x-0.5)*np.pi)
    return np.clip(y, 0, 1)*255.0

def _grain(shape, amount=7.0, seed=7):
    rng = np.random.default_rng(seed)
    n = rng.normal(0, amount, shape[:2])
    return n[:, :, None]

def _vignette(h, w, strength=0.20):
    yy, xx = np.mgrid[0:h, 0:w]
    cy, cx = h/2, w/2
    d = np.sqrt(((xx-cx)/(w/2))**2 + ((yy-cy)/(h/2))**2)
    d = np.clip(d, 0, 1)
    return (d**1.6)[:, :, None]*strength  # 0 centro -> strength bordes

def treat(img, mode='grade', duo_alpha=0.30, desat=0.32,
          grain=6.0, vignette=0.18, contrast=0.10, seed=7):
    """Devuelve PIL.Image tratada."""
    im = img.convert('RGB')
    arr = np.asarray(im, dtype=float)
    h, w = arr.shape[:2]
    gray = _luma(arr)
    gray = _scurve(gray, contrast)               # contraste sobre la luminancia

    if mode == 'tritone':
        out = _apply_lut(gray, _TRITONE)
    elif mode == 'duo':
        out = _apply_lut(gray, _DUO)
    else:  # 'grade' — recomendado para comida
        # 1) desaturar parcialmente
        g3 = np.repeat(gray[:, :, None], 3, axis=2)
        desatd = arr*(1-desat) + g3*desat
        # 2) lavado duotono leve encima (split-tone navy/gold/cream)
        duo = _apply_lut(gray, _TRITONE)
        out = desatd*(1-duo_alpha) + duo*duo_alpha
        # 3) calidez sutil en altas luces
        hi = np.clip((gray-150)/105, 0, 1)[:, :, None]
        warm = np.array(CREAM)-np.array([255,255,255])
        out = out + hi*warm*0.12

    # viñeta navy
    if vignette:
        v = _vignette(h, w, vignette)
        out = out*(1-v) + np.array(NAVY_DEEP)*v
    # grano
    if grain:
        out = out + _grain(arr.shape, grain, seed)

    return Image.fromarray(np.clip(out, 0, 255).astype('uint8'))

def text_overlay(img, side='left', strength=0.82, color=NAVY_DEEP, span=0.62):
    """Gradiente direccional para legibilidad de texto sobre la imagen."""
    im = img.convert('RGB')
    arr = np.asarray(im, dtype=float)
    h, w = arr.shape[:2]
    if side in ('left', 'right'):
        g = np.linspace(1, 0, w)
        if side == 'right': g = g[::-1]
        g = np.clip(g/span, 0, 1)[None, :]
        g = np.repeat(g, h, axis=0)
    else:  # bottom/top
        g = np.linspace(0, 1, h)
        if side == 'top': g = g[::-1]
        g = np.clip(g/span, 0, 1)[:, None]
        g = np.repeat(g, w, axis=1)
    g = (g**1.3*strength)[:, :, None]
    out = arr*(1-g) + np.array(color)*g
    return Image.fromarray(np.clip(out, 0, 255).astype('uint8'))

def gold_rule(draw, x, y, w, color=GOLD, h=3):
    draw.rectangle([x, y, x+w, y+h], fill=color)
