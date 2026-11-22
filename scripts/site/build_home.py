"""Rebuilds coutume's two home pages in Reliure's layout. Keeps each page's <head> (with fonts and colors swapped)
and its JSON-LD, from which the FAQ and feature list are read."""
import json, re, sys
from html import escape

ROOT = sys.argv[1] if len(sys.argv) > 1 else ""

APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.4 12.6c0-2.6 2.1-3.8 2.2-3.9-1.2-1.8-3.1-2-3.7-2-1.6-.2-3.1.9-3.9.9-.8 0-2-.9-3.4-.9-1.7 0-3.3 1-4.2 2.6-1.8 3.1-.5 7.7 1.3 10.2.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8 1.6 0 2 .8 3.4.8 1.4 0 2.3-1.3 3.1-2.5 1-1.4 1.4-2.8 1.4-2.9-.1 0-2.7-1-2.7-4.1ZM13.9 4.9c.7-.9 1.2-2.1 1.1-3.3-1 0-2.3.7-3 1.6-.7.8-1.3 2-1.1 3.2 1.1.1 2.3-.6 3-1.5Z"/></svg>'
HEART = '<path d="M12 21.6 10.3 20C4.2 14.5 0 10.8 0 6.3 0 2.7 2.8 0 6.3 0c2 0 4 .9 5.7 2.5C13.7.9 15.7 0 17.7 0 21.2 0 24 2.7 24 6.3c0 4.5-4.2 8.2-10.3 13.7Z"/>'

# The feature icons, in order, each in its own color.
ICONS = [
    ("#f29a5c", '<circle cx="12" cy="12" r="9" fill="currentColor" fill-opacity=".2"/><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2" pathLength="100" stroke-dasharray="70 100" stroke-linecap="round" transform="rotate(-90 12 12)"/><circle cx="12" cy="12" r="3" fill="currentColor"/>'),
    ("#ff6f91", '<path d="M12 20.5 10.7 19.3C6.2 15.2 3 12.4 3 8.9 3 6.1 5.2 4 7.9 4c1.5 0 3 .7 4.1 1.9C13.1 4.7 14.6 4 16.1 4 18.8 4 21 6.1 21 8.9c0 3.5-3.2 6.3-7.7 10.4Z" fill="currentColor" fill-opacity=".2"/><path d="M5 11.5h3.5l1.5-3 3 6 1.5-3H19" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'),
    ("#8fb3db", '<circle cx="12" cy="12" r="9" fill="currentColor" fill-opacity=".2"/><path d="M12 3a9 9 0 0 1 0 18Z" fill="currentColor"/>'),
    ("#ffb347", '<path d="M12 21c-4 0-7-2.7-7-6.5 0-3.6 3-5.5 4-9 2.5 1.5 3 3.5 3 5 1-1 1.5-2 1.5-3.5 3 2 5.5 4.5 5.5 7.5 0 3.8-3 6.5-7 6.5Z" fill="currentColor" fill-opacity=".2" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>'),
    ("#9ad14b", '<rect x="3" y="3" width="18" height="18" rx="4" fill="currentColor" fill-opacity=".2"/><path d="M7.5 17v-3M12 17v-6M16.5 17V7" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>'),
    ("#ffd23f", '<circle cx="12" cy="14.5" r="6" fill="currentColor" fill-opacity=".2" stroke="currentColor" stroke-width="1.6"/><path d="M8.5 3h7l-2.2 6h-2.6Z" fill="currentColor"/><path d="m12 12 .9 1.8 2 .3-1.4 1.4.3 2-1.8-1-1.8 1 .3-2-1.4-1.4 2-.3Z" fill="currentColor"/>'),
    ("#5ad4e6", '<rect x="3" y="4.5" width="18" height="16" rx="3" fill="currentColor" fill-opacity=".2"/><path d="M3 9.5h18M8 2.5v4M16 2.5v4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="8" cy="14" r="1.4" fill="currentColor"/><circle cx="12" cy="14" r="1.4" fill="currentColor"/><circle cx="16" cy="14" r="1.4" fill="currentColor"/>'),
    ("#b58cff", '<rect x="3" y="3" width="8" height="8" rx="2.4" fill="currentColor"/><rect x="13" y="3" width="8" height="8" rx="2.4" fill="currentColor" fill-opacity=".2"/><rect x="3" y="13" width="8" height="8" rx="2.4" fill="currentColor" fill-opacity=".2"/><rect x="13" y="13" width="8" height="8" rx="2.4" fill="currentColor" fill-opacity=".2"/>'),
    ("#a7b8ff", '<path d="M7 19h10.5a4.5 4.5 0 0 0 .6-8.96A6.5 6.5 0 0 0 5.6 8.6 5.2 5.2 0 0 0 7 19Z" fill="currentColor" fill-opacity=".2" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>'),
    ("#34c77b", '<circle cx="12" cy="12" r="9" fill="currentColor" fill-opacity=".22"/><path d="m7.8 12.3 2.8 2.8 5.6-6.1" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'),
]

