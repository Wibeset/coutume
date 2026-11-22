"""Builds coutume.app's guides (EN + FR) in Reliure's layout, the guides list on both home pages, the footers'
Guides link, sitemap.xml and llms.txt's page list."""
import json, re, sys
from html import escape

sys.path.insert(0, sys.argv[2] if len(sys.argv) > 2 else __import__("os").path.dirname(__file__))
from content import PAGES, RELATED, SCREENS

ROOT = sys.argv[1] if len(sys.argv) > 1 else ""
SITE = "https://coutume.app/"
DATE = "2026-11-21"
UPDATED = {"en": "Last updated: November 21, 2026", "fr": "Dernière mise à jour&nbsp;: 21&nbsp;novembre&nbsp;2026"}
BY_KEY = {p["key"]: p for p in PAGES}
HEART = '<path d="M12 21.6 10.3 20C4.2 14.5 0 10.8 0 6.3 0 2.7 2.8 0 6.3 0c2 0 4 .9 5.7 2.5C13.7.9 15.7 0 17.7 0 21.2 0 24 2.7 24 6.3c0 4.5-4.2 8.2-10.3 13.7Z"/>'


def fr_text(html):
    """French typography in text only (never inside tags): no-break spaces before ? ! : ; » and after «."""
    parts = re.split(r"(<[^>]+>)", html)
    for i in range(0, len(parts), 2):
        t = parts[i]
        t = re.sub(r" ([?!:;»])", r"&nbsp;\1", t)
        t = t.replace("« ", "«&nbsp;")
        parts[i] = t
    return "".join(parts)


def url(page, lang):
    return SITE + (page["en_slug"] if lang == "en" else "fr/" + page["fr_slug"]) + "/"


def head(page, lang, t):
    pre = "../" if lang == "en" else "../../"
    en, fr = url(page, "en"), url(page, "fr")
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": url(page, lang), "url": url(page, lang), "name": t["title"], "description": t["desc"],
         "inLanguage": lang, "dateModified": DATE, "isPartOf": {"@id": SITE + "#website"}, "about": {"@id": SITE + "#app"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Coutume", "item": SITE if lang == "en" else SITE + "fr/"},
            {"@type": "ListItem", "position": 2, "name": t["crumb"], "item": url(page, lang)}]}]}
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(t["title"], quote=False)}</title>
  <meta name="description" content="{escape(t["desc"])}">
  <link rel="canonical" href="{url(page, lang)}">
  <link rel="alternate" hreflang="en" href="{en}">
  <link rel="alternate" hreflang="fr" href="{fr}">
  <link rel="alternate" hreflang="x-default" href="{en}">
  <meta name="color-scheme" content="dark">
  <meta name="theme-color" content="#0a0a0b">
  <link rel="icon" href="{pre}favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="{pre}assets/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="{pre}assets/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{pre}assets/apple-touch-icon.png">
  <link rel="manifest" href="{pre}site.webmanifest">
  <link rel="preload" href="{pre}assets/fonts/headland-one-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{pre}assets/style.min.css">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Coutume">
  <meta property="og:title" content="{escape(t["title"])}">
  <meta property="og:description" content="{escape(t["desc"])}">
  <meta property="og:url" content="{url(page, lang)}">
  <meta property="og:locale" content="{"en_CA" if lang == "en" else "fr_CA"}">
  <meta property="og:locale:alternate" content="{"fr_CA" if lang == "en" else "en_CA"}">
  <meta property="og:image" content="{SITE}assets/og-{lang}.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Coutume">
  <meta name="twitter:card" content="summary_large_image">
  <script>document.documentElement.classList.add("js")</script>
</head>
<body>
  <a class="skip" href="#main">{"Skip to content" if lang == "en" else "Aller au contenu"}</a>
