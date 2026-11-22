"""Builds coutume.app in English, French and Spanish: the three home pages, the 12 guides, the habit-ideas hub and its
how-to articles, the language links and footers of the hand-written pages (support, privacy, 404), sitemap.xml and llms.txt.

    python3 scripts/site/build.py .

Text lives in this folder: content.py (the guides in English and French), guides_es.py (the guides in Spanish),
articles/*.py (the how-to articles, three languages each), build_home.py (the home pages' words in English and French)
and HOME_ES below. The English and French home pages also keep their feature list and questions in their JSON-LD,
which this script reads back: edit them there.
"""
import glob, json, os, re, sys
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_home as BH
import build_guides as BG
from content import PAGES, RELATED, SCREENS

ROOT = sys.argv[1]
SITE = "https://coutume.app/"
DATE = "2026-11-21"
LANGS = ("en", "fr", "es")
PREFIX = {"en": "", "fr": "fr/", "es": "es/"}
NAME = {"en": "English", "fr": "Français", "es": "Español"}
LOCALE = {"en": "en_CA", "fr": "fr_CA", "es": "es_ES"}
OG = {"en": "og-en.png", "fr": "og-fr.png", "es": "og-en.png"}
UPDATED = {"en": "Last updated: November 21, 2026", "fr": "Dernière mise à jour&nbsp;: 21&nbsp;novembre&nbsp;2026",
           "es": "Última actualización: 21 de noviembre de 2026"}
HEART = BH.HEART
SUPPORT = {"en": "support/", "fr": "fr/assistance/", "es": "es/soporte/"}
PRIVACY = {"en": "privacy/", "fr": "fr/confidentialite/", "es": "es/privacidad/"}
L10N = {
    "en": dict(skip="Skip to content", support="Support", privacy="Privacy", footer="Footer", crumbs="Breadcrumb",
               made=f'Made with <svg class="heart" viewBox="0 0 24 22" role="img" aria-label="love">{HEART}</svg> by <a href="https://wibeset.ca">Wibeset</a>. Developed in Canada.',
               aside="Coutume on iPhone", cta="Coutume is coming soon to the App Store, for iPhone: free, with no account, no ads and no subscription.",
               related="Related guides", questions="Questions",
               q='See the <a href="{home}#faq-heading">frequently asked questions</a> or visit <a href="{support}">Support</a>.',
               why="Why it’s worth it", start="How to start", hard="When it gets hard", track="Track it in Coutume",
               more_ideas="More habit ideas", all_ideas="All 40 habit ideas"),
    "fr": dict(skip="Aller au contenu", support="Assistance", privacy="Confidentialité", footer="Pied de page", crumbs="Fil d’Ariane",
               made=f'Fait avec <svg class="heart" viewBox="0 0 24 22" role="img" aria-label="amour">{HEART}</svg> par <a href="https://wibeset.ca">Wibeset</a>. Développé au Canada.',
               aside="Coutume sur iPhone", cta="Coutume arrive bientôt sur l’App Store, pour iPhone : gratuite, sans compte, sans pub et sans abonnement.",
               related="Guides liés", questions="Questions",
               q='Consulte les <a href="{home}#faq-heading">questions fréquentes</a> ou l’<a href="{support}">assistance</a>.',
               why="Pourquoi ça vaut la peine", start="Pour commencer", hard="Quand ça devient difficile", track="Le suivre dans Coutume",
               more_ideas="D’autres idées d’habitudes", all_ideas="Les 40 idées d’habitudes"),
    "es": dict(skip="Saltar al contenido", support="Soporte", privacy="Privacidad", footer="Pie de página", crumbs="Ruta de navegación",
               made=f'Hecho con <svg class="heart" viewBox="0 0 24 22" role="img" aria-label="amor">{HEART}</svg> por <a href="https://wibeset.ca">Wibeset</a>. Desarrollado en Canadá.',
               aside="Coutume en iPhone", cta="Coutume llega pronto a la App Store, para iPhone: gratis, sin cuenta, sin anuncios y sin suscripción.",
               related="Guías relacionadas", questions="Preguntas",
               q='Consulta las <a href="{home}#faq-heading">preguntas frecuentes</a> o visita el <a href="{support}">soporte</a>.',
               why="Por qué vale la pena", start="Cómo empezar", hard="Cuando se pone difícil", track="Síguelo en Coutume",
               more_ideas="Más ideas de hábitos", all_ideas="Las 40 ideas de hábitos"),
}
GUIDES_LABEL = {"en": "Guides", "fr": "Guides", "es": "Guías"}

