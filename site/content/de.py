# -*- coding: utf-8 -*-
"""KWiDi – deutsche Inhalte (Quelle: Website Copy Deck, Phase 7)."""

LANG = "de"
PREFIX = ""  # deutsche URLs ohne Präfix

UI = {
    "skip": "Zum Inhalt springen",
    "home": "Startseite", "home_url": "/",
    "nav_label": "Hauptnavigation", "lang_label": "Sprache", "menu": "Menü", "close": "Schließen",
    "more": "Mehr", "faq": "Häufige Fragen",
    "cta": "Anfragen", "cta_href": "/kontakt",
    "thanks_url": "/danke",
    "nav": [
        {"text": "Pakete", "href": "/pakete"},
        {"text": "Branchen", "href": "/fuer/gastronomie", "children": [
            {"text": "Gastronomie", "sub": "Restaurants, Cafés, Bars", "href": "/fuer/gastronomie"},
            {"text": "Ferienvermietung", "sub": "Ferienhaus & Ferienwohnung", "href": "/fuer/ferienvermietung"},
            {"text": "Handwerk", "sub": "Handwerksbetriebe", "href": "/fuer/handwerk"},
            {"text": "Praxen & Studios", "sub": "Physio, Kosmetik, Heilpraktik", "href": "/fuer/praxen-studios"},
        ]},
        {"text": "Website ohne Anfragen", "href": "/website-ohne-anfragen"},
        {"text": "So funktioniert's", "href": "/so-funktioniert-es"},
        {"text": "Über mich", "href": "/ueber-mich"},
    ],
    "footer": {
        "claim": "Websites, die gesehen werden.",
        "text": "Website, Google-Unternehmensprofil, Instagram und Facebook – fertig eingerichtet, zum Festpreis, aus einer Hand.",
        "pages_label": "Seiten",
        "pages": [
            {"text": "Pakete & Preise", "href": "/pakete"},
            {"text": "Website ohne Anfragen", "href": "/website-ohne-anfragen"},
            {"text": "Sichtbarkeits-Check", "href": "/sichtbarkeits-check"},
            {"text": "So funktioniert's", "href": "/so-funktioniert-es"},
            {"text": "Über mich", "href": "/ueber-mich"},
            {"text": "Kontakt", "href": "/kontakt"},
        ],
        "industries_label": "Branchen",
        "industries": [
            {"text": "Gastronomie", "href": "/fuer/gastronomie"},
            {"text": "Ferienvermietung", "href": "/fuer/ferienvermietung"},
            {"text": "Handwerk", "href": "/fuer/handwerk"},
            {"text": "Praxen & Studios", "href": "/fuer/praxen-studios"},
        ],
        "contact_label": "Kontakt",
        "reply": "Antwort innerhalb von 24 Stunden an Werktagen",
        "imprint": "Impressum", "imprint_href": "/impressum",
        "privacy": "Datenschutz", "privacy_href": "/datenschutz",
        "cookies": "Cookie-Einstellungen",
        "vat": "Alle Preise zzgl. MwSt.",
    },
    "consent": {
        "title": "Kurz zu Cookies.",
        "text": "Ich nutze Cookies für Statistik und Werbung (Google Analytics, Meta-Pixel), damit ich sehe, was auf der Seite gut funktioniert. Du entscheidest.",
        "link": "Details in der Datenschutzerklärung.",
        "all": "Alle akzeptieren", "none": "Nur notwendige", "settings": "Einstellungen", "save": "Auswahl speichern",
        "necessary": "Notwendig (immer aktiv)", "analytics": "Statistik (Google Analytics)", "marketing": "Werbung (Meta-Pixel)",
    },
    "form": {
        "h2": "Lass uns kurz schauen, was für dich passt.",
        "text": "Schreib mir in zwei, drei Sätzen, was du vorhast. Ich antworte innerhalb von 24 Stunden an Werktagen – per E-Mail, ohne Verkaufsgespräch am Telefon.",
        "direct": "Lieber direkt per Mail?",
        "name": "Name", "email": "E-Mail", "industry": "Branche", "interest": "Interesse",
        "industries": ["Gastronomie", "Ferienvermietung", "Handwerk", "Praxis & Studio", "Andere"],
        "interests": ["Neue Website", "Bestehende Website verbessern", "Sichtbarkeits-Check", "Noch unklar"],
        "link": "Link zu Website oder Instagram (optional)", "message": "Nachricht",
        "business": "Betrieb", "link_site": "Link zu deiner Website", "link_google": "Link zum Google-Profil", "link_insta": "Link zu Instagram",
        "check_msg": "Was dich am meisten stört (optional)",
        "privacy_pre": "Ich habe die", "privacy_link": "Datenschutzerklärung", "privacy_post": "gelesen.",
        "submit": "Anfrage senden",
        "js": {"invalid": "Bitte fülle alle Pflichtfelder aus.", "ok": "Danke – deine Nachricht ist da.", "fail": "Das hat nicht geklappt. Schreib mir bitte direkt per E-Mail.", "noEndpoint": "Der Formular-Versand ist noch nicht eingerichtet. Schreib mir bitte per E-Mail."},
    },
}

FORM = {"type": "form"}

PACKAGES_SHORT = [
    {"name": "Website", "price": "ab 549 €", "price_note": "einmalig, netto", "for": "Neu oder Umbau. 4 Seiten, Texte und Bilder von mir, Rechtstexte inklusive.", "button": "Anfragen", "href": "/pakete"},
    {"name": "Website + Google", "price": "729 €", "price_note": "einmalig, netto", "for": "Dazu dein Google-Unternehmensprofil, vollständig eingerichtet.", "button": "Anfragen", "href": "/pakete"},
    {"name": "Website + Google + Social", "price": "1.490 €", "price_note": "einmalig, netto", "tag": "Empfehlung", "highlight": True, "for": "Dazu Instagram und Facebook, eingerichtet und mit den ersten sechs Beiträgen gefüllt.", "button": "Anfragen", "href": "/pakete"},
    {"name": "Rundum", "price": "2.990 €", "price_note": "einmalig, netto", "for": "Alles aus dem dritten Paket plus drei Monate Betreuung.", "button": "Anfragen", "href": "/pakete"},
]

PACKAGES_FULL = [
    {"name": "Website", "price": "ab 549 €", "price_note": "einmalig · zzgl. MwSt.", "for": "Für alle, die gefunden und verstanden werden wollen.",
     "features": ["4 Seiten, individuell gestaltet – kein Template", "Texte und Bilder von mir", "Impressum und Datenschutzerklärung inklusive", "Für Handy, Tablet und Desktop", "Kontaktformular", "Domain und Hosting eingerichtet", "Neu oder Umbau deiner bestehenden Website"],
     "button": "Website anfragen"},
    {"name": "Website + Google", "price": "729 €", "price_note": "einmalig · zzgl. MwSt.", "for": "Für alle, die auf der Karte auftauchen wollen.",
     "features": ["Alles aus „Website“", "Google-Unternehmensprofil vollständig eingerichtet: Kategorien, Öffnungszeiten, Leistungen, Fotos, Beschreibung", "Verknüpfung mit deiner Website"],
     "button": "Website + Google anfragen"},
    {"name": "Website + Google + Social", "price": "1.490 €", "price_note": "einmalig · zzgl. MwSt.", "tag": "Meine Empfehlung", "highlight": True, "for": "Für alle, die im Kopf bleiben wollen.",
     "features": ["Alles aus „Website + Google“", "Instagram-Profil eingerichtet: Bio, Highlights, Profilbild, Verlinkung", "Facebook-Seite eingerichtet", "Je 6 erste Beiträge, damit die Profile nicht leer sind"],
     "button": "Paket anfragen"},
    {"name": "Rundum", "price": "2.990 €", "price_note": "einmalig · zzgl. MwSt.", "for": "Für alle, die es komplett abgeben wollen.",
     "features": ["Alles aus „Website + Google + Social“", "3 Monate Betreuung: Beiträge, Pflege des Google-Profils, Änderungen an der Website – den Umfang stimmen wir auf deinen Betrieb ab"],
     "button": "Rundum anfragen"},
]

