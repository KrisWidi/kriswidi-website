# -*- coding: utf-8 -*-
"""KWiDi – English content (showcase translation of the German copy deck)."""

LANG = "en"
PREFIX = "/en"

# Mapping DE url -> EN url (used for hreflang / language switch)
URL_MAP = {
    "/": "/en/", "/pakete": "/en/packages", "/website-ohne-anfragen": "/en/website-no-enquiries",
    "/sichtbarkeits-check": "/en/visibility-check", "/fuer/gastronomie": "/en/for/restaurants",
    "/fuer/ferienvermietung": "/en/for/holiday-rentals", "/fuer/handwerk": "/en/for/trades",
    "/fuer/praxen-studios": "/en/for/practices-studios", "/so-funktioniert-es": "/en/how-it-works",
    "/ueber-mich": "/en/about", "/kontakt": "/en/contact", "/danke": "/en/thank-you", "/404": "/en/404",
    "/impressum": "/en/legal-notice", "/datenschutz": "/en/privacy",
}

UI = {
    "skip": "Skip to content",
    "home": "Home", "home_url": "/en/",
    "nav_label": "Main navigation", "lang_label": "Language", "menu": "Menu", "close": "Close",
    "more": "More", "faq": "Frequently asked questions",
    "cta": "Get in touch", "cta_href": "/en/contact",
    "thanks_url": "/en/thank-you",
    "nav": [
        {"text": "Packages", "href": "/en/packages"},
        {"text": "Industries", "href": "/en/for/restaurants", "children": [
            {"text": "Restaurants", "sub": "Restaurants, cafés, bars", "href": "/en/for/restaurants"},
            {"text": "Holiday rentals", "sub": "Holiday homes & apartments", "href": "/en/for/holiday-rentals"},
            {"text": "Trades", "sub": "Craft and trade businesses", "href": "/en/for/trades"},
            {"text": "Practices & studios", "sub": "Physio, beauty, wellness", "href": "/en/for/practices-studios"},
        ]},
        {"text": "Website, no enquiries", "href": "/en/website-no-enquiries"},
        {"text": "How it works", "href": "/en/how-it-works"},
        {"text": "About", "href": "/en/about"},
    ],
    "footer": {
        "claim": "Websites that get seen.",
        "text": "Website, Google Business Profile, Instagram and Facebook – fully set up, at a fixed price, from one person.",
        "pages_label": "Pages",
        "pages": [
            {"text": "Packages & prices", "href": "/en/packages"},
            {"text": "Website, no enquiries", "href": "/en/website-no-enquiries"},
            {"text": "Visibility check", "href": "/en/visibility-check"},
            {"text": "How it works", "href": "/en/how-it-works"},
            {"text": "About", "href": "/en/about"},
            {"text": "Contact", "href": "/en/contact"},
        ],
        "industries_label": "Industries",
        "industries": [
            {"text": "Restaurants", "href": "/en/for/restaurants"},
            {"text": "Holiday rentals", "href": "/en/for/holiday-rentals"},
            {"text": "Trades", "href": "/en/for/trades"},
            {"text": "Practices & studios", "href": "/en/for/practices-studios"},
        ],
        "contact_label": "Contact",
        "reply": "Reply within 24 hours on working days",
        "imprint": "Legal notice", "imprint_href": "/en/legal-notice",
        "privacy": "Privacy", "privacy_href": "/en/privacy",
        "cookies": "Cookie settings",
        "vat": "All prices exclude VAT.",
    },
    "consent": {
        "title": "A word on cookies.",
        "text": "I use cookies for statistics and advertising (Google Analytics, Meta Pixel) to see what works on this site. You decide.",
        "link": "Details in the privacy policy.",
        "all": "Accept all", "none": "Necessary only", "settings": "Settings", "save": "Save selection",
        "necessary": "Necessary (always on)", "analytics": "Statistics (Google Analytics)", "marketing": "Advertising (Meta Pixel)",
    },
    "form": {
        "h2": "Let's see what fits you.",
        "text": "Tell me in two or three sentences what you have in mind. I reply within 24 hours on working days – by email, no sales call.",
        "direct": "Prefer to email directly?",
        "name": "Name", "email": "Email", "industry": "Industry", "interest": "Interest",
        "industries": ["Restaurant / café / bar", "Holiday rental", "Trades", "Practice & studio", "Other"],
        "interests": ["New website", "Improve existing website", "Visibility check", "Not sure yet"],
        "link": "Link to website or Instagram (optional)", "message": "Message",
        "business": "Business", "link_site": "Link to your website", "link_google": "Link to Google profile", "link_insta": "Link to Instagram",
        "check_msg": "What bothers you most (optional)",
        "privacy_pre": "I have read the", "privacy_link": "privacy policy", "privacy_post": ".",
        "submit": "Send enquiry",
        "js": {"invalid": "Please fill in all required fields.", "ok": "Thank you – your message has arrived.", "fail": "That didn't work. Please email me directly.", "noEndpoint": "Form delivery is not configured yet. Please email me directly."},
    },
}

FORM = {"type": "form"}

PACKAGES_SHORT = [
    {"name": "Website", "price": "from €549", "price_note": "one-off, excl. VAT", "for": "New or rebuild. 4 pages, texts and images by me, legal pages included.", "button": "Enquire", "href": "/en/packages"},
    {"name": "Website + Google", "price": "€729", "price_note": "one-off, excl. VAT", "for": "Plus your Google Business Profile, fully set up.", "button": "Enquire", "href": "/en/packages"},
    {"name": "Website + Google + Social", "price": "€1,490", "price_note": "one-off, excl. VAT", "tag": "Recommended", "highlight": True, "for": "Plus Instagram and Facebook, set up and filled with the first six posts.", "button": "Enquire", "href": "/en/packages"},
    {"name": "All-round", "price": "€2,990", "price_note": "one-off, excl. VAT", "for": "Everything from the third package plus three months of support.", "button": "Enquire", "href": "/en/packages"},
]

