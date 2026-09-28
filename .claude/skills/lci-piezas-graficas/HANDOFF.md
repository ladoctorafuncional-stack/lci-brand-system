# HANDOFF — Skill "lci-piezas-graficas" (continuidad)
_Última actualización: 2026-06-27. Para retomar en un chat nuevo SIN perder contexto._

## Cómo retomar en un chat NUEVO
1. Sube **`lci-piezas-graficas.skill`** (o instálalo).
2. Di: _"Continúa el skill de piezas LCI desde este .skill; lee el HANDOFF y el MANUAL-LCI.md."_
3. Claude lo descomprime a `/home/claude/lci-piezas-graficas/` y sigue. Biblia de marca:
   `references/marca-oficial/MANUAL-LCI.md`.

## Qué es
Motor de diseño gráfico de LCI que clona el estilo de **Diana Paola Londoño**. Genera piezas
(stories, posts, carruseles, infografías, flyers, banners, citas, datos, avisos, curso de
péptidos, firmas, carnets) como HTML autocontenido → PNG pixel-exacto. Hermano de
`lci-design-system` (ese hace documentos clínicos / planes; este hace piezas gráficas).

## TAREA EN CURSO 🎯 — "Reclaim" como vara de calidad
- **Decisión de la Dra.:** las piezas fotográficas se hacen con **stock libre para uso comercial
  (Unsplash) tratado al estilo del manual** (no subir fotos propias salvo que quiera).
- **Primera pieza a clavar 1:1:** "Reclaim" (rostro/atleta). La Dra. eligió un **close-up de
  rostro masculino MOJADO/sudado, intenso, fondo oscuro**.
- **Foto vetada (libre comercial, Unsplash):** `eU4Xvwp_md8` (OANA BUZATU) —
  pág: https://unsplash.com/photos/sweaty-face-of-a-man-close-up-eU4Xvwp_md8 ·
  descarga: https://unsplash.com/photos/eU4Xvwp_md8/download?force=true
- **PASO SIGUIENTE:** obtener ese archivo (ver "Límite de red" abajo) → tratarlo con
  `assets/lci_treat.py` (duotono navy / tritono navy·gold·cream + velo navy, manteniendo
  expresión neutra) → componer con `M.t_poster(...)` (es el layout Reclaim) usando
  `fondo=M.foto(uri,'navy-side')` → render → comparar 1:1 contra
  `references/muestras-paola/poster_reclaim_face.png` e iterar hasta el nivel de la Dra.
  Texto del master: caja "Reclaim the energy" (Mencken it azul) · "you thought was gone."
  (Mencken bold) · "Regenerate from within." (Mencken reg) · tagline "Your body knows how to
  heal. / We know how to activate it." (azul it) · conector → "More mental clarity. / More
  vitality. / More life." · pill institucional · wordmark blanco arriba-izq.

## ⚠️ LÍMITE DE RED (importante)
El sandbox NO puede descargar imágenes externas: `bash` da **HTTP 403** (Unsplash fuera de la
allowlist) y `web_fetch` **no soporta imágenes**. Para meter stock al pipeline hay 2 vías:
  (A) la Dra. **sube el archivo** con el botón +, o
  (B) habilitar `images.unsplash.com` y `unsplash.com` en **ajustes de red** del entorno y
      entonces Claude lo baja directo.
Sin una de las dos, NO se puede tratar stock; no insistir en bajarlo por bash.
**ACTUALIZACIÓN 2026-06-27:** la Dra. está surtiendo el stock vía botón + (vía A), así que el
límite ya no bloquea. Ver "Biblioteca de stock" abajo.

## Biblioteca de stock ✅ (`references/stock/`)
Material libre de uso comercial provisto por la Dra. Catálogo: `references/stock/MANIFIESTO-STOCK.md`
+ hoja de contactos `LCI_biblioteca_stock.png`. Taxonomía (7 carpetas):
`deportivo · sueno · cientifico · wearables-datos · nutricion-producto · clinico · video`.
- **HI-RES uso final (Pexels 4K–8K + video 1080×1920):** todo `deportivo/` (7) y `sueno/` (4) + `video/`.
  Heroes ✦: `pexels-assomyron-32695888` (luz azul) y `pexels-foadshariyati-30672394` (neutra).
