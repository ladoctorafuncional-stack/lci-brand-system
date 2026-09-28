# LCI — Receta de construcción (catálogo de componentes)

Todo se ensambla con clases definidas en `brand.py → base_css()`. Importa el motor y úsalas
tal cual. Estructura de un builder mínimo:

```python
import sys; sys.path.insert(0,'/mnt/skills/user/lci-design-system/assets')
import brand as B
hero = "...";  sec1 = "...";  # secciones
body = hero + sec1 + ... + B.footer()
open(out,'w',encoding='utf-8').write(B.html_doc("Título", body))
```

## Componentes (clases)
- **Hero** `.hero` → contiene `.hero-top` (con `<img class="seal" src="{B.LOGO_SEAL}">` a la
  izq + `.hero-doc .tag` a la der), `.eyebrow`, `h1` con `<span class="accent">` (Mencken
  itálico light-blue), `.sub` (con `<span class="serif-it">` para acentos), `<hr class="hairline">`,
  y `.patient-card` (grid 2×2 de `.cell` con `.k`/`.v`).
  - Variante con foto: `style="background:linear-gradient(118deg, rgba(25,34,46,.95) 0%,
    rgba(25,34,46,.86) 40%, rgba(42,54,73,.62) 72%, rgba(42,54,73,.42) 100%), url('{HERO_BG}');
    background-size:cover;background-position:center;"`.
- **Sección** `.section` (o `.section.alt` para fondo beige alterno). Encabezado:
  `.sec-head` = `.sec-ico` (cuadro dorado 3D con SVG stroke 24×24) + `.t` (título Mencken con
  `<span class="it">` itálico dorado y borde inferior gold). Texto introductorio: `.lead`.
- **Sección oscura** `.dark-section` (para consejos finales). `.dark-card` para tarjetas navy.
- **Tarjetas** `.card`, `.note` (aviso beige borde gold), `.warn` (lista de precauciones con ✕).
- **Bracket connector** `.bracket` (`.line` + `.items .it` con `.lead-w`). Motivo Paola.
- **Ring-row** `.ring-row` (grid 4 col) con `.ring` (círculo borde gold + SVG) + `.lbl`. Motivo
  "Beneficios".
- **Pill-quote** `.pill-quote` (cápsula borde gold, Mencken itálico).
- **Tablas** `<table>` (thead navy, filas alternas). `.daycol`/`.dish` para énfasis.
- **Zonas/FITT/Día** (deportivo): `.zone`, `.fitt-grid .fitt`, `.day.s/.c/.r/.f` con `.dtag`.
- **Numlist** `.numlist .numitem` (`.nc` número dorado + `.nt` título). `.quote` cita final.
- **Footer** `B.footer()` siempre al cierre. Botón impresión lo añade `B.html_doc`.

## Bandas/banners con foto (estilo editorial)
Banda full-bleed (entre secciones):
```html
<section class="avoid-break" style="position:relative;min-height:280px;display:flex;
 align-items:center;padding:54px;color:#fff;background:linear-gradient(95deg,
 rgba(25,34,46,.93) 0%, rgba(25,34,46,.70) 42%, rgba(25,34,46,.20) 78%, rgba(25,34,46,0) 100%),
 url('{IMG}');background-size:cover;background-position:center 38%;">
  <div style="max-width:540px;position:relative;z-index:2;">
    <div class="eyebrow" style="color:var(--gold);">EYEBROW</div>
    <div class="serif" style="font-size:2.05rem;line-height:1.12;margin-top:10px;">
      Titular <span class="serif-it" style="color:var(--blue);">acento</span> resto.</div>
  </div>
</section>
```
Banner de sección (más bajo, ~200px): mismo patrón con gradiente vertical
`linear-gradient(0deg, rgba(25,34,46,.92), rgba(25,34,46,.10))` y `align-items:flex-end`.

## Generar fotos tratadas embebidas
Ver `build/gen_embeds.py`: `lci_treat.treat(Image.open(f), mode='grade'|'tritone', vignette=..,
contrast=..)` → resize → JPEG q82 → base64 → `data:image/jpeg;base64,...`. Mantener el
documento autocontenido (todo base64; sin CDN, sin links externos).

## Estructura estándar por plan
- **Nutricional**: hero(foto) → enfoque → recomendaciones/macros → guía de alimentos →
  soporte nutracéutico → intercambios → menú 14 días → [banda editorial] → recetas →
  [banner mercado] → lista de mercado (localizada a la ciudad del paciente) → consejos+cita.
- **Deportivo**: hero → evaluación FC/zonas (+warn de seguridad) → FITT → calendario semanal
  (con mapas musculares SVG) → progresión 12 sem → pausas activas + respiración → equipo →
  consejos+cita. FCmax = 206.9 − (0.67×edad).