PACKAGES_FULL = [
    {"id": "website", "name": "Website", "price": "from €549", "price_note": "one-off · excl. VAT", "for": "For everyone who wants to be found and understood.",
     "features": ["4 pages, individually designed – no template", "Texts and images by me", "Legal notice and privacy policy included", "Works on phone, tablet and desktop", "Contact form", "Domain and hosting set up", "New or a rebuild of your existing website"],
     "button": "Enquire about Website"},
    {"id": "website-google", "name": "Website + Google", "price": "€729", "price_note": "one-off · excl. VAT", "for": "For everyone who wants to appear on the map.",
     "features": ["Everything from “Website”", "Google Business Profile fully set up: categories, opening hours, services, photos, description", "Linked to your website"],
     "button": "Enquire about Website + Google"},
    {"id": "website-google-social", "name": "Website + Google + Social", "price": "€1,490", "price_note": "one-off · excl. VAT", "tag": "My recommendation", "highlight": True, "for": "For everyone who wants to stay in mind.",
     "features": ["Everything from “Website + Google”", "Instagram profile set up: bio, highlights, profile picture, links", "Facebook page set up", "6 first posts each, so the profiles are not empty"],
     "button": "Enquire about this package"},
    {"id": "rundum", "name": "All-round", "price": "€2,990", "price_note": "one-off · excl. VAT", "for": "For everyone who wants to hand it all over.",
     "features": ["Everything from “Website + Google + Social”", "3 months of support: posts, Google profile upkeep, website changes – we tailor the scope to your business"],
     "button": "Enquire about All-round"},
]

CHAIN = [
    {"title": "Get found", "sub": "Google Business Profile", "text": "“Restaurant near me”, “holiday home with sea view”, “electrician + your town”: that's how your guests search. Without a complete Google profile you don't show up on the map – no matter how good your website is."},
    {"title": "Convince", "sub": "Website", "text": "The guest clicks and decides in thirty seconds. Pictures, prices, opening hours, reviews, one tap to enquire. That's the moment they come – or move on to the next one."},
    {"title": "Stay in mind", "sub": "Instagram and Facebook", "text": "Whoever has seen you once sees you again. That brings regulars, recommendations and repeat bookings – without posting every day."},
]

def industry_page(slug, title, desc, hero, blocks, industry, faq, name):
    return {
        "url": f"/en/for/{slug}", "title": title, "description": desc, "template": "page",
        "jsonld": [
            {"@context": "https://schema.org", "@type": "Service", "name": name, "provider": {"@type": "Organization", "name": "KWiDi", "url": "https://kriswidi.com"}, "areaServed": ["DE", "AT", "CH"], "offers": {"@type": "Offer", "priceCurrency": "EUR", "price": "549"}},
            {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in faq]},
        ],
        "blocks": [hero] + blocks + [{"type": "faq", "items": faq}, {**FORM, "industry": industry}],
    }

PAGES = []

HOME_FAQ = [
    {"q": "What does a website cost at KWiDi?", "a": "From €549 excl. VAT for four pages including texts, images and legal pages. With Google profile €729, with Instagram and Facebook €1,490. All packages are on the pricing page – no small print."},
    {"q": "Do I have to provide texts and images?", "a": "No. I write the texts and take care of images. If you have your own material, I'm happy to use it – the price stays the same."},
    {"q": "Are there monthly costs?", "a": "Not with me. You pay once, the website is yours. Only domain and hosting run through your provider – I set both up, the running costs (usually under €10 a month) are paid by you directly."},
    {"q": "Why not just build it myself with AI or Wix?", "a": "You can. Then you have a page – but no Google profile set up, no Instagram, no texts that sell, and no one to ask. The website is the easy part. The paths that lead to it are the work."},
    {"q": "Can I call you?", "a": "I work by email – that way everything stays on record and I can focus on your project. You get a reply within 24 hours on working days."},
]
PAGES.append({
    "url": "/en/", "title": "Get a website built from €549 – KWiDi",
    "description": "Website, Google profile and Instagram from one person – fully set up, at a fixed price. For restaurants, holiday rentals, trades and studios.",
    "template": "page",
    "jsonld": [
        {"@context": "https://schema.org", "@type": "Organization", "name": "KWiDi", "url": "https://kriswidi.com", "logo": "https://kriswidi.com/assets/img/logo-stacked.svg", "email": "kristinaswiderski@outlook.com"},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in HOME_FAQ]},
    ],
    "blocks": [
        {"type": "hero", "label": "Website · Google · Instagram · Facebook", "h1": "Websites that get seen.",
         "text": "Your website, your Google profile and your Instagram – fully set up, at a fixed price, by one person. For restaurants, holiday rentals, trades and studios.",
         "primary": {"text": "Get in touch – no obligation", "href": "#anfrage"}, "secondary": {"text": "See packages from €549", "href": "/en/packages"},
         "kiwi": {"hint_desktop": "Hover over the seeds", "hint_mobile": "Tap a seed", "aria": "The KWiDi packages as seeds of a kiwi", "items": [
             {"name": "Visibility check", "price": "€60", "href": "/en/visibility-check"},
             {"name": "Website", "price": "from €549", "href": "/en/packages#website"},
             {"name": "Website + Google", "price": "€729", "href": "/en/packages#website-google"},
             {"name": "Website + Google + Social", "price": "€1,490", "href": "/en/packages#website-google-social"},
             {"name": "All-round", "price": "€2,990", "href": "/en/packages#rundum"},
             {"name": "Custom", "price": "on request", "href": "/en/packages#individuell"}]}},
        {"type": "text", "bg": "sand", "h2": "Most websites bring nothing. Not because they look bad.",
         "paragraphs": ["But because they just exist. Nobody finds them, nobody understands in five seconds what you offer, and nobody knows how to reach you. A website on its own is like a restaurant without a sign on the street.", "That's why I don't just build the website. I build the paths that lead guests to you."]},
        {"type": "chain", "h2": "How clicks turn into guests.", "items": CHAIN, "link": {"text": "Explained in detail", "href": "/en/how-it-works"}},
        {"type": "cards", "bg": "sand", "h2": "For businesses that need someone to walk in tomorrow.", "cols": 4, "items": [
            {"title": "Restaurants", "text": "Restaurants, cafés, bars. Menu, reservations, Google Maps, Instagram. So Tuesday doesn't stay empty.", "href": "/en/for/restaurants"},
            {"title": "Holiday rentals", "text": "Holiday home or apartment, at home or abroad. Multilingual, with direct enquiry.", "href": "/en/for/holiday-rentals"},
            {"title": "Trades", "text": "Whoever googles you should hire you. Google profile, reviews, enquiry in one tap.", "href": "/en/for/trades"},
            {"title": "Practices & studios", "text": "Physio, beauty, massage, naturopathy, vets. A professional presence, appointment requests included.", "href": "/en/for/practices-studios"},
        ]},
        {"type": "packages", "h2": "Four packages. All prices are right here.", "intro": "Pay once, the website is yours. No subscription, no lock-in. All prices excl. VAT.", "items": PACKAGES_SHORT, "link": {"text": "All details and what's not included", "href": "/en/packages"}},
        {"type": "highlight", "h2": "Already have a website – and it brings nothing?", "paragraphs": ["You're not alone. I look at your website, Google profile and Instagram and tell you in plain language what's wrong. The visibility check costs €60 – and is fully credited against any package."],
         "buttons": [{"text": "To the visibility check", "href": "/en/visibility-check"}, {"text": "More about the rebuild", "href": "/en/website-no-enquiries"}], "big": "€60"},
        {"type": "split", "image_left": True, "image": "about-hands", "alt": "Hands over a notebook, espresso cup, shadow of a palm leaf", "h2": "One person. One price. No queue.",
         "paragraphs": ["Behind KWiDi is me, Kristina. I grew an Instagram profile to 6,000 followers in four months – organically, without ads – and run the online presence of a premium service business on Mallorca, where I live. I know what matters because I do it myself every day."],
         "bullets": [{"title": "Everything from one person.", "text": "Website, Google, Instagram, Facebook – one contact, one price."}, {"title": "You provide almost nothing.", "text": "Texts and images come from me. You approve."}, {"title": "You understand what you're buying.", "text": "I explain how it turns into guests – no jargon."}, {"title": "Not alone afterwards.", "text": "Changes later? Same person."}],
         "link": {"text": "More about me", "href": "/en/about"}},
        {"type": "cards", "bg": "sand", "h2": "What I've built myself.", "cols": 3, "items": [
            {"big": "6,000", "title": "followers in 4 months", "text": "An Instagram profile, grown organically. No ads, no giveaways – with posts people actually wanted to see."},
            {"big": "1", "title": "premium service business, fully online", "text": "Website, Google profile and social media of a finca management and rental business – built and run continuously."},
            {"big": "You?", "title": "Your business here", "text": "The first client projects get a special price – and a place on this page.", "href": "#anfrage", "link_text": "Get in touch"},
        ]},
        {"type": "faq", "items": HOME_FAQ},
        FORM,
    ],
})

