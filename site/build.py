#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KWiDi – statischer Site-Generator.
Aufruf: python3 build.py  → schreibt alles nach ../docs/ (GitHub Pages)
Bilder: Liegt assets/img/<name>.jpg|.webp|.png vor, wird es verwendet; sonst ein Platzhalter-SVG.
"""
import os, sys, json, shutil, datetime, importlib
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(os.path.dirname(ROOT), "docs")  # GitHub Pages: Branch main, Ordner /docs
sys.path.insert(0, os.path.join(ROOT, "content"))

SITE = {
    "url": "https://kriswidi.com",
    "email": "kristina@swiderskipropertymanagement.com",   # später: hallo@kriswidi.com
    "instagram": "https://www.instagram.com/",   # KWiDi-Handle eintragen
    "facebook": "https://www.facebook.com/",
    "form_endpoint": "https://formsubmit.co/ajax/kristina@swiderskipropertymanagement.com",  # FormSubmit: erste Anfrage per E-Mail bestätigen              # z. B. https://api.web3forms.com/submit oder https://formspree.io/f/xxxx
}

de = importlib.import_module("de")
en = importlib.import_module("en")
URL_MAP = en.URL_MAP
REV_MAP = {v: k for k, v in URL_MAP.items()}

env = Environment(loader=FileSystemLoader(os.path.join(ROOT, "templates")), autoescape=select_autoescape(["html"]))

def read(p):
    with open(p, encoding="utf8") as f: return f.read()

IMG_DIR = os.path.join(ROOT, "assets", "img")
logo_h = read(os.path.join(IMG_DIR, "logo-horizontal.svg"))
logo_mono_ivory = read(os.path.join(IMG_DIR, "logo-horizontal-mono.svg")).replace('stroke="currentColor"', 'stroke="#FAF6EF"').replace('fill="currentColor"', 'fill="#FAF6EF"')
signet = read(os.path.join(IMG_DIR, "signet.svg"))

# ---------- Platzhalter-Bilder (Bildsprache Markenkit) ----------
PLACEHOLDERS = {
    "hero-kristina":  ("4:5", "linear-gradient(168deg,#EDE0CE 0%,#FAF6EF 58%)", "Hero · echtes Foto von Kristina (Markenkit)"),
    "about-hands":    ("4:5", "linear-gradient(118deg,#FFFDF8 0%,#FAF6EF 46%,#EDE0CE 100%)", "Über mich · Hände, Notizbuch, Espresso"),
    "hero-gastro":    ("3:2", "linear-gradient(180deg,#F8F2E8 0 57%,#E7DAC7 57%)", "Gastronomie · gedeckter Tisch, Terrasse"),
    "hero-fewo":      ("3:2", "linear-gradient(162deg,#C2745A,#A75B41)", "Ferienvermietung · Bogengang, Meer"),
    "hero-handwerk":  ("3:2", "linear-gradient(152deg,#8E7A62 0%,#B99C7C 38%,#E3D3BC 100%)", "Handwerk · Werkbank, Zollstock"),
    "hero-studio":    ("3:2", "linear-gradient(118deg,#FAF6EF 0%,#EDE0CE 100%)", "Praxen & Studios · Behandlungsraum, Leinen"),
    "detail-menu":    ("4:5", "linear-gradient(196deg,#9DB255 0%,#6E8232 58%,#54641E 100%)", "Detail · Speisekarte auf dem Smartphone"),
    "detail-handwerk":("4:5", "linear-gradient(152deg,#B99C7C 0%,#E3D3BC 100%)", "Detail · Google-Profil Handwerk, angedeutet"),
    "detail-studio":  ("4:5", "linear-gradient(118deg,#EDE0CE 0%,#FAF6EF 100%)", "Detail · Terminbuch, Leinen"),
    "check-note":     ("1:1", "linear-gradient(180deg,#FAF6EF 0 60%,#E4EAD0 60%)", "Check · Blatt mit drei Punkten, Kiwi-Scheibe"),
    "how-map":        ("4:5", "linear-gradient(118deg,#FFFDF8 0%,#EDE0CE 100%)", "Schritt 1 · Karte mit Stecknadel, gezeichnet"),
    "how-phone":      ("4:5", "linear-gradient(180deg,#F8F2E8 0 57%,#E7DAC7 57%)", "Schritt 2 · Smartphone, helle Seite"),
    "how-photos":     ("4:5", "linear-gradient(162deg,#C2745A,#A75B41)", "Schritt 3 · Fotos auf Leinen"),
}

def placeholder_svg(name, ratio, grad, caption):
    w, h = {"4:5": (800, 1000), "3:2": (1200, 800), "1:1": (900, 900), "16:9": (1600, 900)}[ratio]
    # CSS-Gradient grob in SVG übersetzen: zwei Stopps reichen für den Platzhalter
    import re
    cols = re.findall(r"#[0-9A-Fa-f]{6}", grad)
    c1, c2 = cols[0], cols[-1]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{caption}">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
<filter id="n"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3"/><feColorMatrix values="0 0 0 0 0.2 0 0 0 0 0.15 0 0 0 0 0.11 0 0 0 0.08 0"/></filter></defs>
<rect width="{w}" height="{h}" fill="url(#g)"/><rect width="{w}" height="{h}" filter="url(#n)"/>
<text x="40" y="{h-40}" font-family="Jost,Avenir Next,system-ui,sans-serif" font-size="22" letter-spacing="2" fill="#33261D" opacity=".6">{caption.upper()}</text>
</svg>'''

def image(name, alt=""):
    for ext in ("jpg", "jpeg", "webp", "png"):
        if os.path.exists(os.path.join(IMG_DIR, f"{name}.{ext}")):
            return f'<img src="/assets/img/{name}.{ext}" alt="{alt}" loading="lazy" decoding="async">'
    return f'<img src="/assets/img/placeholders/{name}.svg" alt="{alt}" loading="lazy" decoding="async">'

from kiwi import kiwi_svg
env.globals.update(image=image, kiwi_svg=kiwi_svg, logo_horizontal=logo_h, logo_mono_ivory=logo_mono_ivory, signet=signet)

def alt_urls(url):
    if url in URL_MAP: return {"de": url, "en": URL_MAP[url]}
    if url in REV_MAP: return {"de": REV_MAP[url], "en": url}
    return {"de": "/", "en": "/en/"}

def out_path(url):
    if url.endswith("/"): return os.path.join(DIST, url.strip("/"), "index.html")
    if url.endswith("/404"): return os.path.join(DIST, url.strip("/") + ".html")
    return os.path.join(DIST, url.strip("/"), "index.html")

def build():
    if os.path.exists(DIST): shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(DIST, "assets"))
    ph = os.path.join(DIST, "assets", "img", "placeholders"); os.makedirs(ph, exist_ok=True)
    from illustrations import ILLUSTRATIONS
    for name, (ratio, grad, cap) in PLACEHOLDERS.items():
        svg = ILLUSTRATIONS[name]() if name in ILLUSTRATIONS else placeholder_svg(name, ratio, grad, cap)
        with open(os.path.join(ph, f"{name}.svg"), "w", encoding="utf8") as f: f.write(svg)
    # config.js (Tracking-IDs, Formulartexte)
    cfg = {"gaId": "", "metaPixelId": "", "formText": {}}
    year = datetime.date.today().year
    urls = []
    for mod in (de, en):
        ui = mod.UI
        cfg_lang = dict(cfg); cfg_lang["formText"] = ui["form"]["js"]
        for page in mod.PAGES:
            page = dict(page)
            page["alt"] = alt_urls(page["url"])
            page.setdefault("jsonld", []); page.setdefault("noindex", False); page.setdefault("lead", False)
            tpl = env.get_template(page.get("template", "page") + ".html")
            html = tpl.render(page=page, ui=ui, site=SITE, lang=mod.LANG, year=year)
            # config.js sprachabhängig inline vor main.js ersetzen
            html = html.replace('<script src="/assets/js/config.js"></script>', f'<script>window.KWIDI={json.dumps(cfg_lang, ensure_ascii=False)};</script>')
            p = out_path(page["url"]); os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf8") as f: f.write(html)
            if not page["noindex"]: urls.append(page["url"])
    # sitemap.xml mit hreflang
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for u in urls:
        a = alt_urls(u)
        sm.append(f'  <url><loc>{SITE["url"]}{u}</loc>'
                  f'<xhtml:link rel="alternate" hreflang="de" href="{SITE["url"]}{a["de"]}"/>'
                  f'<xhtml:link rel="alternate" hreflang="en" href="{SITE["url"]}{a["en"]}"/>'
                  f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE["url"]}{a["de"]}"/></url>')
    sm.append('</urlset>')
    with open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf8") as f: f.write("\n".join(sm))
    with open(os.path.join(DIST, "robots.txt"), "w", encoding="utf8") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /danke\nDisallow: /en/thank-you\nSitemap: {SITE['url']}/sitemap.xml\n")
    # 404 auf Root-Ebene (Netlify/Cloudflare-Konvention)
    # _redirects / .htaccess Hinweise
    fav = os.path.join(ROOT, "assets", "favicon.ico")
    if os.path.exists(fav): shutil.copy(fav, os.path.join(DIST, "favicon.ico"))
    with open(os.path.join(DIST, ".htaccess"), "w") as f:
        f.write("ErrorDocument 404 /404.html\nRewriteEngine On\nRewriteCond %{HTTPS} off\nRewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]\n<IfModule mod_headers.c>\nHeader set X-Content-Type-Options nosniff\n</IfModule>\n")
    with open(os.path.join(DIST, "_redirects"), "w") as f: f.write("/404 /404.html 404\n/en/404 /en/404.html 404\n")
    # GitHub Pages: eigene Domain + kein Jekyll-Processing
    with open(os.path.join(DIST, "CNAME"), "w") as f: f.write(SITE["url"].split("//")[1] + "\n")
    open(os.path.join(DIST, ".nojekyll"), "w").close()
    print(f"OK – {len(urls)} indexierbare Seiten, Ausgabe: {DIST}")

if __name__ == "__main__":
    build()
