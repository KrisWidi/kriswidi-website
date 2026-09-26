# -*- coding: utf-8 -*-
"""KWiDi – Betriebs-App (Jornado): Inhalte für Startseite und /betriebs-app (DE)."""

APP_NAME = "Betriebs-App"
APP_URL = "/betriebs-app"

# ---- Preise (Entscheidung Kristina: 249 € Einrichtung, 39 €/Monat inkl. 1 MA, +9 € je weiterer MA, monatlich kündbar) ----
APP_TARIF = {
    "type": "apptarif", "id": "preise", "bg": "sand",
    "h2": "Zwei Wege zu deiner App. Ein Monatspreis.",
    "intro": "Einmal einrichten lassen – fertig wie sie ist oder komplett auf deinen Betrieb zugeschnitten. Danach ein fester Monatsbetrag, monatlich kündbar. Alle Preise netto zzgl. MwSt.",
    "setups": [
        {"tag": "Standard · einmalig", "price": "249 €", "note": "Einrichtung durch mich", "for": "Die App, wie sie ist – mit allen Modulen, eingerichtet für deinen Betrieb.", "package": "Betriebs-App Standard", "button": "Standard anfragen",
         "features": ["Alle Module: Dienstplan, Zeiterfassung, Berichte, Aufträge, Anträge, Kosten & Fahrten", "Betrieb, Team, Kunden und Objekte angelegt", "Deine Dienstleistungen und Prüfpunkte hinterlegt", "Musterberichte in deinem Design", "Einweisung per Video-Call"]},
        {"tag": "Individuell · einmalig", "price": "4.695 €", "note": "Einrichtung und Anpassung durch mich", "for": "Deine App, exakt auf deinen Betrieb geschnitten – nur die Module, die du brauchst, plus das, was dir fehlt.", "package": "Betriebs-App Individuell", "button": "Individuell anfragen", "highlight": True,
         "features": ["Nur die Module, die du willst – der Rest verschwindet", "Eigene Module und Felder, die dein Betrieb braucht", "Abläufe, Freigaben und Berichte nach deinen Regeln", "Dein Design, dein Wording, deine Sprachen", "Datenübernahme aus deiner bisherigen Lösung", "Einweisung für dich und dein Team"]},
    ],
    "monthly": {"tag": "Monatlich · bei beiden", "price": "39 €", "note": "pro Monat, 1 Mitarbeiter inklusive", "for": "Gilt für Standard und Individuell gleichermaßen.",
                "features": ["Jeder weitere Mitarbeiter + 9 € / Monat", "Web-App für Handy, Tablet und PC – nichts installieren", "Updates und Betrieb inklusive", "Monatlich kündbar, keine Mindestlaufzeit"]},
    "calc": {"tag": "Was kostet es im Monat?", "label": "Mitarbeiter im Team", "base": 39, "per": 9, "setup": 249, "max": 25,
             "month_label": "pro Monat, netto – bei Standard und Individuell",
             "line": "{n} Mitarbeiter · {m} im Monat · plus Einrichtung einmalig (249 € Standard / 4.695 € Individuell)",
             "button": "App anfragen", "package": "Betriebs-App", "href": "#anfrage"},
    "notes": ["Alle Preise netto zzgl. MwSt.", "Keine Mindestlaufzeit, Kündigung zum Monatsende", "Standard-Einrichtung entfällt bei Buchung zusammen mit einem Website-Paket"],
}

APP_KIWI = {
    "hint_desktop": "Fahre über die Kerne", "hint_mobile": "Tippe auf einen Kern",
    "aria": "Die Module der Betriebs-App als Kerne einer Kiwi",
    "items": [
        {"name": "Dienstplan", "price": "Tag, Woche, Bedarf", "href": APP_URL + "#dienstplan"},
        {"name": "Zeiterfassung", "price": "Kommen, Pause, Gehen", "href": APP_URL + "#zeiterfassung"},
        {"name": "Berichte", "price": "mit Fotos & Freigabe", "href": APP_URL + "#berichte"},
        {"name": "Alles in einer App", "price": "für deinen Betrieb", "href": APP_URL, "primary": True},
        {"name": "Aufträge", "price": "Status & Zuweisung", "href": APP_URL + "#module"},
        {"name": "Anträge", "price": "Urlaub, Krank, Korrektur", "href": APP_URL + "#module"},
        {"name": "Kosten & Fahrten", "price": "Belege, Tankbuch, Export", "href": APP_URL + "#module"},
    ],
}

