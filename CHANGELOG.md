# Changelog

## 1.0.0 — 2026-10-25
Consolidación: el repo pasa a ser la fuente única de marca.
- Nuevo `.claude-plugin/marketplace.json` con los plugins `lci-brand` y `lci-fotos`.
- `plugins/lci-brand`: `lci-design-system` y `lci-piezas-graficas` tomados de `lci-suite` v1.58.0 (versión vigente, oct-2026). Reemplazan las copias antiguas de `.claude/skills/`, que ahora son symlinks al plugin.
- `plugins/lci-fotos`: tomado de `lci-fotos` v1.8.0.
- Retiradas del plugin las 4 piezas con errores (`post_biologically40s_crema`, `post_lab_normal_gris`, `story_biologically40s_crema`, `story_lab_normal_gris`).
- Incorporada la regla de teléfono por idioma (EN `300 002 71 15` / ES `301 512 39 91`) vía MANUAL-LCI.md vigente.
- SKILL.md anterior de `lci-design-system` conservado en `references/legado-skill-repo-2026-10-25.md` para revisión.
- Pendiente: las skills clínicas de `lci-suite` (historia clínica, planes, tareas) NO se incluyen aquí; este repo es solo marca.
