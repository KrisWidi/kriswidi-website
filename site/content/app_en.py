# -*- coding: utf-8 -*-
"""KWiDi – Business app (Jornado): content for the homepage and /en/business-app (EN)."""

APP_NAME = "Business app"
APP_URL = "/en/business-app"

APP_TARIF = {
    "type": "apptarif", "id": "pricing", "bg": "sand",
    "h2": "Two ways to your app. One monthly price.",
    "intro": "Set up once – ready-made or tailored completely to your business. Then a fixed monthly fee, cancel monthly. All prices net of VAT.",
    "setups": [
        {"tag": "Standard · one-off", "price": "€249", "note": "set up by me", "for": "The app as it is – all modules, set up for your business.", "package": "Business app Standard", "button": "Request Standard",
         "features": ["All modules: rota, time tracking, reports, jobs, requests, expenses & journeys", "Business, team, customers and sites created", "Your services and checklist items entered", "Report templates in your design", "Onboarding video call"]},
        {"tag": "Custom · one-off", "price": "€4,695", "note": "set up and tailored by me", "for": "Your app, cut exactly to your business – only the modules you need, plus what you are missing.", "package": "Business app Custom", "button": "Request Custom", "highlight": True,
         "features": ["Only the modules you want – the rest disappears", "Custom modules and fields your business needs", "Workflows, approvals and reports by your rules", "Your design, your wording, your languages", "Data migration from your current tool", "Onboarding for you and your team"]},
    ],
    "monthly": {"tag": "Monthly · both options", "price": "€39", "note": "per month, 1 employee included", "for": "Same for Standard and Custom.",
                "features": ["Each additional employee + €9 / month", "Web app for phone, tablet and PC – nothing to install", "Updates and hosting included", "Cancel monthly, no minimum term"]},
    "calc": {"tag": "What does it cost per month?", "label": "Employees in your team", "base": 39, "per": 9, "setup": 249, "max": 25,
             "month_label": "per month, net – Standard and Custom alike",
             "line": "{n} employees · {m} per month · plus one-off setup (€249 Standard / €4,695 Custom)",
             "button": "Request the app", "package": "Business app", "href": "#anfrage"},
    "notes": ["All prices net of VAT.", "No minimum term, cancel at month end", "Standard setup fee waived when booked together with a website package"],
}

APP_KIWI = {
    "hint_desktop": "Hover over the seeds", "hint_mobile": "Tap a seed",
    "aria": "The modules of the business app as seeds of a kiwi",
    "items": [
        {"name": "Rota", "price": "day, week, demand", "href": APP_URL + "#rota"},
        {"name": "Time tracking", "price": "in, break, out", "href": APP_URL + "#time-tracking"},
        {"name": "Reports", "price": "with photos & approval", "href": APP_URL + "#reports"},
        {"name": "Everything in one app", "price": "for your business", "href": APP_URL, "primary": True},
        {"name": "Jobs", "price": "status & assignment", "href": APP_URL + "#modules"},
        {"name": "Requests", "price": "leave, sick, corrections", "href": APP_URL + "#modules"},
        {"name": "Expenses & journeys", "price": "receipts, fuel log, export", "href": APP_URL + "#modules"},
    ],
}

WEB_KIWI = {
    "hint_desktop": "Hover over the seeds", "hint_mobile": "Tap a seed",
    "aria": "KWiDi website and online services as seeds of a kiwi",
    "items": [
        {"name": "Visibility check", "price": "€60", "href": "/en/visibility-check"},
        {"name": "Website", "price": "from €549", "href": "/en/packages#website"},
        {"name": "Website + Google", "price": "€729", "href": "/en/packages#website-google"},
        {"name": "Website + Google + Social", "price": "€1,490", "href": "/en/packages#website-google-social"},
        {"name": "All-round", "price": "€2,990", "href": "/en/packages#rundum"},
        {"name": "Custom", "price": "on request", "href": "/en/packages#individuell"},
    ],
}