T = {
    "en": dict(
        file="index.html", pre="", skip="Skip to content",
        label="Coutume — Habit tracker for iPhone",
        h1='Keep your habits, <em class="swash">one day at a time</em>.',
        intro="Good habits to build, bad ones to quit: one tap to log, and Apple Health fills in your steps. Free, with no account, no ads and no subscription.",
        store="Coming soon to the App Store", platform="iPhone, in English and French",
        screens=[
            ("today", "Tap a ring, the day is logged.", "Your day’s habits, each with its ring. A habit you count, like 8 glasses of water, adds one with each tap; touch and hold to enter a number or undo.", "The day: six habits, each with its ring"),
            ("detail", "Apple Health fills in your steps.", "Steps, exercise minutes, mindful minutes and water log themselves. Each habit keeps its streak and its whole history.", "10,000 steps, filled in by Apple Health, with its streak and history"),
            ("quit", "Bad habits to quit, counted in days without.", "A habit to quit is kept by default: you only log the day you slip. Coutume counts your days without, the money saved and the urges you resisted.", "A habit to quit: 12 days without energy drinks, $42 saved"),
            ("progress", "Levels and milestones for every day kept.", "Eleven levels, from Good intention to Legend, eighteen milestones to celebrate, and a streak that forgives one missed day a week.", "Progress: the level reached and the milestones earned"),
            ("calendar", "Your month, day by day.", "A calendar of every day, brighter as more habits were kept, and widgets for your Home Screen.", "The calendar: the month, brighter as more habits were kept"),
        ],
        features="All the features.", faq="Frequently asked questions.",
        more='More questions? <a href="support/">Visit Support</a>.',
        like="You may also like.", soon="(coming soon)",
        apps=[("https://reliure.me/", "Reliure", "Your reading life, bound together", False),
              ("https://arpente.app/", "Arpente", "Every step tells a story", True),
              ("https://porcom.app/", "Porcom", "A tiny journal for everything you watch", False),
              ("https://dernierverre.app/", "Dernier Verre", "One more, perfectly mixed", True)],
        makers="From the same makers.",
        web=[("https://puuun.ch/", "Puuunch", "Time tracking and timesheets for small teams."),
             ("https://makearesu.me/", "Makearesu.me", "Make a resume in 5 minutes")],
        nav_label="Footer",
        nav=[("support/", "Support", ""), ("privacy/", "Privacy", ""), ("fr/", "Français", ' hreflang="fr" lang="fr"')],
        made='Made with <svg class="heart" viewBox="0 0 24 22" role="img" aria-label="love">' + HEART + '</svg> by <a href="https://wibeset.ca">Wibeset</a>. Developed in Canada.',
        aside="Coutume on iPhone",
    ),
    "fr": dict(
        file="fr/index.html", pre="../", skip="Aller au contenu",
        label="Coutume — Suivi d’habitudes pour iPhone",
        h1='Tiens tes habitudes, <em class="swash">un jour à la fois</em>.',
        intro="Les bonnes à prendre, les mauvaises à laisser&nbsp;: un toucher pour noter, et Santé compte tes pas. Gratuite, sans compte, sans pub et sans abonnement.",
        store="Bientôt sur l’App Store", platform="iPhone, en français et en anglais",
        screens=[
            ("today", "Touche l’anneau, c’est noté.", "Les habitudes de ta journée, chacune avec son anneau. Une habitude qui se compte, comme 8 verres d’eau, en ajoute un à chaque toucher&nbsp;; maintiens l’anneau pour entrer un nombre ou annuler.", "La journée : six habitudes, chacune avec son anneau"),
            ("detail", "Santé compte tes pas pour toi.", "Tes pas, tes minutes d’exercice, ta pleine conscience et ton eau se notent seuls. Chaque habitude garde sa séquence et tout son historique.", "10 000 pas, remplis par Santé, avec la séquence et l’historique"),
            ("quit", "Les mauvaises habitudes, comptées en jours sans.", "Une habitude à éviter est tenue d’office&nbsp;: tu ne notes que le jour où tu craques. Coutume compte tes jours sans, l’argent économisé et les envies auxquelles tu as résisté.", "Une habitude à éviter : 12 jours sans boisson énergisante, 42 $ économisés"),
            ("progress", "Des niveaux et des jalons pour chaque journée tenue.", "Onze niveaux, de Bonne intention à Légende, dix-huit jalons à célébrer, et une séquence qui pardonne un jour manqué par semaine.", "Progrès : le niveau atteint et les jalons gagnés"),
            ("calendar", "Ton mois, jour après jour.", "Un calendrier de chaque journée, plus vif quand plus d’habitudes ont été tenues, et des widgets pour ton écran d’accueil.", "Le calendrier : le mois, plus vif quand plus d’habitudes ont été tenues"),
        ],
        features="Toutes les fonctionnalités.", faq="Questions fréquentes.",
        more='D’autres questions&nbsp;? <a href="../fr/assistance/">Visite l’assistance</a>.',
        like="Tu aimeras aussi.", soon="(bientôt)",
        apps=[("https://reliure.me/fr/", "Reliure", "Toutes tes lectures, reliées", False),
              ("https://arpente.app/fr/", "Arpente", "Chaque pas raconte un parcours", True),
              ("https://porcom.app/fr/", "Porcom", "Un petit journal pour tout ce que tu regardes", False),
              ("https://dernierverre.app/fr/", "Dernier Verre", "Un dernier, parfaitement dosé", True)],
        makers="Des mêmes créateurs.",
        web=[("https://puuun.ch/", "Puuunch", "Suivi du temps et feuilles de temps pour petites équipes."),
             ("https://makearesu.me/", "Makearesu.me", "Crée un CV en 5 minutes")],
        nav_label="Pied de page",
        nav=[("../fr/assistance/", "Assistance", ""), ("../fr/confidentialite/", "Confidentialité", ""), ("../", "English", ' hreflang="en" lang="en"')],
        made='Fait avec <svg class="heart" viewBox="0 0 24 22" role="img" aria-label="amour">' + HEART + '</svg> par <a href="https://wibeset.ca">Wibeset</a>. Développé au Canada.',
        aside="Coutume sur iPhone",
    ),
}