CHAIN = [
    {"title": "Gefunden werden", "sub": "Google-Unternehmensprofil", "text": "„Restaurant in der Nähe“, „Ferienhaus mit Meerblick“, „Elektriker + dein Ort“: So suchen deine Gäste. Ohne vollständiges Google-Profil tauchst du auf der Karte nicht auf – egal wie gut deine Website ist."},
    {"title": "Überzeugen", "sub": "Website", "text": "Der Gast klickt und entscheidet in dreißig Sekunden. Bilder, Preise, Öffnungszeiten, Bewertungen, ein Klick zum Anfragen. Das ist der Moment, in dem er kommt – oder zum nächsten geht."},
    {"title": "Im Kopf bleiben", "sub": "Instagram und Facebook", "text": "Wer dich einmal gesehen hat, sieht dich wieder. Das bringt Stammgäste, Empfehlungen und Wiederbucher – ohne dass du jeden Tag posten musst."},
]

def industry_page(slug, title, desc, hero, blocks, industry, faq, jsonld_name):
    return {
        "url": f"/fuer/{slug}", "title": title, "description": desc, "template": "page",
        "jsonld": [
            {"@context": "https://schema.org", "@type": "Service", "name": jsonld_name, "provider": {"@type": "Organization", "name": "KWiDi", "url": "https://kriswidi.com"}, "areaServed": ["DE", "AT", "CH"], "offers": {"@type": "Offer", "priceCurrency": "EUR", "price": "549", "priceSpecification": {"@type": "UnitPriceSpecification", "price": "549", "priceCurrency": "EUR", "valueAddedTaxIncluded": False}}},
            {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "KWiDi", "item": "https://kriswidi.com/"}, {"@type": "ListItem", "position": 2, "name": jsonld_name, "item": f"https://kriswidi.com/fuer/{slug}"}]},
            {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in faq]},
        ],
        "blocks": [hero] + blocks + [{"type": "faq", "items": faq}, {**FORM, "industry": industry}],
    }

PAGES = []

# ---------------- STARTSEITE ----------------
HOME_FAQ = [
    {"q": "Was kostet eine Website bei KWiDi?", "a": "Ab 549 € netto für vier Seiten inklusive Texte, Bilder und Rechtstexte. Mit Google-Profil 729 €, mit Instagram und Facebook 1.490 €. Alle Pakete stehen auf der Preisseite – ohne Kleingedrucktes."},
    {"q": "Muss ich Texte und Bilder liefern?", "a": "Nein. Ich schreibe die Texte und kümmere mich um Bilder. Wenn du eigenes Material hast, nutze ich es gern – am Preis ändert das nichts."},
    {"q": "Fallen monatliche Kosten an?", "a": "Bei mir nicht. Du zahlst einmal, die Website gehört dir. Nur Domain und Hosting laufen über deinen Anbieter – ich richte beides ein, die laufenden Kosten (meist unter 10 € im Monat) trägst du direkt."},
    {"q": "Warum nicht einfach mit KI oder Wix selbst bauen?", "a": "Kannst du. Dann hast du eine Seite – aber kein eingerichtetes Google-Profil, kein Instagram, keine Texte, die verkaufen, und niemanden, den du fragen kannst. Die Website ist der einfachste Teil. Die Wege dorthin sind die Arbeit."},
    {"q": "Kann ich dich anrufen?", "a": "Ich arbeite per E-Mail – so bleibt alles nachlesbar und ich kann mich konzentriert um dein Projekt kümmern. Du bekommst innerhalb von 24 Stunden an Werktagen eine Antwort."},
]
PAGES.append({
    "url": "/", "title": "Website erstellen lassen ab 549 € – KWiDi",
    "description": "Website, Google-Profil und Instagram aus einer Hand – fertig eingerichtet, zum Festpreis. Für Gastronomie, Ferienvermietung, Handwerk und Studios.",
    "template": "page",
    "jsonld": [
        {"@context": "https://schema.org", "@type": "Organization", "name": "KWiDi", "url": "https://kriswidi.com", "logo": "https://kriswidi.com/assets/img/logo-stacked.svg", "email": "kristinaswiderski@outlook.com", "sameAs": []},
        {"@context": "https://schema.org", "@type": "WebSite", "name": "KWiDi", "url": "https://kriswidi.com", "inLanguage": ["de", "en"]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in HOME_FAQ]},
    ],
    "blocks": [
        {"type": "hero", "label": "Website · Google · Instagram · Facebook", "h1": "Websites, die gesehen werden.",
         "text": "Deine Website, dein Google-Profil und dein Instagram – fertig eingerichtet, zum Festpreis, von einer Person. Für Gastronomie, Ferienvermietung, Handwerk und Studios.",
         "primary": {"text": "Unverbindlich anfragen", "href": "#anfrage"}, "secondary": {"text": "Pakete ab 549 € ansehen", "href": "/pakete"},
         "image": "hero-kristina", "alt": "Kristina, Gründerin von KWiDi, auf einer Terrasse"},
        {"type": "text", "bg": "sand", "h2": "Die meisten Websites bringen nichts. Nicht, weil sie schlecht aussehen.",
         "paragraphs": ["Sondern weil sie nur da sind. Niemand findet sie, niemand versteht in fünf Sekunden, was du anbietest, und niemand weiß, wie er dich erreicht. Eine Website allein ist wie ein Restaurant ohne Schild an der Straße.", "Deshalb baue ich nicht nur die Website. Ich baue die Wege, über die Gäste zu dir finden."]},
        {"type": "chain", "h2": "So werden aus Klicks Gäste.", "items": CHAIN, "link": {"text": "Ausführlich erklärt", "href": "/so-funktioniert-es"}},
        {"type": "cards", "bg": "sand", "h2": "Für Betriebe, bei denen morgen jemand kommen soll.", "cols": 4, "items": [
            {"title": "Gastronomie", "text": "Restaurants, Cafés, Bars. Speisekarte, Reservierung, Google Maps, Instagram. Damit Dienstag nicht leer bleibt.", "href": "/fuer/gastronomie"},
            {"title": "Ferienvermietung", "text": "Ferienhaus oder Ferienwohnung, in Deutschland oder im Ausland. Mehrsprachig, mit Direktanfrage.", "href": "/fuer/ferienvermietung"},
            {"title": "Handwerk", "text": "Wer dich googelt, soll dich beauftragen. Google-Profil, Bewertungen, Anfrage mit einem Klick.", "href": "/fuer/handwerk"},
            {"title": "Praxen & Studios", "text": "Physio, Kosmetik, Massage, Heilpraktik, Tierarzt. Professioneller Auftritt, Terminanfrage inklusive.", "href": "/fuer/praxen-studios"},
        ]},
        {"type": "packages", "h2": "Vier Pakete. Alle Preise stehen hier.", "intro": "Einmal zahlen, die Website gehört dir. Kein Abo, keine Bindung. Alle Preise netto zzgl. MwSt.", "items": PACKAGES_SHORT, "link": {"text": "Alle Details und was nicht enthalten ist", "href": "/pakete"}},
        {"type": "highlight", "h2": "Du hast schon eine Website – und sie bringt nichts?", "paragraphs": ["Dann bist du nicht allein. Ich schaue mir Website, Google-Profil und Instagram an und schreibe dir in Klartext, woran es liegt. Der Sichtbarkeits-Check kostet 60 € – und wird dir bei jedem Paket voll angerechnet."],
         "buttons": [{"text": "Zum Sichtbarkeits-Check", "href": "/sichtbarkeits-check"}, {"text": "Mehr über den Umbau", "href": "/website-ohne-anfragen"}], "big": "60 €"},
        {"type": "split", "image_left": True, "image": "about-hands", "alt": "Hände über einem Notizbuch, Espressotasse, Schatten eines Palmblatts", "h2": "Eine Person. Ein Preis. Keine Warteschleife.",
         "paragraphs": ["Hinter KWiDi stehe ich, Kristina. Ich habe ein Instagram-Profil in vier Monaten auf 6.000 Follower gebracht – organisch, ohne Anzeigen – und führe den Online-Auftritt eines Premium-Dienstleisters auf Mallorca, wo ich lebe. Ich weiß, worauf es ankommt, weil ich es täglich selbst mache."],
         "bullets": [{"title": "Alles aus einer Hand.", "text": "Website, Google, Instagram, Facebook – ein Ansprechpartner, ein Preis."}, {"title": "Du lieferst fast nichts.", "text": "Texte und Bilder kommen von mir. Du gibst frei."}, {"title": "Du verstehst, was du kaufst.", "text": "Ich erkläre dir, wie daraus Gäste werden – ohne Fachchinesisch."}, {"title": "Danach nicht allein.", "text": "Änderungswünsche später? Gleiche Ansprechpartnerin."}],
         "link": {"text": "Mehr über mich", "href": "/ueber-mich"}},
        {"type": "cards", "bg": "sand", "h2": "Was ich selbst aufgebaut habe.", "cols": 3, "items": [
            {"big": "6.000", "title": "Follower in 4 Monaten", "text": "Ein Instagram-Profil, organisch aufgebaut. Ohne Anzeigen, ohne Gewinnspiele – mit Beiträgen, die Menschen wirklich sehen wollten."},
            {"big": "1", "title": "Premium-Dienstleister, komplett online", "text": "Website, Google-Profil und Social Media eines Betriebs für Finca-Betreuung und Vermietung – aufgebaut und laufend geführt."},
            {"big": "Du?", "title": "Dein Betrieb hier", "text": "Die ersten Kundenprojekte bekommen einen Sonderpreis – und einen Platz auf dieser Seite.", "href": "#anfrage", "link_text": "Anfragen"},
        ]},
        {"type": "faq", "items": HOME_FAQ},
        FORM,
    ],
})

