# Changelog

## 1.1.0 — 2026-10-25
Variedad de soportes y acentos (pedido de la Dra.: el panel de vidrio a media pieza se repetía demasiado).
- `r_natural`: nuevos soportes de Paola `linea` (texto directo + línea con nodos y viñetas), `tarjeta` (tarjeta con filo, filete y viñetas) y `blur` (desenfoque local solo detrás del titular); parámetro `vinetas=`.
- `mitad` pasa a excepción: aviso al usarlo y tope de 1 de cada 4 piezas en `auditar_soportes`.
- Acento: `acc_col` deja de ser azul claro fijo (por defecto crema); nuevos `ACENTOS`, `auditar_acentos()` y `plan_variedad(n)`. Cada pieza lleva etiquetas `<!--SOPORTE-->` y `<!--ACENTO-->`.
- Texto directo sube a 84 px (antes 66) para cumplir la jerarquía F8 (titular ≥ 2.4 × subtítulo).
- `_navegador.py`: los auditores ya no fallan si el Chromium de Playwright no coincide; prueban `CHROMIUM_PATH`, `/opt/pw-browsers` y rutas habituales.
- SKILL.md: tabla de soportes de Paola y regla de rotación de acentos; ejemplo visual en `references/estandar-visual-2026/`.
- Verificado: 6 stories de prueba (6 soportes distintos, 6 acentos) pasan `auditar_pieza`, `auditar_fuentes`, `auditar_soportes` y `auditar_acentos`.
- Conocido, sin tocar: la cápsula de contacto casi no se ve sobre fotos muy claras (pasa el auditor).

## 1.0.0 — 2026-10-25
Consolidación: el repo pasa a ser la fuente única de marca.
- Nuevo `.claude-plugin/marketplace.json` con los plugins `lci-brand` y `lci-fotos`.
- `plugins/lci-brand`: `lci-design-system` y `lci-piezas-graficas` tomados de `lci-suite` v1.58.0 (versión vigente, oct-2026). Reemplazan las copias antiguas de `.claude/skills/`, que ahora son symlinks al plugin.
- `plugins/lci-fotos`: tomado de `lci-fotos` v1.8.0.
- Retiradas del plugin las 4 piezas con errores (`post_biologically40s_crema`, `post_lab_normal_gris`, `story_biologically40s_crema`, `story_lab_normal_gris`).
- Incorporada la regla de teléfono por idioma (EN `300 002 71 15` / ES `301 512 39 91`) vía MANUAL-LCI.md vigente.
- SKILL.md anterior de `lci-design-system` conservado en `references/legado-skill-repo-2026-10-25.md` para revisión.
- Pendiente: las skills clínicas de `lci-suite` (historia clínica, planes, tareas) NO se incluyen aquí; este repo es solo marca.
