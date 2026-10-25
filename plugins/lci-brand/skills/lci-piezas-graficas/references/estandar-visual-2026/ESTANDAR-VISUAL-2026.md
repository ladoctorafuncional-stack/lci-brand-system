# ESTÁNDAR VISUAL LCI 2026 — el piso de calidad (aprobado por la Dra. Carolina, oct 2026)

> **Regla dura.** Este feed de 42 publicaciones (137 piezas) es el NIVEL MÍNIMO que debe igualar o superar
> TODO lo que se produzca para LCI de aquí en adelante: piezas de redes, carruseles, stories, flyers,
> brochures, handouts, planes, reportes y presentaciones. La Dra. lo dijo textual: *"que deje de estarme
> dando lo mismo plano de siempre en los documentos"*. Entregar algo más plano que esto = entrega rechazada.

- `grid_feed_EN_2026.jpg` — la cuadrícula completa del perfil (fijadas arriba, luego de la más nueva a la más antigua).
- `posts/NN-slug.jpg` — cada publicación con TODAS sus slides en fila (para ver portada + interiores + ritmo).
- Las piezas a resolución completa viven en el entregable `LCI_feed_42` (Descargas → export → feed-42).

**Antes de diseñar cualquier cosa de LCI: abrir `grid_feed_EN_2026.jpg` y 3–4 `posts/` del tipo más parecido
(Read sobre las imágenes) y fijar el nivel con los ojos, no de memoria.**

- `CATALOGO-EFECTOS.jpg` — cada tratamiento/efecto aplicado a la misma foto, con su llamada de código.
- Fotos originales: plugin `lci-fotos` → skill `lci-banco-fotos`.

## 1. Qué hace que este feed NO sea plano (el ADN a replicar)
1. **Toda imagen lleva tratamiento de marca** — nunca foto cruda. `R.tratar(path, modo)`:
   `bw` (B/N alto contraste, negros profundos) · `azul` (duotono navy→acero) · `frio` (clínica desaturada fría) ·
   `calido` (velo café de Paola, oscuro del lado del texto) · `ambar` (sepia «Schedule») · `claro` (alta clave azul
   pálido «Exosomes») · `natural` (SOLO tour real de la clínica). Recorte de detalle (`crop`) para que la foto
   trabaje como textura y deje zona limpia para el texto.
2. **Efectos de superficie** (reutilizan una misma foto con otra lectura; ninguno es «filtro de app»):
   - `R.vidrio(path, tinte, w=, h=)` — vidrio estriado/reeded glass (canales verticales que refractan).
   - `R.movimiento(path, tinte)` — barrido + doble exposición (familia «Reclaim blur»).
   - `R.gradiente('noche'|'acero'|'aurora'|'niebla', seed, w, h)` — malla difusa con grano, solo colores de marca.
   - `R.ondas(nivel, calor, w, h)` — ondas 3D estriadas con destello gold en la cresta.
   - `R.bacterias(w, h)` — microscopía generada con profundidad de campo.
   - `R.bokeh()` — SOLO interiores / Word of the Day; **nunca en portadas** («parece navidad»).
   - Velos: `VEIL_NAVY`, `VEIL_CAFE` y velo lateral más oscuro donde va el texto.
3. **Tipografía editorial con jerarquía recta/cursiva**: Mencken bold + acento Mencken Head itálico (800 sobre oscuro,
   400+trazo sobre claro), eyebrow Poppins ligero, cuerpo Poppins 300. Titulares GRANDES; el texto de apoyo pequeño.
4. **Objetos gráficos con volumen**: caja de acento traslúcida, marco de filete fino, conector de nodos, cápsula
   (`pildora`) en línea, tarjetas de datos de vidrio, círculos problema/solución, órbitas, red de nodos, nodo
   luminoso, cifras gigantes (`r_cifra_titular`, `r_cifras`), ficha de artículo científico (`r_articulo`).
5. **Variación y ritmo**: nunca dos seguidas con la misma receta, tratamiento ni logo; ≥1 de cada 3 sin foto;
   portadas con foto, interiores reciclan la foto con otro efecto; estilos repartidos homogéneamente.