WEB_KIWI = {
    "hint_desktop": "Fahre über die Kerne", "hint_mobile": "Tippe auf einen Kern",
    "aria": "Die Website- und Online-Leistungen von KWiDi als Kerne einer Kiwi",
    "items": [
        {"name": "Sichtbarkeits-Check", "price": "60 €", "href": "/sichtbarkeits-check"},
        {"name": "Website", "price": "ab 549 €", "href": "/pakete#website"},
        {"name": "Website + Google", "price": "729 €", "href": "/pakete#website-google"},
        {"name": "Website + Google + Social", "price": "1.490 €", "href": "/pakete#website-google-social"},
        {"name": "Rundum", "price": "2.990 €", "href": "/pakete#rundum"},
        {"name": "Individuell", "price": "auf Anfrage", "href": "/pakete#individuell"},
    ],
}

HOME_FAQ = [
    {"q": "Was ist die Betriebs-App genau?", "a": "Eine Web-App für kleine Dienstleistungsbetriebe: Dienstplan, Zeiterfassung, Arbeitsberichte mit Fotos, Aufträge, Urlaubsanträge, Kosten und Kundenverwaltung – alles an einem Ort, vom Handy aus. Ich richte sie für dich ein, du und dein Team nutzt sie ab dem ersten Tag."},
    {"q": "Was kostet die App?", "a": "Standard: 249 € einmalig für die Einrichtung. Individuell: 4.695 € einmalig – dann ist die App exakt auf deinen Betrieb zugeschnitten. In beiden Fällen danach 39 € im Monat mit einem Mitarbeiter inklusive, jeder weitere Mitarbeiter 9 € im Monat. Monatlich kündbar, alle Preise netto."},
    {"q": "Was ist der Unterschied zwischen Standard und Individuell?", "a": "Standard ist die fertige App mit allen Modulen, eingerichtet mit deinen Daten. Individuell heißt: Wir bauen die App um deinen Betrieb herum – nur die Module, die du brauchst, eigene Felder und Abläufe, dein Design. Alles, was in deinem Alltag anders läuft als beim Standard, wird so abgebildet."},
    {"q": "Muss mein Team etwas installieren?", "a": "Nein. Die App läuft im Browser – auf jedem Handy, Tablet oder PC. Dein Mitarbeiter bekommt einen Link und seine Zugangsdaten, mehr nicht. Jeder nutzt die App in seiner Sprache: Du planst auf Deutsch, dein Mitarbeiter liest seinen Tag auf Russisch, Spanisch oder Arabisch."},
    {"q": "Brauche ich trotzdem noch eine Website?", "a": "Die App organisiert deinen Betrieb nach innen. Die Website bringt dir Kunden von außen. Beides kannst du bei mir bekommen – wer die App zusammen mit einem Website-Paket bucht, spart die Einrichtungsgebühr."},
    {"q": "Wie lange dauert die Einrichtung?", "a": "In der Regel ist dein Betrieb innerhalb von einer Woche startklar. Ich lege Team, Kunden, Objekte und deine Dienstleistungen an – du lieferst mir nur eine Liste. Dann gibt es eine Einweisung per Video-Call."},
    {"q": "Was ist mit meinen Daten?", "a": "Deine Daten gehören dir. Zeiten, Berichte und Kundendaten kannst du jederzeit exportieren, zum Beispiel als Excel für dein Steuerbüro."},
    {"q": "Kann ich dich anrufen?", "a": "Ich arbeite per E-Mail – so bleibt alles nachlesbar. Du bekommst innerhalb von 24 Stunden an Werktagen eine Antwort. Für die Einweisung in die App gibt es natürlich einen Video-Call."},
]