PAKETE_FAQ = [
    {"q": "Are prices net or gross?", "a": "Net, plus statutory VAT. Business customers in Germany, Austria and Switzerland are invoiced under the reverse-charge procedure – your accountant knows it."},
    {"q": "What does a website cost per month?", "a": "Nothing at KWiDi. You pay once. Only domain and hosting continue with your provider."},
    {"q": "What's the difference to Wix, Jimdo or IONOS?", "a": "There you build it yourself or get a template on subscription. With me you get an individual website with your own texts – and, if you like, Google profile and Instagram along with it. And the site is yours."},
    {"q": "How many revision rounds are included?", "a": "We work until it fits – within the agreed scope. What that means in detail we clarify before the start."},
    {"q": "How long does it take?", "a": "That depends on how quickly you give feedback. Usually a website is online in two to three weeks."},
]
PAGES.append({
    "url": "/en/packages", "title": "Website packages & prices – fixed price from €549 | KWiDi",
    "description": "Four packages, all prices net and public: website from €549, with Google profile €729, with Instagram & Facebook €1,490, all-round €2,990. No subscription.",
    "template": "page",
    "jsonld": [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in PAKETE_FAQ]}],
    "blocks": [
        {"type": "hero", "short": True, "label": "Prices", "h1": "Packages and prices – pay once, it's yours.", "text": "No subscriptions, no hidden costs, no surprise after twelve months. All prices excl. VAT."},
        {"type": "packages", "bg": "sand", "h2": "The four packages at a glance", "items": PACKAGES_FULL,
         "extra": {"id": "individuell", "name": "Individual", "price": "on request", "text": "More pages, other languages, longer support, a support concept just for you. Tell me what you need.", "button": "Enquire"}},
        {"type": "list", "rows": True, "h2": "Also bookable", "items": [
            {"title": "Ads", "text": "Image ads on Instagram and Facebook – price on request. You pay the ad budget directly to Meta; it's not included."},
            {"title": "Visibility check", "text": "€60, fully credited when you book a package.", "href": "/en/visibility-check"},
            {"title": "More languages", "text": "Your website multilingual, e.g. for holiday rentals. Price on request."},
        ]},
        {"type": "list", "bg": "sand", "h2": "What's not included", "intro": "So there are no surprises:", "items": ["Running costs for domain and hosting (with your provider, usually under €10/month)", "Ad budget", "Online shop features", "Professional photo shoots on site (possible on request)"]},
        {"type": "table", "h2": "What a website really costs with website builders.", "head": ["", "Builder “done for you”", "KWiDi"], "rows": [
            ["Price in year one", "approx. €560–740 (setup + monthly fee)", "from €549 one-off"],
            ["After that", "€360–1,020 every year", "€0"],
            ["Pages", "3", "4"],
            ["Texts", "text modules", "individual, by me"],
            ["Google profile", "not included", "included from €729"],
            ["Instagram, Facebook", "not included", "included from €1,490"],
            ["Yours to keep", "no – ends with the subscription", "yes"],
        ], "note": "Figures according to the providers' public pricing pages, September 2026."},
        {"type": "faq", "h2": "What does a website really cost?", "items": PAKETE_FAQ},
        {**FORM, "interest": "New website"},
    ],
})

