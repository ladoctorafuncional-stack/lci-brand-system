#!/usr/bin/env python3
"""
generate_muscle_svg.py
Genera SVGs de mapas musculares (vista frontal y posterior) con grupos musculares resaltados.
Usado por el skill plan-deportivo para ilustrar ejercicios por día.

Uso:
    python generate_muscle_svg.py --muscles pecho,cuadriceps,deltoides --view front --output chest_day.svg
    python generate_muscle_svg.py --muscles espalda,gluteos,isquiotibiales --view back --output back_day.svg
    python generate_muscle_svg.py --muscles pecho,espalda --view both --output fullbody.svg
    python generate_muscle_svg.py --inbody '{"trunk_muscle":93.9,"legs_muscle":84.8,"arms_muscle":90.2}' --view both --output priorities.svg

Grupos musculares soportados (español e inglés):
  FRONT: pecho/chest, deltoides_ant/front_delts, biceps, abdominales/abs, oblicuos/obliques,
         cuadriceps/quads, aductores/adductors, tibial/shins
  BACK:  trapecio/traps, deltoides_post/rear_delts, espalda/back, triceps, lumbar/lower_back,
         gluteos/glutes, isquiotibiales/hamstrings, pantorrillas/calves
  BOTH:  core (abs+lumbar), hombros/shoulders (front+rear delts)
"""

import argparse
import json
import sys
import base64

# Brand colors
NAVY = "#2d3641"
GOLD = "#c7b39a"
GOLD_DARK = "#a08060"
CREAM = "#f9f3ec"
BEIGE = "#e5dcc8"
HIGHLIGHT = "#c7b39a"       # gold - primary muscle highlight
HIGHLIGHT_STRONG = "#a08060" # dark gold - priority zone
BODY_FILL = "#e8e0d4"       # neutral body tone
BODY_STROKE = "#2d3641"     # navy outline
INACTIVE = "#ddd5c8"        # muted beige for inactive muscles

# ── Muscle group SVG paths ──────────────────────────────────────────
# Coordinates based on a 200x440 viewBox (front) and 200x440 (back)

FRONT_PATHS = {
    "pecho": {
        "path": "M72,108 Q80,100 100,98 Q120,100 128,108 Q130,118 125,125 Q112,130 100,132 Q88,130 75,125 Q70,118 72,108Z",
        "label": "Pectoral",
        "cx": 100, "cy": 115
    },
    "deltoides_ant": {
        "path": "M58,95 Q55,88 60,82 Q67,80 72,85 Q74,95 72,108 Q65,105 58,100Z M142,95 Q145,88 140,82 Q133,80 128,85 Q126,95 128,108 Q135,105 142,100Z",
        "label": "Deltoides",
        "cx": 100, "cy": 88
    },
    "biceps": {
        "path": "M55,110 Q50,108 48,115 Q46,130 48,148 Q50,155 55,152 Q58,140 58,125 Q58,115 55,110Z M145,110 Q150,108 152,115 Q154,130 152,148 Q150,155 145,152 Q142,140 142,125 Q142,115 145,110Z",
        "label": "Bíceps",
        "cx": 100, "cy": 132
    },
    "abdominales": {
        "path": "M82,135 Q80,145 80,165 Q80,185 82,200 Q90,205 100,206 Q110,205 118,200 Q120,185 120,165 Q120,145 118,135 Q110,132 100,132 Q90,132 82,135Z",
        "label": "Abdominales",
        "cx": 100, "cy": 168
    },
    "oblicuos": {
        "path": "M70,130 Q72,135 75,150 Q76,165 75,180 Q74,190 72,195 Q68,185 66,170 Q65,155 66,140 Q67,132 70,130Z M130,130 Q128,135 125,150 Q124,165 125,180 Q126,190 128,195 Q132,185 134,170 Q135,155 134,140 Q133,132 130,130Z",
        "label": "Oblicuos",
        "cx": 100, "cy": 162
    },
    "cuadriceps": {
        "path": "M72,215 Q70,210 72,225 Q74,250 76,275 Q78,295 80,310 Q85,315 92,312 Q95,300 94,280 Q92,255 90,235 Q88,218 85,212 Q78,210 72,215Z M128,215 Q130,210 128,225 Q126,250 124,275 Q122,295 120,310 Q115,315 108,312 Q105,300 106,280 Q108,255 110,235 Q112,218 115,212 Q122,210 128,215Z",
        "label": "Cuádriceps",
        "cx": 100, "cy": 262
    },
    "aductores": {
        "path": "M88,215 Q92,220 95,235 Q98,250 100,260 Q102,250 105,235 Q108,220 112,215 Q108,212 100,210 Q92,212 88,215Z",
        "label": "Aductores",
        "cx": 100, "cy": 235
    },
    "tibial": {
        "path": "M78,320 Q76,335 76,355 Q76,375 78,390 Q82,395 86,390 Q87,375 86,355 Q85,335 83,320Z M122,320 Q124,335 124,355 Q124,375 122,390 Q118,395 114,390 Q113,375 114,355 Q115,335 117,320Z",
        "label": "Tibial anterior",
        "cx": 100, "cy": 355
    },
    "antebrazo_front": {
        "path": "M44,155 Q42,165 40,180 Q39,195 40,205 Q44,210 48,205 Q49,192 49,178 Q49,165 47,155Z M156,155 Q158,165 160,180 Q161,195 160,205 Q156,210 152,205 Q151,192 151,178 Q151,165 153,155Z",
        "label": "Antebrazo",
        "cx": 100, "cy": 180
    }
}

