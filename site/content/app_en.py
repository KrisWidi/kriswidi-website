# -*- coding: utf-8 -*-
"""KWiDi – Business app (Jornado): content for the homepage and /en/business-app (EN)."""

APP_NAME = "Business app"
APP_URL = "/en/business-app"

APP_TARIF = {
    "type": "apptarif", "id": "pricing", "bg": "sand",
    "h2": "One price. No surprises.",
    "intro": "A one-off setup, then a fixed monthly fee. Cancel monthly, no minimum term. All prices net of VAT.",
    "setup": {"tag": "One-off", "price": "€249", "note": "set up by me",
              "features": ["Business, team, customers and sites created", "Your services and checklist items entered", "Report templates in your design", "Legal notice and privacy policy inside the app", "Onboarding for you and your team (video call)"]},
    "monthly": {"tag": "Monthly", "price": "€39", "note": "per month, 1 employee included",
                "features": ["All modules: rota, time tracking, reports, jobs, requests, expenses", "Each additional employee + €9 / month", "Web app for phone, tablet and PC – nothing to install", "Updates included", "Cancel monthly"]},
    "calc": {"tag": "What does it cost for you?", "label": "Employees in your team", "base": 39, "per": 9, "setup": 249, "max": 25,
             "month_label": "per month, net",
             "line": "{n} employees · {m} per month · plus €249 one-off setup",
             "button": "Request the app", "package": "Business app", "href": "#anfrage"},
    "notes": ["All prices net of VAT.", "No minimum term, cancel at month end", "Setup fee waived when booked together with a website package"],
}

APP_KIWI = {
    "hint_desktop": "Hover over the seeds", "hint_mobile": "Tap a seed",
    "aria": "KWiDi services as seeds of a kiwi – the business app in the centre",
    "items": [
        {"name": "Visibility check", "price": "€60", "href": "/en/visibility-check"},
        {"name": "Website", "price": "from €549", "href": "/en/packages#website"},
        {"name": "Website + Google", "price": "€729", "href": "/en/packages#website-google"},
        {"name": "Business app", "price": "€39 / month", "href": APP_URL, "primary": True},
        {"name": "Website + Google + Social", "price": "€1,490", "href": "/en/packages#website-google-social"},
        {"name": "All-round", "price": "€2,990", "href": "/en/packages#rundum"},
        {"name": "Custom", "price": "on request", "href": "/en/packages#individuell"},
    ],
}

HOME_FAQ = [
    {"q": "What exactly is the business app?", "a": "A web app for small service businesses: rota, time tracking, work reports with photos, jobs, leave requests, expenses and customer management – all in one place, from your phone. I set it up for you; you and your team use it from day one."},
    {"q": "What does the app cost?", "a": "€249 one-off for the setup, then €39 per month with one employee included. Each additional employee is €9 per month. Cancel monthly, all prices net."},
    {"q": "Does my team have to install anything?", "a": "No. The app runs in the browser – on any phone, tablet or PC. Your employee gets a link and their login, nothing else. Everyone uses the app in their own language: you plan in English, your employee reads their day in Russian, Spanish or Arabic."},
    {"q": "Do I still need a website?", "a": "The app organises your business on the inside. The website brings customers from the outside. You can get both from me – and if you book the app together with a website package, the setup fee is waived."},
    {"q": "How long does the setup take?", "a": "Your business is usually ready within a week. I create team, customers, sites and your services – you only send me a list. Then there is an onboarding video call."},
    {"q": "What about my data?", "a": "Your data is yours. Times, reports and customer data can be exported at any time, for example as Excel for your accountant."},
    {"q": "Can I call you?", "a": "I work by e-mail – so everything stays on record. You get a reply within 24 hours on working days. The app onboarding is, of course, a video call."},
]