RELAUNCH_FAQ = [
    {"q": "Why isn't my new website found on Google?", "a": "New sites take weeks before Google even knows them – and without a Google Business Profile, clean page titles and a few links from outside, they stay invisible. That's exactly what I set up in a rebuild."},
    {"q": "What does it cost to have a website reworked?", "a": "At KWiDi from €549 excl. VAT – the same price as a new website. What exactly is needed is clarified by the visibility check."},
    {"q": "Do I need a completely new website?", "a": "Not necessarily. Often it's enough to rebuild structure, texts and Google profile. What can stay, stays."},
    {"q": "Can I keep my domain?", "a": "Yes. Your address stays, your Google reviews stay, nothing is lost."},
]
PAGES.append({
    "url": "/en/website-no-enquiries", "title": "Website not found on Google? Rebuild from €549 | KWiDi",
    "description": "Your website brings no enquiries? I tell you in plain language why – and rebuild it so guests come. Fixed price, no subscription.",
    "template": "page",
    "jsonld": [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in RELAUNCH_FAQ]}],
    "blocks": [
        {"type": "hero", "short": True, "label": "Rebuild · Relaunch", "h1": "Your website is there. But where are the enquiries?", "text": "You put money and time into a website – and nothing happens. It's almost never the design. I tell you what it is and rebuild it so it works.",
         "primary": {"text": "Visibility check for €60", "href": "/en/visibility-check"}, "secondary": {"text": "Rebuild from €549", "href": "#anfrage"}},
        {"type": "reasons", "h2": "Five reasons a website brings no enquiries.", "items": [
            {"title": "Nobody finds it.", "text": "No Google Business Profile, no link, no page titles anyone searches for. The website exists – but only for you."},
            {"title": "Nobody understands it.", "text": "The visitor needs five seconds to know: what do you do, for whom, and what should I do now? If they don't see it immediately, they're gone."},
            {"title": "It doesn't look good on the phone.", "text": "Three out of four visitors come via smartphone. If the menu isn't readable there or the enquiry button is missing, you lose three out of four guests."},
            {"title": "There's no reason to trust you.", "text": "No pictures of you, no reviews, no clear process. The visitor doesn't know you – the website has to change that."},
            {"title": "There's no easy way to reach you.", "text": "The contact form has twelve fields, the phone number is hidden, the reservation link is missing. Every hurdle costs enquiries."},
        ]},
        {"type": "text", "bg": "sand", "h2": "Why your website isn't found on Google.", "paragraphs": ["Usually it's three things: the Google Business Profile is missing or incomplete, the pages have no titles anyone searches for, and nothing on the page tells Google what you actually stand for. All three can be fixed – without rebuilding the website."]},
        {"type": "chain", "h2": "How your website becomes a path to guests.", "intro": "If one of the three is missing, the chain breaks. In a rebuild I look at all three.", "items": CHAIN, "link": {"text": "Explained in detail", "href": "/en/how-it-works"}},
        {"type": "highlight", "h2": "Understand first, then rebuild.", "paragraphs": ["In the visibility check I review website, Google profile and Instagram and email you three to five points in plain language – what's missing, what's off, what comes first. €60 excl. VAT, fully credited against any package. Not an automated report, but my assessment."],
         "buttons": [{"text": "Book the check", "href": "/en/visibility-check"}], "big": "€60"},
        {"type": "text", "h2": "Rebuild at a fixed price – from €549.", "paragraphs": ["You keep your domain and everything that works. I restructure, write the texts, set up the Google profile and make sure the site looks as good on the phone as on the desktop. Instagram and Facebook can be added if you like."], "link": {"text": "See packages", "href": "/en/packages"}},
        {"type": "faq", "items": RELAUNCH_FAQ},
        {**FORM, "interest": "Improve existing website"},
    ],
})

CHECK_FAQ = [
    {"q": "Is the check automated or manual?", "a": "Manual. I look myself – the way a guest would."},
    {"q": "What happens after the check?", "a": "Nothing, if you don't want anything. If you'd like a rebuild, I credit the €60 against the package."},
    {"q": "I don't have a website yet – is the check still worth it?", "a": "Yes, if you have a Google profile or an Instagram account. Then I review those two and tell you what a website would need to add."},
]
PAGES.append({
    "url": "/en/visibility-check", "title": "Website review – visibility check €60 | KWiDi",
    "description": "I review website, Google profile and Instagram and send you 3–5 points in plain language. €60 excl. VAT, fully credited when you book a package.",
    "template": "page",
    "jsonld": [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in CHECK_FAQ]}],
    "blocks": [
        {"type": "hero", "short": True, "label": "€60 · credited", "h1": "Visibility check: why aren't guests coming?", "text": "I look at what a guest sees when they search for you – and tell you what keeps them from coming.", "primary": {"text": "Book the check", "href": "#anfrage"}},
        {"type": "cards", "bg": "sand", "h2": "Three looks that decide.", "cols": 3, "items": [
            {"title": "Google", "text": "Does your business show up on the map? Is the profile complete, are the pictures good, do the categories fit?"},
            {"title": "Website", "text": "Does a stranger understand in five seconds what you do? Does it work on the phone? Does it lead to an enquiry?"},
            {"title": "Instagram and Facebook", "text": "Does the profile look like a business or a private account? Is there a path to the website?"},
        ]},
        {"type": "split", "image": "check-note", "alt": "A sheet of paper with three handwritten points, espresso cup, kiwi slice", "h2": "One email. Three to five points. Plain language.", "paragraphs": ["Not an automated report with scores, but my assessment: what's missing, what's off, what comes first – and what you can do yourself. Within three working days."]},
        {"type": "highlight", "h2": "€60 – and free once you book.", "paragraphs": ["The check costs €60 excl. VAT. If you decide on a package afterwards, I deduct the full €60. So you lose nothing – except the uncertainty."], "big": "€60"},
        {"type": "steps", "inline": True, "h2": "How it works", "items": [
            {"text": "You send me the links (website, Google profile, Instagram – whatever you have)."},
            {"text": "I take a look and write to you within three working days."},
            {"text": "You decide if and what you want to change. No pressure."},
        ]},
        {"type": "faq", "items": CHECK_FAQ},
        {**FORM, "variant": "check", "h2": "Book the check", "text": "Send me the links – I'll get back to you within three working days with my assessment.", "button": "Book the check for €60", "note": "You receive an invoice by email. The check starts once payment is received."},
    ],
})

