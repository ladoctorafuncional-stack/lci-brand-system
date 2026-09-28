# Ejemplo: comunicado/aviso a pacientes (reproduce story_something_important).
# Demuestra el nivel de marca con fondo de partículas real + composición densa.
import sys; sys.path.insert(0,'../../assets'); import marca as M

BG = M.bg_particulas('story')        # navy a sangre + onda de partículas (membrete)

wm = M.logo('principal','blanco', h=86)
head = (f'<div style="text-align:center;">'
  f'<div class="serif-it" style="font-size:46px;color:var(--blue);">I want to share</div>'
  f'<div style="margin:14px 0;">{M.caja("<span class=\'serif-it\' style=\'font-size:54px;color:var(--blue);\'>something important</span>")}</div>'
  f'<div>{M.caja("<span class=\'serif-it\' style=\'font-size:54px;color:var(--blue);\'>with you:</span>")}</div></div>')
body1 = ('<div class="body" style="text-align:center;color:#fff;font-size:31px;line-height:1.55;max-width:800px;margin:0 auto;">'
  'For some time now, I\'ve embarked on a new professional chapter, working independently and building a new space for you:</div>')
body2 = ('<div class="body" style="text-align:center;font-size:30px;line-height:1.55;max-width:820px;margin:0 auto;">'
  '<strong>In line with this, I want to clarify that I am no longer affiliated with any other brands or practices,</strong> '
  'and that all my care, treatments, and support are managed through my official channels and at this new location.</div>')

center = (f'<div>{head}</div><div style="margin-top:48px;">{body1}</div>'
  f'<div style="display:flex;justify-content:center;margin:54px 0;">{wm}</div><div>{body2}</div>')
inner = (f'<div style="margin-top:120px;">{center}</div>'
  f'<div style="margin-top:auto;display:flex;justify-content:center;">{M.pill(True,fill=True)}</div>')

html = M.lienzo('story', M.content(inner, pad='90px', justify='flex-start'),
                fondo=M.foto(BG, veil=None), theme='navy')
open('comunicado_aviso.html','w').write(html)
# render: python3 ../../scripts/render.py comunicado_aviso.html comunicado_aviso.png story 2
