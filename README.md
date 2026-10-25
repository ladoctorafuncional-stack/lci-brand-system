# LCI Brand System

Sistema de diseño de marca del **Longevity Clinical Institute (LCI)**.
Dra. Carolina Rodríguez Morales · Medellín, Colombia.

Repositorio hermano de `lci-clinical-scribe` (la app clínica). Aquí vive solo
marca: logos, fuentes, piezas de referencia, tokens y guidelines. La app
clínica sigue siendo la fuente de verdad para el motor de la consulta; este
repo es el kit reutilizable para cualquier pieza gráfica, documento o
integración externa (como Claude Design).

## Estructura

```
brand/
  logos/                          17 logos oficiales (PNG transparente)
  papeleria/                      membrete institucional
  fondos/                         38 fondos de marca en 9 familias (ver FONDOS.md)
  equipo/                         retratos y firmas de correo del equipo (ver EQUIPO.md)
  piezas-referencia/              30 piezas maestras de Paola Londoño (Ikigai)
  referencias-estilo/             35 referencias externas de layout/estilo (Pinterest)
  referencias-ilustracion-anatomica/  3 renders 3D de anatomía para animaciones
tokens/
  colors.css                      paleta institucional + semaforización
  typography.css                  Mencken Std + Poppins, @font-face -> fonts/
fonts/                            13 archivos de fuente reales (otf/ttf)
guidelines/                       manual de marca, catálogo de piezas, recetas de diseño
.claude-plugin/marketplace.json   marketplace: lci-brand + lci-fotos
plugins/
  lci-brand/skills/               lci-design-system (documentos HTML) · lci-piezas-graficas (piezas estilo Paola)
  lci-fotos/                      banco de fotos oficial
.claude/skills/                   symlinks a plugins/lci-brand/skills (carga directa en Claude Code)
VERSION · CHANGELOG.md · MIGRACION.md
```

**Fuente única:** los skills viven en `plugins/`. Ver `MIGRACION.md` para instalar en Cowork y actualizar Claude Design.

## Origen del material

Todo el contenido de `brand/logos/`, `fonts/`, `brand/piezas-referencia/` y
`guidelines/` viene decodificado o copiado directamente de las skills
`lci-design-system` y `lci-piezas-graficas`, que ya traían el kit de marca
embebido. Desde 1.0.0 los skills vigentes (lci-suite v1.58.0) viven en `plugins/lci-brand/`. No se inventó ni se resumió nada.

`brand/fondos/` viene de `Fondos-LCI-todas-las-opciones.zip`, copiado byte a
byte; solo se reorganizó por familia y se normalizaron los nombres (la
equivalencia con los nombres originales está en `brand/fondos/FONDOS.md`).

## Referencias externas — `brand/referencias-estilo/` y `referencias-ilustracion-anatomica/`

**No son piezas de LCI.** Son inspiración de layout guardada de Pinterest por
la Dra. Carolina: composición, tratamiento tipográfico y tono visual de otras
marcas (skincare, longevidad, suplementos, ciencia). Se usan como referencia
de estructura para generar piezas nuevas con la marca y los datos de LCI —
nunca se presentan como trabajo propio de LCI ni de Paola Londoño.

Las anatómicas (hombro, rodilla, tobillo) son renders 3D neutros para usar
como base de animaciones de anatomía/lesión en contenido para pacientes.

## Piezas excluidas del set de Paola

Cuatro piezas de la fuente original (`post_biologically40s_crema`,
`post_lab_normal_gris`, `story_biologically40s_crema`,
`story_lab_normal_gris`) tenían errores de diseño — no fueron hechas por
Paola — y se excluyeron tanto de `brand/piezas-referencia/` como de la copia
de la skill en este repo. La skill original en la cuenta no se modificó.

## Inventario completo

Ver `brand/ASSETS.md`.