'''


def shot(screen, lang, pre, cls="device shot"):
    alt = SCREENS[screen][0 if lang == "en" else 1]
    return f'<figure class="{cls}"><img src="{pre}assets/screens/fr/{screen}.webp" width="750" height="1630" alt="{escape(alt)}" loading="lazy" decoding="async"></figure>'


def ending(page, lang):
    """The call to action, the related guides and the questions, shared by both layouts."""
    rel = []
    for key in RELATED[page["key"]]:
        other = BY_KEY[key]
        href = f'../{other["en_slug"]}/' if lang == "en" else f'../{other["fr_slug"]}/'
        o = other[lang]
        rel.append(f'          <li><span class="name"><a href="{href}">{o["crumb"]}</a></span><p>{o["guide"]}</p></li>')
    if lang == "en":
        cta = "Coutume is coming soon to the App Store, for iPhone: free, with no account, no ads and no subscription."
        q = 'See the <a href="../#faq-heading">frequently asked questions</a> or visit <a href="../support/">Support</a>.'
        h_rel, h_q = "Related guides", "Questions"
    else:
        cta = "Coutume arrive bientôt sur l’App Store, pour iPhone : gratuite, sans compte, sans pub et sans abonnement."
        q = 'Consulte les <a href="../#faq-heading">questions fréquentes</a> ou l’<a href="../assistance/">assistance</a>.'
        h_rel, h_q = "Guides liés", "Questions"
    return f'''      <section>
        <p><strong>{cta}</strong></p>
      </section>
      <section>
        <h2>{h_rel}</h2>
        <ul class="rows">
{chr(10).join(rel)}
        </ul>
      </section>
      <section>
        <h2>{h_q}</h2>
        <p>{q}</p>
      </section>
'''


def footer(page, lang, current=True):
    if lang == "en":
        other = f'../fr/{page["fr_slug"]}/'
        links = [("../support/", "Support", ""), ("../privacy/", "Privacy", ""), ("../#guides", "Guides", ""), (other, "Français", ' hreflang="fr" lang="fr"')]
        made = f'Made with <svg class="heart" viewBox="0 0 24 22" role="img" aria-label="love">{HEART}</svg> by <a href="https://wibeset.ca">Wibeset</a>. Developed in Canada.'
        label = "Footer"
    else:
        other = f'../../{page["en_slug"]}/'
        links = [("../assistance/", "Assistance", ""), ("../confidentialite/", "Confidentialité", ""), ("../#guides", "Guides", ""), (other, "English", ' hreflang="en" lang="en"')]
        made = f'Fait avec <svg class="heart" viewBox="0 0 24 22" role="img" aria-label="amour">{HEART}</svg> par <a href="https://wibeset.ca">Wibeset</a>. Développé au Canada.'
        label = "Pied de page"
    nav = "\n".join(f'      <a href="{h}"{a}>{l}</a>' for h, l, a in links)
    return f'''  <footer>
    <nav aria-label="{label}">
{nav}
    </nav>
    <p>{made}</p>
  </footer>
'''


def breadcrumb(lang, crumb, pre):
    home = "../" if lang == "en" else "../"
    label = "Breadcrumb" if lang == "en" else "Fil d’Ariane"
    return f'''      <nav class="breadcrumb" aria-label="{label}">
        <ol>
          <li><a href="{home}"><img src="{pre}assets/icon.png" width="20" height="20" alt="">Coutume</a></li>
          <li aria-current="page">{crumb}</li>
        </ol>
      </nav>
'''


def build(page, lang):
    t = page[lang]
    pre = "../" if lang == "en" else "../../"
    out = [head(page, lang, t)]
    intro = f'''        <h1>{t["h1"]}</h1>
        <p class="updated">{UPDATED[lang]}</p>

        <p class="lede">{t["lede"]}</p>
'''
    if page["layout"] == "plain":
        body = f'''  <main id="main">
    <article class="legal">
{breadcrumb(lang, t["crumb"], pre)}{intro.replace("        ", "      ")}{t["body"]}{ending(page, lang)}    </article>
  </main>

{footer(page, lang)}  <script src="{pre}assets/main.js" defer></script>
</body>
</html>
'''
        out.append(body)
    else:
        first = t["sections"][0][0]
        secs = [f'''      <section class="intro" data-screen="{first}">
{intro}        {shot(first, lang, pre)}
      </section>
''']
        shown = {first}
        for screen, h2, html in t["sections"]:
            fig = "" if screen in shown else f"\n        {shot(screen, lang, pre)}"
            shown.add(screen)
            secs.append(f'''      <section data-screen="{screen}">
        <h2>{h2}</h2>
        {html}{fig}
      </section>
''')
        extra = f'      {t["extra"]}\n' if t.get("extra") else ""
        order = []
        for screen, _, _ in t["sections"]:
            if screen not in order:
                order.append(screen)
        imgs = "\n".join(
            f'      <img src="{pre}assets/screens/fr/{s}.webp" width="750" height="1630" alt="{escape(SCREENS[s][0 if lang == "en" else 1])}" data-screen="{s}" {"fetchpriority=\"high\"" if i == 0 else "loading=\"lazy\""} decoding="async">'
            for i, s in enumerate(order))
        foot = footer(page, lang).replace("\n  ", "\n    ").replace("  <footer>", "    <footer>", 1)
        out.append(f'''  <div class="split">
  <main id="main" class="content">
    <article class="legal">
{breadcrumb(lang, t["crumb"], pre)}{"".join(secs)}{extra}{ending(page, lang)}    </article>
{foot}  </main>

  <!-- Captured from the simulator with sample habits (scripts/capture-screens.sh). main.js shows the screen of the section being read. -->
  <aside class="preview" aria-label="{"Coutume on iPhone" if lang == "en" else "Coutume sur iPhone"}">
    <div class="device">
{imgs}
    </div>
  </aside>
  </div>
  <script src="{pre}assets/main.js" defer></script>
