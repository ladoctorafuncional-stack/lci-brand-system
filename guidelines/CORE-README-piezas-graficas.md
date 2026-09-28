# lci-piezas-graficas — CORE (versión liviana < 30 MB para subir al chat)

Motor 100% funcional. Para mantener el peso bajo el límite de subida de Claude (30 MB) se dejó
FUERA el material pesado de referencia, que vive en tu Drive como "maestro":
- `references/marca-oficial/`: brandbook PDF + videos + Hoja_Membrete.docx
- `references/stock/`: fotos en ALTA (Pexels) + video  → aquí solo queda el CATÁLOGO
  (`MANIFIESTO-STOCK.md` + `LCI_biblioteca_stock.png`). Cuando vayas a tratar una foto para
  una pieza final, **súbela suelta al chat** (1 archivo < 30 MB) y se trata con `lci_treat.py`.
- `references/muestras-paola/`: reducidas a 1500px (referencia de estilo; las de alta están en el maestro).
- `assets/fonts|logos` crudos, `img-library`, `assets.json`: redundantes (el motor usa los JSON base64).

Todo lo necesario para generar piezas (motor, fuentes, logos, membrete, biblia, muestras, catálogo) está aquí.