# ---------------- PAKETE ----------------
PAKETE_FAQ = [
    {"q": "Sind die Preise netto oder brutto?", "a": "Netto, zzgl. der gesetzlichen Mehrwertsteuer. Für Firmenkunden in Deutschland, Österreich und der Schweiz wird die Rechnung im Reverse-Charge-Verfahren gestellt – dein Steuerberater kennt das."},
    {"q": "Was kostet eine Website monatlich?", "a": "Bei KWiDi nichts. Du zahlst einmal. Nur Domain und Hosting laufen bei deinem Anbieter weiter."},
    {"q": "Was ist der Unterschied zu Wix, Jimdo oder IONOS?", "a": "Dort baust du selbst oder bekommst eine Vorlage im Abo. Bei mir bekommst du eine individuelle Website mit eigenen Texten – und auf Wunsch Google-Profil und Instagram gleich mit. Und die Seite gehört dir."},
    {"q": "Wie viele Änderungsrunden sind enthalten?", "a": "Wir arbeiten so lange, bis es passt – innerhalb des vereinbarten Umfangs. Was das konkret heißt, besprechen wir vor dem Start."},
    {"q": "Wie lange dauert es?", "a": "Das hängt davon ab, wie schnell du Rückmeldung gibst. In der Regel ist eine Website in zwei bis drei Wochen online."},
]
PAGES.append({
    "url": "/pakete", "title": "Website Pakete & Preise – Festpreis ab 549 € | KWiDi",
    "description": "Vier Pakete, alle Preise netto und öffentlich: Website ab 549 €, mit Google-Profil 729 €, mit Instagram & Facebook 1.490 €, Rundum 2.990 €. Kein Abo.",
    "template": "page",
    "jsonld": [
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in PAKETE_FAQ]},
        {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
            {"@type": "Offer", "name": p["name"], "price": p["price"].replace("ab ", "").replace(" €", "").replace(".", ""), "priceCurrency": "EUR", "priceSpecification": {"@type": "UnitPriceSpecification", "valueAddedTaxIncluded": False, "priceCurrency": "EUR"}, "seller": {"@type": "Organization", "name": "KWiDi"}} for p in PACKAGES_FULL]},
    ],
    "blocks": [
        {"type": "hero", "short": True, "label": "Preise", "h1": "Pakete und Preise – einmal zahlen, gehört dir.", "text": "Keine Abos, keine versteckten Kosten, keine Überraschung nach zwölf Monaten. Alle Preise netto zzgl. MwSt."},
        {"type": "packages", "bg": "sand", "h2": "Die vier Pakete im Überblick", "items": PACKAGES_FULL,
         "extra": {"name": "Individuell", "price": "auf Anfrage", "text": "Mehr Seiten, andere Sprachen, längere Betreuung, ein Betreuungskonzept nur für dich. Schreib mir, was du brauchst.", "button": "Anfragen"}},
        {"type": "list", "rows": True, "h2": "Zusätzlich buchbar", "items": [
            {"title": "Werbeanzeigen", "text": "Bild-Anzeigen auf Instagram und Facebook – Preis auf Anfrage. Das Werbebudget zahlst du direkt an Meta, es ist nicht im Preis enthalten."},
            {"title": "Sichtbarkeits-Check", "text": "60 €, bei Buchung eines Pakets voll angerechnet.", "href": "/sichtbarkeits-check"},
            {"title": "Weitere Sprachen", "text": "Deine Website mehrsprachig, z. B. für Ferienvermieter. Preis auf Anfrage."},
        ]},
        {"type": "list", "bg": "sand", "h2": "Was nicht enthalten ist", "intro": "Damit es keine Überraschung gibt:", "items": ["Laufende Kosten für Domain und Hosting (bei deinem Anbieter, meist unter 10 €/Monat)", "Werbebudget für Anzeigen", "Onlineshop-Funktionen", "Professionelle Fotoshootings vor Ort (auf Anfrage möglich)"]},
        {"type": "table", "h2": "Was eine Website bei Baukasten-Anbietern wirklich kostet.", "head": ["", "Baukasten „erstellen lassen“", "KWiDi"], "rows": [
            ["Preis im ersten Jahr", "ca. 560–740 € (Einrichtung + Monatsgebühr)", "ab 549 € einmalig"],
            ["Danach", "360–1.020 € jedes Jahr", "0 €"],
            ["Seiten", "3", "4"],
            ["Texte", "Textbausteine", "individuell von mir"],
            ["Google-Profil", "nicht enthalten", "ab 729 € enthalten"],
            ["Instagram, Facebook", "nicht enthalten", "ab 1.490 € enthalten"],
            ["Gehört dir", "nein – endet mit dem Abo", "ja"],
        ], "note": "Zahlen laut öffentlichen Preisseiten der Anbieter, Stand September 2026."},
        {"type": "faq", "h2": "Was kostet eine Website wirklich?", "items": PAKETE_FAQ},
        {**FORM, "interest": "Neue Website"},
    ],
})

