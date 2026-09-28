# MANUAL DE MARCA — Longevity Clinical Institute (LCI)
**La biblia.** Fuente única de verdad para diseñar cualquier pieza de LCI. Destilado del
`BRANDBOOK_LONGEVITY_CLINICAL_INSTITUTE.pdf` (oficial, Ikigai / Diana Paola Londoño) + las
34 piezas maestras en `../muestras-paola/`. Si algo aquí choca con una ocurrencia del momento,
**manda esto**.

> Línea de marca: **THE MEDICINE OF THE FUTURE.** · MED / COL · 2026.

---

## 0. Esencia
No sumar años a la vida (*lifespan*) sino vida a los años (*healthspan*). Enfoque proactivo,
anticiparse a la enfermedad, optimizar la biología a nivel celular, proteger el ADN.
Tono: experto, sereno, de vanguardia. **Palabras clave:** Líder · Experticia · Innovación ·
Ciencia · Tecnología.

---

## 1. Paleta oficial (los 5 colores — usar HEX exactos)
| Rol | Nombre | HEX | RGB | CMYK |
|---|---|---|---|---|
| Oscuro (principal) | Navy | `#2A3649` | 42,54,73 | 87,71,46,47 |
| Claro | Light blue | `#CAD3DD` | 202,211,221 | 25,13,11,0 |
| **Medio (contraste)** | **Azul medio** | **`#5D768C`** | 93,118,140 | 67,44,31,14 |
| Golden | Gold | `#D2B58A` | 210,181,138 | 18,27,49,5 |
| Beige | Cream | `#EDE5DA` | 237,229,218 | 8,9,16,0 |

**Proporciones de uso (regla del manual):**
- **Oscuro** → color principal, fondos sólidos.
- **Medio `#5D768C`** → secundario, resaltar elementos importantes (texto-acento, subrayados).
- **Claro** → todos los elementos gráficos sobre fondos oscuros, o como fondo alterno.
- **Beige** → fondos livianos.
- **Golden** → elementos gráficos de apoyo, **junto al azul medio**. Nunca dominante.

---

## 2. Tipografía
Tres roles. **Nunca** Google Fonts/CDN: todo embebido base64 desde `../../assets/fonts_brand.json`.

1. **Tipografía del logo** — sans geométrica fina (viene rasterizada en los logos; no se reproduce en texto).
2. **Mencken Std** — serif editorial. En el manual es la *"tipografía minimal / textos largos"* (variante **Mencken Std Text**) y el **texto especial / botón**. En la práctica de Paola es además el **display emocional**: titulares grandes y palabras-acento ("Péptidos", "Exosomes", "Muscle Cells", "*Thousand*"). Cortes disponibles: 400, 700, **800** (titulares grandes) y **Mencken Std Head itálica 400/800** (acentos itálicos).
3. **Poppins** — *tipografía de acentos y de sistema.* Jerarquía formal del manual:
   - **Título** → Poppins Regular
   - **Subtítulo** → Poppins Medium
   - **Cuerpo** → Poppins Medium (en piezas densas, Poppins Light 300)
   - **Párrafos a resaltar** → Poppins **Italic**
   - **Texto especial / botón** → Mencken Std Text
   Cortes: 300/400/500/700 + itálicas.

**Regla de oro tipográfica:** las tipografías de acento no compiten entre sí; cada una con un
propósito. Patrón firma de titular = palabra-acento en **Mencken itálico** (azul/crema/oro) +
resto en **Mencken bold** (blanco/navy).

---

## 3. Logo — jerarquía, variaciones y uso
Registro embebido: `../../assets/logos_brand.json` (17 logos recortados, base64).

**Jerarquía (manual 3.2):**
- **Principal** = wordmark apilado `LONGEVITY / CLINICAL / —INSTITUTE—`. Úsalo la mayor parte del tiempo (recordación), siempre que haya espacio. → claves `principal_*`.
- **Secundario** = variante para cuando el principal no cabe en el formato. → (apoyarse en `terciario_*` o el principal compacto).
- **Símbolo** = monograma `LCI` / sello circular. Para formatos pequeños: foto de perfil en redes, impresiones pequeñas. → claves `sello_*` (circular) / `terciario_*` (LCI + bajada).