# ------------------------------------------------------------------ Spanish data
SCREENS_ES = {
    "today": "El día: seis hábitos, cada uno con su anillo",
    "detail": "10.000 pasos, completados por Salud, con su racha y su historial",
    "quit": "Un hábito por dejar: 12 días sin bebidas energéticas, 42 $ ahorrados",
    "progress": "Progreso: el nivel alcanzado y los logros ganados",
    "calendar": "El calendario: el mes, más vivo cuantos más hábitos se cumplieron",
}
HOME_ES = dict(
    title="Coutume — Mantén tus hábitos, un día a la vez",
    desc="Coutume es un registro de hábitos gratis para iPhone: buenos hábitos por crear, malos por dejar, un toque para anotar, y Salud completa tus pasos. Sin cuenta, sin anuncios.",
    label="Coutume — Registro de hábitos para iPhone",
    h1='Mantén tus hábitos, <em class="swash">un día a la vez</em>.',
    intro="Los buenos por crear, los malos por dejar: un toque para anotar, y Salud cuenta tus pasos. Gratis, sin cuenta, sin anuncios y sin suscripción.",
    store="Próximamente en la App Store", platform="iPhone, en inglés y francés",
    screens=[
        ("today", "Toca un anillo y el día queda anotado.", "Los hábitos de tu día, cada uno con su anillo. Un hábito que se cuenta, como 8 vasos de agua, suma uno con cada toque; mantén pulsado el anillo para introducir un número o deshacer."),
        ("detail", "Salud cuenta tus pasos por ti.", "Los pasos, los minutos de ejercicio, la atención plena y el agua se anotan solos. Cada hábito guarda su racha y todo su historial."),
        ("quit", "Los malos hábitos, contados en días sin.", "Un hábito por dejar se cumple por defecto: solo anotas el día que fallas. Coutume cuenta tus días sin, el dinero ahorrado y las ganas que resististe."),
        ("progress", "Niveles y logros por cada día cumplido.", "Once niveles, de Buena intención a Leyenda, dieciocho logros que celebrar, y una racha que perdona un día perdido por semana."),
        ("calendar", "Tu mes, día a día.", "Un calendario de cada día, más vivo cuantos más hábitos cumpliste, y widgets para tu pantalla de inicio."),
    ],
    features_h="Todas las funciones.", faq_h="Preguntas frecuentes.",
    more='¿Más preguntas? <a href="soporte/">Visita el soporte</a>.',
    like="También te puede gustar.", soon="(próximamente)",
    apps=[("https://reliure.me/", "Reliure", "Tu vida lectora, encuadernada", False),
          ("https://arpente.app/", "Arpente", "Cada paso cuenta una historia", True),
          ("https://porcom.app/", "Porcom", "Un pequeño diario de todo lo que ves", False),
          ("https://dernierverre.app/", "Dernier Verre", "Uno más, perfectamente mezclado", True)],
    makers="De los mismos creadores.",
    web=[("https://puuun.ch/", "Puuunch", "Control de tiempo y hojas de horas para equipos pequeños."),
         ("https://makearesu.me/", "Makearesu.me", "Crea un currículum en 5 minutos")],
    features=["Un toque: Toca el anillo y queda anotado", "Salud: Tus pasos y tu agua se anotan solos",
              "Por crear o por dejar: Anillos que llenar, días sin que contar", "Rachas indulgentes: Un día perdido por semana, perdonado",
              "Niveles: De Buena intención a Leyenda", "Logros: Dieciocho por ganar y celebrar", "Calendario: Tu mes, día a día",
              "Widgets: Tus anillos en la pantalla de inicio", "Sincronización con iCloud: Tus hábitos en tu iCloud privado",
              "Gratis: Sin cuenta, sin anuncios, sin suscripción"],
    faq=[("¿Coutume es gratis?", "Sí. Coutume es gratis, sin anuncios, sin suscripción y sin cuenta."),
         ("¿Necesito una cuenta?", "No. Coutume funciona sin cuenta ni registro. Tus hábitos se guardan en tu iPhone y se sincronizan con tu iCloud privado, al que no tenemos acceso."),
         ("¿Cómo anoto un hábito?", "Toca su anillo. Un hábito que se cuenta, como 8 vasos de agua, suma uno con cada toque; mantén pulsado el anillo para introducir un número o deshacer. Los pasos, los minutos de ejercicio, la atención plena y el agua pueden completarse solos desde Salud."),
         ("¿Cómo funcionan los hábitos por dejar?", "Cada día cuenta como cumplido salvo que anotes un desliz. Coutume cuenta tus días sin, el dinero ahorrado y las ganas que resististe. Un desliz reinicia la cuenta, nunca tu mes ni tu nivel."),
         ("¿Y si me salto un día?", "Tu racha perdona un día perdido por semana. Si fallas más, la racha vuelve a empezar, pero tu nivel y tus logros se quedan: cuentan cada día cumplido."),
         ("¿Qué lee Coutume de Salud?", "Solo lo que autorices: pasos, minutos de ejercicio, atención plena y agua. Coutume nunca escribe en Salud, y tus totales se quedan en tu iPhone y en tu iCloud."),
         ("¿Y si cambio de iPhone?", "Tus hábitos se sincronizan con tu iCloud y vuelven en tu nuevo iPhone, con todo su historial, sus niveles y sus logros."),
         ("¿Coutume está en español?", "Todavía no: la app está en inglés y en francés. Este sitio está en español para que puedas conocerla."),
         ("¿Coutume está disponible en Android?", "No. Coutume está disponible para iPhone, en inglés y en francés.")],
)


