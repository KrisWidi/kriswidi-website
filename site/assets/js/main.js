/* KWiDi – main.js: navigation, reveal, forms, consent (Consent Mode v2) */
(function () {
  'use strict';
  var cfg = window.KWIDI || {};

  /* ---------- Header / mobile menu ---------- */
  var header = document.querySelector('.site-header');
  var menu = document.getElementById('mobile-menu');
  var burger = document.querySelector('.burger');
  var closeBtn = menu && menu.querySelector('.close');
  function openMenu () { menu.classList.add('open'); document.body.style.overflow = 'hidden'; burger.setAttribute('aria-expanded', 'true'); }
  function closeMenu () { menu.classList.remove('open'); document.body.style.overflow = ''; burger.setAttribute('aria-expanded', 'false'); }
  if (burger && menu) {
    burger.addEventListener('click', openMenu);
    closeBtn && closeBtn.addEventListener('click', closeMenu);
    menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', closeMenu); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMenu(); });
  }
  window.addEventListener('scroll', function () {
    if (header) header.classList.toggle('is-compact', window.scrollY > 40);
  }, { passive: true });

  /* ---------- Sticky CTA hides when a form is visible ---------- */
  var sticky = document.querySelector('.sticky-cta');
  var forms = document.querySelectorAll('form.form');
  if (sticky && forms.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      var visible = entries.some(function (e) { return e.isIntersecting; });
      sticky.classList.toggle('hidden', visible);
    }, { threshold: 0.1 });
    forms.forEach(function (f) { io.observe(f); });
  }

  /* ---------- Reveal on scroll ---------- */
  // Interaktive Kiwi: Desktop = Hover-Labels (CSS). Touch/Mobil = Kerne leuchten beim ersten Sichtbarwerden
  // nacheinander auf, der Paketname erscheint darunter; Tippen zeigt das Paket, zweites Tippen folgt dem Link.
  document.querySelectorAll('.kiwi').forEach(function (kiwi) {
    var seeds = Array.prototype.slice.call(kiwi.querySelectorAll('.seed'));
    var live = kiwi.querySelector('.kiwi-live');
    var mobile = window.matchMedia('(hover: none), (max-width: 820px)').matches;
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var current = -1, timer = null;
    var show = function (i) {
      seeds.forEach(function (a, k) { a.classList.toggle('on', k === i); });
      if (live && i >= 0) {
        var b = seeds[i].querySelector('b');
        live.innerHTML = '<b>' + (b ? b.textContent : '') + '</b> <span class="p">· ' + seeds[i].querySelector('span').lastChild.textContent + '</span>';
        live.classList.add('show');
      }
      current = i;
    };
    var sequence = function () {
      if (!mobile) return;
      if (reduce) { show(0); return; }
      var i = 0;
      timer = setInterval(function () { show(i); i++; if (i >= seeds.length) { clearInterval(timer); timer = null; } }, 900);
    };
    if ('IntersectionObserver' in window) {
      var ko = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { kiwi.classList.add('play'); sequence(); ko.disconnect(); } }); }, { threshold: 0.5 });
      ko.observe(kiwi);
    } else { kiwi.classList.add('play'); sequence(); }
    seeds.forEach(function (a, k) {
      a.addEventListener('click', function (ev) {
        kiwi.classList.add('touched');
        if (mobile && current !== k) {
          ev.preventDefault();
          if (timer) { clearInterval(timer); timer = null; }
          show(k);
        }
      });
    });
  });

  var reveals = document.querySelectorAll('.reveal');
  if (reveals.length && 'IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var ro = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); ro.unobserve(e.target); } });
    }, { threshold: 0.12 });
    reveals.forEach(function (el) { ro.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- Forms ---------- */
  document.querySelectorAll('form.form').forEach(function (form) {
    var msg = form.querySelector('.form-msg');
    var t = cfg.formText || {};
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      // Honeypot
      var hp = form.querySelector('input[name="website_url"]');
      if (hp && hp.value) return;
      var required = form.querySelectorAll('[required]');
      var ok = true;
      required.forEach(function (el) {
        var field = el.closest('.field, .check');
        var valid = el.type === 'checkbox' ? el.checked : el.value.trim().length > 0;
        if (el.type === 'email' && valid) valid = /.+@.+\..+/.test(el.value);
        field && field.classList.toggle('error', !valid);
        if (!valid) ok = false;
      });
      if (!ok) { show(msg, 'err', t.invalid || 'Bitte fülle alle Pflichtfelder aus.'); return; }
      var endpoint = form.getAttribute('action');
      if (!endpoint || endpoint.indexOf('FORM_ENDPOINT') !== -1) {
        show(msg, 'err', t.noEndpoint || 'Formular-Versand ist noch nicht konfiguriert (FORM_ENDPOINT in config.js).');
        return;
      }
      var btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      var data = new FormData(form);
      fetch(endpoint, { method: 'POST', body: data, headers: { 'Accept': 'application/json' } })
        .then(function (r) { if (!r.ok) throw new Error('bad'); return r; })
        .then(function () {
          var next = form.getAttribute('data-thanks');
          if (next) window.location.href = next; else { show(msg, 'ok', t.ok || 'Danke – deine Nachricht ist da.'); form.reset(); }
        })
        .catch(function () { show(msg, 'err', t.fail || 'Das hat nicht geklappt. Schreib mir bitte direkt per E-Mail.'); })
        .finally(function () { btn.disabled = false; });
    });
  });
  function show (el, cls, text) { if (!el) return; el.className = 'form-msg show ' + cls; el.textContent = text; }

  /* ---------- Consent (Google Consent Mode v2 + Meta Pixel) ---------- */
  var KEY = 'kwidi-consent-v1';
  var banner = document.getElementById('consent');
  window.dataLayer = window.dataLayer || [];
  function gtag () { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;
  gtag('consent', 'default', {
    ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied', wait_for_update: 500
  });

  function read () { try { return JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { return null; } }
  function save (c) { try { localStorage.setItem(KEY, JSON.stringify(c)); } catch (e) {} }

  var loaded = { ga: false, meta: false };
  function loadGA () {
    if (loaded.ga || !cfg.gaId) return; loaded.ga = true;
    var s = document.createElement('script'); s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + cfg.gaId; document.head.appendChild(s);
    gtag('js', new Date()); gtag('config', cfg.gaId, { anonymize_ip: true });
  }
  function loadMeta () {
    if (loaded.meta || !cfg.metaPixelId) return; loaded.meta = true;
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    window.fbq('init', cfg.metaPixelId); window.fbq('track', 'PageView');
    if (document.body.getAttribute('data-lead') === '1') window.fbq('track', 'Lead');
  }
  function apply (c) {
    gtag('consent', 'update', {
      analytics_storage: c.analytics ? 'granted' : 'denied',
      ad_storage: c.marketing ? 'granted' : 'denied',
      ad_user_data: c.marketing ? 'granted' : 'denied',
      ad_personalization: c.marketing ? 'granted' : 'denied'
    });
    if (c.analytics) loadGA();
    if (c.marketing) loadMeta();
  }
  var stored = read();
  if (stored) { apply(stored); } else if (banner) { banner.classList.add('show'); }
  if (banner) {
    banner.querySelector('[data-consent="all"]').addEventListener('click', function () { var c = { analytics: true, marketing: true }; save(c); apply(c); banner.classList.remove('show'); });
    banner.querySelector('[data-consent="none"]').addEventListener('click', function () { var c = { analytics: false, marketing: false }; save(c); apply(c); banner.classList.remove('show'); });
    banner.querySelector('[data-consent="settings"]').addEventListener('click', function () { banner.classList.toggle('expanded'); });
    banner.querySelector('[data-consent="save"]').addEventListener('click', function () {
      var c = { analytics: banner.querySelector('#c-analytics').checked, marketing: banner.querySelector('#c-marketing').checked };
      save(c); apply(c); banner.classList.remove('show');
    });
    document.querySelectorAll('[data-open-consent]').forEach(function (a) {
      a.addEventListener('click', function (e) { e.preventDefault(); var s = read() || {}; banner.querySelector('#c-analytics').checked = !!s.analytics; banner.querySelector('#c-marketing').checked = !!s.marketing; banner.classList.add('show', 'expanded'); });
    });
  }

  /* ---------- Tarif-Rechner (Betriebs-App) ---------- */
  document.querySelectorAll('[data-calc]').forEach(function (box) {
    var base = parseFloat(box.getAttribute('data-base')) || 0, per = parseFloat(box.getAttribute('data-per')) || 0;
    var setup = parseFloat(box.getAttribute('data-setup')) || 0;
    var range = box.querySelector('input[type=range]'), out = box.querySelector('#calc-n-out'), month = box.querySelector('#calc-month'), line = box.querySelector('#calc-line');
    var tpl = line ? line.textContent : '';
    function fmt (n) { return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, '.') + ' €'; }
    function upd () {
      var n = parseInt(range.value, 10) || 1, m = base + per * (n - 1);
      if (out) out.textContent = n;
      if (month) month.textContent = fmt(m);
      if (line) line.textContent = tpl.replace('{n}', n).replace('{m}', fmt(m)).replace('{y}', fmt(m * 12)).replace('{s}', fmt(setup)).replace('{extra}', n - 1);
      var btn = box.querySelector('[data-package]'); if (btn) btn.setAttribute('data-package', (btn.getAttribute('data-package') || '').split(' (')[0] + ' (' + n + ')');
    }
    if (range) { range.addEventListener('input', upd); upd(); }
  });

  /* ---------- Paket-Buttons füllen das Formular vor ---------- */
  document.querySelectorAll('a[data-package]').forEach(function (a) {
    a.addEventListener('click', function () {
      var pkg = a.getAttribute('data-package') || '', sel = document.getElementById('f-interest'), msg = document.getElementById('f-msg');
      if (sel) { var opts = Array.prototype.slice.call(sel.options), hit = opts.filter(function (o) { return pkg.indexOf(o.value.split(' (')[0]) === 0 || o.value.indexOf(pkg.split(' (')[0]) === 0; })[0]; if (hit) sel.value = hit.value; }
      if (msg && !msg.value) msg.value = pkg + ': ';
    });
  });
})();