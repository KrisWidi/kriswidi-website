# -*- coding: utf-8 -*-
"""KWiDi – Betriebs-App (Jornado): Inhalte für Startseite und /betriebs-app (DE)."""

APP_NAME = "Betriebs-App"
APP_URL = "/betriebs-app"

# ---- Preise (Entscheidung Kristina: 249 € Einrichtung, 39 €/Monat inkl. 1 MA, +9 € je weiterer MA, monatlich kündbar) ----
APP_TARIF = {
    "type": "apptarif", "id": "preise", "bg": "sand",
    "h2": "Ein Preis. Keine Überraschung.",
    "intro": "Einmal einrichten lassen, dann ein fester Monatsbetrag. Monatlich kündbar, keine Mindestlaufzeit. Alle Preise netto zzgl. MwSt.",
    "setup": {"tag": "Einmalig", "price": "249 €", "note": "Einrichtung durch mich",
              "features": ["Betrieb, Team, Kunden und Objekte angelegt", "Deine Dienstleistungen und Prüfpunkte hinterlegt", "Musterberichte in deinem Design", "Impressum und Datenschutz in der App", "Einweisung für dich und dein Team (Video-Call)"]},
    "monthly": {"tag": "Monatlich", "price": "39 €", "note": "pro Monat, 1 Mitarbeiter inklusive",
                "features": ["Alle Module: Dienstplan, Zeiterfassung, Berichte, Aufträge, Anträge, Kosten", "Jeder weitere Mitarbeiter + 9 € / Monat", "Web-App für Handy, Tablet und PC – nichts installieren", "Updates inklusive", "Monatlich kündbar"]},
    "calc": {"tag": "Was kostet es für dich?", "label": "Mitarbeiter im Team", "base": 39, "per": 9, "setup": 249, "max": 25,
             "month_label": "pro Monat, netto",
             "line": "{n} Mitarbeiter · {m} im Monat · plus 249 € Einrichtung einmalig",
             "button": "App anfragen", "package": "Betriebs-App", "href": "#anfrage"},
    "notes": ["Alle Preise netto zzgl. MwSt.", "Keine Mindestlaufzeit, Kündigung zum Monatsende", "Einrichtung entfällt bei Buchung zusammen mit einem Website-Paket"],
}

APP_KIWI = {
    "hint_desktop": "Fahre über die Kerne", "hint_mobile": "Tippe auf einen Kern",
    "aria": "Die KWiDi-Leistungen als Kerne einer Kiwi – die Betriebs-App in der Mitte",
    "items": [
        {"name": "Sichtbarkeits-Check", "price": "60 €", "href": "/sichtbarkeits-check"},
        {"name": "Website", "price": "ab 549 €", "href": "/pakete#website"},
        {"name": "Website + Google", "price": "729 €", "href": "/pakete#website-google"},
        {"name": "Betriebs-App", "price": "39 € / Monat", "href": APP_URL, "primary": True},
        {"name": "Website + Google + Social", "price": "1.490 €", "href": "/pakete#website-google-social"},
        {"name": "Rundum", "price": "2.990 €", "href": "/pakete#rundum"},
        {"name": "Individuell", "price": "auf Anfrage", "href": "/pakete#individuell"},
    ],
}