# ---------------- RELAUNCH ----------------
RELAUNCH_FAQ = [
    {"q": "Warum wird meine neue Website bei Google nicht gefunden?", "a": "Neue Seiten brauchen Wochen, bis Google sie überhaupt kennt – und ohne Google-Unternehmensprofil, saubere Seitentitel und ein paar Verweise von außen bleibt sie unsichtbar. Genau das richte ich beim Umbau ein."},
    {"q": "Was kostet es, eine Website überarbeiten zu lassen?", "a": "Bei KWiDi ab 549 € netto – derselbe Preis wie eine neue Website. Was genau nötig ist, klärt der Sichtbarkeits-Check."},
    {"q": "Muss ich eine komplett neue Website machen?", "a": "Nicht unbedingt. Oft reicht es, Struktur, Texte und Google-Profil neu aufzusetzen. Was bleiben kann, bleibt."},
    {"q": "Kann ich meine Domain behalten?", "a": "Ja. Deine Adresse bleibt, deine Google-Bewertungen bleiben, nichts geht verloren."},
]
PAGES.append({
    "url": "/website-ohne-anfragen", "title": "Website wird nicht gefunden? Relaunch ab 549 € | KWiDi",
    "description": "Deine Website bringt keine Anfragen? Ich sage dir in Klartext, woran es liegt – und baue sie so um, dass Gäste kommen. Festpreis, kein Abo.",
    "template": "page",
    "jsonld": [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in RELAUNCH_FAQ]}],
    "blocks": [
        {"type": "hero", "short": True, "label": "Umbau · Relaunch", "h1": "Deine Website ist da. Aber wo bleiben die Anfragen?", "text": "Du hast Geld und Zeit in eine Website gesteckt – und es passiert nichts. Das liegt fast nie am Design. Ich sage dir, woran es liegt, und baue sie so um, dass sie arbeitet.",
         "primary": {"text": "Sichtbarkeits-Check für 60 €", "href": "/sichtbarkeits-check"}, "secondary": {"text": "Umbau ab 549 €", "href": "#umbau"}},
        {"type": "reasons", "h2": "Fünf Gründe, warum eine Website keine Anfragen bringt.", "items": [
            {"title": "Niemand findet sie.", "text": "Kein Google-Unternehmensprofil, keine Verknüpfung, keine Seitentitel, die jemand sucht. Die Website existiert – aber nur für dich."},
            {"title": "Niemand versteht sie.", "text": "Der Besucher braucht fünf Sekunden, um zu wissen: Was machst du, für wen, und was soll ich jetzt tun? Wenn er das nicht sofort sieht, ist er weg."},
            {"title": "Sie sieht auf dem Handy nicht gut aus.", "text": "Drei von vier Besuchern kommen über das Smartphone. Wenn dort die Speisekarte nicht lesbar ist oder der Anfrage-Button fehlt, verlierst du drei von vier Gästen."},
            {"title": "Es fehlt der Grund, dir zu vertrauen.", "text": "Keine Bilder von dir, keine Bewertungen, kein klarer Prozess. Der Besucher kennt dich nicht – die Website muss das ändern."},
            {"title": "Es gibt keinen einfachen Weg zu dir.", "text": "Das Kontaktformular hat zwölf Felder, die Telefonnummer ist versteckt, der Reservierungslink fehlt. Jede Hürde kostet Anfragen."},
        ]},
        {"type": "text", "bg": "sand", "h2": "Warum deine Website bei Google nicht gefunden wird.", "paragraphs": ["Meistens sind es drei Dinge: Das Google-Unternehmensprofil fehlt oder ist unvollständig, die Seiten haben keine Titel, nach denen jemand sucht, und nichts auf der Seite sagt Google, wofür du eigentlich stehst. Alle drei lassen sich beheben – ohne die Website neu zu bauen."]},
        {"type": "chain", "h2": "So wird aus deiner Website ein Weg zu Gästen.", "intro": "Wenn eines der drei fehlt, bricht die Kette. Beim Umbau schaue ich mir alle drei an.", "items": CHAIN, "link": {"text": "Ausführlich erklärt", "href": "/so-funktioniert-es"}},
        {"type": "highlight", "h2": "Erst verstehen, dann umbauen.", "paragraphs": ["Beim Sichtbarkeits-Check prüfe ich Website, Google-Profil und Instagram und schicke dir per E-Mail drei bis fünf Punkte in Klartext – was fehlt, was stört, was zuerst dran ist. 60 € netto, bei jedem Paket voll angerechnet. Kein automatischer Report, sondern meine Einschätzung."],
         "buttons": [{"text": "Check buchen", "href": "/sichtbarkeits-check"}], "big": "60 €"},
        {"type": "text", "h2": "Umbau zum Festpreis – ab 549 €.", "paragraphs": ["Du behältst deine Domain und alles, was funktioniert. Ich strukturiere neu, schreibe die Texte, richte das Google-Profil ein und sorge dafür, dass die Seite auf dem Handy so gut aussieht wie am Rechner. Auf Wunsch kommen Instagram und Facebook dazu."], "link": {"text": "Pakete ansehen", "href": "/pakete"}},
        {"type": "faq", "items": RELAUNCH_FAQ},
        {**FORM, "interest": "Bestehende Website verbessern"},
    ],
})

# ---------------- SICHTBARKEITS-CHECK ----------------
CHECK_FAQ = [
    {"q": "Ist der Check automatisch oder manuell?", "a": "Manuell. Ich schaue selbst hin – so wie ein Gast es tun würde."},
    {"q": "Was passiert nach dem Check?", "a": "Nichts, wenn du nichts willst. Wenn du umbauen möchtest, rechne ich die 60 € auf das Paket an."},
    {"q": "Ich habe noch keine Website – lohnt sich der Check trotzdem?", "a": "Ja, wenn du ein Google-Profil oder ein Instagram-Konto hast. Dann prüfe ich diese beiden und sage dir, was eine Website ergänzen müsste."},
]
PAGES.append({
    "url": "/sichtbarkeits-check", "title": "Website analysieren lassen – Sichtbarkeits-Check 60 € | KWiDi",
    "description": "Ich prüfe Website, Google-Profil und Instagram und schicke dir 3–5 Punkte in Klartext. 60 € netto, bei Buchung eines Pakets voll angerechnet.",
    "template": "page",
    "jsonld": [
        {"@context": "https://schema.org", "@type": "Service", "name": "Sichtbarkeits-Check", "provider": {"@type": "Organization", "name": "KWiDi"}, "offers": {"@type": "Offer", "price": "60", "priceCurrency": "EUR"}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in CHECK_FAQ]},
    ],
    "blocks": [
        {"type": "hero", "short": True, "label": "60 € · wird angerechnet", "h1": "Sichtbarkeits-Check: Warum kommen keine Gäste?", "text": "Ich schaue mir an, was ein Gast sieht, wenn er dich sucht – und schreibe dir, was ihn davon abhält, zu kommen.", "primary": {"text": "Check buchen", "href": "#anfrage"}},
        {"type": "cards", "bg": "sand", "h2": "Drei Blicke, die entscheiden.", "cols": 3, "items": [
            {"title": "Google", "text": "Taucht dein Betrieb auf der Karte auf? Ist das Profil vollständig, sind die Bilder gut, passen die Kategorien?"},
            {"title": "Website", "text": "Versteht ein Fremder in fünf Sekunden, was du machst? Funktioniert sie auf dem Handy? Führt sie zur Anfrage?"},
            {"title": "Instagram und Facebook", "text": "Wirkt das Profil wie ein Betrieb oder wie ein Privatkonto? Gibt es einen Weg zur Website?"},
        ]},
        {"type": "split", "image": "check-note", "alt": "Ein Blatt Papier mit drei handschriftlichen Punkten, Espressotasse, Kiwi-Scheibe", "h2": "Eine E-Mail. Drei bis fünf Punkte. Klartext.", "paragraphs": ["Kein automatischer Report mit Punktzahlen, sondern meine Einschätzung: Was fehlt, was stört, was zuerst dran ist – und was du davon selbst erledigen kannst. Innerhalb von drei Werktagen."]},
        {"type": "highlight", "h2": "60 € – und bei Buchung geschenkt.", "paragraphs": ["Der Check kostet 60 € netto. Entscheidest du dich danach für ein Paket, ziehe ich die 60 € komplett ab. Du verlierst also nichts – außer der Ungewissheit."], "big": "60 €"},
        {"type": "steps", "inline": True, "h2": "So läuft es", "items": [
            {"text": "Du schickst mir die Links (Website, Google-Profil, Instagram – was du hast)."},
            {"text": "Ich schaue hin und schreibe dir innerhalb von drei Werktagen."},
            {"text": "Du entscheidest, ob und was du ändern willst. Kein Druck."},
        ]},
        {"type": "faq", "items": CHECK_FAQ},
        {**FORM, "variant": "check", "h2": "Check buchen", "text": "Schick mir die Links – ich melde mich innerhalb von drei Werktagen mit meiner Einschätzung.", "button": "Check für 60 € buchen", "note": "Du bekommst eine Rechnung per E-Mail. Der Check startet nach Zahlungseingang."},
    ],
})

