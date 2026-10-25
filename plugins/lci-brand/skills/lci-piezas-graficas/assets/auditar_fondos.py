"""Auditor de VARIEDAD DE FONDOS (la Dra., 10-oct-2026: «recuerda todas las opciones que tienes»).
Uso: python3 auditar_fondos.py build1.py [build2.py ...]
Cuenta cuántas veces se usa cada una de las 12 familias del catálogo de 38 fondos (lci-fotos → fondos/ + FONDOS.md)
y marca las que NO se han usado y las que se repiten de más. Correr ANTES de entregar cualquier tanda o feed."""
import sys, re
FAM = {
 '01-02 noche':            r"(gradiente|GR)\('noche",
 '03 acero':               r"(gradiente|GR)\('acero",
 '04-05 aurora':           r"(gradiente|GR)\('aurora",
 '06-07 niebla clara':     r"(gradiente|GR)\('niebla",
 'cielo / cielo_crema':    r"gradiente\('cielo",
 '08-10 ondas':            r"ondas\(",
 '11 bacterias':           r"bacterias\(",
 '12 bokeh':               r"bokeh\(",
 '13-15 galaxias':         r"galaxia\(|FXB\('galaxia",
 '16-18 mallas':           r"malla\(|FXB\('malla",
 '19-26 mesh gradient':    r"mesh\(|FXB\('mesh",
 '27-33 foto tratada':     r"tratar\(|M\.foto\(",
 '34-36 vidrio estriado':  r"R\.vidrio\(|[^a-zA-Z_]VD\(",
 '37-38 movimiento':       r"movimiento\(",
 'lámina tipo ducha':      r"columna_(izq|der)",
}
txt = '\n'.join(dict.fromkeys(l.strip() for f in sys.argv[1:] for l in open(f).read().split('\n') if not l.lstrip().startswith(('def ','return ','"""','#')) and '_fx.' not in l))   # sin duplicados (versiones EN/ES y copias de corrección cuentan una vez)
tot = 0; res = {}
for k, p in FAM.items():
    n = len(re.findall(p, txt)); res[k] = n; tot += n
for k, n in res.items():
    flag = '  ← SIN USAR: incluirlo en la próxima tanda' if n == 0 else ('  ← DEMASIADO: cambiar algunas' if (k != '27-33 foto tratada' and n > max(4, tot*0.12)) or (k == 'lámina tipo ducha' and n > 3) else '')
    print(f'{k:24s} {n:3d}{flag}')