HOME_FAQ = [
    {"q": "Was ist die Betriebs-App genau?", "a": "Eine Web-App für kleine Dienstleistungsbetriebe: Dienstplan, Zeiterfassung, Arbeitsberichte mit Fotos, Aufträge, Urlaubsanträge, Kosten und Kundenverwaltung – alles an einem Ort, vom Handy aus. Ich richte sie für dich ein, du und dein Team nutzt sie ab dem ersten Tag."},
    {"q": "Was kostet die App?", "a": "249 € einmalig für die Einrichtung, dann 39 € im Monat mit einem Mitarbeiter inklusive. Jeder weitere Mitarbeiter kostet 9 € im Monat. Monatlich kündbar, alle Preise netto."},
    {"q": "Muss mein Team etwas installieren?", "a": "Nein. Die App läuft im Browser – auf jedem Handy, Tablet oder PC. Dein Mitarbeiter bekommt einen Link und seine Zugangsdaten, mehr nicht. Verfügbar auf Deutsch, Englisch, Spanisch und Arabisch."},
    {"q": "Brauche ich trotzdem noch eine Website?", "a": "Die App organisiert deinen Betrieb nach innen. Die Website bringt dir Kunden von außen. Beides kannst du bei mir bekommen – wer die App zusammen mit einem Website-Paket bucht, spart die Einrichtungsgebühr."},
    {"q": "Wie lange dauert die Einrichtung?", "a": "In der Regel ist dein Betrieb innerhalb von einer Woche startklar. Ich lege Team, Kunden, Objekte und deine Dienstleistungen an – du lieferst mir nur eine Liste. Dann gibt es eine Einweisung per Video-Call."},
    {"q": "Was ist mit meinen Daten?", "a": "Deine Daten gehören dir. Zeiten, Berichte und Kundendaten kannst du jederzeit exportieren, zum Beispiel als Excel für dein Steuerbüro."},
    {"q": "Kann ich dich anrufen?", "a": "Ich arbeite per E-Mail – so bleibt alles nachlesbar. Du bekommst innerhalb von 24 Stunden an Werktagen eine Antwort. Für die Einweisung in die App gibt es natürlich einen Video-Call."},
]