- **PREVIEW iStock 612px = SOLO referencia de mood** (conseguir licenciada en alta antes de arte final):
  `cientifico/` (13, incl. TELÓMERO `698059132` ✦ y cerebro plexus `1153710314` ✦),
  `wearables-datos/` (4), `nutricion-producto/` (3), `clinico/` (2).
- Tratar SIEMPRE con `assets/lci_treat.py` (duo/tritone/grade) + velo navy bajo texto.
  Correcciones marca pendientes: naranja de la bici, morado de red neuronal, fondo rosa de la cápsula.

## Estado del motor ✅ (assets/marca.py v2)
- Templates: `t_poster` (=Reclaim), `t_concepto` (=Exosomes), `t_story`, `t_curso`, `t_cita`.
- Helpers: eyebrow, titular, hl (barra resaltado blue/gold/mid/grey), caja, goldbox, conector
  (nodos), bullets, checklist, chips, stat, bloque_fecha, bloque_ubicacion, pill
  (institucional/personal), logo / logo_cr (recolor marca personal).
- Fondos: GRAD_NAVY/_DEEP, GRAD_CURSO (azul eléctrico curso), GRAD_CREAM/_BLUE/_GRIS (+theme="light").
  **NUEVO** `M.bg_particulas(formato)` → navy a sangre con la onda de partículas oficial
  (del membrete), reutilizable. `M.foto(uri, veil=...)` para fotos.
- **Arreglos de esta sesión:** (1) `_bg` ahora envuelve data-URI crudo en url() — antes dejaba el
  fondo en BLANCO (causa de las primeras pruebas "horribles"); (2) imágenes ya no se estiran
  (`align-self:flex-start`); (3) bg_particulas añadido.
- **Fuentes verificadas:** Mencken Std 400/700/800 + Head it 400/800 y Poppins 300–700
  renderizan REALES en Chromium (no fallback). El problema nunca fue tipográfico.

## Lección clave (no repetir)
Las primeras pruebas (`prueba_reclaim_navy`, `prueba_exosomes_claro`) fueron rechazadas por la
Dra. ("horribles, nada que ver con Paola"). Causa: **degradado plano SIN foto** (medio lienzo
muerto) + el bug de `_bg`. La marca es **fotográfica / textura a SANGRE COMPLETA** con
composición llena. NUNCA entregar piezas con fondo plano vacío. Ver `prueba_comunicado.png` y
`build/ejemplos/comunicado_aviso.py` como el nivel correcto (reproduce `story_something_important`).

## Pendientes 🔜
1. Clavar el Reclaim tratado (tarea en curso, arriba). YA hay stock deportivo HI-RES en
   `references/stock/deportivo/` para trabajar sin depender de Unsplash.
2. Templates faltantes: `t_firma` (firma email), `t_carnet`, `t_soon` (panel foto vertical +
   marca "+" + ubicación), `t_invitacion` (fecha + goldbox), `t_dato`, infografías íconos/ring/timeline.
3. Logos de aliados (Kharrazian/CFMC/AFMC) NO embebidos — pedirlos para avisos formales.
4. Template de carta membreteada (usar `assets/papeleria/membrete_lci.png` de cabezote).
5. Reempaquetar el .skill tras cada avance (zip con raíz `lci-piezas-graficas/`, excluir
   `__pycache__`, salida a `/mnt/user-data/outputs/...skill`).

## Inventario embebido (todo viaja en el .skill)
fonts_brand.json (13) · logos_brand.json (17) · papeleria/membrete_lci.png · lci_treat.py ·
marca.py v2 · muestras-paola/ (34, vara de calidad estilo Paola) · marca-oficial/ (BRANDBOOK pdf +
Hoja_Membrete docx + MANUAL-LCI.md + video) · ejemplos-clinicos/ · build/ejemplos/ (comunicado) ·
**references/stock/** (34 fotos + 1 video, 7 temas + MANIFIESTO-STOCK.md).
