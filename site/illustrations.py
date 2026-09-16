# -*- coding: utf-8 -*-
"""Markenkonforme SVG-Illustrationen als Bildflächen (bis echte Fotos vorliegen).
Stil: Sand/Ivory-Flächen, feine Espresso-Linien, ein Kiwi-Akzent, Korn. Keine Gesichter, keine App-Oberflächen."""

ESP = "#33261D"; IVORY = "#FAF6EF"; SAND = "#EDE0CE"; TAUPE = "#C7B7A3"; KIWI = "#8FA748"; KIWI_D = "#4F6321"; KIWI_H = "#E4EAD0"; TERRA = "#B2654A"

GRAIN = '<filter id="n"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3"/><feColorMatrix values="0 0 0 0 0.2 0 0 0 0 0.15 0 0 0 0 0.11 0 0 0 0.07 0"/></filter>'
KIWI_SLICE = lambda x, y, r: (
    f'<path d="M{x-r} {y}A{r} {r} 0 0 1 {x+r} {y}Z" fill="{KIWI}" stroke="{ESP}" stroke-width="{r*0.12:.1f}" stroke-linejoin="miter"/>'
    + ''.join(f'<line x1="{x}" y1="{y}" x2="{x + r*0.62*__import__("math").cos(__import__("math").radians(a)):.1f}" y2="{y - r*0.62*__import__("math").sin(__import__("math").radians(a)):.1f}" stroke="{ESP}" stroke-width="{r*0.025:.1f}"/>' for a in (20, 45, 70, 90, 110, 135, 160))
    + f'<path d="M{x-r*0.12} {y}A{r*0.12} {r*0.12} 0 0 1 {x+r*0.12} {y}Z" fill="{ESP}"/>'
)