HOME_BLOCKS = [
    {"type": "hero", "label": "Business app for small teams · Rota · Time tracking · Reports",
     "h1": "Plan. Clock in. Report. Done.",
     "text": "Everything your team and your customers need – from the app. For cleaning, property care, trades, gardening and any business where people work on site. I set it up, you get going.",
     "primary": {"text": "Request the app", "href": "#anfrage"}, "secondary": {"text": "See all features", "href": APP_URL},
     "kiwi": APP_KIWI},
    {"type": "text", "bg": "sand", "lede": True, "h2": "Paper notes, WhatsApp groups, Excel lists. Sound familiar?",
     "paragraphs": ["Who is working where tomorrow? How many hours did Ana do in July? Did anyone clean the pool filter at the villa on Calle Mayor – and can I show the owner? As long as the answers live in five chats and three heads, every evening costs you an hour of paperwork.",
                    "The business app puts everything in one place: rota, time clock, report with photo, job, leave, fuel receipt. Your team taps, you see. Your customer gets a report that looks like it came from a big company."]},
    {"type": "cards", "h2": "What the app takes off your plate every day.", "cols": 3, "items": [
        {"title": "Rota in minutes", "text": "Day and week view, target times by drag & drop, demand and suggestion. Everyone sees only their own day – on their phone.", "href": APP_URL + "#rota", "link_text": "More"},
        {"title": "Clock in instead of paper", "text": "In, break, out – one tap. Working hours flow automatically into the monthly overview and the export for your accountant.", "href": APP_URL + "#time-tracking", "link_text": "More"},
        {"title": "Reports customers love", "text": "Tick the checklist, attach photos, send. The customer receives a clean report in your design – automatically.", "href": APP_URL + "#reports", "link_text": "More"},
        {"title": "Jobs & notes", "text": "Create a job, assign staff, track status. Notes about a site stay where they belong.", "href": APP_URL + "#modules", "link_text": "More"},
        {"title": "Leave, sick, corrections", "text": "Requests arrive digitally, you approve with one tap. The rota knows.", "href": APP_URL + "#modules", "link_text": "More"},
        {"title": "Expenses & fuel log", "text": "Photograph the receipt, enter the amount, done. At month end it is all there – per vehicle, per employee, per site.", "href": APP_URL + "#modules", "link_text": "More"},
    ]},
    {"type": "split", "bg": "sand", "frame": True, "image": "app-dienstplan", "alt": "Rota in the business app: week view with staff and assignments",
     "label": "Rota", "h2": "Tomorrow morning, everyone knows where to go.",
     "paragraphs": ["You drag the assignments onto your staff, the app calculates hours and flags conflicts. Your employee opens their phone and sees their day: site, address, tasks, contact person."],
     "bullets": [{"title": "Day, week, demand.", "text": "Three views, one plan."}, {"title": "Suggestion at the push of a button.", "text": "The app distributes open services, you only correct."}, {"title": "Holidays and absences included.", "text": "Whoever is on leave is not scheduled."}],
     "link": {"text": "How the rota works", "href": APP_URL + "#rota"}},
    {"type": "split", "image_left": True, "frame": True, "image": "app-report", "alt": "Work report in the business app: checklist with items, photos and status",
     "label": "Reports", "h2": "The report your customer forwards.",
     "paragraphs": ["Your employee ticks the checklist items, takes photos, writes two sentences. You review, approve – and the customer has the report in their inbox. With your logo, your legal notice, your handwriting."],
     "bullets": [{"title": "Checklist items from the builder.", "text": "Set up once, equally good every time."}, {"title": "Draft → reviewed → sent.", "text": "Nothing goes out that you have not seen."}, {"title": "Readings included.", "text": "Chlorine, temperature, meter readings – as a history per site."}],
     "link": {"text": "See a sample report", "href": APP_URL + "#reports"}},
    {"type": "split", "bg": "sand", "frame": True, "image": "app-mein-tag", "alt": "“My day” view in the business app: time clock and today's appointments",
     "label": "My day", "h2": "For your team: one page, one button.",
     "paragraphs": ["In, break, out. Below it, today's appointments with address and tasks. Your employee does not need to see more – and does not see more. And in their own language – you plan in English, they read in Russian, Spanish or Arabic."],
     "bullets": [{"title": "Time tracking that adds up.", "text": "Automatic monthly overview, Excel export for payroll."}, {"title": "No installation.", "text": "Open the link, log in, work."}, {"title": "Privacy built in.", "text": "You decide who sees what."}],
     "link": {"text": "See all features", "href": APP_URL}},
    APP_TARIF,
    {"type": "steps", "h2": "How the setup works.", "intro": "You send a list. I build the rest.", "items": [
        {"title": "Enquiry", "text": "You tell me what your business does and how many people are on the team. I reply within 24 hours."},
        {"title": "List", "text": "You send me staff, customers, sites and your services – as Excel, photo or voice message."},
        {"title": "Setup", "text": "I create everything: team, sites, checklist items, report templates in your design, legal notice and privacy policy."},
        {"title": "Onboarding", "text": "Video call with you and your team. Then you are live – usually within a week."},
    ], "note": "Questions afterwards? By e-mail, for as long as you are a customer."},
    {"type": "cards", "bg": "sand", "h2": "For businesses where people work on site.", "cols": 4, "items": [
        {"title": "Cleaning & property care", "text": "Sites, keys, checklists, reports to owners. Villas, holiday homes, offices."},
        {"title": "Trades & installation", "text": "Document jobs with photos, hours per job, materials and journeys."},
        {"title": "Garden & pool", "text": "Recurring visits, readings such as chlorine and pH, history per site."},
        {"title": "Care & support", "text": "Rota with demand, legally compliant time tracking, reports per client."},
    ]},
    {"type": "packages", "h2": "Also: your website, your Google profile, your Instagram.", "intro": "The app organises your business on the inside. To bring customers in from the outside, there are the website packages – pay once, it's yours. Book both and the app setup is free.", "items": None,
     "link": {"text": "All website packages and prices", "href": "/en/packages"}},
    {"type": "split", "image_left": True, "image": "hero-kristina", "portrait": True, "alt": "Kristina, founder of KWiDi", "h2": "One person. One price. No hold music.",
     "paragraphs": ["Behind KWiDi is me, Kristina. I run the online presence of a villa-care and rental business – and I know how much time gets lost between rota, timesheet and customer report. That is why you get both from me: the app that organises the day-to-day, and the website that brings customers."],
     "bullets": [{"title": "Everything from one person.", "text": "App, website, Google, Instagram – one contact."}, {"title": "You deliver almost nothing.", "text": "One list, one video call. I do the rest."}, {"title": "Plain language.", "text": "Fixed prices, no sales calls, reply within 24 hours."}],
     "link": {"text": "More about me", "href": "/en/about"}},
    {"type": "faq", "items": HOME_FAQ},
]