HOME_FAQ = [
    {"q": "What exactly is the business app?", "a": "A web app for service businesses with a team: rota, time tracking, work reports with photos, jobs, leave requests, expenses and customer management – all in one place, from your phone. I set it up for you; you and your team use it from day one."},
    {"q": "What does the app cost?", "a": "Standard: €249 one-off for the setup. Custom: €4,695 one-off – then the app is cut exactly to your business. In both cases €39 per month afterwards with one employee included, each additional employee €9 per month. Cancel monthly, all prices net."},
    {"q": "What is the difference between Standard and Custom?", "a": "Standard is the ready-made app with all modules, set up with your data. Custom means we build the app around your business – only the modules you need, custom fields and workflows, your design. Everything that works differently in your day-to-day than in the standard is reflected."},
    {"q": "Does my team have to install anything?", "a": "No. The app runs in the browser – on any phone, tablet or PC. Your employee gets a link and their login, nothing else. Everyone uses the app in their own language: you plan in English, your employee reads their day in Russian, Spanish or Arabic."},
    {"q": "Do I still need a website?", "a": "The app organises your business on the inside. The website brings customers from the outside. You can get both from me – and if you book the app together with a website package, the setup fee is waived."},
    {"q": "How long does the setup take?", "a": "Your business is usually ready within a week. I create team, customers, sites and your services – you only send me a list. Then there is an onboarding video call."},
    {"q": "What about my data?", "a": "Your data is yours. Times, reports and customer data can be exported at any time, for example as Excel for your accountant."},
    {"q": "Can I call you?", "a": "I work by e-mail – so everything stays on record. You get a reply within 24 hours on working days. The app onboarding is, of course, a video call."},
]