HOME_BLOCKS = [
    {"type": "hero", "label": "Die Betriebs-App für Kleinunternehmer",
     "h1": "Planen. Stempeln. Berichten. Fertig.",
     "text": "Alles, was dein Team und deine Kunden brauchen – von der App aus. Dienstplan, Zeiterfassung, Berichte, Aufträge, Kosten und Fahrten in einer App. Fertig eingerichtet oder komplett auf deinen Betrieb zugeschnitten.",
     "primary": {"text": "App unverbindlich anfragen", "href": "#anfrage"}, "secondary": {"text": "Preise ansehen", "href": "#preise"},
     "kiwi": APP_KIWI},
    {"type": "text", "bg": "sand", "lede": True, "h2": "Dein ganzer Betrieb in einer App – nicht in fünf Chats und drei Excel-Listen.",
     "paragraphs": ["Wer arbeitet morgen wo? Wie viele Stunden hatte Ana im Juli? Wurde der Poolfilter beim Objekt in der Calle Mayor gemacht – und kann ich dem Kunden das zeigen? Was hat der Monat an Fahrten und Material gekostet? Solange die Antworten verstreut sind, kostet dich jeder Abend eine Stunde Nacharbeit.",
                    "Die Betriebs-App legt alles an einen Ort: Dein Team plant, stempelt und berichtet vom Handy aus. Du siehst Zeiten, Kosten, Fahrten und Berichte auf einen Blick – und dein Steuerbüro bekommt saubere Exporte statt Zettel."]},
    {"type": "split", "frame": True, "image": "app-dienstplan", "alt": "Dienstplan der Betriebs-App: Wochenansicht mit Mitarbeitern und Einsätzen",
     "label": "Planen", "h2": "Dienstplan in Minuten statt Stunden.",
     "paragraphs": ["Du ziehst die Einsätze auf die Mitarbeiter, die App rechnet Stunden und Konflikte mit. Der Mitarbeiter öffnet sein Handy und sieht seinen Tag: Objekt, Adresse, Aufgaben, Ansprechpartner."],
     "bullets": [{"title": "Tag, Woche, Bedarf.", "text": "Drei Ansichten, ein Plan."}, {"title": "Vorschlag auf Knopfdruck.", "text": "Die App verteilt die offenen Leistungen, du korrigierst nur noch."}, {"title": "Urlaub & Feiertage drin.", "text": "Wer nicht da ist, wird nicht verplant."}],
     "link": {"text": "Mehr zum Dienstplan", "href": APP_URL + "#dienstplan"}},
    {"type": "split", "image_left": True, "bg": "sand", "frame": True, "image": "app-mein-tag", "alt": "Ansicht „Mein Tag“ in der Betriebs-App: Stempeluhr und heutige Termine",
     "label": "Stempeln", "h2": "Zeiterfassung, die stimmt – ohne Zettel.",
     "paragraphs": ["Kommen, Pause, Gehen: ein Tipp auf dem Handy. Die Zeiten laufen in die Monatsübersicht pro Mitarbeiter, Korrekturen kommen als Antrag zu dir. Am Monatsende exportierst du eine Excel für die Lohnabrechnung. Jeder Mitarbeiter nutzt die App in seiner Sprache."],
     "bullets": [{"title": "Stunden, Pausen, Überstunden.", "text": "Automatisch gerechnet."}, {"title": "Export fürs Steuerbüro.", "text": "Monatlich, als Excel oder PDF."}, {"title": "Keine Installation.", "text": "Link öffnen, anmelden, arbeiten."}],
     "link": {"text": "Mehr zur Zeiterfassung", "href": APP_URL + "#zeiterfassung"}},
    {"type": "split", "frame": True, "image": "app-report", "alt": "Arbeitsbericht in der Betriebs-App: Checkliste mit Prüfpunkten, Fotos und Status",
     "label": "Berichten", "h2": "Der Bericht, den dein Kunde weiterleitet.",
     "paragraphs": ["Prüfpunkte abhaken, Fotos anhängen, zwei Sätze schreiben. Du gibst frei, der Kunde hat den Bericht im Postfach – mit deinem Logo, als PDF. Messwerte wie Chlor oder Zählerstände bleiben als Verlauf pro Objekt."],
     "bullets": [{"title": "Prüfpunkte aus dem Baukasten.", "text": "Einmal angelegt, jedes Mal gleich gut."}, {"title": "Freigabe vor Versand.", "text": "Nichts geht raus, was du nicht gesehen hast."}, {"title": "Aufträge, Anträge, Kosten & Fahrten.", "text": "Alles weitere läuft in derselben App."}],
     "link": {"text": "Alle Module ansehen", "href": APP_URL + "#module"}},
    APP_TARIF,
    {"type": "steps", "h2": "So läuft die Einrichtung.", "intro": "Du lieferst eine Liste. Ich baue den Rest.", "items": [
        {"title": "Anfrage", "text": "Du schreibst mir, was dein Betrieb macht, wie viele Leute im Team sind und ob Standard oder Individuell. Ich antworte innerhalb von 24 Stunden."},
        {"title": "Liste", "text": "Du schickst mir Mitarbeiter, Kunden, Objekte und deine Dienstleistungen – als Excel, Foto oder Sprachnachricht. Bei Individuell: ein Gespräch, wie dein Betrieb wirklich arbeitet."},
        {"title": "Einrichtung", "text": "Ich lege alles an – oder baue bei Individuell die App nach deinen Vorgaben um: Module, Felder, Abläufe, Design."},
        {"title": "Einweisung", "text": "Video-Call mit dir und deinem Team. Danach seid ihr live – Standard meist innerhalb einer Woche."},
    ], "note": "Fragen danach? Per E-Mail, so lange du Kunde bist."},
    {"type": "cards", "bg": "sand", "h2": "Für Betriebe, in denen Leute unterwegs arbeiten.", "cols": 4, "items": [
        {"title": "Reinigung & Hausbetreuung", "text": "Objekte, Schlüssel, Checklisten, Berichte an Eigentümer. Fincas, Ferienhäuser, Büros."},
        {"title": "Handwerk & Montage", "text": "Aufträge mit Fotos dokumentieren, Stunden pro Auftrag, Material und Fahrten erfassen."},
        {"title": "Garten & Pool", "text": "Wiederkehrende Einsätze, Messwerte wie Chlor und pH, Verlauf pro Objekt."},
        {"title": "Pflege & Betreuung", "text": "Dienstplan mit Bedarf, Zeiterfassung nach Gesetz, Berichte pro Klient."},
    ]},
    {"type": "faq", "items": HOME_FAQ},
    {"type": "kiwi", "id": "websites", "bg": "sand", "label": "Außerdem", "h2": "Websites & Online-Präsenz – aus derselben Hand.",
     "paragraphs": ["Die App organisiert deinen Betrieb nach innen. Wenn von außen Kunden kommen sollen, baue ich dir dazu die Website, das Google-Profil und Instagram – einmal zahlen, gehört dir. Wer beides bucht, spart die Standard-Einrichtung der App."],
     "buttons": [{"text": "Website-Pakete ansehen", "href": "/pakete"}, {"text": "Sichtbarkeits-Check 60 €", "href": "/sichtbarkeits-check"}],
     "kiwi": WEB_KIWI},
    {"type": "split", "image_left": True, "image": "hero-kristina", "portrait": True, "alt": "Kristina, Gründerin von KWiDi", "h2": "Eine Person. Ein Preis. Keine Warteschleife.",
     "paragraphs": ["Hinter KWiDi stehe ich, Kristina. Ich führe den Online-Auftritt eines Betriebs für Finca-Betreuung und Vermietung – und ich weiß, wie viel Zeit zwischen Plan, Stempelzettel und Kundenbericht verloren geht. Deshalb gibt es bei mir die App, die den Alltag organisiert – und auf Wunsch die Website, die Kunden bringt."],
     "bullets": [{"title": "Alles aus einer Hand.", "text": "App, Website, Google, Instagram – ein Ansprechpartner."}, {"title": "Du lieferst fast nichts.", "text": "Eine Liste, ein Video-Call. Den Rest mache ich."}, {"title": "Klartext.", "text": "Feste Preise, keine Verkaufsgespräche, Antwort in 24 Stunden."}],
     "link": {"text": "Mehr über mich", "href": "/ueber-mich"}},
]