PAGES.append(industry_page("restaurants", "Restaurant website from €549 | KWiDi",
    "Website with menu, Google profile and Instagram for restaurants, cafés and bars – fully set up at a fixed price. So guests find you before they get hungry.",
    {"type": "hero", "label": "Restaurants · Cafés · Bars", "h1": "Tuesday doesn't have to stay empty.", "text": "Website with menu, Google profile and Instagram – fully set up, so guests find you before they get hungry.", "primary": {"text": "Get in touch – no obligation", "href": "#anfrage"}, "secondary": {"text": "Packages from €549", "href": "/en/packages"}, "image": "hero-gastro", "alt": "Set table on a terrace, a smartphone next to the plate"},
    [
        {"type": "text", "bg": "sand", "h2": "How guests find a restaurant today.", "paragraphs": ["Not by your name. But via “Italian near me”, “breakfast + neighbourhood”, “bar with terrace”. They look at the map, the reviews, three photos – and decide in a minute. Whoever doesn't show up there doesn't exist for that guest."]},
        {"type": "chain", "h2": "Found. Convinced. Came back.", "items": [
            {"title": "Google profile", "sub": "Get found", "text": "Opening hours, map, photos, reviews – what the guest sees first. I set it up completely."},
            {"title": "Website", "sub": "Convince", "text": "Menu readable on the phone in thirty seconds, reservation in one tap, pictures that make you hungry."},
            {"title": "Instagram", "sub": "Stay in mind", "text": "Today's dish, the terrace in the evening, the team. So people think of you when Saturday is being planned."},
        ]},
        {"type": "split", "bg": "sand", "image": "detail-menu", "alt": "Menu on a smartphone", "h2": "What your restaurant website includes.", "bullets": ["A menu you can change yourself", "Opening hours, address, directions with Google Maps", "Reservations: link to your system or an enquiry form", "Gallery with your best pictures", "Pages for events, celebrations, catering – if you offer them", "Legal notice and privacy policy"]},
        {"type": "highlight", "h2": "What two more tables a week mean.", "paragraphs": ["Two additional tables per week at an average of €60 per table: that's over €6,000 a year. The website costs €549 once. You don't need to be good at maths to see it pays off."], "big": "€6,240"},
        {"type": "packages", "h2": "My package for restaurants: Website + Google + Social.", "intro": "Website with menu, complete Google profile, Instagram and Facebook set up and filled with six posts. Because food is the most rewarding Instagram topic there is.", "items": [PACKAGES_SHORT[2]], "link": {"text": "All packages", "href": "/en/packages"}},
    ], "Restaurant / café / bar",
    [
        {"q": "What does a restaurant website cost?", "a": "At KWiDi from €549 excl. VAT. With Google profile €729, with Instagram and Facebook €1,490."},
        {"q": "Can I change the menu myself?", "a": "Yes, it's set up so you can adjust prices and dishes without me. Or you send me the change – that works too."},
        {"q": "Do I need a reservation feature?", "a": "If you use a system (resmio, OpenTable, Quandoo …), I integrate it. If not, an enquiry form or a tap on your phone number is enough."},
        {"q": "Is Instagram worth it for a small restaurant?", "a": "Yes – especially for small ones. A good picture of a plate reaches more people than any newspaper ad. And you don't have to post daily: I set everything up so two posts a week keep you going."},
    ], "Website for restaurants"))

PAGES.append(industry_page("holiday-rentals", "Holiday rental website – multilingual | KWiDi",
    "Your own website for a holiday home or apartment – multilingual, with direct enquiry and Google profile. For properties at home or abroad. From €549.",
    {"type": "hero", "label": "Holiday home · Apartment · Finca", "h1": "Your holiday home. Your website. Your bookings.", "text": "Multilingual, with direct enquiry and Google profile – for owners whose property is in Germany, on the Mediterranean or anywhere else in Europe.", "primary": {"text": "Get in touch – no obligation", "href": "#anfrage"}, "secondary": {"text": "Packages from €549", "href": "/en/packages"}, "image": "hero-fewo", "alt": "Archway with sea view, rattan chair, notebook with calendar"},
    [
        {"type": "text", "bg": "sand", "h2": "Booking and Airbnb bring guests. But they don't belong to you.", "paragraphs": ["Every booking via a portal costs you 15 to 20 percent. The guest knows your house, but not you. When they want to come back, they book via the portal again – and you pay again. Your own website changes that: repeat guests, recommendations and everyone who finds you on Google book directly."]},
        {"type": "chain", "h2": "How guests find your holiday home directly.", "items": [
            {"title": "Google profile for your property", "sub": "Get found", "text": "Yes, a holiday home can be on the map too – with photos, reviews and a link to you."},
            {"title": "Website", "sub": "Convince", "text": "Pictures, amenities, location, prices, availability calendar, enquiry in a minute. In your guests' language."},
            {"title": "Instagram", "sub": "Stay in mind", "text": "The view from the terrace, the village market, the way to the beach. So guests are already on holiday before they book."},
        ]},
        {"type": "cards", "bg": "sand", "h2": "Multilingual. Connected. From experience.", "cols": 3, "items": [
            {"title": "Set up multilingually", "text": "German and English are standard, I add further languages as needed. Just like this site: tap DE at the top right – you get that too."},
            {"title": "Your booking system stays", "text": "Using Smoobu, Lodgify or another system? I embed the availability calendar so no double booking happens. You don't have to switch anything."},
            {"title": "I live where your guests go on holiday", "text": "I live on Mallorca and run the online presence of a business that manages and rents fincas. I know what guests ask, what they want to see in pictures and where enquiries fail."},
        ]},
        {"type": "highlight", "h2": "Ten direct bookings a year – and the website is paid for.", "paragraphs": ["A week at €900 via the portal costs you €135 to €180 in commission. Ten weeks booked directly: €1,350 saved. The website costs €549 once."], "big": "€1,350"},
        {"type": "packages", "h2": "My package for holiday rentals: Website + Google.", "intro": "€729 excl. VAT – or with Instagram and Facebook for €1,490 if you want to show your house there too.", "items": [PACKAGES_SHORT[1], PACKAGES_SHORT[2]], "link": {"text": "All packages", "href": "/en/packages"}},
    ], "Holiday rental",
    [
        {"q": "Can I embed my availability calendar from Booking or Smoobu?", "a": "Yes. Calendar sync via iCal or directly from your system, so everything stays up to date."},
        {"q": "Which languages?", "a": "German and English are always included. I set up further languages – the translation runs through a system that I review and adjust."},
        {"q": "Is a website worth it with just one property?", "a": "Yes, as soon as you have or want repeat guests. A property rented directly for five weeks a year saves more commission than the website costs."},
        {"q": "My house is abroad – what do I need to consider?", "a": "On the website: nothing special. For taxes and rental law in the respective country, please ask your tax advisor – that's not my job, but I'll tell you what needs to go on the site."},
    ], "Website for holiday rentals"))