def frame(w, h, bg, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img">
<defs>{GRAIN}<linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{IVORY}"/><stop offset="1" stop-color="{bg}"/></linearGradient></defs>
<rect width="{w}" height="{h}" fill="url(#g)"/>
<g fill="none" stroke="{ESP}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{body}</g>
<rect width="{w}" height="{h}" filter="url(#n)"/></svg>'''

def hero_kristina():
    # Bogengang mit Sonne – Platz für das echte Foto
    w, h = 800, 1000
    body = f'''<path d="M120 900V420A280 280 0 0 1 680 420V900" stroke-width="4"/>
<path d="M60 900H740" stroke="{TAUPE}"/>
<circle cx="400" cy="470" r="120" fill="{KIWI_H}" stroke="none"/>
<path d="M300 620Q400 560 500 620" stroke="{TAUPE}"/>
<path d="M200 900V760M600 900V760" stroke="{TAUPE}"/>
<path d="M0 640H120M680 640H800" stroke="{TAUPE}"/>
<path d="M330 900c0-60 30-110 70-110s70 50 70 110" stroke="{TAUPE}"/>'''
    return frame(w, h, SAND, body)

def about_hands():
    w, h = 800, 1000
    body = f'''<rect x="140" y="300" width="420" height="520" rx="6" fill="{IVORY}" stroke-width="3"/>
<path d="M200 400H500M200 460H460M200 520H500M200 580H420M200 640H480" stroke="{TAUPE}"/>
<circle cx="620" cy="300" r="70" fill="{SAND}"/><path d="M690 290q60 10 0 60" /><ellipse cx="620" cy="300" rx="44" ry="18" fill="{ESP}" stroke="none"/>
<path d="M120 880c120-60 220-90 360-40" stroke="{KIWI_D}" stroke-width="2"/>
<path d="M560 760l120-80M560 800l120-80M560 840l120-80" stroke="{TAUPE}"/>'''
    return frame(w, h, SAND, body)

def hero_gastro():
    w, h = 1200, 800
    body = f'''<path d="M0 560H1200" stroke-width="4"/>
<ellipse cx="480" cy="560" rx="220" ry="60" fill="{IVORY}"/><ellipse cx="480" cy="560" rx="150" ry="40" stroke="{TAUPE}"/>
<path d="M780 420v120M760 430c0-40 40-40 40 0v40h-40z" fill="{IVORY}"/><path d="M760 540h40" />
<path d="M230 480v90M250 480v90M260 480q0 40-20 40" stroke="{TAUPE}"/>
<path d="M160 640h880" stroke="{TAUPE}"/>
<path d="M120 720c200-80 500-80 760 0" stroke="{TAUPE}"/>
{KIWI_SLICE(980, 300, 60)}
<path d="M60 200h300" stroke="{TAUPE}"/>'''
    return frame(w, h, SAND, body)

def hero_fewo():
    w, h = 1200, 800
    body = f'''<path d="M200 800V360A260 260 0 0 1 720 360V800" stroke-width="4"/>
<path d="M260 800V420A200 200 0 0 1 660 420V800" fill="{KIWI_H}" stroke="none"/>
<path d="M260 560H660" stroke="{ESP}" stroke-width="3"/>
<path d="M300 500q60-30 120 0t120 0t120 0" stroke="{TAUPE}"/>
<circle cx="560" cy="400" r="36" fill="{IVORY}"/>
<path d="M820 800V520h240" stroke="{TAUPE}"/><path d="M860 560h160M860 610h160M860 660h100" stroke="{TAUPE}"/>
<path d="M0 800H1200" stroke-width="4"/>'''
    return frame(w, h, SAND, body)

def hero_handwerk():
    w, h = 1200, 800
    body = f'''<path d="M0 620H1200" stroke-width="4"/>
<rect x="160" y="540" width="880" height="80" fill="{IVORY}"/>
<path d="M240 540V800M960 540V800" stroke="{TAUPE}"/>
<g transform="rotate(-18 520 440)"><rect x="300" y="420" width="440" height="40" rx="4" fill="{KIWI_H}"/><path d="M340 420v20M380 420v12M420 420v20M460 420v12M500 420v20M540 420v12M580 420v20M620 420v12M660 420v20M700 420v12"/></g>
<circle cx="900" cy="470" r="40" fill="{IVORY}"/><path d="M900 430v80M860 470h80" stroke="{TAUPE}"/>
<path d="M80 200h280M80 260h180" stroke="{TAUPE}"/>'''
    return frame(w, h, SAND, body)

def hero_studio():
    w, h = 1200, 800
    body = f'''<path d="M0 640H1200" stroke-width="4"/>
<rect x="240" y="480" width="520" height="160" rx="10" fill="{IVORY}"/><path d="M240 540h520M240 590h520" stroke="{TAUPE}"/>
<path d="M880 620c40-120 120-180 200-200c-20 90-80 170-200 200z" fill="{KIWI_H}"/><path d="M900 610c40-70 100-130 170-180" stroke="{KIWI_D}" stroke-width="2"/>
<path d="M120 300h220M120 350h140" stroke="{TAUPE}"/>
<circle cx="640" cy="300" r="70" fill="{SAND}" stroke="{TAUPE}"/>'''
    return frame(w, h, SAND, body)

def phone(x, y, w, h, inner):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="36" fill="{IVORY}" stroke-width="4"/><rect x="{x+18}" y="{y+18}" width="{w-36}" height="{h-36}" rx="24" fill="{IVORY}" stroke="{TAUPE}"/>{inner}'

def detail_menu():
    w, h = 800, 1000
    inner = f'<path d="M280 260h240" stroke-width="4"/>' + ''.join(f'<path d="M280 {y}h180M280 {y+26}h120" stroke="{TAUPE}"/><path d="M500 {y+8}h20" stroke="{KIWI_D}"/>' for y in range(330, 720, 80))
    inner += f'<rect x="280" y="780" width="240" height="56" rx="3" fill="{KIWI_D}" stroke="none"/>'
    return frame(w, h, SAND, phone(220, 160, 360, 720, inner))

def detail_handwerk():
    w, h = 800, 1000
    body = f'''<rect x="140" y="240" width="520" height="560" rx="6" fill="{IVORY}"/>
<path d="M400 520c-60-60-90-100-90-150a90 90 0 0 1 180 0c0 50-30 90-90 150z" fill="{KIWI}"/><circle cx="400" cy="370" r="32" fill="{IVORY}"/>
<path d="M200 600h400M200 650h280" stroke="{TAUPE}"/>
<g fill="{KIWI_D}" stroke="none">{''.join(f'<path transform="translate({x} 700) scale(1.2)" d="M10 0l3 6 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1z"/>' for x in (200,236,272,308,344))}</g>
<rect x="200" y="740" width="200" height="40" rx="3" fill="{KIWI_D}" stroke="none"/>'''
    return frame(w, h, SAND, body)

def detail_studio():
    w, h = 800, 1000
    cells = ''.join(f'<rect x="{180+ (i%7)*64}" y="{380+(i//7)*64}" width="52" height="52" rx="3" fill="{IVORY}" stroke="{TAUPE}"/>' for i in range(35))
    body = f'''<rect x="140" y="280" width="520" height="520" rx="6" fill="{SAND}" stroke-width="3"/>
<path d="M180 330h240" stroke-width="4"/>{cells}
<rect x="372" y="508" width="52" height="52" rx="3" fill="{KIWI}" stroke="{ESP}"/>
<path d="M120 900c150-40 300-40 560 0" stroke="{TAUPE}"/>'''
    return frame(w, h, SAND, body)

def check_note():
    w, h = 900, 900
    body = f'''<rect x="180" y="150" width="460" height="600" rx="4" fill="{IVORY}" stroke-width="3"/>
<path d="M240 240h200" stroke-width="4"/>
<circle cx="250" cy="340" r="10" fill="{KIWI_D}" stroke="none"/><path d="M280 340h300" stroke="{TAUPE}"/>
<circle cx="250" cy="420" r="10" fill="{KIWI_D}" stroke="none"/><path d="M280 420h260" stroke="{TAUPE}"/>
<circle cx="250" cy="500" r="10" fill="{KIWI_D}" stroke="none"/><path d="M280 500h300" stroke="{TAUPE}"/>
<path d="M280 600h200M280 640h160" stroke="{TAUPE}"/>
{KIWI_SLICE(720, 700, 90)}
<circle cx="160" cy="720" r="50" fill="{SAND}"/><ellipse cx="160" cy="720" rx="32" ry="12" fill="{ESP}" stroke="none"/>'''
    return frame(w, h, SAND, body)

def how_map():
    w, h = 800, 1000
    body = f'''<rect x="120" y="220" width="560" height="620" rx="6" fill="{IVORY}"/>
<path d="M120 400c100-40 200 60 300 20s160-60 260-20M120 620c120 40 260-60 380-10s120 30 180 10M300 220v620M520 220v620" stroke="{TAUPE}"/>
<path d="M400 560c-60-60-90-100-90-150a90 90 0 0 1 180 0c0 50-30 90-90 150z" fill="{KIWI}"/><circle cx="400" cy="410" r="30" fill="{IVORY}"/>
<path d="M60 900h300" stroke="{TAUPE}"/>'''
    return frame(w, h, SAND, body)

def how_phone():
    w, h = 800, 1000
    inner = f'<rect x="270" y="230" width="260" height="150" rx="4" fill="{KIWI_H}" stroke="none"/><path d="M280 430h200" stroke-width="4"/><path d="M280 480h220M280 520h180M280 560h220" stroke="{TAUPE}"/><rect x="280" y="620" width="160" height="48" rx="3" fill="{KIWI_D}" stroke="none"/>'
    return frame(w, h, SAND, phone(220, 160, 360, 720, inner))

def how_photos():
    w, h = 800, 1000
    body = f'''<g transform="rotate(-8 400 520)"><rect x="160" y="300" width="380" height="440" fill="{IVORY}" stroke-width="3"/><rect x="190" y="330" width="320" height="300" fill="{SAND}"/></g>
<g transform="rotate(6 440 560)"><rect x="240" y="360" width="380" height="440" fill="{IVORY}" stroke-width="3"/><rect x="270" y="390" width="320" height="300" fill="{KIWI_H}"/><path d="M0 620H1200" /></g>
<path d="M300 560q60-40 120 0t120 0" stroke="{KIWI_D}" stroke-width="2"/>
<path d="M120 900h560" stroke="{TAUPE}"/>'''
    return frame(w, h, SAND, body)

ILLUSTRATIONS = {
    "hero-kristina": hero_kristina, "about-hands": about_hands, "hero-gastro": hero_gastro, "hero-fewo": hero_fewo,
    "hero-handwerk": hero_handwerk, "hero-studio": hero_studio, "detail-menu": detail_menu, "detail-handwerk": detail_handwerk,
    "detail-studio": detail_studio, "check-note": check_note, "how-map": how_map, "how-phone": how_phone, "how-photos": how_photos,
}