# ---------------- BRANCHEN ----------------
PAGES.append(industry_page("gastronomie", "Restaurant Website erstellen lassen ab 549 € | KWiDi",
    "Website mit Speisekarte, Google-Profil und Instagram für Restaurants, Cafés und Bars – fertig eingerichtet zum Festpreis ab 549 €.",
    {"type": "hero", "label": "Restaurants · Cafés · Bars", "h1": "Dienstag muss nicht leer bleiben.", "text": "Website mit Speisekarte, Google-Profil und Instagram – fertig eingerichtet, damit Gäste dich finden, bevor sie Hunger haben.", "primary": {"text": "Unverbindlich anfragen", "href": "#anfrage"}, "secondary": {"text": "Pakete ab 549 €", "href": "/pakete"}, "image": "hero-gastro", "alt": "Gedeckter Tisch auf einer Terrasse, ein Smartphone neben dem Teller"},
    [
        {"type": "text", "bg": "sand", "h2": "So finden Gäste heute ein Restaurant.", "paragraphs": ["Nicht über deinen Namen. Sondern über „Italiener in der Nähe“, „Frühstück + Stadtteil“, „Bar mit Terrasse“. Sie schauen auf die Karte, auf die Bewertungen, auf drei Fotos – und entscheiden in einer Minute. Wer dort nicht auftaucht, existiert für diesen Gast nicht."]},
        {"type": "chain", "h2": "Gefunden. Überzeugt. Wiedergekommen.", "items": [
            {"title": "Google-Profil", "sub": "Gefunden werden", "text": "Öffnungszeiten, Karte, Fotos, Bewertungen – das, was der Gast zuerst sieht. Ich richte es vollständig ein."},
            {"title": "Website", "sub": "Überzeugen", "text": "Speisekarte in dreißig Sekunden auf dem Handy lesbar, Reservierung mit einem Klick, Bilder, die Appetit machen."},
            {"title": "Instagram", "sub": "Im Kopf bleiben", "text": "Das Gericht von heute, die Terrasse am Abend, das Team. Damit man an dich denkt, wenn der Samstag geplant wird."},
        ]},
        {"type": "split", "bg": "sand", "image": "detail-menu", "alt": "Speisekarte auf dem Smartphone", "h2": "Was deine Restaurant-Website enthält.", "bullets": ["Speisekarte, die du selbst ändern kannst", "Öffnungszeiten, Adresse, Anfahrt mit Google Maps", "Reservierung: Link zu deinem System oder ein Anfrageformular", "Galerie mit deinen besten Bildern", "Seiten für Events, Feiern, Catering – wenn du das anbietest", "Impressum und Datenschutz"]},
        {"type": "highlight", "h2": "Was zwei Tische mehr pro Woche bedeuten.", "paragraphs": ["Zwei zusätzliche Tische pro Woche, im Schnitt 60 € pro Tisch: Das sind über 6.000 € im Jahr. Die Website kostet einmal 549 €. Du musst nicht rechnen können, um zu sehen, dass sich das lohnt."], "big": "6.240 €"},
        {"type": "packages", "h2": "Mein Paket für Gastronomie: Website + Google + Social.", "intro": "Website mit Speisekarte, Google-Profil vollständig, Instagram und Facebook eingerichtet und mit sechs Beiträgen gefüllt. Weil Essen das dankbarste Instagram-Thema ist, das es gibt.", "items": [PACKAGES_SHORT[2]], "link": {"text": "Alle Pakete", "href": "/pakete"}},
    ], "Gastronomie",
    [
        {"q": "Was kostet eine Restaurant-Website?", "a": "Bei KWiDi ab 549 € netto. Mit Google-Profil 729 €, mit Instagram und Facebook 1.490 €."},
        {"q": "Kann ich die Speisekarte selbst ändern?", "a": "Ja, das bekommst du so eingerichtet, dass du Preise und Gerichte ohne mich anpassen kannst. Oder du schickst mir die Änderung – geht auch."},
        {"q": "Brauche ich eine Reservierungsfunktion?", "a": "Wenn du ein System nutzt (resmio, OpenTable, Quandoo …), binde ich es ein. Wenn nicht, reicht ein Anfrageformular oder ein Klick auf deine Telefonnummer."},
        {"q": "Lohnt sich Instagram für ein kleines Restaurant?", "a": "Ja – gerade für kleine. Ein gutes Bild vom Teller erreicht mehr Menschen als jede Anzeige in der Zeitung. Und du musst nicht täglich posten: Ich richte alles so ein, dass du mit zwei Beiträgen pro Woche gut dabei bist."},
    ], "Website für Gastronomie"))

PAGES.append(industry_page("ferienvermietung", "Ferienwohnung Website erstellen lassen – mehrsprachig | KWiDi",
    "Eigene Website für Ferienhaus oder Ferienwohnung – mehrsprachig, mit Direktanfrage und Google-Profil. Für Objekte in Deutschland oder im Ausland. Ab 549 €.",
    {"type": "hero", "label": "Ferienhaus · Ferienwohnung · Finca", "h1": "Dein Ferienhaus. Deine Website. Deine Buchungen.", "text": "Mehrsprachig, mit Direktanfrage und Google-Profil – für Eigentümer, deren Objekt in Deutschland, am Mittelmeer oder sonst wo in Europa steht.", "primary": {"text": "Unverbindlich anfragen", "href": "#anfrage"}, "secondary": {"text": "Pakete ab 549 €", "href": "/pakete"}, "image": "hero-fewo", "alt": "Bogengang mit Blick aufs Meer, Rattanstuhl, Notizbuch mit Kalender"},
    [
        {"type": "text", "bg": "sand", "h2": "Booking und Airbnb bringen Gäste. Aber sie gehören dir nicht.", "paragraphs": ["Jede Buchung über ein Portal kostet dich 15 bis 20 Prozent. Der Gast kennt dein Haus, aber nicht dich. Wenn er wiederkommen will, bucht er wieder über das Portal – und du zahlst wieder. Eine eigene Website ändert das: Wiederbucher, Empfehlungen und alle, die dich über Google suchen, buchen direkt."]},
        {"type": "chain", "h2": "So finden Gäste dein Ferienhaus direkt.", "items": [
            {"title": "Google-Profil für dein Objekt", "sub": "Gefunden werden", "text": "Ja, auch ein Ferienhaus kann auf der Karte stehen – mit Fotos, Bewertungen und einem Link zu dir."},
            {"title": "Website", "sub": "Überzeugen", "text": "Bilder, Ausstattung, Lage, Preise, Belegungskalender, Anfrage in einer Minute. In der Sprache deiner Gäste."},
            {"title": "Instagram", "sub": "Im Kopf bleiben", "text": "Der Blick von der Terrasse, der Markt im Dorf, der Weg zum Strand. Damit Gäste schon Urlaub machen, bevor sie buchen."},
        ]},
        {"type": "cards", "bg": "sand", "h2": "Mehrsprachig. Angebunden. Aus Erfahrung.", "cols": 3, "items": [
            {"title": "Mehrsprachig eingerichtet", "text": "Deutsch und Englisch sind Standard, weitere Sprachen richte ich nach Bedarf ein. So wie diese Seite: Klick oben rechts auf EN – das bekommst du auch."},
            {"title": "Dein Buchungssystem bleibt", "text": "Nutzt du Smoobu, Lodgify oder ein anderes System? Ich binde den Belegungskalender ein, damit keine Doppelbuchung passiert. Du musst nichts umstellen."},
            {"title": "Ich lebe dort, wo eure Gäste Urlaub machen", "text": "Ich wohne auf Mallorca und führe den Online-Auftritt eines Betriebs, der Fincas betreut und vermietet. Ich weiß, wonach Gäste fragen, was sie auf Bildern sehen wollen und woran Anfragen scheitern."},
        ]},
        {"type": "highlight", "h2": "Zehn Direktbuchungen im Jahr – und die Website ist bezahlt.", "paragraphs": ["Eine Woche für 900 € über das Portal kostet dich 135 bis 180 € Provision. Zehn Wochen direkt gebucht: 1.350 € gespart. Die Website kostet einmal 549 €."], "big": "1.350 €"},
        {"type": "packages", "h2": "Mein Paket für Ferienvermieter: Website + Google.", "intro": "729 € netto – oder mit Instagram und Facebook für 1.490 €, wenn du dein Haus auch dort zeigen willst.", "items": [PACKAGES_SHORT[1], PACKAGES_SHORT[2]], "link": {"text": "Alle Pakete", "href": "/pakete"}},
    ], "Ferienvermietung",
    [
        {"q": "Kann ich meinen Belegungskalender von Booking oder Smoobu einbinden?", "a": "Ja. Kalender-Synchronisation über iCal oder direkt aus deinem System, damit alles auf einem Stand bleibt."},
        {"q": "In welchen Sprachen?", "a": "Deutsch und Englisch sind immer dabei. Weitere Sprachen richte ich ein – die Übersetzung läuft über ein System, das ich prüfe und anpasse."},
        {"q": "Lohnt sich eine eigene Website bei nur einem Objekt?", "a": "Ja, sobald du Wiederbucher hast oder haben willst. Ein Objekt, das jedes Jahr fünf Wochen direkt vermietet wird, spart mehr Provision, als die Website kostet."},
        {"q": "Mein Haus liegt im Ausland – was muss ich beachten?", "a": "Auf der Website: nichts Besonderes. Für Steuern und Vermietungsrecht im jeweiligen Land frag bitte deinen Steuerberater – das ist nicht meine Baustelle, aber ich sage dir, was auf die Seite muss."},
    ], "Website für Ferienvermietung"))

