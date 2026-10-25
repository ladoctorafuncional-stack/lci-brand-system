# Migración a fuente única (LCI)

Regla: **todo cambio de marca se edita en este repo.** Cowork y Claude Design se actualizan desde aquí; no se editan directamente.

## Cowork / Claude Code
1. Añadir el marketplace: `ladoctorafuncional-stack/lci-brand-system`.
2. Instalar `lci-brand` y `lci-fotos`.
3. Desinstalar los plugins "My Uploads": `lci-fotos` (antiguo) y, cuando se decida, `lci-suite`.
   Mientras `lci-suite` siga instalado, contiene copias de `lci-design-system` y `lci-piezas-graficas` con el mismo nombre → riesgo de duplicado. Las skills clínicas (historia, planes, tareas) dependen de `lci-design-system`, así que `lci-brand` debe quedar instalado junto a ellas.
4. Quitar skills sueltas con el mismo nombre.

## Claude Design
Re-importar el repo después de cada versión nueva (`VERSION`).

## Publicar un cambio
1. Editar en `plugins/lci-brand/skills/...` o `brand/`.
2. Subir `version` en `plugins/*/.claude-plugin/plugin.json`, `VERSION` y `CHANGELOG.md`.
3. Merge a `main` → actualizar plugin en Cowork → re-importar en Claude Design.
