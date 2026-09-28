---
name: lci-piezas-graficas
description: >
  Motor de DISEÑO GRÁFICO y diagramación del Longevity Clinical Institute (Dra. Carolina
  Rodríguez) — clona el estilo de la diseñadora Diana Paola Londoño (Ikigai). Úsalo SIEMPRE
  que se pida crear, diseñar, diagramar o adaptar cualquier PIEZA GRÁFICA de LCI: Instagram
  Story o post, carrusel, infografía, flyer/afiche, banner, portada, pieza de redes, anuncio,
  cita, dato/estadística, invitación, aviso a pacientes, pieza del curso de péptidos, firma de
  correo o carnet. Dispara con términos como "diseña", "hazme una pieza", "story", "post",
  "carrusel", "infografía", "flyer", "banner", "pieza para Instagram", "diagrama esto con mi
  marca", "adáptalo a mi estilo", o cuando se suba contenido para convertir en pieza visual.
  TODO el material de marca está embebido (fuentes Mencken Std + Poppins, kit de logos oficial,
  paleta del brandbook, 34 piezas maestras, membrete): nunca pedir que se vuelvan a subir.
  Resultado: PNG pixel-exacto (no documentos clínicos; esos son del skill lci-design-system).
---

# LCI — Piezas Gráficas (clon de Diana Paola Londoño)

Motor para producir piezas de redes/marketing idénticas al estándar de marca de LCI. **No se
reinventa el diseño**: se ensambla con `marca.py`, que ya trae fuentes, logos, paleta y los
motivos firma de Paola. La doctrina de marca completa está en
`references/marca-oficial/MANUAL-LCI.md` — **léela primero** ante cualquier duda de color,
tipografía, logo o foto.

## Regla de oro
Nunca recrear CSS, colores, fuentes ni logos a mano. Siempre `import marca as B`. Si una pieza
no usa `marca.py`, está mal hecha.

## Flujo de trabajo
1. `import sys; sys.path.insert(0,'/mnt/skills/user/lci-piezas-graficas/assets'); import marca as M`
2. Elegir formato (`M.PRESETS`: story, post, post_v, carrusel, infografia, flyer, banner, email_sig, carnet…).
3. Construir con un **template** de alto nivel (`M.t_poster`, `M.t_concepto`, `M.t_story`,
   `M.t_curso`, `M.t_cita`) o ensamblar a mano con los **helpers** (eyebrow, titular, hl, caja,
   conector, bullets, checklist, chips, goldbox, bloque_fecha, bloque_ubicacion, pill, logo…).
4. Escribir el HTML a archivo y renderizar a PNG exacto:
   `python3 scripts/render.py salida.html salida.png <formato> 2`  (2 = densidad retina).
5. **Verificar visualmente** el PNG contra las muestras de `references/muestras-paola/` antes de entregar.
6. Entregar con `present_files` (PNG para publicar + HTML editable).

## Identidad de marca (resumen — detalle en MANUAL-LCI.md)
- **Paleta (5):** navy `#2A3649` (principal) · azul medio `#5D768C` (resaltar) · light blue
  `#CAD3DD` (sobre oscuro) · gold `#D2B58A` (apoyo, junto al medio) · cream `#EDE5DA` (fondos livianos).
- **Tipografía:** Mencken Std (display + textos largos "Text" + botón) · Poppins (títulos,
  subtítulos, cuerpo, itálicas de acento). Patrón firma: palabra-acento Mencken itálico
  (azul/crema/oro) + resto Mencken bold (blanco/navy). Todo embebido base64 (`fonts_brand.json`).
- **Logos (`logos_brand.json`):** `logo('principal'|'sello'|'terciario', tema)` con tema
  blanco/beige/gold/navy/claro. `principal` = wordmark apilado (default). Marca personal:
  `logo_cr('wordmark'|'sello', color=hex)` — solo cuando la Dra. lo pida.
- **Foto:** expresiones neutras (sin sonrisas fuertes), luz bioluminiscente, close-ups de
  células/ADN/neuronas; tratar con `lci_treat` (tritone/duo navy) + velo navy bajo texto.
- **Contacto (pill obligado al cierre):** institucional `M.pill()` o personal `M.pill(False)`.
- **Sub-paletas de fondo:** `M.GRAD_NAVY/_DEEP` (institucional) · `M.GRAD_CURSO` (azul eléctrico,
  curso de péptidos) · `M.GRAD_CREAM/_BLUE/_GRIS` (temas claros, usar `theme="light"`).

## Motivos firma disponibles (helpers en marca.py)
barra de resaltado `hl(txt,'blue'|'gold'|'mid'|'grey')` · caja de borde `caja()` · caja dorada
`goldbox()` · conector con nodos `conector([...])` · viñetas diamante `bullets([...])` · lista
check dorada `checklist([...])` · chips `chips([...])` · dato grande `stat()` · fecha
`bloque_fecha()` · ubicación `bloque_ubicacion()` · pill `pill()`.

## Catálogo y referencias
- `references/marca-oficial/MANUAL-LCI.md` — biblia de marca (paleta, tipografía, logo, foto, contactos).
- `references/marca-oficial/BRANDBOOK_*.pdf` — manual oficial fuente.
- `references/muestras-paola/` — 34 piezas maestras aprobadas = estándar visual a igualar.
- `references/catalogo-piezas.md` — recetas por tipo de pieza.
- `assets/papeleria/membrete_lci.png` — cabezote navy / textura de partículas.