PAGES.append(industry_page("handwerk", "Handwerker Website erstellen lassen ab 549 € | KWiDi",
    "Website und Google-Unternehmensprofil für Handwerksbetriebe – seriös, schnell gefunden, mit Klick zur Anfrage. Festpreis, kein Abo, Texte inklusive.",
    {"type": "hero", "label": "Handwerksbetriebe", "h1": "Wer dich googelt, soll dich beauftragen.", "text": "Website und Google-Unternehmensprofil für Handwerksbetriebe – seriös, schnell gefunden, mit einem Klick zur Anfrage.", "primary": {"text": "Unverbindlich anfragen", "href": "#anfrage"}, "secondary": {"text": "Pakete ab 549 €", "href": "/pakete"}, "image": "hero-handwerk", "alt": "Werkbank aus Holz, Hände mit Zollstock im Sonnenlicht"},
    [
        {"type": "text", "bg": "sand", "h2": "So suchen Kunden heute einen Handwerker.", "paragraphs": ["„Elektriker + Ort“, „Dachdecker in der Nähe“, „Malerbetrieb Bewertungen“. Sie sehen drei Betriebe auf der Karte, vergleichen Sterne und Fotos und rufen den an, der am vertrauenswürdigsten wirkt. Empfehlungen reichen nicht mehr, wenn die Empfohlenen online nicht zu finden sind."]},
        {"type": "text", "h2": "Google-Profil: Karte, Bewertungen, Anruf.", "paragraphs": ["Für Handwerker ist das Google-Unternehmensprofil wichtiger als jede Website. Vollständig eingerichtet mit Leistungen, Einzugsgebiet, Fotos von der Baustelle und einem Anruf-Button. Ich richte es ein und verknüpfe es mit deiner Website."]},
        {"type": "split", "bg": "sand", "image": "detail-handwerk", "alt": "Google-Unternehmensprofil eines Handwerksbetriebs, angedeutet", "h2": "Was deine Handwerker-Website enthält.", "bullets": ["Deine Leistungen, klar und ohne Fachchinesisch", "Einzugsgebiet", "Bilder von echten Projekten (wenn du keine hast, sage ich dir, welche fünf Fotos du mit dem Handy machen sollst)", "Anfrageformular und Klick-zum-Anrufen", "Über den Betrieb: Wer ihr seid, seit wann, was euch ausmacht", "Impressum und Datenschutz"]},
        {"type": "text", "h2": "Auch für Bewerber zählt der erste Eindruck.", "paragraphs": ["Wer sich bei dir bewerben will, googelt dich zuerst. Ein Betrieb mit ordentlichem Auftritt bekommt die besseren Bewerbungen. Eine Seite „Jobs“ ist im Paket drin, wenn du sie brauchst."]},
        {"type": "packages", "bg": "sand", "h2": "Mein Paket für Handwerk: Website + Google.", "intro": "729 € netto. Vier Seiten plus vollständiges Google-Profil – das, was Kunden und Bewerber zuerst sehen.", "items": [PACKAGES_SHORT[1]], "link": {"text": "Alle Pakete", "href": "/pakete"}},
    ], "Handwerk",
    [
        {"q": "Was kostet eine Handwerker-Website?", "a": "Ab 549 € netto, mit Google-Profil 729 €."},
        {"q": "Ich habe keine Fotos – geht das trotzdem?", "a": "Ja. Ich sage dir genau, welche Bilder du mit dem Handy machen sollst – und den Rest löse ich."},
        {"q": "Brauche ich Instagram als Handwerker?", "a": "Nicht unbedingt. Für die meisten Betriebe reichen Website und Google-Profil. Wenn du Vorher-Nachher-Bilder hast, kann Instagram ein guter Kanal für Bewerber sein – das besprechen wir."},
    ], "Website für Handwerk"))

PAGES.append(industry_page("praxen-studios", "Praxis & Studio Website erstellen lassen ab 549 € | KWiDi",
    "Website, Google-Profil und Instagram für Physiotherapie, Kosmetik, Massage, Heilpraktiker und Tierärzte – professionell, mit Terminanfrage. Festpreis.",
    {"type": "hero", "label": "Physio · Kosmetik · Massage · Heilpraktik · Tierarzt", "h1": "Dein Auftritt – so professionell wie deine Arbeit.", "text": "Website, Google-Profil und Instagram für Praxen und Studios – mit Terminanfrage, damit der Kalender voll wird.", "primary": {"text": "Unverbindlich anfragen", "href": "#anfrage"}, "secondary": {"text": "Pakete ab 549 €", "href": "/pakete"}, "image": "hero-studio", "alt": "Behandlungsraum in Sandtönen, gefaltetes Leinen, Olivenzweig"},
    [
        {"type": "text", "bg": "sand", "h2": "So finden neue Kunden eine Praxis oder ein Studio.", "paragraphs": ["Über Google und über Empfehlungen – und in beiden Fällen schauen sie sich vorher deinen Auftritt an. Wirkt er wie ein Privatkonto oder wie ein Betrieb, dem man seinen Rücken oder sein Gesicht anvertraut?"]},
        {"type": "split", "image": "detail-studio", "alt": "Terminbuch und Leinen", "h2": "Was deine Website enthält.", "bullets": ["Leistungen mit Preisen oder Preisrahmen", "Terminanfrage – oder Einbindung deines Buchungssystems", "Über dich: Ausbildung, Erfahrung, dein Ansatz", "Räume und Atmosphäre in Bildern", "Google-Bewertungen eingebunden", "Impressum und Datenschutz"]},
        {"type": "text", "bg": "sand", "h2": "Instagram für Studios: Zeigen, was du kannst.", "paragraphs": ["Behandlungsräume, Ergebnisse (wo erlaubt), Tipps, dein Team. Ich richte das Profil so ein, dass es zu deiner Website passt – und fülle es mit den ersten Beiträgen."]},
        {"type": "packages", "h2": "Mein Paket für Praxen & Studios: Website + Google + Social.", "intro": "1.490 € netto. Weil in dieser Branche Instagram oft der erste Kontakt ist – und Google der zweite.", "items": [PACKAGES_SHORT[2]], "link": {"text": "Alle Pakete", "href": "/pakete"}},
    ], "Praxis & Studio",
    [
        {"q": "Kann ich eine Online-Terminbuchung einbinden?", "a": "Ja. Wenn du ein System nutzt, binde ich es ein. Wenn nicht, bekommst du ein Terminanfrage-Formular."},
        {"q": "Was darf ich als Heilpraktiker oder Physio auf der Website schreiben?", "a": "Keine Heilversprechen, keine Vorher-Nachher-Bilder bei medizinischen Behandlungen – das regelt das Heilmittelwerbegesetz. Ich schreibe die Texte so, dass sie überzeugen, ohne diese Grenzen zu überschreiten. Die finale Prüfung liegt bei dir."},
        {"q": "Was kostet eine Praxis-Website?", "a": "Ab 549 € netto, mit Google-Profil 729 €, mit Instagram und Facebook 1.490 €."},
    ], "Website für Praxen & Studios"))