BACK_PATHS = {
    "trapecio": {
        "path": "M80,80 Q85,75 100,72 Q115,75 120,80 Q125,90 122,98 Q112,100 100,100 Q88,100 78,98 Q75,90 80,80Z",
        "label": "Trapecio",
        "cx": 100, "cy": 88
    },
    "deltoides_post": {
        "path": "M58,95 Q55,88 60,82 Q67,80 72,85 Q74,95 72,105 Q65,102 58,98Z M142,95 Q145,88 140,82 Q133,80 128,85 Q126,95 128,105 Q135,102 142,98Z",
        "label": "Deltoides post.",
        "cx": 100, "cy": 88
    },
    "espalda": {
        "path": "M72,105 Q75,100 82,98 Q90,100 95,108 Q98,120 96,135 Q92,145 85,148 Q78,145 74,135 Q72,125 72,115Z M128,105 Q125,100 118,98 Q110,100 105,108 Q102,120 104,135 Q108,145 115,148 Q122,145 126,135 Q128,125 128,115Z",
        "label": "Dorsal / Espalda",
        "cx": 100, "cy": 122
    },
    "triceps": {
        "path": "M55,108 Q50,106 48,115 Q46,130 47,148 Q48,155 53,152 Q56,140 56,128 Q56,118 55,108Z M145,108 Q150,106 152,115 Q154,130 153,148 Q152,155 147,152 Q144,140 144,128 Q144,118 145,108Z",
        "label": "Tríceps",
        "cx": 100, "cy": 130
    },
    "lumbar": {
        "path": "M78,150 Q82,148 90,150 Q95,155 100,160 Q105,155 110,150 Q118,148 122,150 Q125,160 124,175 Q122,188 118,195 Q110,198 100,200 Q90,198 82,195 Q78,188 76,175 Q75,160 78,150Z",
        "label": "Lumbar",
        "cx": 100, "cy": 175
    },
    "gluteos": {
        "path": "M72,200 Q70,195 72,208 Q76,222 82,230 Q90,235 100,236 Q110,235 118,230 Q124,222 128,208 Q130,195 128,200 Q125,198 118,200 Q110,205 100,206 Q90,205 82,200 Q75,198 72,200Z",
        "label": "Glúteos",
        "cx": 100, "cy": 218
    },
    "isquiotibiales": {
        "path": "M72,238 Q70,245 72,260 Q74,280 76,298 Q78,310 82,315 Q88,312 90,300 Q90,280 88,260 Q86,245 84,238Z M128,238 Q130,245 128,260 Q126,280 124,298 Q122,310 118,315 Q112,312 110,300 Q110,280 112,260 Q114,245 116,238Z",
        "label": "Isquiotibiales",
        "cx": 100, "cy": 275
    },
    "pantorrillas": {
        "path": "M76,318 Q74,330 74,348 Q75,365 78,378 Q82,385 88,380 Q90,368 89,350 Q88,335 85,322 Q82,316 76,318Z M124,318 Q126,330 126,348 Q125,365 122,378 Q118,385 112,380 Q110,368 111,350 Q112,335 115,322 Q118,316 124,318Z",
        "label": "Pantorrillas",
        "cx": 100, "cy": 350
    },
    "antebrazo_back": {
        "path": "M44,155 Q42,165 40,180 Q39,195 40,205 Q44,208 48,205 Q49,192 49,178 Q49,165 47,155Z M156,155 Q158,165 160,180 Q161,195 160,205 Q156,208 152,205 Q151,192 151,178 Q151,165 153,155Z",
        "label": "Antebrazo",
        "cx": 100, "cy": 180
    }
}