APP_FAQ = [
    {"q": "How many employees is the app for?", "a": "From one to about 50. One employee is included in the monthly price, each additional one is €9 per month. From 25 employees we agree a custom price."},
    {"q": "What about statutory time tracking?", "a": "The app keeps a working-time register with in, break and out per employee, exportable monthly. The register follows the Spanish Art. 34.9 ET; whether it is sufficient for your business and country is something to confirm with your accountant or lawyer – I set up what you need."},
    {"q": "Can I bring existing data?", "a": "Yes. I import staff, customers and sites from Excel or another tool. That is part of the setup."},
    {"q": "What happens if I cancel?", "a": "You cancel at month end, export your data beforehand – times, reports, customers – and that's it. No trailing costs."},
    {"q": "Can every employee see everything?", "a": "No. Employees see their day, their hours and their reports. You and your office staff see everything. We define who has which rights during setup."},
    {"q": "Does the app work offline?", "a": "Clocking in and reporting need a connection – mobile data is enough. Photos upload as soon as the connection is back."},
    {"q": "Who is behind the app?", "a": "The software is called Jornado and is continuously developed. I set it up for your business, support you and am your contact – you don't have to deal with anything."},
    {"q": "Can I get the app together with a website?", "a": "Yes, and that is the best combination: the website brings customers, the app organises the work. Booked together, the app setup fee is waived."},
]