def esc(s):
    return escape(s, quote=True)


def fr_text(html):
    return BG.fr_text(html)


def depth_pre(path):
    """The relative prefix back to the site root from a page at <path> (e.g. 'fr/guides/x/')."""
    return "../" * path.count("/")


def head(lang, path, alts, title, desc, ld, extra=""):
    """alts: {lang: path} of this page in each language (paths from the root, '' for the home)."""
    pre = depth_pre(path)
    links = "\n".join(f'  <link rel="alternate" hreflang="{l}" href="{SITE}{p}">' for l, p in alts.items())
    others = "\n".join(f'  <meta property="og:locale:alternate" content="{LOCALE[l]}">' for l in alts if l != lang)
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title, quote=False)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="canonical" href="{SITE}{path}">
{links}
  <link rel="alternate" hreflang="x-default" href="{SITE}{alts["en"]}">
  <meta name="color-scheme" content="dark">
  <meta name="theme-color" content="#0a0a0b">
  <link rel="icon" href="{pre}favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="{pre}assets/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="{pre}assets/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{pre}assets/apple-touch-icon.png">
  <link rel="manifest" href="{pre}site.webmanifest">
  <link rel="preload" href="{pre}assets/fonts/headland-one-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{pre}assets/style.min.css">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Coutume">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{SITE}{path}">
  <meta property="og:locale" content="{LOCALE[lang]}">
{others}
  <meta property="og:image" content="{SITE}assets/{OG[lang]}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{esc(title)}">
  <meta name="twitter:card" content="summary_large_image">
  <script>document.documentElement.classList.add("js")</script>
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>{extra}
</head>
<body>
  <a class="skip" href="#main">{L10N[lang]["skip"]}</a>
'''


def footer(lang, path, alts, current=None, indent="  "):
    pre = depth_pre(path)
    t = L10N[lang]
    items = [(pre + SUPPORT[lang], t["support"], current == "support", ""),
             (pre + PRIVACY[lang], t["privacy"], current == "privacy", ""),
             (pre + PREFIX[lang] + "#guides" if current != "home" else "#guides", GUIDES_LABEL[lang], False, "")]
    for l in LANGS:
        if l != lang and l in alts:
            items.append((pre + alts[l], NAME[l], False, f' hreflang="{l}" lang="{l}"'))
    nav = "\n".join(f'{indent}    <a href="{h or "./"}"{" aria-current=\"page\"" if cur else ""}{a}>{label}</a>' for h, label, cur, a in items)
    return f'''{indent}<footer>
{indent}  <nav aria-label="{t["footer"]}">
{nav}
{indent}  </nav>
{indent}  <p>{t["made"]}</p>
{indent}</footer>
'''


def finish(lang, html):
    if lang == "fr":
        i = html.index("<body>")
        html = html[:i] + fr_text(html[i:])
    return html


def write(path, html):
    full = os.path.join(ROOT, path, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(html)


def alt_text(screen, lang):
    return SCREENS[screen][0] if lang == "en" else SCREENS[screen][1] if lang == "fr" else SCREENS_ES[screen]


def shot_fig(screen, lang, pre):
    return f'<figure class="device shot"><img src="{pre}assets/screens/fr/{screen}.webp" width="750" height="1630" alt="{esc(alt_text(screen, lang))}" loading="lazy" decoding="async"></figure>'


def preview(lang, pre, screens):
    imgs = "\n".join(
        f'      <img src="{pre}assets/screens/fr/{s}.webp" width="750" height="1630" alt="{esc(alt_text(s, lang))}" data-screen="{s}" {"fetchpriority=\"high\"" if i == 0 else "loading=\"lazy\""} decoding="async">'
        for i, s in enumerate(screens))
    return f'''  <!-- Captured from the simulator with sample habits (scripts/capture-screens.sh). main.js shows the screen of the section being read. -->
  <aside class="preview" aria-label="{L10N[lang]["aside"]}">
    <div class="device">
{imgs}
    </div>
  </aside>