PAGES.append(industry_page("trades", "Website for tradespeople from €549 | KWiDi",
    "Website and Google Business Profile for craft and trade businesses – credible, quickly found, enquiry in one tap. Fixed price, no subscription, texts included.",
    {"type": "hero", "label": "Craft & trade businesses", "h1": "Whoever googles you should hire you.", "text": "Website and Google Business Profile for trade businesses – credible, quickly found, with one tap to the enquiry.", "primary": {"text": "Get in touch – no obligation", "href": "#anfrage"}, "secondary": {"text": "Packages from €549", "href": "/en/packages"}, "image": "hero-handwerk", "alt": "Wooden workbench, hands with a folding rule in sunlight"},
    [
        {"type": "text", "bg": "sand", "h2": "How customers look for a tradesperson today.", "paragraphs": ["“Electrician + town”, “roofer near me”, “painter reviews”. They see three businesses on the map, compare stars and photos and call the one that looks most trustworthy. Recommendations aren't enough anymore if the recommended can't be found online."]},
        {"type": "text", "h2": "Google profile: map, reviews, call.", "paragraphs": ["For trades, the Google Business Profile matters more than any website. Fully set up with services, service area, photos from the job site and a call button. I set it up and link it to your website."]},
        {"type": "split", "bg": "sand", "image": "detail-handwerk", "alt": "Google Business Profile of a trade business, suggested", "h2": "What your trade website includes.", "bullets": ["Your services, clear and without jargon", "Service area", "Pictures of real projects (if you have none, I tell you which five photos to take with your phone)", "Enquiry form and tap-to-call", "About the business: who you are, since when, what sets you apart", "Legal notice and privacy policy"]},
        {"type": "text", "h2": "First impressions count for applicants too.", "paragraphs": ["Anyone who wants to apply to you googles you first. A business with a tidy presence gets the better applications. A “Jobs” page is included in the package if you need it."]},
        {"type": "packages", "bg": "sand", "h2": "My package for trades: Website + Google.", "intro": "€729 excl. VAT. Four pages plus a complete Google profile – what customers and applicants see first.", "items": [PACKAGES_SHORT[1]], "link": {"text": "All packages", "href": "/en/packages"}},
    ], "Trades",
    [
        {"q": "What does a trade website cost?", "a": "From €549 excl. VAT, with Google profile €729."},
        {"q": "I have no photos – does it still work?", "a": "Yes. I tell you exactly which pictures to take with your phone – and I solve the rest."},
        {"q": "Do I need Instagram as a tradesperson?", "a": "Not necessarily. For most businesses, website and Google profile are enough. If you have before-and-after pictures, Instagram can be a good channel for applicants – we'll discuss it."},
    ], "Website for trades"))

PAGES.append(industry_page("practices-studios", "Practice & studio website from €549 | KWiDi",
    "Website, Google profile and Instagram for physiotherapy, beauty, massage, naturopathy and vets – professional, with appointment requests. Fixed price.",
    {"type": "hero", "label": "Physio · Beauty · Massage · Naturopathy · Vets", "h1": "Your presence – as professional as your work.", "text": "Website, Google profile and Instagram for practices and studios – with appointment requests, so the calendar fills up.", "primary": {"text": "Get in touch – no obligation", "href": "#anfrage"}, "secondary": {"text": "Packages from €549", "href": "/en/packages"}, "image": "hero-studio", "alt": "Treatment room in sand tones, folded linen, olive branch"},
    [
        {"type": "text", "bg": "sand", "h2": "How new clients find a practice or studio.", "paragraphs": ["Via Google and via recommendations – and in both cases they look at your presence first. Does it look like a private account or like a business you'd trust with your back or your face?"]},
        {"type": "split", "image": "detail-studio", "alt": "Appointment book and linen", "h2": "What your website includes.", "bullets": ["Services with prices or price ranges", "Appointment request – or integration of your booking system", "About you: training, experience, your approach", "Rooms and atmosphere in pictures", "Google reviews embedded", "Legal notice and privacy policy"]},
        {"type": "text", "bg": "sand", "h2": "Instagram for studios: show what you can do.", "paragraphs": ["Treatment rooms, results (where permitted), tips, your team. I set up the profile to match your website – and fill it with the first posts."]},
        {"type": "packages", "h2": "My package for practices & studios: Website + Google + Social.", "intro": "€1,490 excl. VAT. Because in this industry Instagram is often the first contact – and Google the second.", "items": [PACKAGES_SHORT[2]], "link": {"text": "All packages", "href": "/en/packages"}},
    ], "Practice & studio",
    [
        {"q": "Can I integrate online appointment booking?", "a": "Yes. If you use a system, I integrate it. If not, you get an appointment request form."},
        {"q": "What am I allowed to write as a naturopath or physio?", "a": "No promises of cure, no before-and-after pictures for medical treatments – that's regulated by German health advertising law. I write the texts so they convince without crossing those lines. The final review is yours."},
        {"q": "What does a practice website cost?", "a": "From €549 excl. VAT, with Google profile €729, with Instagram and Facebook €1,490."},
    ], "Website for practices & studios"))