# Body outline paths
FRONT_BODY_OUTLINE = """
M100,20
Q108,20 112,28 Q115,35 115,45 Q114,55 112,60
Q120,62 130,68 Q140,72 148,76 Q155,80 158,88
Q162,98 160,110 Q158,120 155,130 Q152,140 150,155
Q148,168 146,180 Q144,195 142,210 Q140,218 136,222
Q132,218 128,215
Q130,225 128,240 Q126,260 124,280 Q122,300 120,315
Q118,330 118,345 Q118,360 118,375 Q118,390 118,400
Q118,410 115,418 Q112,422 108,425 Q104,428 100,430
Q96,428 92,425 Q88,422 85,418 Q82,410 82,400
Q82,390 82,375 Q82,360 82,345 Q82,330 80,315
Q78,300 76,280 Q74,260 72,240 Q70,225 72,215
Q68,218 64,222 Q60,218 58,210
Q56,195 54,180 Q52,168 50,155
Q48,140 45,130 Q42,120 40,110
Q38,98 42,88 Q45,80 52,76
Q60,72 70,68 Q80,62 88,60
Q86,55 85,45 Q85,35 88,28
Q92,20 100,20Z
"""

BACK_BODY_OUTLINE = FRONT_BODY_OUTLINE  # Same silhouette, different muscle overlays

# Alias mapping (Spanish → canonical key)
ALIASES = {
    # Front
    "chest": "pecho", "pectoral": "pecho", "pectorales": "pecho",
    "front_delts": "deltoides_ant", "deltoides_anterior": "deltoides_ant",
    "bicep": "biceps", "bíceps": "biceps",
    "abs": "abdominales", "core_front": "abdominales", "abdomen": "abdominales",
    "obliques": "oblicuos",
    "quads": "cuadriceps", "cuádriceps": "cuadriceps", "quadriceps": "cuadriceps",
    "adductors": "aductores", "aductor": "aductores",
    "shins": "tibial", "tibial_anterior": "tibial",
    "forearm_front": "antebrazo_front", "antebrazo": "antebrazo_front",
    # Back
    "traps": "trapecio", "trapecios": "trapecio",
    "rear_delts": "deltoides_post", "deltoides_posterior": "deltoides_post",
    "back": "espalda", "dorsal": "espalda", "dorsales": "espalda", "lats": "espalda", "latissimus": "espalda",
    "tricep": "triceps", "tríceps": "triceps",
    "lower_back": "lumbar", "erector": "lumbar", "erectores": "lumbar",
    "glutes": "gluteos", "glúteos": "gluteos", "gluteo": "gluteos",
    "hamstrings": "isquiotibiales", "hamstring": "isquiotibiales", "femoral": "isquiotibiales",
    "calves": "pantorrillas", "calf": "pantorrillas", "gastrocnemio": "pantorrillas", "soleo": "pantorrillas",
    "forearm_back": "antebrazo_back",
    # Composite
    "core": ["abdominales", "lumbar", "oblicuos"],
    "hombros": ["deltoides_ant", "deltoides_post"],
    "shoulders": ["deltoides_ant", "deltoides_post"],
    "deltoides": ["deltoides_ant", "deltoides_post"],
    "piernas": ["cuadriceps", "isquiotibiales", "gluteos", "pantorrillas", "aductores"],
    "legs": ["cuadriceps", "isquiotibiales", "gluteos", "pantorrillas", "aductores"],
    "tren_superior": ["pecho", "espalda", "deltoides_ant", "deltoides_post", "biceps", "triceps"],
    "upper_body": ["pecho", "espalda", "deltoides_ant", "deltoides_post", "biceps", "triceps"],
    "tren_inferior": ["cuadriceps", "isquiotibiales", "gluteos", "pantorrillas", "aductores"],
    "lower_body": ["cuadriceps", "isquiotibiales", "gluteos", "pantorrillas", "aductores"],
    "antebrazo_both": ["antebrazo_front", "antebrazo_back"],
    "antebrazos": ["antebrazo_front", "antebrazo_back"],
}