'''


def breadcrumb(lang, path, trail):
    """trail: [(label, path or None)], after the home."""
    pre = depth_pre(path)
    items = [f'          <li><a href="{pre + PREFIX[lang] or "./"}"><img src="{pre}assets/icon.png" width="20" height="20" alt="">Coutume</a></li>']
    for label, p in trail:
        items.append(f'          <li><a href="{pre + p}">{label}</a></li>' if p else f'          <li aria-current="page">{label}</li>')
    return f'''      <nav class="breadcrumb" aria-label="{L10N[lang]["crumbs"]}">
        <ol>
{chr(10).join(items)}
        </ol>
      </nav>
'''


def crumbs_ld(lang, trail):
    items = [{"@type": "ListItem", "position": 1, "name": "Coutume", "item": SITE + PREFIX[lang]}]
    for i, (name, p) in enumerate(trail, 2):
        items.append({"@type": "ListItem", "position": i, "name": re.sub("<[^>]+>", "", name), "item": SITE + p})
    return {"@type": "BreadcrumbList", "itemListElement": items}


# ------------------------------------------------------------------ Home pages
def home_data(lang):
    """Everything the home page needs, in one shape for the three languages."""
    if lang == "es":
        d = dict(HOME_ES)
        d["screens"] = [(n, h, p, SCREENS_ES[n]) for n, h, p in HOME_ES["screens"]]
        return d
    t = BH.T[lang]
    src = open(os.path.join(ROOT, t["file"])).read()
    graph = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', src).group(1))["@graph"]
    app = next(g for g in graph if g["@type"] == "MobileApplication")
    faq = next(g for g in graph if g["@type"] == "FAQPage")["mainEntity"]
    title = re.search(r"<title>(.*?)</title>", src).group(1)
    desc = re.search(r'<meta name="description" content="([^"]*)"', src).group(1).replace("&#x27;", "’")
    return dict(title=title, desc=desc, label=t["label"], h1=t["h1"], intro=t["intro"], store=t["store"], platform=t["platform"],
                screens=t["screens"], features_h=t["features"], faq_h=t["faq"],
                more=t["more"].replace("../fr/assistance/", "assistance/"), like=t["like"], soon=t["soon"], apps=t["apps"],
                makers=t["makers"], web=t["web"], features=app["featureList"],
                faq=[(q["name"], q["acceptedAnswer"]["text"]) for q in faq])


def build_home(lang, data):
    d = data[lang]
    path = PREFIX[lang]
    pre = depth_pre(path)
    alts = {l: PREFIX[l] for l in LANGS}
    graph = [
        {"@type": "MobileApplication", "@id": SITE + "#app", "name": "Coutume", "description": d["desc"], "operatingSystem": "iOS",
         "applicationCategory": "HealthApplication", "inLanguage": lang, "url": SITE + path, "image": SITE + "assets/" + OG[lang],
         "publisher": {"@id": SITE + "#organization"}, "isAccessibleForFree": True,
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "CAD"}, "featureList": d["features"],
         "screenshot": [SITE + f"assets/screens/fr/{s}.webp" for s in ("progress", "quit", "today", "detail", "calendar")]},
        {"@type": "FAQPage", "inLanguage": lang, "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]},
        {"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "Coutume", "inLanguage": list(LANGS),
         "publisher": {"@id": SITE + "#organization"}},
        {"@type": "Organization", "@id": SITE + "#organization", "name": "Wibeset", "url": "https://wibeset.ca",
         "logo": SITE + "assets/icon.png", "email": "hello@wibeset.ca", "address": {"@type": "PostalAddress", "addressCountry": "CA"}},
    ]
    out = [head(lang, path, alts, d["title"], d["desc"], {"@context": "https://schema.org", "@graph": graph})]
    first = d["screens"][0]
    out.append(f'''
  <div class="split">
  <main id="main" class="content">
    <section class="screen hero" data-screen="{first[0]}">
      <img class="logo" src="{pre}assets/icon.png" width="56" height="56" alt="">
      <p class="label">{d["label"]}</p>
      <h1>{d["h1"]}</h1>
      <div>
        <p>{d["intro"]}</p>
        <div class="get"><span class="store">{BH.APPLE}{d["store"]}</span><span class="soon">{d["platform"]}</span></div>
      </div>
      {shot_fig(first[0], lang, pre)}
    </section>