HOME_BLOCKS = [
    {"type": "hero", "label": "Betriebs-App für Kleinbetriebe · Dienstplan · Zeiterfassung · Berichte",
     "h1": "Planen. Stempeln. Berichten. Fertig.",
     "text": "Alles, was dein Team und deine Kunden brauchen – von der App aus. Für Reinigung, Hausbetreuung, Handwerk, Garten und jeden Betrieb, in dem Leute unterwegs arbeiten. Ich richte sie ein, du legst los.",
     "primary": {"text": "App unverbindlich anfragen", "href": "#anfrage"}, "secondary": {"text": "Alle Funktionen ansehen", "href": APP_URL},
     "kiwi": APP_KIWI},
    {"type": "text", "bg": "sand", "lede": True, "h2": "Zettel, WhatsApp-Gruppen, Excel-Listen. Kennst du.",
     "paragraphs": ["Wer arbeitet morgen wo? Wie viele Stunden hatte Ana im Juli? Hat jemand den Poolfilter beim Objekt in der Calle Mayor gemacht – und kann ich dem Kunden das zeigen? Solange die Antworten in fünf Chats und drei Köpfen stecken, kostet dich jeder Abend eine Stunde Nacharbeit.",
                    "Die Betriebs-App legt alles an einen Ort: Plan, Stempeluhr, Bericht mit Foto, Auftrag, Urlaub, Tankquittung. Dein Team tippt, du siehst. Dein Kunde bekommt einen Bericht, der aussieht wie von einem Großen."]},
    {"type": "cards", "h2": "Was die App dir jeden Tag abnimmt.", "cols": 3, "items": [
        {"title": "Dienstplan in Minuten", "text": "Tag- und Wochenansicht, Sollzeiten per Drag & Drop, Bedarf und Vorschlag. Jeder sieht nur seinen Tag – auf dem Handy.", "href": APP_URL + "#dienstplan", "link_text": "Mehr"},
        {"title": "Stempeln statt Zettel", "text": "Kommen, Pause, Gehen – ein Tipp. Arbeitszeiten laufen automatisch in die Monatsübersicht und den Export fürs Steuerbüro.", "href": APP_URL + "#zeiterfassung", "link_text": "Mehr"},
        {"title": "Berichte, die Kunden lieben", "text": "Checkliste abhaken, Fotos anhängen, absenden. Der Kunde bekommt einen sauberen Bericht in deinem Design – automatisch.", "href": APP_URL + "#berichte", "link_text": "Mehr"},
        {"title": "Aufträge & Notizen", "text": "Auftrag anlegen, Mitarbeiter zuweisen, Status verfolgen. Notizen zum Objekt bleiben da, wo sie hingehören.", "href": APP_URL + "#module", "link_text": "Mehr"},
        {"title": "Urlaub, Krank, Korrektur", "text": "Anträge kommen digital, du gibst mit einem Tipp frei. Der Dienstplan weiß Bescheid.", "href": APP_URL + "#module", "link_text": "Mehr"},
        {"title": "Kosten & Tankbuch", "text": "Quittung fotografieren, Betrag eintragen, fertig. Am Monatsende ist alles da – pro Fahrzeug, pro Mitarbeiter, pro Objekt.", "href": APP_URL + "#module", "link_text": "Mehr"},
    ]},
    {"type": "split", "bg": "sand", "frame": True, "image": "app-dienstplan", "alt": "Dienstplan der Betriebs-App: Wochenansicht mit Mitarbeitern und Einsätzen",
     "label": "Dienstplan", "h2": "Morgen früh weiß jeder, wo er hin muss.",
     "paragraphs": ["Du ziehst die Einsätze auf die Mitarbeiter, die App rechnet Stunden und Konflikte mit. Der Mitarbeiter öffnet sein Handy und sieht seinen Tag: Objekt, Adresse, Aufgaben, Ansprechpartner."],
     "bullets": [{"title": "Tag, Woche, Bedarf.", "text": "Drei Ansichten, ein Plan."}, {"title": "Vorschlag auf Knopfdruck.", "text": "Die App verteilt die offenen Leistungen, du korrigierst nur noch."}, {"title": "Feiertage & Abwesenheiten drin.", "text": "Wer im Urlaub ist, wird nicht verplant."}],
     "link": {"text": "So funktioniert der Dienstplan", "href": APP_URL + "#dienstplan"}},
    {"type": "split", "image_left": True, "frame": True, "image": "app-report", "alt": "Arbeitsbericht in der Betriebs-App: Checkliste mit Prüfpunkten, Fotos und Status",
     "label": "Berichte", "h2": "Der Bericht, den dein Kunde weiterleitet.",
     "paragraphs": ["Dein Mitarbeiter hakt die Prüfpunkte ab, macht Fotos, schreibt zwei Sätze. Du prüfst, gibst frei – und der Kunde hat den Bericht im Postfach. Mit deinem Logo, deinem Impressum, deiner Handschrift."],
     "bullets": [{"title": "Prüfpunkte aus dem Baukasten.", "text": "Einmal angelegt, jedes Mal gleich gut."}, {"title": "Entwurf → geprüft → versandt.", "text": "Nichts geht raus, was du nicht gesehen hast."}, {"title": "Messwerte inklusive.", "text": "Chlor, Temperatur, Zählerstand – als Verlauf pro Objekt."}],
     "link": {"text": "Beispielbericht ansehen", "href": APP_URL + "#berichte"}},
    {"type": "split", "bg": "sand", "frame": True, "image": "app-mein-tag", "alt": "Ansicht „Mein Tag“ in der Betriebs-App: Stempeluhr und heutige Termine",
     "label": "Mein Tag", "h2": "Für dein Team: eine Seite, ein Knopf.",
     "paragraphs": ["Kommen, Pause, Gehen. Darunter die Termine des Tages mit Adresse und Aufgaben. Mehr braucht dein Mitarbeiter nicht zu sehen – und mehr sieht er auch nicht. Auf Deutsch, Englisch, Spanisch oder Arabisch."],
     "bullets": [{"title": "Zeiterfassung, die stimmt.", "text": "Automatische Monatsübersicht, Export als Excel für die Lohnabrechnung."}, {"title": "Keine Installation.", "text": "Link öffnen, anmelden, arbeiten."}, {"title": "Datenschutz eingebaut.", "text": "Wer was sieht, legst du fest."}],
     "link": {"text": "Alle Funktionen ansehen", "href": APP_URL}},
    APP_TARIF,
    {"type": "steps", "h2": "So läuft die Einrichtung.", "intro": "Du lieferst eine Liste. Ich baue den Rest.", "items": [
        {"title": "Anfrage", "text": "Du schreibst mir, was dein Betrieb macht und wie viele Leute im Team sind. Ich antworte innerhalb von 24 Stunden."},
        {"title": "Liste", "text": "Du schickst mir Mitarbeiter, Kunden, Objekte und deine Dienstleistungen – als Excel, Foto oder Sprachnachricht."},
        {"title": "Einrichtung", "text": "Ich lege alles an: Team, Objekte, Prüfpunkte, Musterberichte in deinem Design, Impressum und Datenschutz."},
        {"title": "Einweisung", "text": "Video-Call mit dir und deinem Team. Danach seid ihr live – meist innerhalb einer Woche."},
    ], "note": "Fragen danach? Per E-Mail, so lange du Kunde bist."},
    {"type": "cards", "bg": "sand", "h2": "Für Betriebe, in denen Leute unterwegs arbeiten.", "cols": 4, "items": [
        {"title": "Reinigung & Hausbetreuung", "text": "Objekte, Schlüssel, Checklisten, Berichte an Eigentümer. Fincas, Ferienhäuser, Büros."},
        {"title": "Handwerk & Montage", "text": "Aufträge mit Fotos dokumentieren, Stunden pro Auftrag, Material und Fahrten erfassen."},
        {"title": "Garten & Pool", "text": "Wiederkehrende Einsätze, Messwerte wie Chlor und pH, Verlauf pro Objekt."},
        {"title": "Pflege & Betreuung", "text": "Dienstplan mit Bedarf, Zeiterfassung nach Gesetz, Berichte pro Klient."},
    ]},
    {"type": "packages", "h2": "Außerdem: deine Website, dein Google-Profil, dein Instagram.", "intro": "Die App organisiert deinen Betrieb nach innen. Damit von außen Kunden kommen, gibt es die Website-Pakete – einmal zahlen, gehört dir. Wer beides bucht, spart die App-Einrichtung.", "items": None,
     "link": {"text": "Alle Website-Pakete und Preise", "href": "/pakete"}},
    {"type": "split", "image_left": True, "image": "hero-kristina", "alt": "Kristina, Gründerin von KWiDi", "h2": "Eine Person. Ein Preis. Keine Warteschleife.",
     "paragraphs": ["Hinter KWiDi stehe ich, Kristina. Ich führe den Online-Auftritt eines Betriebs für Finca-Betreuung und Vermietung – und ich weiß, wie viel Zeit zwischen Plan, Stempelzettel und Kundenbericht verloren geht. Deshalb bekommst du bei mir beides: die App, die den Alltag organisiert, und die Website, die Kunden bringt."],
     "bullets": [{"title": "Alles aus einer Hand.", "text": "App, Website, Google, Instagram – ein Ansprechpartner."}, {"title": "Du lieferst fast nichts.", "text": "Eine Liste, ein Video-Call. Den Rest mache ich."}, {"title": "Klartext.", "text": "Feste Preise, keine Verkaufsgespräche, Antwort in 24 Stunden."}],
     "link": {"text": "Mehr über mich", "href": "/ueber-mich"}},
    {"type": "faq", "items": HOME_FAQ},
]