**Color del logo según fondo:** fondo oscuro → `*_blanco` / `*_beige` / `principal_fondo_oscuro`. Fondo claro → `*_navy`. Acento de lujo → `*_gold` / `*_dorado`.

**Área de reserva (planimetría 3.3):** X = altura de la "C" de CLINIC. Reserva mínima **2X** alrededor (nada cruza esa zona: ni foto, ni textura, ni texto). Márgenes derivados: 2X lados/arriba.

**Tamaño mínimo (3.4):** impreso **2,0 cm** · digital **180 px** (lado mayor del logo).

**Marca personal (Dra. Carolina):** monograma `CR` y wordmark `Carolina Rodríguez, MD · Longevity Medicine`. Claves `cr_*`. Se usa cuando la Dra. lo pida (p. ej. materiales de sus pacientes). Es marca personal, no reemplaza a LCI: LCI es el default institucional.

---

## 4. Estilo fotográfico (manual 6.x)
- **Expresiones neutras:** rostros serenos, tranquilos. **Evitar sonrisas y expresiones fuertes.**
- **Iluminación bioluminiscente:** priorizar para transmitir tecnología/innovación. Azules eléctricos sobre negro.
- **Close-ups científicos:** neuronas, células, ADN, sistemas del cuerpo humano.
- **Categorías:** Producto (viales, kits, fondo claro+oro) · Lifestyle (cuerpo, gimnasio, B/N) · Tonos neutros (ondas de partículas, texturas).
- **Tratamiento → familia LCI** (`../../assets/lci_treat.py`): `tritone` (navy·gold·cream, para fotos con mucho texto) · `duo` (navy→cream) · `grade` (comida/producto). Toda foto bajo texto lleva velo navy para legibilidad.
- Textura firma disponible: `../../assets/papeleria/membrete_lci.png` (onda de partículas navy).

---

## 5. Contacto (dos sistemas)
- **Institucional (LCI):** `(+57) 301 512 39 91` · `carolina_md@longevityclinicalinstitute.com` · `@longevityclinicalinstitute` · `longevityclinicalinstitute.com`.
- **Personal (Dra. Carolina):** `(+57) 301 512 39 91` · `@longevitymedicaldoctor` · `longevitymedicaldoctor.com` (se ve en etiquetas de procedimiento/sueros de pacientes).

Pill de contacto = motivo de cierre obligado en piezas de redes (outline redondeado o relleno translúcido; WhatsApp + tel + IG + web).

---

## 6. Motivos visuales firma ("estilo Paola")
Catálogo completo con sus muestras en `../muestras-paola/`. Resumen de los recurrentes:
barra de **resaltado** translúcida (azul/oro/gris) detrás de una palabra · **caja de borde fino**
alrededor de la línea-acento · **conector** con nodos (vertical o en ángulo recto) → sub-lista ·
**viñetas ✦ doradas** · **lista ✓ dorada con subrayado** · **chips** de síntomas/keywords ·
**caja de borde dorado** para ofertas/CTA · **bloque de fecha** (oro tracked + reglas) ·
**bloque de ubicación** con pin · **panel de foto vertical** con marca de recorte "+" ·
**firma de email** y **carnet** (split/arco navy-blanco con foto circular).

Dos sub-paletas de fondo: **LCI navy** (institucional) y **azul eléctrico radial** (curso de
péptidos / sub-marca académica). El **morado** de una pieza antigua de ejercicio NO es de marca.

---

## 7. Inventario embebido (todo viaja dentro del skill)
- `assets/fonts_brand.json` — 13 cortes (Poppins 300–700 +it · Mencken Std 400/700/800 · Mencken Std Head it 400/800).
- `assets/logos_brand.json` — 17 logos (principal/sello/terciario ×colores + CR personal).
- `assets/papeleria/membrete_lci.png` — cabezote/textura navy.
- `assets/lci_treat.py` — pipeline de tratamiento de imagen.
- `references/muestras-paola/` — 34 piezas maestras aprobadas.
- `references/marca-oficial/BRANDBOOK_LONGEVITY_CLINICAL_INSTITUTE.pdf` — manual oficial (fuente).
- `references/marca-oficial/Hoja_Membrete_LCI.docx` — membrete editable original.
- `references/marca-oficial/brand_video_2026-06-07.mp4` — material audiovisual.
- `references/ejemplos-clinicos/` — plan nutricional de referencia.