''')
    for i, (name, h2, p, _alt) in enumerate(d["screens"]):
        fig = "" if i == 0 else f"\n      {shot_fig(name, lang, pre)}"
        out.append(f'''    <section class="screen" data-screen="{name}">
      <h2>{h2}</h2>
      <p>{p}</p>{fig}
    </section>
''')
    rows = "\n".join(
        f'        <li><h3 class="name"><svg class="icon" viewBox="0 0 24 24" style="color: {c}" aria-hidden="true">{svg}</svg>{f.split(": ", 1)[0]}</h3><p>{f.split(": ", 1)[1]}</p></li>'
        for (c, svg), f in zip(BH.ICONS, d["features"]))
    qa = "\n".join(f'''        <details>
          <summary><h3>{q}</h3></summary>
          <p>{a}</p>
        </details>''' for q, a in d["faq"])
    guides = "\n".join(f'        <li><span class="name"><a href="{guide_slug(p, lang)}/">{guide_t(p, lang)["crumb"]}</a></span><p>{guide_t(p, lang)["guide"]}</p></li>' for p in PAGES)
    apps = "\n".join(f'        <li><span class="name"><a href="{u}">{n}</a></span><p>{t}{" <span class=\"soon\">" + d["soon"] + "</span>" if s else ""}</p></li>' for u, n, t, s in d["apps"])
    web = "\n".join(f'        <li><span class="name"><a href="{u}">{n}</a></span><p>{t}</p></li>' for u, n, t in d["web"])
    out.append(f'''    <section>
      <h2>{d["features_h"]}</h2>
      <ul class="rows">
{rows}
      </ul>
    </section>
    <section aria-labelledby="faq-heading">
      <h2 id="faq-heading">{d["faq_h"]}</h2>
      <div class="faq-list">
{qa}
      </div>
      <p class="faq-more">{d["more"]}</p>
    </section>
    <section id="guides">
      <h2>{GUIDES_LABEL[lang]}.</h2>
      <ul class="rows">
{guides}
      </ul>
    </section>
    <!-- Friendly ads: the makers' other apps (Reliure, Arpente, Porcom, Dernier Verre), then Wibeset's web products. -->
    <section>
      <h2>{d["like"]}</h2>
      <ul class="rows">
{apps}
      </ul>
    </section>
    <section>
      <h2>{d["makers"]}</h2>
      <ul class="rows">
{web}
      </ul>
    </section>
{footer(lang, path, alts, current="home", indent="    ")}  </main>

{preview(lang, pre, [s[0] for s in d["screens"]])}  </div>

  <script src="{pre}assets/main.js" defer></script>
</body>
</html>
''')
    write(path, finish(lang, "".join(out)))


# ------------------------------------------------------------------ Guides
GUIDES_ES = {}
SLUG_ES = {}


def guide_slug(page, lang):
    return page["en_slug"] if lang == "en" else page["fr_slug"] if lang == "fr" else SLUG_ES[page["key"]]


def guide_t(page, lang):
    return page[lang] if lang != "es" else GUIDES_ES[page["key"]]


def guide_path(page, lang):
    return PREFIX[lang] + guide_slug(page, lang) + "/"


def ending(lang, path, related):
    t = L10N[lang]
    pre = depth_pre(path)
    rows = "\n".join(f'          <li><span class="name"><a href="{pre + p}">{label}</a></span><p>{text}</p></li>' for p, label, text in related)
    q = t["q"].format(home=pre + PREFIX[lang], support=pre + SUPPORT[lang])
    return f'''      <section>
        <p><strong>{t["cta"]}</strong></p>
      </section>
      <section>
        <h2>{t["related"]}</h2>
        <ul class="rows">
{rows}
        </ul>
      </section>
      <section>
        <h2>{t["questions"]}</h2>
        <p>{q}</p>
      </section>