# ---------------- SO FUNKTIONIERT ES ----------------
PAGES.append({
    "url": "/so-funktioniert-es", "title": "Wie eine Website Gäste bringt – so funktioniert KWiDi",
    "description": "Google-Profil, Website, Instagram – wie das zusammenspielt und wie die Zusammenarbeit abläuft. In vier Schritten, ohne Fachchinesisch.",
    "template": "page",
    "jsonld": [{"@context": "https://schema.org", "@type": "HowTo", "name": "So läuft die Zusammenarbeit mit KWiDi", "step": [
        {"@type": "HowToStep", "name": "Du fragst an", "text": "Über das Formular, in zwei, drei Sätzen. Antwort innerhalb von 24 Stunden an Werktagen."},
        {"@type": "HowToStep", "name": "Wir klären, was du brauchst", "text": "Per E-Mail: Paket, Inhalte, vorhandenes Material. Danach ein Angebot."},
        {"@type": "HowToStep", "name": "Ich baue, du gibst frei", "text": "Entwurf, Feedback, Anpassung – bis es stimmt."},
        {"@type": "HowToStep", "name": "Alles geht online", "text": "Website, Google-Profil, Instagram – eingerichtet und verknüpft. Du bekommst alle Zugänge."},
    ]}],
    "blocks": [
        {"type": "hero", "short": True, "label": "Erklärt", "h1": "So werden aus Klicks Gäste.", "text": "Online sichtbar sein ist keine Technik-Frage. Es ist die Frage, ob morgen jemand kommt. Hier ist die Kette – und wie unsere Zusammenarbeit abläuft."},
        {"type": "split", "image_left": True, "image": "how-map", "alt": "Hände zeichnen eine Karte mit Stecknadel auf Papier", "label": "Schritt 1", "h2": "Gefunden werden – das Google-Unternehmensprofil.", "paragraphs": ["Wenn jemand „Café in der Nähe“ oder „Ferienhaus Kroatien Meerblick“ eingibt, zeigt Google zuerst die Karte. Dort stehen Betriebe mit vollständigem Profil: Öffnungszeiten, Fotos, Bewertungen, Kategorie. Wer kein Profil hat oder eines mit drei Angaben, ist nicht auf der Karte. Das Profil kostet nichts – die Arbeit ist, es richtig zu machen. Genau das ist in Paket 2 drin."]},
        {"type": "split", "bg": "sand", "image": "how-phone", "alt": "Smartphone in der Hand, Display zeigt eine helle Seite", "label": "Schritt 2", "h2": "Überzeugen – die Website.", "paragraphs": ["Der Klick vom Profil führt auf deine Website. Jetzt hat der Gast eine Frage: Passt das zu mir? Er will Bilder, Preise, ein Gefühl für den Ort und einen Weg, dich zu erreichen. Alles auf dem Handy, in dreißig Sekunden. Eine Website, die das schafft, bringt Anfragen. Eine, die es nicht schafft, bringt nichts – egal wie schön sie ist."]},
        {"type": "split", "image_left": True, "image": "how-photos", "alt": "Stapel Fotos von Tellern und Terrassen auf Leinen", "label": "Schritt 3", "h2": "Im Kopf bleiben – Instagram und Facebook.", "paragraphs": ["Die meisten Gäste kommen nicht beim ersten Kontakt. Sie sehen dich, vergessen dich, sehen dich wieder – und dann kommen sie. Instagram und Facebook sorgen für das Wiedersehen. Dafür brauchst du kein tägliches Posten, sondern ein Profil, das wie ein Betrieb aussieht, und ein paar gute Beiträge zum Start. Das ist Paket 3."]},
        {"type": "text", "bg": "sand", "h2": "Ist Instagram für kleine Betriebe überhaupt sinnvoll?", "paragraphs": ["Für Gastronomie, Studios und Ferienvermieter: ja, eindeutig – weil Bilder dort verkaufen. Für Handwerker: meistens reicht Google. Ich sage dir ehrlich, wenn du etwas nicht brauchst."]},
        {"type": "steps", "h2": "So läuft die Zusammenarbeit.", "items": [
            {"title": "Du fragst an.", "text": "Über das Formular, in zwei, drei Sätzen. Ich antworte innerhalb von 24 Stunden an Werktagen."},
            {"title": "Wir klären, was du brauchst.", "text": "Per E-Mail: Welches Paket, welche Inhalte, was du schon hast. Danach bekommst du ein Angebot."},
            {"title": "Ich baue, du gibst frei.", "text": "Du bekommst einen Entwurf, sagst, was passt und was nicht. Wir arbeiten, bis es stimmt."},
            {"title": "Alles geht online.", "text": "Website, Google-Profil, Instagram – eingerichtet und verknüpft. Du bekommst alle Zugänge."},
        ], "note": "In der Regel dauert das zwei bis drei Wochen – abhängig davon, wie schnell du Rückmeldung gibst."},
        {"type": "highlight", "h2": "Was musst du liefern? Fast nichts.", "paragraphs": ["Ein paar Antworten auf meine Fragen, deine Öffnungszeiten, Preise – und wenn du hast, Bilder. Texte schreibe ich. Bilder organisiere ich, wenn du keine hast. Technik ist komplett meine Sache."], "buttons": [{"text": "Unverbindlich anfragen", "href": "#anfrage"}]},
        FORM,
    ],
})

# ---------------- ÜBER MICH ----------------
PAGES.append({
    "url": "/ueber-mich", "title": "Über KWiDi – Kristina, eine Ansprechpartnerin für alles",
    "description": "Hinter KWiDi steht eine Person: Kristina. 6.000 Follower in 4 Monaten selbst aufgebaut, Online-Auftritte für Betriebe geführt. Kein Team, kein Ticketsystem.",
    "template": "page",
    "jsonld": [{"@context": "https://schema.org", "@type": "Person", "name": "Kristina", "jobTitle": "Gründerin", "worksFor": {"@type": "Organization", "name": "KWiDi", "url": "https://kriswidi.com"}}],
    "blocks": [
        {"type": "hero", "label": "Über mich", "h1": "Hallo, ich bin Kristina.", "text": "Hinter KWiDi steht keine Agentur, sondern ich. Ich baue Websites und Online-Auftritte für kleine Betriebe – und erkläre dabei so, dass man versteht, was man kauft.", "image": "hero-kristina", "alt": "Kristina, Gründerin von KWiDi"},
        {"type": "split", "image": "about-hands", "alt": "Hände über einem Notizbuch, Espressotasse", "h2": "Warum KWiDi.", "paragraphs": ["Ich habe zu oft gesehen, wie kleine Betriebe Geld für eine Website ausgeben und dann nichts passiert. Nicht, weil die Website schlecht war. Sondern weil niemand ihnen gesagt hat, dass die Website nur ein Teil ist – und Google und Instagram die anderen zwei. KWiDi ist mein Versuch, das anders zu machen: alles aus einer Hand, zu einem Preis, den man sich leisten kann, und mit einer Erklärung, die man versteht."], "quote": "Der Name? Kristina Swiderski und Kiwi. Frisch, ehrlich, nicht kompliziert."},
        {"type": "cards", "bg": "sand", "h2": "Was ich selbst aufgebaut habe.", "cols": 3, "items": [
            {"big": "6.000", "title": "Follower in vier Monaten", "text": "Ein Instagram-Profil, organisch, ohne Anzeigen. Mit Beiträgen über Mallorca, wo ich lebe."},
            {"big": "1", "title": "Premium-Dienstleister", "text": "Den Online-Auftritt eines Betriebs für Finca-Betreuung und Vermietung: Website, Google-Profil, Social Media, laufende Betreuung."},
            {"big": "Bald", "title": "Die ersten KWiDi-Kunden", "text": "Die ersten Betriebe bekommen einen Sonderpreis – dafür darf ich sie hier zeigen.", "href": "#anfrage", "link_text": "Anfragen"},
        ]},
        {"type": "cards", "h2": "Wie ich arbeite.", "cols": 2, "items": [
            {"title": "Per E-Mail.", "text": "Nicht, weil ich nicht reden mag – sondern weil so alles nachlesbar bleibt und ich mich konzentriert um dein Projekt kümmern kann. Du bekommst innerhalb von 24 Stunden an Werktagen eine Antwort."},
            {"title": "Zum Festpreis.", "text": "Du weißt vorher, was es kostet. Ohne Abo, ohne Überraschung."},
            {"title": "Ehrlich.", "text": "Wenn du etwas nicht brauchst, sage ich es. Ein Handwerker braucht kein Instagram. Ein Café schon."},
            {"title": "Danach erreichbar.", "text": "Änderungswünsche in einem Jahr? Schreib mir. Gleiche Person, gleiche Adresse."},
        ]},
        FORM,
    ],
})

# ---------------- KONTAKT ----------------
PAGES.append({
    "url": "/kontakt", "title": "Kontakt – Anfrage an KWiDi",
    "description": "Schreib mir kurz, was du vorhast. Antwort innerhalb von 24 Stunden an Werktagen – per E-Mail, ohne Telefontermin.",
    "template": "page",
    "jsonld": [{"@context": "https://schema.org", "@type": "ContactPage", "name": "Kontakt – KWiDi", "url": "https://kriswidi.com/kontakt"}],
    "blocks": [
        {"type": "form", "bg": "ivory", "as_h1": True, "h2": "Lass uns kurz schauen, was für dich passt.", "text": "Schreib mir, was du vorhast – zwei, drei Sätze reichen. Ich antworte innerhalb von 24 Stunden an Werktagen, per E-Mail. Kein Verkaufsgespräch, keine Warteschleife.",
         "aside": ["<b>Schon eine Website?</b> Dann ist der Sichtbarkeits-Check vielleicht der bessere erste Schritt. <a class=\"link\" href=\"/sichtbarkeits-check\">Mehr</a>"]},
    ],
})

# ---------------- DANKE / 404 / RECHTLICHES ----------------
PAGES.append({"url": "/danke", "title": "Danke – KWiDi", "description": "Deine Nachricht ist angekommen.", "template": "page", "noindex": True, "lead": True, "jsonld": [],
    "blocks": [{"type": "simple", "h1": "Danke – deine Nachricht ist da.", "paragraphs": ["Ich melde mich innerhalb von 24 Stunden an Werktagen bei dir. Schau in der Zwischenzeit gern, wie die Zusammenarbeit abläuft."], "buttons": [{"text": "So funktioniert's", "href": "/so-funktioniert-es"}, {"text": "Zurück zur Startseite", "href": "/"}]}]})