</body>
</html>
''')
    html = "".join(out)
    if lang == "fr":
        # Only the body: the head's attributes and JSON-LD keep plain text.
        i = html.index("<body>")
        html = html[:i] + fr_text(html[i:])
    path = f'{ROOT}/{page["en_slug"] if lang == "en" else "fr/" + page["fr_slug"]}/index.html'
    import os
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(html)
    return path


if __name__ == "__main__":
  pass
  for page in PAGES:
      for lang in ("en", "fr"):
          print(build(page, lang))


  # The guides list on both home pages, before "You may also like".
  for lang, path in (("en", "index.html"), ("fr", "fr/index.html")):
      s = open(f"{ROOT}/{path}").read()
      s = re.sub(r'    <section id="guides">.*?</section>\n', "", s, flags=re.S)
      rows = "\n".join(
          f'        <li><span class="name"><a href="{p["en_slug"] if lang == "en" else p["fr_slug"]}/">{p[lang]["crumb"]}</a></span><p>{p[lang]["guide"]}</p></li>'
          for p in PAGES)
      sec = f'''    <section id="guides">
        <h2>{"Guides." if lang == "en" else "Guides."}</h2>
        <ul class="rows">
  {rows}
        </ul>
      </section>
  '''
      if lang == "fr":
          sec = fr_text(sec)
      marker = "    <!-- Friendly ads"
      assert marker in s
      s = s.replace(marker, sec + marker, 1)
      open(f"{ROOT}/{path}", "w").write(s)

  # The Guides link in the footers of the home, support and privacy pages.
  for path, href in (("index.html", "#guides"), ("support/index.html", "../#guides"), ("privacy/index.html", "../#guides"),
                     ("fr/index.html", "#guides"), ("fr/assistance/index.html", "../#guides"), ("fr/confidentialite/index.html", "../#guides")):
      s = open(f"{ROOT}/{path}").read()
      if 'Guides</a>' not in s:
          s, n = re.subn(r'(\n(\s*)<a href="[^"]*(?:privacy|confidentialite)/"[^>]*>[^<]*</a>)', lambda m: f'{m.group(1)}\n{m.group(2)}<a href="{href}">Guides</a>', s, count=1)
          assert n == 1, path
      open(f"{ROOT}/{path}", "w").write(s)

  # sitemap.xml: every page with its two languages.
  pairs = [("", "fr/"), ("support/", "fr/assistance/"), ("privacy/", "fr/confidentialite/")] + [(p["en_slug"] + "/", "fr/" + p["fr_slug"] + "/") for p in PAGES]
  urls = []
  for en, fr in pairs:
      for loc in (en, fr):
          urls.append(f'''  <url>
      <loc>{SITE}{loc}</loc>
      <lastmod>{DATE}</lastmod>
      <xhtml:link rel="alternate" hreflang="en" href="{SITE}{en}"/>
      <xhtml:link rel="alternate" hreflang="fr" href="{SITE}{fr}"/>
      <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{en}"/>
    </url>''')
  open(f"{ROOT}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")

  # llms.txt: the guides under Pages and Français.
  s = open(f"{ROOT}/llms.txt").read()
  s = re.sub(r"\n- \[[^\]]+\]\(https://coutume\.app/(?:fr/)?[a-z-]+/\): guide[^\n]*", "", s)
  s = re.sub(r"\n- \[[^\]]+\]\(https://coutume\.app/fr/(?!assistance|confidentialite)[a-z-]+/\)(?=\n|$)", "", s)
  en_lines = "".join(f'\n- [{p["en"]["crumb"]}]({SITE}{p["en_slug"]}/): guide, {p["en"]["guide"][0].lower() + p["en"]["guide"][1:]}' for p in PAGES)
  fr_lines = "".join(f'\n- [{p["fr"]["crumb"]}]({SITE}fr/{p["fr_slug"]}/)' for p in PAGES)
  s = s.replace("\n\n## Français", en_lines + "\n\n## Français", 1)
  s = s.rstrip("\n") + fr_lines + "\n"
  open(f"{ROOT}/llms.txt", "w").write(s)
  print("home, footers, sitemap.xml and llms.txt updated")