APP_FAQ = [
    {"q": "Für wie viele Mitarbeiter ist die App gedacht?", "a": "Von einem bis etwa 50. Ein Mitarbeiter ist im Monatspreis enthalten, jeder weitere kostet 9 € im Monat. Ab 25 Mitarbeitern machen wir einen eigenen Preis."},
    {"q": "Was ist mit der gesetzlichen Zeiterfassung?", "a": "Die App führt ein Arbeitszeitregister mit Kommen, Pause und Gehen pro Mitarbeiter, monatlich exportierbar. In Spanien erfüllt sie damit die Registerpflicht nach Art. 34.9 ET; für andere Länder besprechen wir, was dein Steuerbüro braucht."},
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
         "text": "Dienstplan, Stempeluhr, Berichte mit Fotos, Aufträge, Urlaubsanträge, Kosten. Für Reinigung, Hausbetreuung, Handwerk, Garten und Pflege. Ich richte sie ein – 249 € einmalig, dann 39 € im Monat.",
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
         "paragraphs": ["Ein Knopf, drei Zustände. Die Zeiten laufen in die Monatsübersicht pro Mitarbeiter, Korrekturen gehen als Antrag an dich. Am Monatsende exportierst du eine Excel für die Lohnabrechnung – in Spanien gleich als Arbeitszeitregister nach Art. 34.9 ET."],
         "bullets": [{"title": "Kein Zettel, kein Nachrechnen.", "text": "Stunden, Pausen, Überstunden – automatisch."}, {"title": "Export fürs Steuerbüro.", "text": "Monatlich, als Excel oder PDF."}, {"title": "Vier Sprachen.", "text": "Deutsch, Englisch, Spanisch, Arabisch – jeder Mitarbeiter wählt selbst."}]},
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