6. **Constantes de marca**: paleta (navy #2A3649, light blue #CAD3DD, gold #D2B58A — mínimo, cream #EDE5DA,
   azul medio #5D768C, acero #9FB2C6), solo Poppins + Mencken (auditar), cápsula de contacto, márgenes 7.5% W,
   logo en zona de contraste, teléfono por idioma (EN 300 002 71 15 · ES 301 512 39 91).
7. **Evidencia**: dato clínico con referencia Vancouver [n] en la pieza y en el copy, verificada en PubMed.

## 2. Catálogo de las 42 publicaciones (receta · efectos)
| # | Publicación | Slides | Recetas y efectos | Archivo |
|---|---|---|---|---|
| 01 | who-we-are | 6 | r_centrado · r_derecha · r_marco · r_poster · r_claro · r_titulo_arriba (calido, azul, azul+blur, calido+VEIL_CAFE, claro, ambar) | `posts/01-who-we-are.jpg` |
| 02 | reclaim-the-energy | 3 | Paola original (t_poster «Reclaim»): foto B/N/low-key + caja de acento + conector de nodos | `posts/02-reclaim-the-energy.jpg` |
| 03 | meet-the-founder | 5 | r_retrato · r_derecha · r_poster · r_centrado · r_titulo_arriba — efectos: brain_b:azul, cons:calido, lab:frio, mri:azul, p_sit:calido | `posts/03-meet-the-founder.jpg` |
| 04 | word-healthspan | 1 | r_palabra — efectos: n_juiceg:natural | `posts/04-word-healthspan.jpg` |
| 05 | we-measure | 6 | r_eyebrow_gigante · r_centrado · r_marco · r_derecha · r_claro · r_titulo_arriba — efectos: brain_w:claro, chair:calido, edan:azul, mri:bw, ther:bw, vidrio | `posts/05-we-measure.jpg` |
| 06 | the-brain-ages-too | 1 | Paola original: cerebro sobre navy, «ages too.» Mencken it 800 | `posts/06-the-brain-ages-too.jpg` |
| 07 | thyroid-tsh | 3 | r_ondas · r_circulos · r_centrado — efectos: ondas | `posts/07-thyroid-tsh.jpg` |
| 08 | inside-lci | 5 | r_natural — efectos: coffee:natural, cons:natural, meas_w:natural, recep:natural, ther:natural | `posts/08-inside-lci.jpg` |
| 09 | evidence-waist-vs-bmi | 6 | r_eyebrow_gigante · r_claro · r_articulo · r_centrado · r_marco · r_poster — efectos: desk:natural, gradiente, inbody:azul, meas_dna:azul | `posts/09-evidence-waist-vs-bmi.jpg` |
| 10 | lpa-measure-once | 5 | r_claro · r_centrado · r_articulo · r_circulos · r_titulo_arriba — efectos: gradiente, lab:claro, vidrio | `posts/10-lpa-measure-once.jpg` |
| 11 | thousand-supplements | 1 | Paola original «Thousand supplements»: foto cálida low-key, estrella crema | `posts/11-thousand-supplements.jpg` |
| 12 | not-just-tired | 4 | r_icono · r_derecha · r_circulos · r_titulo_arriba — efectos: gradiente, vidrio | `posts/12-not-just-tired.jpg` |
| 13 | patient-journey | 6 | r_centrado · r_paso — efectos: brain_h:claro, chair:ambar, gradiente, inbody:azul, meas_dna:frio, n_cons:frio | `posts/13-patient-journey.jpg` |
| 14 | evidence-antioxidants | 6 | r_poster · r_marco · r_articulo · r_centrado · r_claro · r_derecha — efectos: bokeh, coffee:azul, cons:azul, desk:claro, meas_w:calido, vidrio | `posts/14-evidence-antioxidants.jpg` |
| 15 | gut-microbiota | 3 | r_tarjeta_micro · r_cifras · r_titulo_arriba — efectos: bacterias, vidrio | `posts/15-gut-microbiota.jpg` |
| 16 | muscle-cells | 1 | Paola original (t_timeline «Muscle Cells»): gotas de nivel justificadas al titular | `posts/16-muscle-cells.jpg` |
| 17 | functional-with-rigor | 4 | r_poster · r_derecha · r_marco · r_centrado — efectos: equip:bw, gradiente, hall:frio, meas_w:bw | `posts/17-functional-with-rigor.jpg` |
| 18 | one-measurement | 1 | r_nodo_luz — efectos: coffee:frio | `posts/18-one-measurement.jpg` |
| 19 | visit-medellin | 5 | r_titulo_arriba · r_poster · r_derecha · r_claro · r_natural — efectos: chair:natural, desk:calido, hall:azul, night:calido, recep:claro | `posts/19-visit-medellin.jpg` |
| 20 | evidence-vo2max | 6 | r_eyebrow_gigante · r_claro · r_articulo · r_centrado · r_derecha · r_titulo_arriba — efectos: face:bw, gradiente, inbody:ambar, meas_w:azul, movimiento | `posts/20-evidence-vo2max.jpg` |
| 21 | founder-quote | 1 | r_cita — efectos: vidrio | `posts/21-founder-quote.jpg` |
| 22 | exosomes | 1 | Paola original (t_concepto_hero «Exosomes»): alta clave azul pálido | `posts/22-exosomes.jpg` |
| 23 | social-jet-lag | 5 | r_derecha · r_claro · r_articulo · r_paso · r_titulo_arriba — efectos: g_sofa:azul, gradiente, vidrio | `posts/23-social-jet-lag.jpg` |
| 24 | word-inflammaging | 2 | r_palabra · r_red — efectos: gradiente | `posts/24-word-inflammaging.jpg` |
| 25 | your-body-knows | 1 | Paola original (t_seal_hero «Your body knows how to heal») | `posts/25-your-body-knows.jpg` |
| 26 | evidence-sleep-regularity | 6 | r_centrado · r_derecha · r_articulo · r_paso · r_poster — efectos: cons:calido, gradiente, recep:claro, ther:azul, vidrio | `posts/26-evidence-sleep-regularity.jpg` |
| 27 | grip-strength | 3 | r_dato · r_articulo · r_paso — efectos: gradiente, movimiento, vidrio | `posts/27-grip-strength.jpg` |
| 28 | 4p-medicine | 3 | r_titulo_arriba · r_orbitas · r_centrado — efectos: gradiente, n_doc:calido, vidrio | `posts/28-4p-medicine.jpg` |
| 29 | healthspan | 6 | r_eyebrow_gigante · r_claro · r_centrado · r_derecha · r_marco · r_titulo_arriba — efectos: brain_b:bw, brain_w:claro, cons:ambar, gradiente, night:azul, vidrio | `posts/29-healthspan.jpg` |
| 30 | apob | 4 | r_tarjeta_datos · r_claro · r_articulo · r_titulo_arriba — efectos: gradiente, ph_edan:frio, vidrio | `posts/30-apob.jpg` |
| 31 | reel-cover-why-i-founded | 1 | r_titulo_arriba — efectos: p_sit:bw | `posts/31-reel-cover-why-i-founded.jpg` |
| 32 | measured-not-assumed | 3 | r_poster · r_red · r_cifras — efectos: gradiente, oxi:azul, vidrio | `posts/32-measured-not-assumed.jpg` |
| 33 | word-sarcopenia | 2 | r_palabra · r_centrado — efectos: gradiente, n_mus:bw | `posts/33-word-sarcopenia.jpg` |
| 34 | schedule-assessment | 1 | Paola original «Schedule»: foto cálida con velo café | `posts/34-schedule-assessment.jpg` |
| 35 | brainspan | 1 | r_claro — efectos: brain_l:claro | `posts/35-brainspan.jpg` |
| 36 | daily-steps | 3 | r_cifras · r_articulo · r_paso — efectos: gradiente, vidrio | `posts/36-daily-steps.jpg` |
| 37 | biological-age | 1 | r_derecha — efectos: n_age:azul | `posts/37-biological-age.jpg` |
| 38 | longevity-journey | 3 | r_centrado · r_orbitas — efectos: gradiente, n_check:calido, vidrio | `posts/38-longevity-journey.jpg` |
| 39 | treat-the-person | 1 | r_marco — efectos: ibdisp:azul | `posts/39-treat-the-person.jpg` |
| 40 | welcome-to-lci | 3 | r_poster · r_natural — efectos: cons:frio, hall:calido, vidrio | `posts/40-welcome-to-lci.jpg` |
| 41 | testosterone | 4 | r_cifra_titular · r_articulo · r_circulos · r_titulo_arriba — efectos: gradiente, n_rope:bw, vidrio | `posts/41-testosterone.jpg` |
| 42 | insulin-1921 | 4 | r_eyebrow_gigante · r_centrado · r_derecha · r_titulo_arriba — efectos: gradiente, vidrio, vlab:calido | `posts/42-insulin-1921.jpg` |

## 3. Checklist «¿está al nivel?» (pasar ANTES de entregar — piezas Y documentos)
- [ ] ¿Cada foto tiene tratamiento de marca y recorte con intención? (ninguna cruda, ninguna repetida en portadas)
- [ ] ¿Hay al menos un efecto de superficie (vidrio, gradiente, ondas, movimiento, microscopía) donde antes habría un fondo plano?
- [ ] ¿El titular tiene jerarquía recta/cursiva Mencken y escala editorial (no tamaño «de Word»)?
- [ ] ¿Hay objetos gráficos con volumen (cápsula, marco, conector, tarjeta de vidrio, cifra gigante) y no solo texto + íconos?
- [ ] ¿Se alternan fondos oscuros, claros y foto? ¿El ojo descansa entre bloques (aire amplio entre, apretado dentro)?
- [ ] ¿Las barras/cajas de resaltado abrazan el texto (sin aire vertical, `M.barra`)? ¿Ningún descendente toca la barra?
- [ ] ¿Solo Poppins/Mencken (auditoría OK), solo paleta de marca, oro ≤2 veces por vista?
- [ ] Puesto al lado del grid de referencia, ¿se ve de la MISMA familia y al mismo nivel o mejor? Si no, rehacer.