APP_FAQ = [
    {"q": "Was bekomme ich bei Individuell für 4.695 €?", "a": "Eine App, die nur das enthält, was dein Betrieb braucht – und das so, wie ihr arbeitet: eigene Module und Felder, Abläufe und Freigaben nach deinen Regeln, Berichte in deinem Design, deine Sprachen, Datenübernahme aus der bisherigen Lösung. Der Monatspreis ist derselbe wie bei Standard."},
    {"q": "Für wie viele Mitarbeiter ist die App gedacht?", "a": "Von einem bis etwa 50. Ein Mitarbeiter ist im Monatspreis enthalten, jeder weitere kostet 9 € im Monat. Ab 25 Mitarbeitern machen wir einen eigenen Preis."},
    {"q": "Was ist mit der gesetzlichen Zeiterfassung?", "a": "Die App führt ein Arbeitszeitregister mit Kommen, Pause und Gehen pro Mitarbeiter, monatlich exportierbar. Das Register ist am spanischen Art. 34.9 ET ausgerichtet; ob es für deinen Betrieb und dein Land ausreicht, klärst du mit deinem Steuerbüro oder Anwalt – ich richte ein, was ihr braucht."},
    {"q": "Kann ich bestehende Daten übernehmen?", "a": "Ja. Mitarbeiter, Kunden und Objekte importiere ich aus Excel oder einer anderen Software. Das ist Teil der Einrichtung."},
    {"q": "Was passiert, wenn ich kündige?", "a": "Du kündigst zum Monatsende, exportierst vorher deine Daten – Zeiten, Berichte, Kunden – und gut. Keine Nachlaufkosten."},
    {"q": "Kann jeder Mitarbeiter alles sehen?", "a": "Nein. Mitarbeiter sehen ihren Tag, ihre Zeiten und ihre Berichte. Du und deine Bürokraft seht alles. Wer welche Rechte hat, legen wir bei der Einrichtung fest."},
    {"q": "Funktioniert die App ohne Internet?", "a": "Zum Stempeln und Berichten braucht das Handy eine Verbindung – mobiles Netz reicht. Fotos werden hochgeladen, sobald die Verbindung steht."},
    {"q": "Wer steckt hinter der App?", "a": "Die Software heißt Jornado und wird laufend weiterentwickelt. Ich richte sie für deinen Betrieb ein, betreue dich und bin dein Ansprechpartner – du musst dich um nichts kümmern."},
    {"q": "Gibt es die App auch mit Website?", "a": "Ja, und das ist die beste Kombination: Die Website bringt Kunden, die App organisiert die Arbeit. Bei gemeinsamer Buchung entfällt die Einrichtungsgebühr der App."},
]