PAGES.append({
    "url": "/en/how-it-works", "title": "How a website brings guests – how KWiDi works",
    "description": "Google profile, website, Instagram – how they work together and how the collaboration runs. In four steps, no jargon.",
    "template": "page", "jsonld": [],
    "blocks": [
        {"type": "hero", "short": True, "label": "Explained", "h1": "How clicks turn into guests.", "text": "Being visible online isn't a technical question. It's the question of whether someone walks in tomorrow. Here's the chain – and how our collaboration works."},
        {"type": "split", "image_left": True, "image": "how-map", "alt": "Hands drawing a map with a pin on paper", "label": "Step 1", "h2": "Get found – the Google Business Profile.", "paragraphs": ["When someone types “café near me” or “holiday home Croatia sea view”, Google shows the map first. There you find businesses with a complete profile: opening hours, photos, reviews, category. Whoever has no profile, or one with three details, isn't on the map. The profile costs nothing – the work is doing it right. That's exactly what's in package 2."]},
        {"type": "split", "bg": "sand", "image": "how-phone", "alt": "Smartphone in hand, screen shows a light page", "label": "Step 2", "h2": "Convince – the website.", "paragraphs": ["The click from the profile leads to your website. Now the guest has one question: is this for me? They want pictures, prices, a feel for the place and a way to reach you. All on the phone, in thirty seconds. A website that manages that brings enquiries. One that doesn't brings nothing – no matter how pretty."]},
        {"type": "split", "image_left": True, "image": "how-photos", "alt": "Stack of photos of plates and terraces on linen", "label": "Step 3", "h2": "Stay in mind – Instagram and Facebook.", "paragraphs": ["Most guests don't come at first contact. They see you, forget you, see you again – and then they come. Instagram and Facebook take care of the reunion. For that you don't need daily posting, but a profile that looks like a business and a few good posts to start. That's package 3."]},
        {"type": "text", "bg": "sand", "h2": "Is Instagram even worth it for small businesses?", "paragraphs": ["For restaurants, studios and holiday rentals: yes, clearly – because pictures sell there. For trades: usually Google is enough. I'll tell you honestly if you don't need something."]},
        {"type": "steps", "h2": "How the collaboration works.", "items": [
            {"title": "You get in touch.", "text": "Via the form, in two or three sentences. I reply within 24 hours on working days."},
            {"title": "We clarify what you need.", "text": "By email: which package, which content, what you already have. Then you get a quote."},
            {"title": "I build, you approve.", "text": "You get a draft, say what fits and what doesn't. We work until it's right."},
            {"title": "Everything goes live.", "text": "Website, Google profile, Instagram – set up and linked. You get all access details."},
        ], "note": "Usually this takes two to three weeks – depending on how quickly you give feedback."},
        {"type": "highlight", "h2": "What do you have to provide? Almost nothing.", "paragraphs": ["A few answers to my questions, your opening hours, prices – and pictures if you have them. I write the texts. I organise images if you have none. Tech is entirely my job."], "buttons": [{"text": "Get in touch – no obligation", "href": "#anfrage"}]},
        FORM,
    ],
})

PAGES.append({
    "url": "/en/about", "title": "About KWiDi – Kristina, one contact for everything",
    "description": "Behind KWiDi is one person: Kristina. 6,000 followers in 4 months built herself, online presences run for businesses. No team, no ticket system.",
    "template": "page", "jsonld": [],
    "blocks": [
        {"type": "hero", "label": "About", "h1": "Hi, I'm Kristina.", "text": "Behind KWiDi is not an agency, but me. I build websites and online presences for small businesses – and explain it so you understand what you're buying.", "image": "hero-kristina", "alt": "Kristina, founder of KWiDi"},
        {"type": "split", "image": "about-hands", "alt": "Hands over a notebook, espresso cup", "h2": "Why KWiDi.", "paragraphs": ["I've seen too often how small businesses spend money on a website and then nothing happens. Not because the website was bad. But because nobody told them that the website is only one part – and Google and Instagram are the other two. KWiDi is my attempt to do it differently: everything from one person, at a price you can afford, with an explanation you understand."], "quote": "The name? Kristina Swiderski and kiwi. Fresh, honest, uncomplicated."},
        {"type": "cards", "bg": "sand", "h2": "What I've built myself.", "cols": 3, "items": [
            {"big": "6,000", "title": "followers in four months", "text": "An Instagram profile, organic, no ads. With posts about Mallorca, where I live."},
            {"big": "1", "title": "premium service business", "text": "The online presence of a finca management and rental business: website, Google profile, social media, ongoing support."},
            {"big": "Soon", "title": "The first KWiDi clients", "text": "The first businesses get a special price – in return I get to show them here.", "href": "#anfrage", "link_text": "Get in touch"},
        ]},
        {"type": "cards", "h2": "How I work.", "cols": 2, "items": [
            {"title": "By email.", "text": "Not because I don't like talking – but because everything stays on record and I can focus on your project. You get a reply within 24 hours on working days."},
            {"title": "At a fixed price.", "text": "You know beforehand what it costs. No subscription, no surprise."},
            {"title": "Honestly.", "text": "If you don't need something, I say so. A tradesperson doesn't need Instagram. A café does."},
            {"title": "Reachable afterwards.", "text": "Changes in a year? Write to me. Same person, same address."},
        ]},
        FORM,
    ],
})

PAGES.append({
    "url": "/en/contact", "title": "Contact – enquiry to KWiDi",
    "description": "Tell me briefly what you have in mind. Reply within 24 hours on working days – by email, no phone appointment.",
    "template": "page", "jsonld": [],
    "blocks": [{"type": "form", "bg": "ivory", "as_h1": True, "h2": "Let's see what fits you.", "text": "Tell me what you have in mind – two or three sentences are enough. I reply within 24 hours on working days, by email. No sales talk, no queue.",
                "aside": ["<b>Already have a website?</b> Then the visibility check might be the better first step. <a class=\"link\" href=\"/en/visibility-check\">More</a>"]}],
})

PAGES.append({"url": "/en/thank-you", "title": "Thank you – KWiDi", "description": "Your message has arrived.", "template": "page", "noindex": True, "lead": True, "jsonld": [],
    "blocks": [{"type": "simple", "h1": "Thank you – your message has arrived.", "paragraphs": ["I'll get back to you within 24 hours on working days. In the meantime, have a look at how the collaboration works."], "buttons": [{"text": "How it works", "href": "/en/how-it-works"}, {"text": "Back to home", "href": "/en/"}]}]})