def resolve_muscles(muscle_list):
    """Resolve aliases and composites to canonical muscle keys."""
    resolved = set()
    for m in muscle_list:
        m = m.strip().lower().replace(" ", "_")
        if m in ALIASES:
            val = ALIASES[m]
            if isinstance(val, list):
                resolved.update(val)
            else:
                resolved.add(val)
        elif m in FRONT_PATHS or m in BACK_PATHS:
            resolved.add(m)
        else:
            print(f"⚠ Muscle group not recognized: {m}", file=sys.stderr)
    return resolved


def generate_svg(muscles_active, view="front", priority_muscles=None, title=None, width=200, height=440):
    """Generate SVG for a single view (front or back)."""
    if priority_muscles is None:
        priority_muscles = set()

    paths_dict = FRONT_PATHS if view == "front" else BACK_PATHS
    view_label = "ANTERIOR" if view == "front" else "POSTERIOR"

    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
                     f'width="{width}" height="{height}" style="font-family:Poppins,sans-serif;">')

    # Background
    svg_parts.append(f'<rect width="{width}" height="{height}" fill="none"/>')

    # Body silhouette (base)
    outline = FRONT_BODY_OUTLINE if view == "front" else BACK_BODY_OUTLINE
    svg_parts.append(f'<path d="{outline.strip()}" fill="{BODY_FILL}" stroke="{BODY_STROKE}" '
                     f'stroke-width="1.2" stroke-linejoin="round"/>')

    # Draw muscle groups
    for key, data in paths_dict.items():
        is_active = key in muscles_active
        is_priority = key in priority_muscles

        if is_active and is_priority:
            fill = HIGHLIGHT_STRONG
            opacity = "0.85"
        elif is_active:
            fill = HIGHLIGHT
            opacity = "0.75"
        else:
            fill = INACTIVE
            opacity = "0.25"

        svg_parts.append(f'<path d="{data["path"]}" fill="{fill}" opacity="{opacity}" '
                         f'stroke="{NAVY}" stroke-width="0.5"/>')

    # Labels for active muscles
    for key, data in paths_dict.items():
        if key in muscles_active:
            is_priority = key in priority_muscles
            font_weight = "600" if is_priority else "400"
            font_size = "6.5" if is_priority else "6"
            color = NAVY
            # Add label with background
            label = data["label"]
            cx, cy = data["cx"], data["cy"]

    # View label at bottom
    svg_parts.append(f'<text x="100" y="435" text-anchor="middle" '
                     f'font-size="7" font-weight="600" fill="{NAVY}" '
                     f'letter-spacing="0.15em">{view_label}</text>')

    # Title at top
    if title:
        svg_parts.append(f'<text x="100" y="14" text-anchor="middle" '
                         f'font-size="8" font-weight="600" fill="{NAVY}">{title}</text>')

    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def generate_both_views(muscles_active, priority_muscles=None, title=None):
    """Generate combined front+back SVG."""
    if priority_muscles is None:
        priority_muscles = set()

    width = 440
    height = 470

    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
                     f'width="{width}" height="{height}" style="font-family:Poppins,sans-serif;">')

    # Background
    svg_parts.append(f'<rect width="{width}" height="{height}" fill="none" rx="12"/>')

    # Title
    if title:
        svg_parts.append(f'<text x="220" y="20" text-anchor="middle" '
                         f'font-size="11" font-weight="600" fill="{NAVY}" '
                         f'letter-spacing="0.05em">{title}</text>')

    y_offset = 28

    # ── Front view ──
    svg_parts.append(f'<g transform="translate(10,{y_offset})">')
    front_outline = FRONT_BODY_OUTLINE.strip()
    svg_parts.append(f'<path d="{front_outline}" fill="{BODY_FILL}" stroke="{BODY_STROKE}" '
                     f'stroke-width="1.2" stroke-linejoin="round"/>')
    for key, data in FRONT_PATHS.items():
        is_active = key in muscles_active
        is_priority = key in priority_muscles
        if is_active and is_priority:
            fill, opacity = HIGHLIGHT_STRONG, "0.85"
        elif is_active:
            fill, opacity = HIGHLIGHT, "0.75"
        else:
            fill, opacity = INACTIVE, "0.25"
        svg_parts.append(f'<path d="{data["path"]}" fill="{fill}" opacity="{opacity}" '
                         f'stroke="{NAVY}" stroke-width="0.5"/>')
    svg_parts.append(f'<text x="100" y="435" text-anchor="middle" font-size="7" '
                     f'font-weight="600" fill="{NAVY}" letter-spacing="0.15em">ANTERIOR</text>')
    svg_parts.append('</g>')

    # ── Back view ──
    svg_parts.append(f'<g transform="translate(230,{y_offset})">')
    back_outline = BACK_BODY_OUTLINE.strip()
    svg_parts.append(f'<path d="{back_outline}" fill="{BODY_FILL}" stroke="{BODY_STROKE}" '
                     f'stroke-width="1.2" stroke-linejoin="round"/>')
    for key, data in BACK_PATHS.items():
        is_active = key in muscles_active
        is_priority = key in priority_muscles
        if is_active and is_priority:
            fill, opacity = HIGHLIGHT_STRONG, "0.85"
        elif is_active:
            fill, opacity = HIGHLIGHT, "0.75"
        else:
            fill, opacity = INACTIVE, "0.25"
        svg_parts.append(f'<path d="{data["path"]}" fill="{fill}" opacity="{opacity}" '
                         f'stroke="{NAVY}" stroke-width="0.5"/>')
    svg_parts.append(f'<text x="100" y="435" text-anchor="middle" font-size="7" '
                     f'font-weight="600" fill="{NAVY}" letter-spacing="0.15em">POSTERIOR</text>')
    svg_parts.append('</g>')

    # Legend
    legend_y = height - 18
    svg_parts.append(f'<g transform="translate(60,{legend_y})">')
    # Active
    svg_parts.append(f'<rect x="0" y="0" width="12" height="8" rx="2" fill="{HIGHLIGHT}" opacity="0.75"/>')
    svg_parts.append(f'<text x="16" y="7" font-size="6" fill="{NAVY}">Músculo trabajado</text>')
    # Priority
    svg_parts.append(f'<rect x="120" y="0" width="12" height="8" rx="2" fill="{HIGHLIGHT_STRONG}" opacity="0.85"/>')
    svg_parts.append(f'<text x="136" y="7" font-size="6" fill="{NAVY}">Zona prioritaria (InBody)</text>')
    # Inactive
    svg_parts.append(f'<rect x="280" y="0" width="12" height="8" rx="2" fill="{INACTIVE}" opacity="0.25"/>')
    svg_parts.append(f'<text x="296" y="7" font-size="6" fill="{NAVY}">Inactivo</text>')
    svg_parts.append('</g>')

    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def inbody_to_priorities(inbody_data):
    """
    Convert InBody segmental analysis to priority muscle groups.
    
    Input format:
    {
        "trunk_muscle": 93.9,    # % of ideal (from InBody segmental)
        "legs_muscle": 84.8,     # % of ideal
        "arms_muscle": 90.2,     # % of ideal
        "trunk_fat": 328.4,      # % of ideal
        "legs_fat": 228.0,       # % of ideal
        "arms_fat": 286.3        # % of ideal
    }
    
    Returns set of priority muscle groups.
    """
    priorities = set()
    
    # Low muscle zones (below 90% = needs strengthening priority)
    trunk_m = inbody_data.get("trunk_muscle", 100)
    legs_m = inbody_data.get("legs_muscle", 100)
    arms_m = inbody_data.get("arms_muscle", 100)
    
    if legs_m < 90:
        priorities.update(["cuadriceps", "isquiotibiales", "gluteos", "pantorrillas"])
    if trunk_m < 90:
        priorities.update(["abdominales", "lumbar", "oblicuos"])
    if arms_m < 90:
        priorities.update(["biceps", "triceps"])
    
    # High fat zones (above 200% = extra cardio/targeted training focus)
    trunk_f = inbody_data.get("trunk_fat", 100)
    legs_f = inbody_data.get("legs_fat", 100)
    arms_f = inbody_data.get("arms_fat", 100)
    
    if trunk_f > 250:
        priorities.update(["abdominales", "oblicuos"])
    if legs_f > 200:
        priorities.update(["cuadriceps", "gluteos"])
    if arms_f > 250:
        priorities.update(["biceps", "triceps"])
    
    return priorities