PAGES.append({"url": "/404", "title": "Seite nicht gefunden – KWiDi", "description": "Diese Seite gibt es nicht.", "template": "page", "noindex": True, "jsonld": [],
    "blocks": [{"type": "simple", "h1": "Diese Seite gibt es nicht.", "paragraphs": ["Vielleicht ist der Link alt – oder ich habe umgebaut. Hier geht's weiter:"], "buttons": [{"text": "Startseite", "href": "/"}, {"text": "Pakete & Preise", "href": "/pakete"}, {"text": "Kontakt", "href": "/kontakt"}]}]})

IMPRESSUM_HTML = """
<p class="lede">Angaben gemäß § 5 DDG</p>
<p><b>KWiDi</b> ist eine Marke der<br>
<b>Swiderski Property Management S.L.</b><br>
Calle San Miguel 36, PTA B5<br>
07002 Palma de Mallorca, Illes Balears, Spanien</p>
<h2>Vertreten durch</h2>
<p>Patrick Swiderski, Administrador</p>
<h2>Kontakt</h2>
<p>E-Mail: <a href="mailto:kristinaswiderski@outlook.com">kristinaswiderski@outlook.com</a><br>Telefon: +34 601 993 373</p>
<h2>Registereintrag</h2>
<p>Eingetragen im Registro Mercantil de las Illes Balears, Palma de Mallorca<br>NIF: B21648753</p>
<h2>Umsatzsteuer-Identifikationsnummer</h2>
<p>ESB21648753</p>
<h2>Verantwortlich für den Inhalt</h2>
<p>Kristina Swiderski, Anschrift wie oben</p>
<h2>Streitbeilegung</h2>
<p>Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: <a href="https://ec.europa.eu/consumers/odr/" rel="noopener" target="_blank">https://ec.europa.eu/consumers/odr/</a>. Wir sind nicht verpflichtet und nicht bereit, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Haftung für Inhalte und Links</h2>
<p>Die Inhalte dieser Website wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte übernehmen wir jedoch keine Gewähr. Für Inhalte externer Links sind ausschließlich deren Betreiber verantwortlich; zum Zeitpunkt der Verlinkung waren keine Rechtsverstöße erkennbar.</p>
<p class="muted">Alle Angebote auf dieser Website richten sich an Unternehmer. Preise verstehen sich netto zzgl. gesetzlicher Umsatzsteuer.</p>
"""
PAGES.append({"url": "/impressum", "title": "Impressum – KWiDi", "description": "Impressum von KWiDi.", "template": "page", "noindex": True, "jsonld": [],
    "blocks": [{"type": "legal", "h1": "Impressum", "html": IMPRESSUM_HTML}]})

DATENSCHUTZ_HTML = """
<p class="lede">Stand: September 2026</p>
<h2>1. Verantwortlicher</h2>
<p>Swiderski Property Management S.L. (Marke KWiDi), Calle San Miguel 36, PTA B5, 07002 Palma de Mallorca, Spanien · E-Mail: <a href="mailto:kristinaswiderski@outlook.com">kristinaswiderski@outlook.com</a></p>
<h2>2. Allgemeines</h2>
<p>Wir verarbeiten personenbezogene Daten nur, soweit dies zur Bereitstellung dieser Website und unserer Leistungen erforderlich ist oder du eingewilligt hast. Rechtsgrundlagen sind Art. 6 Abs. 1 lit. a (Einwilligung), lit. b (Vertrag/Anbahnung) und lit. f (berechtigtes Interesse) DSGVO.</p>
<h2>3. Hosting und Server-Logfiles</h2>
<p>Diese Website wird bei einem externen Hosting-Anbieter innerhalb der EU gehostet. Beim Aufruf werden automatisch Server-Logfiles verarbeitet (IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Browsertyp, Referrer). Diese Daten dienen der Sicherheit und Stabilität des Betriebs (Art. 6 Abs. 1 lit. f DSGVO) und werden nach spätestens 14 Tagen gelöscht. Mit dem Hosting-Anbieter besteht ein Vertrag zur Auftragsverarbeitung.</p>
<h2>4. Kontaktformular und E-Mail</h2>
<p>Wenn du uns über das Formular oder per E-Mail kontaktierst, verarbeiten wir die von dir angegebenen Daten (Name, E-Mail-Adresse, Angaben zum Betrieb, Nachricht, optional Links) zur Bearbeitung deiner Anfrage und für Anschlussfragen (Art. 6 Abs. 1 lit. b DSGVO). Die Formulardaten werden über den Dienst FormSubmit (formsubmit.co) an unsere E-Mail-Adresse weitergeleitet; der Anbieter verarbeitet die Daten ausschließlich zur Zustellung. Wir speichern Anfragen, bis die Bearbeitung abgeschlossen ist und keine gesetzlichen Aufbewahrungspflichten entgegenstehen.</p>
<h2>5. Cookies und Einwilligung</h2>
<p>Technisch notwendige Cookies bzw. Speichervorgänge (z. B. deine Cookie-Auswahl) setzen wir ohne Einwilligung ein (§ 25 Abs. 2 TDDDG). Statistik- und Marketing-Cookies werden erst gesetzt, wenn du im Cookie-Banner zustimmst. Deine Auswahl wird lokal in deinem Browser gespeichert und kann jederzeit über „Cookie-Einstellungen“ im Footer geändert oder widerrufen werden.</p>
<h2>6. Google Analytics 4</h2>
<p>Mit deiner Einwilligung (Art. 6 Abs. 1 lit. a DSGVO) nutzen wir Google Analytics 4 der Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Google Analytics verwendet Cookies und ähnliche Technologien, um die Nutzung der Website auszuwerten. IP-Adressen werden gekürzt verarbeitet. Daten können an Google LLC in die USA übermittelt werden; Google ist nach dem EU-US Data Privacy Framework zertifiziert. Wir setzen den Google Consent Mode ein, sodass ohne Einwilligung keine Cookies gesetzt werden. Speicherdauer: 14 Monate. Weitere Informationen: <a href="https://policies.google.com/privacy" rel="noopener" target="_blank">policies.google.com/privacy</a>.</p>
<h2>7. Meta-Pixel (Facebook, Instagram)</h2>
<p>Mit deiner Einwilligung (Art. 6 Abs. 1 lit. a DSGVO) nutzen wir das Meta-Pixel der Meta Platforms Ireland Limited, Merrion Road, Dublin 4, Irland, um die Wirksamkeit unserer Anzeigen zu messen und Zielgruppen zu bilden. Dabei können Daten an Meta Platforms Inc. in die USA übermittelt werden; Meta ist nach dem EU-US Data Privacy Framework zertifiziert. Wir sind mit Meta gemeinsam verantwortlich im Sinne von Art. 26 DSGVO für die Erhebung und Übermittlung; die weitere Verarbeitung verantwortet Meta. Informationen: <a href="https://www.facebook.com/privacy/policy" rel="noopener" target="_blank">facebook.com/privacy/policy</a>.</p>
<h2>8. Schriftarten</h2>
<p>Die verwendeten Schriften (Fraunces, Jost) werden lokal auf unserem Server bereitgestellt. Es findet keine Verbindung zu Servern von Google statt.</p>
<h2>9. Links zu Instagram und Facebook</h2>
<p>Unsere Website enthält Links zu unseren Profilen bei Instagram und Facebook. Es werden keine Inhalte dieser Plattformen eingebettet; erst beim Klick auf einen Link verlässt du unsere Website und es gelten die Datenschutzbestimmungen des jeweiligen Anbieters.</p>
<h2>10. Deine Rechte</h2>
<p>Du hast das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch (Art. 21 DSGVO). Eine erteilte Einwilligung kannst du jederzeit mit Wirkung für die Zukunft widerrufen. Außerdem hast du das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren – in Spanien bei der Agencia Española de Protección de Datos (AEPD), in Deutschland bei der für dich zuständigen Landesbehörde.</p>
<h2>11. Änderungen</h2>
<p>Wir passen diese Erklärung an, wenn sich die Rechtslage oder unsere Leistungen ändern. Es gilt die jeweils hier veröffentlichte Fassung.</p>
"""
PAGES.append({"url": "/datenschutz", "title": "Datenschutzerklärung – KWiDi", "description": "Datenschutzerklärung von KWiDi.", "template": "page", "noindex": True, "jsonld": [],
    "blocks": [{"type": "legal", "h1": "Datenschutzerklärung", "html": DATENSCHUTZ_HTML}]})