PAGES.append({"url": "/en/404", "title": "Page not found – KWiDi", "description": "This page doesn't exist.", "template": "page", "noindex": True, "jsonld": [],
    "blocks": [{"type": "simple", "h1": "This page doesn't exist.", "paragraphs": ["Maybe the link is old – or I've rebuilt. Continue here:"], "buttons": [{"text": "Home", "href": "/en/"}, {"text": "Packages & prices", "href": "/en/packages"}, {"text": "Contact", "href": "/en/contact"}]}]})

LEGAL_HTML = """
<p class="lede">Information according to § 5 DDG (German Digital Services Act). The German version is legally binding.</p>
<p><b>KWiDi</b> is a brand of<br><b>Swiderski Property Management S.L.</b><br>Calle San Miguel 36, PTA B5<br>07002 Palma de Mallorca, Illes Balears, Spain</p>
<h2>Represented by</h2><p>Patrick Swiderski, Administrador</p>
<h2>Contact</h2><p>Email: <a href="mailto:kristinaswiderski@outlook.com">kristinaswiderski@outlook.com</a><br>Phone: +34 601 993 373</p>
<h2>Register entry</h2><p>Registro Mercantil de las Illes Balears, Palma de Mallorca · NIF: B21648753</p>
<h2>VAT ID</h2><p>ESB21648753</p>
<h2>Responsible for content</h2><p>Kristina Swiderski, address as above</p>
<h2>Dispute resolution</h2><p>The European Commission provides a platform for online dispute resolution: <a href="https://ec.europa.eu/consumers/odr/" rel="noopener" target="_blank">https://ec.europa.eu/consumers/odr/</a>. We are neither obliged nor willing to participate in dispute resolution proceedings before a consumer arbitration board.</p>
<h2>Liability for content and links</h2><p>The content of this website was created with great care; we do not guarantee its accuracy, completeness or timeliness. The operators of linked pages are solely responsible for their content.</p>
<p class="muted">All offers on this website are aimed at businesses. Prices are net plus statutory VAT.</p>
"""
PAGES.append({"url": "/en/legal-notice", "title": "Legal notice – KWiDi", "description": "Legal notice of KWiDi.", "template": "page", "noindex": True, "jsonld": [],
    "blocks": [{"type": "legal", "h1": "Legal notice", "html": LEGAL_HTML}]})

PRIVACY_HTML = """
<p class="lede">Last updated: September 2026. The German version is legally binding.</p>
<h2>1. Controller</h2><p>Swiderski Property Management S.L. (brand KWiDi), Calle San Miguel 36, PTA B5, 07002 Palma de Mallorca, Spain · Email: <a href="mailto:kristinaswiderski@outlook.com">kristinaswiderski@outlook.com</a></p>
<h2>2. General</h2><p>We process personal data only as far as necessary to provide this website and our services, or with your consent. Legal bases are Art. 6(1)(a) (consent), (b) (contract) and (f) (legitimate interest) GDPR.</p>
<h2>3. Hosting and server logs</h2><p>This website is hosted by an external provider within the EU. Server log files (IP address, date and time, page requested, browser type, referrer) are processed automatically for security and stability (Art. 6(1)(f) GDPR) and deleted after 14 days at the latest. A data processing agreement is in place with the hosting provider.</p>
<h2>4. Contact form and email</h2><p>When you contact us via the form or by email, we process the data you provide (name, email address, business details, message, optional links) to handle your enquiry and follow-up questions (Art. 6(1)(b) GDPR). Form data is forwarded to our email address via the service FormSubmit (formsubmit.co), which processes the data solely for delivery. We keep enquiries until they are dealt with and no statutory retention periods apply.</p>
<h2>5. Cookies and consent</h2><p>Technically necessary storage (e.g. your cookie choice) is used without consent. Statistics and marketing cookies are only set once you agree in the cookie banner. Your choice is stored locally in your browser and can be changed or withdrawn at any time via “Cookie settings” in the footer.</p>
<h2>6. Google Analytics 4</h2><p>With your consent (Art. 6(1)(a) GDPR) we use Google Analytics 4 by Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Ireland. Google Analytics uses cookies and similar technologies to analyse website usage. IP addresses are truncated. Data may be transferred to Google LLC in the USA; Google is certified under the EU-US Data Privacy Framework. We use Google Consent Mode so no cookies are set without consent. Retention: 14 months. More: <a href="https://policies.google.com/privacy" rel="noopener" target="_blank">policies.google.com/privacy</a>.</p>
<h2>7. Meta Pixel (Facebook, Instagram)</h2><p>With your consent (Art. 6(1)(a) GDPR) we use the Meta Pixel by Meta Platforms Ireland Limited, Merrion Road, Dublin 4, Ireland, to measure our ads and build audiences. Data may be transferred to Meta Platforms Inc. in the USA; Meta is certified under the EU-US Data Privacy Framework. We are jointly responsible with Meta (Art. 26 GDPR) for collection and transfer; Meta is responsible for further processing. More: <a href="https://www.facebook.com/privacy/policy" rel="noopener" target="_blank">facebook.com/privacy/policy</a>.</p>
<h2>8. Fonts</h2><p>The fonts used (Fraunces, Jost) are hosted locally on our server. No connection to Google servers is made.</p>
<h2>9. Links to Instagram and Facebook</h2><p>Our website links to our Instagram and Facebook profiles. No content from these platforms is embedded; only when you click a link do you leave our website, and the respective provider's privacy policy applies.</p>
<h2>10. Your rights</h2><p>You have the right to access (Art. 15 GDPR), rectification (Art. 16), erasure (Art. 17), restriction (Art. 18), data portability (Art. 20) and objection (Art. 21 GDPR). You may withdraw consent at any time with effect for the future. You also have the right to lodge a complaint with a supervisory authority – in Spain the Agencia Española de Protección de Datos (AEPD).</p>
<h2>11. Changes</h2><p>We update this policy when the legal situation or our services change. The version published here applies.</p>
"""
PAGES.append({"url": "/en/privacy", "title": "Privacy policy – KWiDi", "description": "Privacy policy of KWiDi.", "template": "page", "noindex": True, "jsonld": [],
    "blocks": [{"type": "legal", "h1": "Privacy policy", "html": PRIVACY_HTML}]})