def svg_to_base64(svg_string):
    """Convert SVG string to base64 data URI for HTML embedding."""
    encoded = base64.b64encode(svg_string.encode('utf-8')).decode('utf-8')
    return f"data:image/svg+xml;base64,{encoded}"


def generate_exercise_card_svg(exercise_name, muscles, is_priority=False):
    """
    Generate a small inline SVG icon showing a simplified body with highlighted muscles.
    Compact version for use inside exercise cards (80x160).
    """
    active = resolve_muscles(muscles) if isinstance(muscles, list) else resolve_muscles(muscles.split(","))
    
    svg = []
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 200" width="80" height="160" '
               'style="font-family:Poppins,sans-serif;">')
    
    # Scaled-down body outline
    svg.append(f'<g transform="scale(0.45) translate(5,5)">')
    svg.append(f'<path d="{FRONT_BODY_OUTLINE.strip()}" fill="{BODY_FILL}" stroke="{BODY_STROKE}" '
               f'stroke-width="1.5" stroke-linejoin="round"/>')
    
    for key, data in FRONT_PATHS.items():
        if key in active:
            fill = HIGHLIGHT_STRONG if is_priority else HIGHLIGHT
            svg.append(f'<path d="{data["path"]}" fill="{fill}" opacity="0.8" '
                       f'stroke="{NAVY}" stroke-width="0.5"/>')
    svg.append('</g>')
    
    svg.append('</svg>')
    return '\n'.join(svg)


