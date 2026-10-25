"""Lanzador de Chromium robusto para los auditores y el render de piezas.
Probar primero el Chromium que trae Playwright; si no existe (versión de Playwright ≠ navegador instalado), usar el
ejecutable que haya en el equipo. Orden: variable CHROMIUM_PATH · /opt/pw-browsers · rutas habituales de Linux/macOS.
Uso:  b = await lanzar(p)   (p = el objeto de async_playwright())."""
import os, glob

def _candidatos():
    c = [os.environ.get('CHROMIUM_PATH')]
    for base in (os.environ.get('PLAYWRIGHT_BROWSERS_PATH'), '/opt/pw-browsers', os.path.expanduser('~/.cache/ms-playwright')):
        if base:
            c += sorted(glob.glob(os.path.join(base, 'chromium-*', 'chrome-linux*', 'chrome')), reverse=True)
            c += sorted(glob.glob(os.path.join(base, 'chromium_headless_shell-*', 'chrome-headless-shell-linux*', 'chrome-headless-shell')), reverse=True)
    c += ['/usr/bin/chromium', '/usr/bin/chromium-browser', '/usr/bin/google-chrome',
          '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome']
    return [x for x in c if x and os.path.exists(x)]

async def lanzar(p):
    try:
        return await p.chromium.launch()
    except Exception as e:
        for exe in _candidatos():
            try:
                return await p.chromium.launch(executable_path=exe)
            except Exception:
                continue
        raise RuntimeError(f'No se pudo abrir Chromium ({e}). Define CHROMIUM_PATH con la ruta del ejecutable.')