'''


def build_guide(page, lang, hub_bodies):
    t = guide_t(page, lang)
    path = guide_path(page, lang)
    pre = depth_pre(path)
    alts = {l: guide_path(page, l) for l in LANGS}
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": SITE + path, "url": SITE + path, "name": t["title"], "description": t["desc"], "inLanguage": lang,
         "dateModified": DATE, "isPartOf": {"@id": SITE + "#website"}, "about": {"@id": SITE + "#app"}},
        crumbs_ld(lang, [(t["crumb"], path)])]}
    related = [(guide_path(BG.BY_KEY[k], lang), guide_t(BG.BY_KEY[k], lang)["crumb"], guide_t(BG.BY_KEY[k], lang)["guide"]) for k in RELATED[page["key"]]]
    intro = f'''        <h1>{t["h1"]}</h1>
        <p class="updated">{UPDATED[lang]}</p>

        <p class="lede">{t["lede"]}</p>
'''
    out = [head(lang, path, alts, t["title"], t["desc"], ld)]
    bc = breadcrumb(lang, path, [(t["crumb"], None)])
    if page["layout"] == "plain":
        body = hub_bodies.get(lang) if page["key"] == "ideas" else t["body"]
        out.append(f'''  <main id="main">
    <article class="legal">
{bc}{intro.replace("        ", "      ")}{body}{ending(lang, path, related)}    </article>
  </main>

{footer(lang, path, alts)}  <script src="{pre}assets/main.js" defer></script>
</body>
</html>
''')
    else:
        secs, shown, order = [], set(), []
        first = t["sections"][0][0]
        secs.append(f'''      <section class="intro" data-screen="{first}">
{intro}        {shot_fig(first, lang, pre)}
      </section>
''')
        shown.add(first)
        for screen, h2, html in t["sections"]:
            fig = "" if screen in shown else f"\n        {shot_fig(screen, lang, pre)}"
            shown.add(screen)
            secs.append(f'''      <section data-screen="{screen}">
        <h2>{h2}</h2>
        {html}{fig}
      </section>
''')
        for s, _, _ in t["sections"]:
            if s not in order:
                order.append(s)
        extra = f'      {t["extra"]}\n' if t.get("extra") else ""
        out.append(f'''  <div class="split">
  <main id="main" class="content">
    <article class="legal">
{bc}{"".join(secs)}{extra}{ending(lang, path, related)}    </article>
{footer(lang, path, alts, indent="    ")}  </main>

{preview(lang, pre, order)}  </div>
  <script src="{pre}assets/main.js" defer></script>
</body>
</html>
''')
    write(path, finish(lang, "".join(out)))


# ------------------------------------------------------------------ Habit ideas: the 40 how-to articles
# The hub's 40 items, in order; energy and vaping already have their own guide.
IDEAS_ORDER = ["water", "steps", "exercise", "stretch", "veg", "stairs", "cook", "vitamins",
               "bedtime", "noscreens", "prepare", "light", "journal",
               "read", "meditate", "language", "instrument", "gratitude", "keepintouch", "makebed", "tidy",
               "energy", "vaping", "sugarydrinks", "snacking", "coffee", "socialmorning", "phonetable", "doomscroll", "takeout", "impulse", "nails", "snooze",
               "expenses", "lunch", "owncoffee", "wait24", "save", "checkaccounts", "subscription"]
EXISTING = {"energy": "energy", "vaping": "vaping"}


def load_articles():
    arts = {}
    for f in ("example.py", "health.py", "mind.py", "quit.py", "sleepmoney.py"):
        p = os.path.join(HERE, "articles", f)
        if not os.path.exists(p):
            continue
        ns = {}
        exec(open(p).read(), ns)
        for a in ns["ARTICLES"]:
            arts[a["key"]] = a
    return arts


def article_path(a, lang):
    hub = guide_path(BG.BY_KEY["ideas"], lang)
    return hub + a[lang]["slug"] + "/"


def build_article(a, lang, arts):
    t = a[lang]
    path = article_path(a, lang)
    pre = depth_pre(path)
    alts = {l: article_path(a, l) for l in LANGS}
    hub = BG.BY_KEY["ideas"]
    hub_path, hub_t = guide_path(hub, lang), guide_t(hub, lang)
    trail = [(hub_t["crumb"], hub_path), (t["crumb"], path)]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "@id": SITE + path, "url": SITE + path, "headline": t["h1"], "description": t["desc"], "inLanguage": lang,
         "dateModified": DATE, "datePublished": DATE, "author": {"@id": SITE + "#organization"}, "publisher": {"@id": SITE + "#organization"},
         "isPartOf": {"@id": SITE + "#website"}, "about": {"@id": SITE + "#app"}, "image": SITE + "assets/" + OG[lang]},
        crumbs_ld(lang, trail)]}
    L = L10N[lang]
    steps = "\n".join(f"        <li>{s}</li>" for s in t["steps"])
    hard = "\n".join(f"        <li>{s}</li>" for s in t["hard"])
    note = f'\n      <p class="note">{t["note"]}</p>' if t.get("note") else ""
    # Related: the other articles of the same theme, around this one, then the hub.
    same = [k for k in IDEAS_ORDER if k in arts and arts[k]["theme"] == a["theme"] and k != a["key"]]
    i = IDEAS_ORDER.index(a["key"])
    same.sort(key=lambda k: (IDEAS_ORDER.index(k) < i, IDEAS_ORDER.index(k)))
    related = [(article_path(arts[k], lang), arts[k][lang]["crumb"], arts[k][lang]["h1"]) for k in same[:3]]
    related.append((hub_path, L["all_ideas"], hub_t["guide"]))
    body = f'''  <main id="main">
    <article class="legal">
{breadcrumb(lang, path, [(hub_t["crumb"], hub_path), (t["crumb"], None)])}      <h1>{t["h1"]}</h1>
      <p class="updated">{UPDATED[lang]}</p>

      <p class="lede">{t["lede"]}</p>

      <h2>{L["why"]}</h2>
      <p>{t["why"]}</p>

      <h2>{L["start"]}</h2>
      <ol>
{steps}
      </ol>

      <h2>{L["hard"]}</h2>
      <ul>
{hard}
      </ul>

      <h2>{L["track"]}</h2>
      <p>{t["track"]}</p>{note}
{ending(lang, path, related).replace(L["related"], L["more_ideas"], 1)}    </article>
  </main>