# ── CLI interface ──────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Genera SVG de mapas musculares para planes deportivos")
    parser.add_argument("--muscles", type=str, help="Lista de músculos separados por coma")
    parser.add_argument("--priority", type=str, default="", help="Músculos prioritarios (InBody-driven)")
    parser.add_argument("--view", choices=["front", "back", "both"], default="both", help="Vista a generar")
    parser.add_argument("--title", type=str, default=None, help="Título del mapa")
    parser.add_argument("--output", type=str, default=None, help="Archivo de salida (.svg)")
    parser.add_argument("--base64", action="store_true", help="Output as base64 data URI")
    parser.add_argument("--inbody", type=str, default=None, help="JSON de datos segmentales InBody")
    parser.add_argument("--exercise-card", type=str, default=None, help="Genera mini-SVG para card de ejercicio")
    
    args = parser.parse_args()
    
    # Parse muscles
    muscles_active = set()
    if args.muscles:
        muscles_active = resolve_muscles(args.muscles.split(","))
    
    # Parse priority muscles
    priority_muscles = set()
    if args.priority:
        priority_muscles = resolve_muscles(args.priority.split(","))
    
    # InBody data
    if args.inbody:
        inbody_data = json.loads(args.inbody)
        priority_muscles.update(inbody_to_priorities(inbody_data))
    
    # Generate
    if args.exercise_card:
        svg = generate_exercise_card_svg(args.exercise_card, args.muscles.split(",") if args.muscles else [])
    elif args.view == "both":
        svg = generate_both_views(muscles_active, priority_muscles, args.title)
    else:
        svg = generate_svg(muscles_active, args.view, priority_muscles, args.title)
    
    # Output
    if args.base64:
        print(svg_to_base64(svg))
    elif args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(svg)
        print(f"✓ SVG saved to {args.output}", file=sys.stderr)
    else:
        print(svg)


if __name__ == "__main__":
    main()
