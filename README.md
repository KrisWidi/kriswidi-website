# kriswidi.com – Website

Statische Website (HTML/CSS/JS), zweisprachig DE/EN. Kein CMS, keine Datenbank, kein Plugin-Zwang.

## Ordner
- `content/de.py`, `content/en.py` – **alle Texte**. Hier ändern, dann neu bauen.
- `templates/` – Seitenaufbau (Blöcke: hero, text, chain, cards, packages, highlight, split, reasons, steps, list, table, faq, form, legal, simple)
- `assets/` – CSS, JS, Logos, Bilder, Fonts
- `build.py` – erzeugt `../docs/` (fertige Website; GitHub Pages liefert diesen Ordner aus)

## Neu bauen
```
python3 build.py
```
Voraussetzung: Python 3 und `pip install jinja2`. Ausgabe liegt in `docs/` – GitHub Pages veröffentlicht genau diesen Ordner (Settings → Pages → Branch `main`, Ordner `/docs`).

## Vor dem Launch (Checkliste)
1. **Schriften**: Doppelklick auf `site/get-fonts.bat` (Windows). Lädt Fraunces und Jost einmalig von Google und legt sie in `assets/fonts/` ab – in `site/` und `docs/`. Danach ist kein Google-Server mehr im Spiel (DSGVO). Bis dahin greifen Georgia/System-Schriften.
2. **Bilder**: Echte Bilder als `assets/img/<name>.jpg` ablegen (Namen siehe `PLACEHOLDERS` in build.py: hero-kristina, about-hands, hero-gastro, hero-fewo, hero-handwerk, hero-studio, detail-menu, detail-handwerk, detail-studio, check-note, how-map, how-phone, how-photos). Liegt eine Datei vor, ersetzt sie den Platzhalter automatisch. Empfohlen: max. 1600 px Breite, unter 250 KB.
3. **Formular-Versand**: bereits verdrahtet mit FormSubmit (kostenlos, ohne Konto) an kristinaswiderski@outlook.com. **Einmalig aktivieren:** nach dem Hochladen selbst eine Testanfrage über die Website schicken → FormSubmit schickt eine Aktivierungs-Mail → Link klicken. Ab dann kommen alle Anfragen als E-Mail an. Sobald hallo@kriswidi.com existiert: Adresse in `build.py` (`SITE["email"]` und `form_endpoint`) tauschen, neu bauen, erneut aktivieren.
4. **Tracking**: In `build.py` → `cfg = {"gaId": "G-XXXX", "metaPixelId": "1234..."}`. Beide laden erst nach Einwilligung im Cookie-Banner (Consent Mode v2). Auf /danke feuert das Meta-Event „Lead“.
5. **Impressum/Datenschutz**: ausgefüllt mit den Daten der Swiderski Property Management S.L. (Adresse, NIF B21648753, Administrador) und einer vollständigen Datenschutzerklärung (Hosting, Formular/FormSubmit, Consent, GA4, Meta-Pixel, lokale Fonts, Rechte). Bitte einmal lesen; Hosting-Anbieter ggf. namentlich ergänzen. Ersetzt keine Rechtsberatung.
6. **Social-Links**: `SITE["instagram"]`, `SITE["facebook"]` in `build.py`.
7. **Domain** in `SITE["url"]` prüfen (für Canonical, hreflang, Sitemap).

## Hosting: GitHub Pages (kostenlos)
1. Auf github.com ein neues Repository anlegen, z. B. `kriswidi-website` (Public – bei Free-Konten ist Pages nur für öffentliche Repos frei).
2. Kompletten Inhalt dieses Ordners hochladen („Add file → Upload files", Ordner per Drag & Drop) und committen.
3. Settings → Pages → Source „Deploy from a branch" → Branch `main`, Ordner `/docs` → Save.
4. Settings → Pages → Custom domain: `kriswidi.com` eintragen → Save. Danach „Enforce HTTPS" anhaken (erscheint, sobald DNS stimmt; kann bis zu 1 Std. dauern).
5. Beim Domain-Anbieter von kriswidi.com im DNS eintragen:
   - `A`-Records für `@` (kriswidi.com): `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` für `www` → `<github-benutzername>.github.io`
6. `docs/CNAME` enthält bereits `kriswidi.com`, `docs/.nojekyll` verhindert Jekyll. `404.html` im Root wird von GitHub Pages automatisch als Fehlerseite benutzt.
- Änderungen später: `docs/` neu bauen bzw. neue Dateien hochladen – GitHub veröffentlicht innerhalb von ~1 Minute.
- Nach Launch: Google Search Console anlegen, `https://kriswidi.com/sitemap.xml` einreichen.

## Texte ändern
Beispiel: Preis ändern → in `content/de.py` und `content/en.py` in `PACKAGES_SHORT` und `PACKAGES_FULL` (und in FAQ-Texten, wo Preise genannt sind) anpassen, `python3 build.py`, geänderte Dateien aus `docs/` auf GitHub hochladen.