APP_PAGE = {
    "url": APP_URL, "title": "Betriebs-App für Kleinbetriebe – Dienstplan, Zeiterfassung, Berichte | KWiDi",
    "description": "Dienstplan, Zeiterfassung, Arbeitsberichte mit Fotos, Aufträge und Kosten in einer App. Eingerichtet für deinen Betrieb: 249 € einmalig, dann 39 €/Monat. Monatlich kündbar.",
    "template": "page",
    "jsonld": [
        {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Betriebs-App by KWiDi", "applicationCategory": "BusinessApplication", "operatingSystem": "Web", "url": "https://kriswidi.com" + APP_URL,
         "description": "Dienstplan, Zeiterfassung, Arbeitsberichte, Aufträge, Anträge und Kosten für kleine Dienstleistungsbetriebe.",
         "offers": [{"@type": "Offer", "name": "Einrichtung", "price": "249", "priceCurrency": "EUR"}, {"@type": "Offer", "name": "Monatlich, 1 Mitarbeiter inklusive", "price": "39", "priceCurrency": "EUR"}],
         "provider": {"@type": "Organization", "name": "KWiDi", "url": "https://kriswidi.com"}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in APP_FAQ]},
    ],
    "blocks": [
        {"type": "hero", "frame": True, "image": "app-woche", "alt": "Wochenplan der Betriebs-App mit Einsätzen pro Mitarbeiter",
         "label": "Betriebs-App · Dienstplan · Zeiterfassung · Berichte · Aufträge",
         "h1": "Dein ganzer Betrieb in einer App.",
         "text": "Dienstplan, Stempeluhr, Berichte mit Fotos, Aufträge, Urlaubsanträge, Kosten und Fahrten. Fertig eingerichtet ab 249 € – oder komplett auf deinen Betrieb zugeschnitten für 4.695 €. Danach 39 € im Monat.",
         "primary": {"text": "App unverbindlich anfragen", "href": "#anfrage"}, "secondary": {"text": "Preis berechnen", "href": "#preise"}},
        {"type": "reasons", "bg": "sand", "h2": "Fünf Dinge, die ohne App jeden Tag schiefgehen.", "items": [
            {"title": "Der Plan steht in WhatsApp.", "text": "Und wird dreimal geändert. Wer den letzten Stand hat, weiß keiner."},
            {"title": "Stunden auf Zetteln.", "text": "Am Monatsende sitzt du zwei Abende am Küchentisch und rechnest nach."},
            {"title": "Der Kunde fragt: Wart ihr da? ", "text": "Und du hast kein Foto, keinen Bericht, keine Uhrzeit."},
            {"title": "Urlaub per Sprachnachricht.", "text": "Genehmigt, vergessen, doppelt verplant."},
            {"title": "Tankquittungen im Handschuhfach.", "text": "Das Steuerbüro wartet, du suchst."},
        ]},
        {"type": "split", "id": "dienstplan", "frame": True, "image": "app-dienstplan", "alt": "Dienstplan: Tagesansicht mit Mitarbeitern, Einsätzen und offenen Leistungen", "label": "Dienstplan", "h2": "Planen: Einsätze ziehen, fertig.",
         "paragraphs": ["Offene Leistungen liegen rechts, deine Mitarbeiter links. Ziehen, ablegen, die App rechnet Stunden und zeigt Konflikte. Wochenansicht für den Überblick, Bedarfsansicht für Objekte mit festen Zeiten, Vorschlag für den schnellen Start."],
         "bullets": [{"title": "Sollzeiten pro Objekt.", "text": "Montags Pool, donnerstags Garten – die App erinnert dich."}, {"title": "Abwesenheiten drin.", "text": "Urlaub und Krankheit blocken automatisch."}, {"title": "Jeder sieht seinen Tag.", "text": "Auf dem Handy, mit Adresse und Aufgaben."}]},
        {"type": "split", "id": "zeiterfassung", "image_left": True, "bg": "sand", "frame": True, "image": "app-mein-tag", "alt": "Mein Tag: Stempeluhr mit Kommen, Pause, Gehen und den Terminen des Tages", "label": "Zeiterfassung", "h2": "Stempeln: Kommen, Pause, Gehen.",
         "paragraphs": ["Ein Knopf, drei Zustände. Die Zeiten laufen in die Monatsübersicht pro Mitarbeiter, Korrekturen gehen als Antrag an dich. Am Monatsende exportierst du eine Excel für die Lohnabrechnung – in Spanien im Format des Arbeitszeitregisters nach Art. 34.9 ET."],
         "bullets": [{"title": "Kein Zettel, kein Nachrechnen.", "text": "Stunden, Pausen, Überstunden – automatisch."}, {"title": "Export fürs Steuerbüro.", "text": "Monatlich, als Excel oder PDF."}, {"title": "Jede Sprache.", "text": "Du planst auf Deutsch, jeder Mitarbeiter liest die App in seiner Sprache – Russisch, Spanisch, Arabisch, was er braucht."}]},
        {"type": "split", "id": "berichte", "frame": True, "image": "app-report", "alt": "Arbeitsbericht mit Prüfpunkten, Fotos und Status Freigegeben", "label": "Berichte", "h2": "Berichten: Checkliste, Fotos, absenden.",
         "paragraphs": ["Für jede Leistung gibt es Prüfpunkte aus dem Baukasten – Pool gereinigt, Filter geprüft, Chlor 1,2 mg/l. Der Mitarbeiter hakt ab, fotografiert, schreibt eine Bemerkung. Du prüfst, gibst frei, der Kunde bekommt den Bericht per E-Mail – mit deinem Logo, als PDF."],
         "bullets": [{"title": "Workflow mit Freigabe.", "text": "Entwurf, eingereicht, zurückgegeben, freigegeben, versandt."}, {"title": "Musterberichte in deinem Design.", "text": "Richte ich bei der Einrichtung ein."}, {"title": "Messwerte als Verlauf.", "text": "Chlor, pH, Temperatur, Zählerstände – pro Objekt über Monate."}]},
        {"type": "gallery", "bg": "sand", "h2": "Und alles andere, was in einem Betrieb anfällt.", "cols": 3, "items": [
            {"image": "app-reports", "alt": "Übersicht aller Arbeitsberichte mit Status", "title": "Berichtsübersicht", "text": "Alle Berichte auf einen Blick: Entwurf, eingereicht, freigegeben, versandt. Filter nach Kunde, Objekt, Mitarbeiter."},
            {"image": "app-objekt", "alt": "Objektseite mit Messwert-Verlauf für Chlor", "title": "Kunden & Objekte", "text": "Jeder Kunde, jedes Objekt mit Adresse, Ansprechpartner, Schlüsselinfo, Notizen und Messwert-Verlauf."},
            {"image": "app-woche", "alt": "Wochenplan mit Einsätzen", "title": "Wochenplan", "text": "Die Woche auf einer Seite. Wer, wann, wo – und was noch offen ist."},
        ]},
        {"type": "list", "id": "module", "rows": True, "h2": "Alle Module im Überblick", "intro": "Alles im Monatspreis enthalten – kein Modul kostet extra.", "items": [
            {"title": "Aufträge", "text": "Auftrag anlegen, Mitarbeiter zuweisen, Status verfolgen, mit Fotos dokumentieren, abrechnen."},
            {"title": "Notizen", "text": "Notizen zu Objekten und Kunden – für alle im Team oder nur für dich."},
            {"title": "Anträge", "text": "Urlaub, Krankmeldung, Zeitkorrektur. Digital eingereicht, mit einem Tipp genehmigt, im Dienstplan berücksichtigt."},
            {"title": "Kosten & Tankbuch", "text": "Quittung fotografieren, Betrag eintragen, Fahrzeug wählen. Auswertung pro Monat, Fahrzeug, Mitarbeiter, Objekt."},
            {"title": "Team, Abteilungen, Feiertage", "text": "Wochenstunden, Rollen, Abteilungen, regionale Feiertage – die Basis für Plan und Zeiterfassung."},
            {"title": "Baukasten", "text": "Deine Dienstleistungen mit Prüfpunkten und Vorlagen. Einmal angelegt, jedes Mal gleich gut."},
            {"title": "Handbuch", "text": "Anleitungen für dein Team direkt in der App – Arbeitsschritte, Regeln, Ansprechpartner."},
            {"title": "Einstellungen & Recht", "text": "Impressum, Datenschutz, Ortungsregeln, Musterberichte, Datenimport – richte ich für dich ein."},
        ]},
        APP_TARIF,
        {"type": "steps", "h2": "So läuft die Einrichtung.", "intro": "Du lieferst eine Liste. Ich baue den Rest.", "items": [
            {"title": "Anfrage", "text": "Du schreibst mir, was dein Betrieb macht und wie viele Leute im Team sind. Ich antworte innerhalb von 24 Stunden."},
            {"title": "Liste", "text": "Du schickst mir Mitarbeiter, Kunden, Objekte und deine Dienstleistungen – als Excel, Foto oder Sprachnachricht."},
            {"title": "Einrichtung", "text": "Ich lege alles an: Team, Objekte, Prüfpunkte, Musterberichte in deinem Design, Impressum und Datenschutz."},
            {"title": "Einweisung", "text": "Video-Call mit dir und deinem Team. Danach seid ihr live – meist innerhalb einer Woche."},
        ], "note": "Fragen danach? Per E-Mail, so lange du Kunde bist."},
        {"type": "cards", "bg": "sand", "h2": "Beispiele aus dem Alltag.", "cols": 3, "items": [
            {"title": "Reinigungsfirma, 6 Mitarbeiter", "text": "Wochenplan für 30 Objekte, Berichte mit Fotos an die Eigentümer, Zeiterfassung fürs Steuerbüro. 84 € im Monat."},
            {"title": "Poolservice, 2 Mitarbeiter", "text": "Sollzeiten pro Pool, Chlor- und pH-Werte als Verlauf, Kunde bekommt jeden Besuch als PDF. 48 € im Monat."},
            {"title": "Handwerksbetrieb, 12 Mitarbeiter", "text": "Aufträge mit Fotos, Stunden pro Auftrag, Tankbuch für vier Fahrzeuge, Urlaubsanträge digital. 138 € im Monat."},
        ]},
        {"type": "faq", "items": APP_FAQ},
    ],
}