- **Sueño**: hero → por qué el sueño es medicina (bracket) → diagnóstico actual (fortalezas vs
  corregir) → regla de oro (luz/melatonina) → ritual nocturno (timeline) → respiración 4·4·6
  (ring-row) → café y reloj interno → el día construye la noche (cinta circadiana SVG) →
  consejos+cita.

## Paginación al imprimir / exportar PDF (ya en `brand.py`)
- Cada `.section`, `.section.alt` y `.dark-section` **empieza en página nueva** (`break-before:page`).
- El `.hero` queda como **portada** (página 1, sin salto antes).
- Bandas y banners full-bleed que introducen una sección llevan la clase **`band-intro`**:
  saltan a página nueva y **arrastran consigo la sección siguiente** (no la dejan huérfana).
  Aplica `class="avoid-break band-intro"` a esas `<section>` con foto.
- El footer queda pegado a la última sección (no salta).
Esto ya vive en el motor; no hay que reconfigurarlo por documento. Verificar siempre con un
render `--print-to-pdf` antes de entregar.

## Grids de tarjetas (evitar estiramiento / huecos)
Cuando un grid de 2 columnas tiene tarjetas de alturas distintas (recetas, etc.), usa
`display:grid;grid-template-columns:1fr 1fr;gap:18px;**align-items:start**;` para que la
tarjeta más corta NO se estire a la altura de la más alta (queda en su altura natural). Empareja
items de altura similar (p. ej. las dos recetas más cortas juntas en la última fila) para
minimizar el espacio entre filas. Cada tarjeta lleva `break-inside:avoid`. Esto optimiza el
espacio sin verse apretado y mantiene la elegancia.

## Gestión inteligente del espacio (revisar SIEMPRE en PDF)
Tras construir un plan, renderiza a PDF (`--print-to-pdf`) y revisa cada página. La meta:
no desperdiciar espacio sin perder elegancia.
- **Hueco grande al final de una sección** → llénalo en este orden de preferencia:
  1. *Reflujo:* pon bloques lado a lado (p. ej. "Objetivo calórico" + "Ayuno" en 2 columnas;
     tarjetas con `align-items:start`).
  2. *Elemento gráfico aprobado:* añade una banda `B.img_strip(...)` con una imagen tratada
     de la biblioteca, pertinente a esa sección.
  3. *Texto útil y real:* agrega un bloque educativo alineado con la prescripción (p. ej. la
     "guía de porciones con la mano" en Intercambios). Nunca contenido inventado.
- **Desborde mínimo (párrafo huérfano)** → compacta (2 columnas, tarjetas más densas) o usa
  `keep-with-prev` para que la sección corta llene el espacio de la anterior si cabe entera.
- **Nunca recargar:** las imágenes marcan ritmo (~1 cada 2–3 páginas), no llenan cada hueco.
  Si una sección ya está llena y elegante, déjala respirar.
- Solo se usan elementos **previamente acordados y aprobados** por la Dra. Rodríguez.

## Biblioteca de elementos gráficos aprobados
Originales en `assets/img-library/`; versiones tratadas (lci_treat 'grade') listas en
`build/embeds.json`. Aprobadas para el plan **nutricional**:
- `hero_flatlay` → fondo del hero.
- `band_bowl` → banda editorial antes de Recetas.
- `banner_market` → banner antes de Lista de mercado.
- `nutra_hands` → banda de cierre de Soporte nutracéutico ("comida real + ciencia").
- `inter_bowls` → banda de cierre de Intercambios ("porción a ojo").
- `despensa_jars` → disponible para Mercado/Despensa.
Componente: `B.img_strip(bg, eyebrow, head_a, head_b, h=220, pos='center')`.
Para regenerar tratadas (paciente o foto nueva): `build/gen_embeds.py` con `lci_treat`.
**No usar** imágenes de gym/whey/scoop en el plan nutricional (reservadas para deportivo);
desentonan con la estética de longevidad.

## Reglas inviolables
1. Español colombiano, tutear ("tú"), tono cálido de médica. Inglés solo si el paciente es
   internacional.
2. Contenido clínico: 100% según la prescripción de la doctora. Nunca inventar, omitir,
   alterar ni resumir dosis, diagnósticos o indicaciones.
3. Fuentes y logos SIEMPRE embebidos base64 vía `brand.py`. Nunca CDN ni Google Fonts.
4. Verificar con render (Chrome headless screenshot) antes de entregar.
5. El diseño es idéntico al de las referencias LOCKED; solo cambia el contenido del paciente.