{footer(lang, path, alts)}  <script src="{pre}assets/main.js" defer></script>
</body>
</html>
'''
    write(path, finish(lang, head(lang, path, alts, t["title"], t["desc"], ld) + body))


def hub_body(lang, arts):
    """The habit-ideas page, with each of its 40 ideas linked to its article (or to the existing guide)."""
    body = guide_t(BG.BY_KEY["ideas"], lang)["body"]
    hub_path = guide_path(BG.BY_KEY["ideas"], lang)
    items = list(re.finditer(r"<li><strong>(.*?)</strong>", body))
    assert len(items) >= 40, (lang, len(items))
    out, last = [], 0
    for m, key in zip(items[:40], IDEAS_ORDER):
        if key in EXISTING:
            href = "../" + guide_slug(BG.BY_KEY[EXISTING[key]], lang) + "/"
        elif key in arts:
            href = arts[key][lang]["slug"] + "/"
        else:
            href = None
        text = re.sub(r"</?a[^>]*>", "", m.group(1))
        inner = f'<a href="{href}">{text}</a>' if href else text
        out.append(body[last:m.start()] + f"<li><strong>{inner}</strong>")
        last = m.end()
    out.append(body[last:])
    return "".join(out)


# ------------------------------------------------------------------ Hand-written pages: languages and alternates
def patch_static():
    pages = {"support": {"en": "support/", "fr": "fr/assistance/", "es": "es/soporte/"},
             "privacy": {"en": "privacy/", "fr": "fr/confidentialite/", "es": "es/privacidad/"}}
    for kind, alts in pages.items():
        for lang, path in alts.items():
            f = os.path.join(ROOT, path, "index.html")
            s = open(f).read()
            s = re.sub(r'  <link rel="alternate" hreflang="(?:en|fr|es|x-default)"[^\n]*\n', "", s)
            links = "".join(f'  <link rel="alternate" hreflang="{l}" href="{SITE}{alts[l]}">\n' for l in LANGS)
            links += f'  <link rel="alternate" hreflang="x-default" href="{SITE}{alts["en"]}">\n'
            s = re.sub(r'(  <link rel="canonical"[^\n]*\n)', lambda m: m.group(1) + links, s, count=1)
            s = re.sub(r'  <meta property="og:locale:alternate"[^\n]*\n', "", s)
            s = re.sub(r'(  <meta property="og:locale"[^\n]*\n)', lambda m: m.group(1) + "".join(
                f'  <meta property="og:locale:alternate" content="{LOCALE[l]}">\n' for l in LANGS if l != lang), s, count=1)
            # The footer: rebuilt like every other page.
            s = re.sub(r"  <footer>.*?</footer>\n", footer(lang, path, alts, current=kind), s, count=1, flags=re.S)
            if lang == "fr":
                i = s.index("<footer>")
                s = s[:i] + fr_text(s[i:])
            open(f, "w").write(s)
    f = os.path.join(ROOT, "404.html")
    s = open(f).read()
    if 'lang="es"' not in s:
        s = s.replace('<br><span lang="fr">Un jour manqué.</span>', '<br><span lang="fr">Un jour manqué.</span><br><span lang="es">Un día perdido.</span>')
        s = s.replace('<span lang="fr">Cette page n’existe pas, mais ta séquence en pardonne un.</span>',
                      '<span lang="fr">Cette page n’existe pas, mais ta séquence en pardonne un.</span> <span lang="es">Esta página no existe, pero tu racha perdona uno.</span>')
        s = s.replace('<a href="/fr/" lang="fr">Retour à Coutume</a>', '<a href="/fr/" lang="fr">Retour à Coutume</a> · <a href="/es/" lang="es">Volver a Coutume</a>')
        open(f, "w").write(s)


# ------------------------------------------------------------------ sitemap.xml and llms.txt
def sitemap(groups):
    urls = []
    for alts in groups:
        for l in LANGS:
            links = "\n".join(f'    <xhtml:link rel="alternate" hreflang="{x}" href="{SITE}{alts[x]}"/>' for x in LANGS)
            urls.append(f'''  <url>
    <loc>{SITE}{alts[l]}</loc>
    <lastmod>{DATE}</lastmod>
{links}
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{alts["en"]}"/>
  </url>''')
    open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
    return len(urls)


def llms(arts):
    s = open(os.path.join(ROOT, "llms.txt")).read()
    s = s[: s.index("## Pages")]
    s = s.replace("Coutume is a free habit tracker for iPhone, in French and English.",
                  "Coutume is a free habit tracker for iPhone, in French and English (this site is also in Spanish).")
    lines = ["## Pages", "",
             f"- [Home]({SITE}): features and frequently asked questions",
             f"- [Support]({SITE}support/): contact, Health access, steps that don't match, undoing a slip, widgets, archiving",
             f"- [Privacy policy]({SITE}privacy/): what information the app handles"]
    for p in PAGES:
        lines.append(f'- [{p["en"]["crumb"]}]({SITE}{guide_path(p, "en")}): {p["en"]["guide"][0].lower() + p["en"]["guide"][1:]}')
    lines += ["", "## How-to articles", ""]
    for k in IDEAS_ORDER:
        if k in arts:
            lines.append(f'- [{arts[k]["en"]["h1"]}]({SITE}{article_path(arts[k], "en")})')
    for lang, title, home, sup, priv in (("fr", "Français", "Accueil", "Assistance", "Politique de confidentialité"),
                                         ("es", "Español", "Inicio", "Soporte", "Política de privacidad")):
        lines += ["", f"## {title}", "", f"- [{home}]({SITE}{PREFIX[lang]})", f"- [{sup}]({SITE}{SUPPORT[lang]})", f"- [{priv}]({SITE}{PRIVACY[lang]})"]
        lines += [f'- [{guide_t(p, lang)["crumb"]}]({SITE}{guide_path(p, lang)})' for p in PAGES]
    open(os.path.join(ROOT, "llms.txt"), "w").write(s + "\n".join(lines) + "\n")


def main():
    ns = {}
    exec(open(os.path.join(HERE, "guides_es.py")).read(), ns)
    GUIDES_ES.update(ns["ES"])
    SLUG_ES.update({k: v["slug"] for k, v in GUIDES_ES.items()})
    arts = load_articles()
    data = {l: home_data(l) for l in LANGS}  # read before the en/fr pages are rewritten
    for l in LANGS:
        build_home(l, data)
    hubs = {l: hub_body(l, arts) for l in LANGS}
    for p in PAGES:
        for l in LANGS:
            build_guide(p, l, hubs)
    n = 0
    for k in IDEAS_ORDER:
        if k in arts:
            for l in LANGS:
                build_article(arts[k], l, arts)
                n += 1
    patch_static()
    groups = [{l: PREFIX[l] for l in LANGS}, SUPPORT, PRIVACY]
    groups += [{l: guide_path(p, l) for l in LANGS} for p in PAGES]
    groups += [{l: article_path(arts[k], l) for l in LANGS} for k in IDEAS_ORDER if k in arts]
    urls = sitemap(groups)
    llms(arts)
    print(f"{len(arts)} articles ({n} pages), {len(PAGES) * 3} guide pages, sitemap: {urls} URLs")


main()