def fr_space(text, lang):
    """The JSON-LD holds plain spaces; the page sets a no-break space before French double punctuation."""
    return re.sub(r" ([?!:;])", "&nbsp;\\1", text) if lang == "fr" else text


def build(lang):
    t = T[lang]
    path = f"{ROOT}/{t['file']}"
    src = open(path).read()
    head = src[: src.index("<body>")]
    head = head.replace('<meta name="color-scheme" content="light">', '<meta name="color-scheme" content="dark">')
    head = head.replace('<meta name="theme-color" content="#f5f3ee">', '<meta name="theme-color" content="#0a0a0b">')
    head = re.sub(r'  <link rel="preconnect" href="https://fonts\.googleapis\.com">\n  <link rel="preconnect"[^\n]*\n  <link rel="stylesheet" href="https://fonts\.googleapis[^\n]*\n',
                  f'  <link rel="preload" href="{t["pre"]}assets/fonts/headland-one-latin.woff2" as="font" type="font/woff2" crossorigin>\n', head)
    graph = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', head).group(1))["@graph"]
    app = next(g for g in graph if g["@type"] == "MobileApplication")
    faq = next(g for g in graph if g["@type"] == "FAQPage")["mainEntity"]

    pre = t["pre"]
    shot = lambda name, alt: f'<figure class="device shot"><img src="{pre}assets/screens/fr/{name}.webp" width="750" height="1630" alt="{escape(alt, quote=True)}" loading="lazy" decoding="async"></figure>'
    first = t["screens"][0]
    out = [head, "<body>\n", f'  <a class="skip" href="#main">{t["skip"]}</a>\n\n  <div class="split">\n  <main id="main" class="content">\n']
    out.append(f'''    <section class="screen hero" data-screen="{first[0]}">
      <img class="logo" src="{pre}assets/icon.png" width="56" height="56" alt="">
      <p class="label">{t["label"]}</p>
      <h1>{t["h1"]}</h1>
      <div>
        <p>{t["intro"]}</p>
        <div class="get"><span class="store">{APPLE}{t["store"]}</span><span class="soon">{t["platform"]}</span></div>
      </div>
      {shot(first[0], first[3])}
    </section>
''')
    for i, (name, h2, p, alt) in enumerate(t["screens"]):
        fig = "" if i == 0 else f"\n      {shot(name, alt)}"
        out.append(f'''    <section class="screen" data-screen="{name}">
      <h2>{h2}</h2>
      <p>{p}</p>{fig}
    </section>
''')
    rows = []
    for (color, svg), feature in zip(ICONS, app["featureList"]):
        name, desc = feature.split(": ", 1)
        rows.append(f'        <li><h3 class="name"><svg class="icon" viewBox="0 0 24 24" style="color: {color}" aria-hidden="true">{svg}</svg>{name}</h3><p>{desc}</p></li>')
    out.append(f'''    <section>
      <h2>{t["features"]}</h2>
      <ul class="rows">
{chr(10).join(rows)}
      </ul>
    </section>
''')
    qa = []
    for q in faq:
        qa.append(f'''        <details>
          <summary><h3>{fr_space(q["name"], lang)}</h3></summary>
          <p>{fr_space(q["acceptedAnswer"]["text"], lang)}</p>
        </details>''')
    out.append(f'''    <section aria-labelledby="faq-heading">
      <h2 id="faq-heading">{t["faq"]}</h2>
      <div class="faq-list">
{chr(10).join(qa)}
      </div>
      <p class="faq-more">{t["more"]}</p>
    </section>
''')
    apps = "\n".join(f'        <li><span class="name"><a href="{u}">{n}</a></span><p>{d}{" <span class=\"soon\">" + t["soon"] + "</span>" if soon else ""}</p></li>' for u, n, d, soon in t["apps"])
    web = "\n".join(f'        <li><span class="name"><a href="{u}">{n}</a></span><p>{d}</p></li>' for u, n, d in t["web"])
    nav = "\n".join(f'        <a href="{h}"{a}>{l}</a>' for h, l, a in t["nav"])
    out.append(f'''    <!-- Friendly ads: the makers' other apps (Reliure, Arpente, Porcom, Dernier Verre), then Wibeset's web products. -->
    <section>
      <h2>{t["like"]}</h2>
      <ul class="rows">
{apps}
      </ul>
    </section>
    <section>
      <h2>{t["makers"]}</h2>
      <ul class="rows">
{web}
      </ul>
    </section>
    <footer>
      <nav aria-label="{t["nav_label"]}">
{nav}
      </nav>
      <p>{t["made"]}</p>
    </footer>
  </main>

  <!-- The app, captured from the simulator with sample habits (scripts/capture-screens.sh). main.js shows the screen of the section being read. -->
  <aside class="preview" aria-label="{t["aside"]}">
    <div class="device">
''')
    for i, (name, _, _, alt) in enumerate(t["screens"]):
        load = 'fetchpriority="high"' if i == 0 else 'loading="lazy"'
        out.append(f'      <img src="{pre}assets/screens/fr/{name}.webp" width="750" height="1630" alt="{escape(alt, quote=True)}" data-screen="{name}" {load} decoding="async">\n')
    out.append(f'''    </div>
  </aside>
  </div>

  <script src="{pre}assets/main.js" defer></script>
</body>
</html>
''')
    open(path, "w").write("".join(out))
    print("wrote", path)


if __name__ == "__main__":
    for lang in T:
        build(lang)