HOME_BLOCKS = [
    {"type": "hero", "label": "The business app for business owners with a team",
     "h1": "Plan. Clock in. Report. Done.",
     "text": "Everything your team and your customers need – from the app. Rota, time tracking, reports, jobs, expenses and journeys in one app. Ready-made or tailored completely to your business.",
     "primary": {"text": "Request the app", "href": "#anfrage"}, "secondary": {"text": "See prices", "href": "#pricing"},
     "kiwi": APP_KIWI},
    {"type": "text", "bg": "sand", "lede": True, "h2": "Your whole business in one app – not in five chats and three spreadsheets.",
     "paragraphs": ["Who is working where tomorrow? How many hours did Ana do in July? Was the pool filter at the villa on Calle Mayor done – and can I show the owner? What did the month cost in journeys and materials? As long as the answers are scattered, every evening costs you an hour of paperwork.",
                    "The business app puts everything in one place: your team plans, clocks in and reports from their phones. You see hours, expenses, journeys and reports at a glance – and your accountant gets clean exports instead of paper."]},
    {"type": "split", "frame": True, "image": "app-dienstplan", "alt": "Rota in the business app: week view with staff and assignments",
     "label": "Plan", "h2": "A rota in minutes instead of hours.",
     "paragraphs": ["You drag the assignments onto your staff, the app calculates hours and flags conflicts. Your employee opens their phone and sees their day: site, address, tasks, contact person."],
     "bullets": [{"title": "Day, week, demand.", "text": "Three views, one plan."}, {"title": "Suggestion at the push of a button.", "text": "The app distributes open services, you only correct."}, {"title": "Leave and holidays included.", "text": "Whoever is away is not scheduled."}],
     "link": {"text": "More about the rota", "href": APP_URL + "#rota"}},
    {"type": "split", "image_left": True, "bg": "sand", "frame": True, "image": "app-mein-tag", "alt": "“My day” view in the business app: time clock and today's appointments",
     "label": "Clock in", "h2": "Time tracking that adds up – without paper.",
     "paragraphs": ["In, break, out: one tap on the phone. Times flow into the monthly overview per employee, corrections come to you as a request. At month end you export an Excel for payroll. Every employee uses the app in their own language."],
     "bullets": [{"title": "Hours, breaks, overtime.", "text": "Calculated automatically."}, {"title": "Export for your accountant.", "text": "Monthly, as Excel or PDF."}, {"title": "No installation.", "text": "Open the link, log in, work."}],
     "link": {"text": "More about time tracking", "href": APP_URL + "#time-tracking"}},
    {"type": "split", "frame": True, "image": "app-report", "alt": "Work report in the business app: checklist with items, photos and status",
     "label": "Report", "h2": "The report your customer forwards.",
     "paragraphs": ["Tick the checklist items, attach photos, write two sentences. You approve, the customer has the report in their inbox – with your logo, as PDF. Readings such as chlorine or meter values stay as a history per site."],
     "bullets": [{"title": "Checklist items from the builder.", "text": "Set up once, equally good every time."}, {"title": "Approval before sending.", "text": "Nothing goes out that you have not seen."}, {"title": "Jobs, requests, expenses & journeys.", "text": "Everything else runs in the same app."}],
     "link": {"text": "See all modules", "href": APP_URL + "#modules"}},
    APP_TARIF,
    {"type": "steps", "h2": "How the setup works.", "intro": "You send a list. I build the rest.", "items": [
        {"title": "Enquiry", "text": "You tell me what your business does, how many people are on the team and whether Standard or Custom. I reply within 24 hours."},
        {"title": "List", "text": "You send me staff, customers, sites and your services – as Excel, photo or voice message. For Custom: a conversation about how your business really works."},
        {"title": "Setup", "text": "I create everything – or, for Custom, rebuild the app to your specifications: modules, fields, workflows, design."},
        {"title": "Onboarding", "text": "Video call with you and your team. Then you are live – Standard usually within a week."},
    ], "note": "Questions afterwards? By e-mail, for as long as you are a customer."},
    {"type": "cards", "bg": "sand", "h2": "For businesses where people work on site.", "cols": 4, "items": [
        {"title": "Cleaning & property care", "text": "Sites, keys, checklists, reports to owners. Villas, holiday homes, offices."},
        {"title": "Trades & installation", "text": "Document jobs with photos, hours per job, materials and journeys."},
        {"title": "Garden & pool", "text": "Recurring visits, readings such as chlorine and pH, history per site."},
        {"title": "Care & support", "text": "Rota with demand, legally compliant time tracking, reports per client."},
    ]},
    {"type": "faq", "items": HOME_FAQ},
    {"type": "kiwi", "id": "websites", "bg": "sand", "label": "Also", "h2": "Websites & online presence – from the same hands.",
     "paragraphs": ["The app organises your business on the inside. If customers should come from the outside, I also build your website, Google profile and Instagram – pay once, it's yours. Book both and the Standard app setup is free."],
     "buttons": [{"text": "See website packages", "href": "/en/packages"}, {"text": "Visibility check €60", "href": "/en/visibility-check"}],
     "kiwi": WEB_KIWI},
    {"type": "split", "image_left": True, "image": "hero-kristina", "portrait": True, "alt": "Kristina, founder of KWiDi", "h2": "One person. One price. No hold music.",
     "paragraphs": ["Behind KWiDi is me, Kristina. I run the online presence of a villa-care and rental business – and I know how much time gets lost between rota, timesheet and customer report. That is why you get the app that organises the day-to-day from me – and, if you want, the website that brings customers."],
     "bullets": [{"title": "Everything from one person.", "text": "App, website, Google, Instagram – one contact."}, {"title": "You deliver almost nothing.", "text": "One list, one video call. I do the rest."}, {"title": "Plain language.", "text": "Fixed prices, no sales calls, reply within 24 hours."}],
     "link": {"text": "More about me", "href": "/en/about"}},
]

APP_FAQ = [
    {"q": "What do I get with Custom for €4,695?", "a": "An app that contains only what your business needs – and the way you work: custom modules and fields, workflows and approvals by your rules, reports in your design, your languages, data migration from your current tool. The monthly price is the same as Standard."},
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
    "url": APP_URL, "title": "Business app for service businesses – rota, time tracking, reports | KWiDi",
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
         "text": "Rota, time clock, reports with photos, jobs, leave requests, expenses and journeys. Ready-made from €249 – or tailored completely to your business for €4,695. Then €39 per month.",
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