APP_PAGE = {
    "url": APP_URL, "title": "Business app for small teams – rota, time tracking, reports | KWiDi",
    "description": "Rota, time tracking, work reports with photos, jobs and expenses in one app. Set up for your business: €249 one-off, then €39/month. Cancel monthly.",
    "template": "page",
    "jsonld": [
        {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Business app by KWiDi", "applicationCategory": "BusinessApplication", "operatingSystem": "Web", "url": "https://kriswidi.com" + APP_URL,
         "description": "Rota, time tracking, work reports, jobs, requests and expenses for small service businesses.",
         "offers": [{"@type": "Offer", "name": "Setup", "price": "249", "priceCurrency": "EUR"}, {"@type": "Offer", "name": "Monthly, 1 employee included", "price": "39", "priceCurrency": "EUR"}],
         "provider": {"@type": "Organization", "name": "KWiDi", "url": "https://kriswidi.com"}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in APP_FAQ]},
    ],
    "blocks": [
        {"type": "hero", "frame": True, "image": "app-woche", "alt": "Week plan of the business app with assignments per employee",
         "label": "Business app · Rota · Time tracking · Reports · Jobs",
         "h1": "Your whole business in one app.",
         "text": "Rota, time clock, reports with photos, jobs, leave requests, expenses. For cleaning, property care, trades, gardening and care. I set it up – €249 one-off, then €39 per month.",
         "primary": {"text": "Request the app", "href": "#anfrage"}, "secondary": {"text": "Calculate your price", "href": "#pricing"}},
        {"type": "reasons", "bg": "sand", "h2": "Five things that go wrong every day without an app.", "items": [
            {"title": "The rota lives in WhatsApp.", "text": "And gets changed three times. Nobody knows who has the latest version."},
            {"title": "Hours on paper.", "text": "At month end you spend two evenings at the kitchen table adding up."},
            {"title": "The customer asks: were you there?", "text": "And you have no photo, no report, no time stamp."},
            {"title": "Leave by voice message.", "text": "Approved, forgotten, double-booked."},
            {"title": "Fuel receipts in the glove box.", "text": "The accountant is waiting, you are searching."},
        ]},
        {"type": "split", "id": "rota", "frame": True, "image": "app-dienstplan", "alt": "Rota: day view with staff, assignments and open services", "label": "Rota", "h2": "Plan: drag the assignments, done.",
         "paragraphs": ["Open services on the right, your staff on the left. Drag, drop, the app calculates hours and shows conflicts. Week view for the overview, demand view for sites with fixed times, suggestion for a quick start."],
         "bullets": [{"title": "Target times per site.", "text": "Pool on Mondays, garden on Thursdays – the app reminds you."}, {"title": "Absences included.", "text": "Leave and sick days block automatically."}, {"title": "Everyone sees their day.", "text": "On their phone, with address and tasks."}]},
        {"type": "split", "id": "time-tracking", "image_left": True, "bg": "sand", "frame": True, "image": "app-mein-tag", "alt": "My day: time clock with in, break, out and today's appointments", "label": "Time tracking", "h2": "Clock in: in, break, out.",
         "paragraphs": ["One button, three states. Times flow into the monthly overview per employee, corrections go to you as a request. At month end you export an Excel for payroll – in Spain in the format of the working-time register under Art. 34.9 ET."],
         "bullets": [{"title": "No paper, no recalculating.", "text": "Hours, breaks, overtime – automatic."}, {"title": "Export for your accountant.", "text": "Monthly, as Excel or PDF."}, {"title": "Any language.", "text": "You plan in English, every employee reads the app in their own language – Russian, Spanish, Arabic, whatever they need."}]},
        {"type": "split", "id": "reports", "frame": True, "image": "app-report", "alt": "Work report with checklist items, photos and status Approved", "label": "Reports", "h2": "Report: checklist, photos, send.",
         "paragraphs": ["Every service has checklist items from the builder – pool cleaned, filter checked, chlorine 1.2 mg/l. The employee ticks, photographs, adds a remark. You review, approve, the customer receives the report by e-mail – with your logo, as PDF."],
         "bullets": [{"title": "Workflow with approval.", "text": "Draft, submitted, returned, approved, sent."}, {"title": "Report templates in your design.", "text": "Set up by me during onboarding."}, {"title": "Readings as a history.", "text": "Chlorine, pH, temperature, meter readings – per site over months."}]},
        {"type": "gallery", "bg": "sand", "h2": "And everything else a business needs.", "cols": 3, "items": [
            {"image": "app-reports", "alt": "Overview of all work reports with status", "title": "Report overview", "text": "All reports at a glance: draft, submitted, approved, sent. Filter by customer, site, employee."},
            {"image": "app-objekt", "alt": "Site page with chlorine reading history", "title": "Customers & sites", "text": "Every customer, every site with address, contact, key info, notes and reading history."},
            {"image": "app-woche", "alt": "Week plan with assignments", "title": "Week plan", "text": "The week on one page. Who, when, where – and what is still open."},
        ]},
        {"type": "list", "id": "modules", "rows": True, "h2": "All modules at a glance", "intro": "Everything is included in the monthly price – no module costs extra.", "items": [
            {"title": "Jobs", "text": "Create a job, assign staff, track status, document with photos, invoice."},
            {"title": "Notes", "text": "Notes on sites and customers – for the whole team or only for you."},
            {"title": "Requests", "text": "Leave, sick note, time correction. Submitted digitally, approved with one tap, reflected in the rota."},
            {"title": "Expenses & fuel log", "text": "Photograph the receipt, enter the amount, pick the vehicle. Evaluation per month, vehicle, employee, site."},
            {"title": "Team, departments, public holidays", "text": "Weekly hours, roles, departments, regional holidays – the basis for rota and time tracking."},
            {"title": "Builder", "text": "Your services with checklist items and templates. Set up once, equally good every time."},
            {"title": "Handbook", "text": "Instructions for your team inside the app – procedures, rules, contacts."},
            {"title": "Settings & legal", "text": "Legal notice, privacy policy, location rules, report templates, data import – set up by me."},
        ]},
        APP_TARIF,
        {"type": "steps", "h2": "How the setup works.", "intro": "You send a list. I build the rest.", "items": [
            {"title": "Enquiry", "text": "You tell me what your business does and how many people are on the team. I reply within 24 hours."},
            {"title": "List", "text": "You send me staff, customers, sites and your services – as Excel, photo or voice message."},
            {"title": "Setup", "text": "I create everything: team, sites, checklist items, report templates in your design, legal notice and privacy policy."},
            {"title": "Onboarding", "text": "Video call with you and your team. Then you are live – usually within a week."},
        ], "note": "Questions afterwards? By e-mail, for as long as you are a customer."},
        {"type": "cards", "bg": "sand", "h2": "Examples from everyday life.", "cols": 3, "items": [
            {"title": "Cleaning company, 6 employees", "text": "Week plan for 30 sites, reports with photos to the owners, time tracking for the accountant. €84 per month."},
            {"title": "Pool service, 2 employees", "text": "Target times per pool, chlorine and pH history, customer receives every visit as PDF. €48 per month."},
            {"title": "Trades business, 12 employees", "text": "Jobs with photos, hours per job, fuel log for four vehicles, leave requests digital. €138 per month."},
        ]},
        {"type": "faq", "items": APP_FAQ},
    ],
}
