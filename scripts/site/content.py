# The guides of coutume.app, in English and French. Text is HTML; the generator adds French no-break spaces.
# Split pages: "sections" is a list of (screen, h2, html). Plain pages: "body" is HTML.

from alternatives import ALT_PAGES, ALT_RELATED

SCREENS = {
    "today": ("The day: six habits, each with its ring", "La journée : six habitudes, chacune avec son anneau"),
    "detail": ("10,000 steps, filled in by Apple Health, with its streak and history", "10 000 pas, remplis par Santé, avec la séquence et l’historique"),
    "quit": ("A habit to quit: 12 days without energy drinks, $42 saved", "Une habitude à éviter : 12 jours sans boisson énergisante, 42 $ économisés"),
    "progress": ("Statistics: the level reached and the milestones earned", "Statistiques : le niveau atteint et les jalons gagnés"),
    "calendar": ("The calendar: the month, brighter as more habits were kept", "Le calendrier : le mois, plus vif quand plus d’habitudes ont été tenues"),
}

PAGES = [
# ---------------------------------------------------------------- Alternatives (alternatives.py)
*ALT_PAGES,

# ---------------------------------------------------------------- Features and uses
dict(key="health", layout="split", en_slug="habit-tracker-apple-health", fr_slug="suivi-habitudes-sante",
en=dict(
  title="Habit Tracker with Apple Health: Steps Log Themselves — Coutume",
  desc="A free iPhone habit tracker that reads Apple Health: steps, exercise, mindful minutes and water fill in your habits on their own. Read only, no account.",
  crumb="Apple Health habit tracker", guide="Steps, exercise, mindful minutes and water, filled in by Apple Health",
  h1="A habit tracker that Apple Health fills in for you",
  lede="Walk, and your steps habit fills itself. Coutume reads four kinds of data from Apple Health to log your habits on its own, so you only tap for the rest. Free, with no account and no ads.",
  sections=[
    ("detail", "Four habits that log themselves", "<p>Steps, exercise minutes, mindful minutes and water. Link a habit to one of them, like 10,000 steps or 8 glasses of water, and its ring fills as Health counts.</p>"),
    ("detail", "The same total as the Health app", "<p>Coutume uses the same daily total as Health, which counts your iPhone and Apple Watch only once. Apple Watch data can reach your iPhone a little later: each time you open Coutume, it reads the last seven days again and catches up.</p>"),
    ("today", "Next to the habits you tap", "<p>Your Health habits sit with the others in your day: reading 20 pages, meditating, going to bed on time. One tap logs those; Health logs the rest.</p>"),
    ("calendar", "Read only, and private", "<p>Coutume never writes to Health, and never reads anything you didn’t allow. The daily totals stay on your iPhone and in your private iCloud: they are never sent to us or used for advertising. You can change what Coutume reads at any time in Settings › Privacy &amp; Security › Health › Coutume.</p>"),
  ]),
fr=dict(
  title="Suivi d’habitudes avec Santé : tes pas se notent seuls — Coutume",
  desc="Coutume suit tes habitudes sur iPhone et lit Santé : pas, exercice, pleine conscience et eau remplissent tes habitudes seuls. Gratuite, sans compte.",
  crumb="Suivi d’habitudes avec Santé", guide="Pas, exercice, pleine conscience et eau, remplis par Santé",
  h1="Une app d’habitudes que Santé remplit pour toi",
  lede="Marche, et ton habitude de pas se remplit seule. Coutume lit quatre types de données dans Santé pour noter tes habitudes à ta place : tu ne touches que pour le reste. Gratuite, sans compte et sans pub.",
  sections=[
    ("detail", "Quatre habitudes qui se notent seules", "<p>Les pas, les minutes d’exercice, la pleine conscience et l’eau. Relie une habitude à l’un d’eux, comme 10 000 pas ou 8 verres d’eau, et son anneau se remplit au rythme de Santé.</p>"),
    ("detail", "Le même total que l’app Santé", "<p>Coutume utilise le même total quotidien que Santé, qui ne compte qu’une fois ton iPhone et ton Apple Watch. Les données de l’Apple Watch peuvent arriver un peu plus tard sur ton iPhone : chaque fois que tu ouvres Coutume, elle relit les sept derniers jours et se rattrape.</p>"),
    ("today", "À côté des habitudes que tu touches", "<p>Tes habitudes Santé côtoient les autres dans ta journée : lire 20 pages, méditer, te coucher à l’heure. Un toucher note celles-là ; Santé note le reste.</p>"),
    ("calendar", "En lecture seule, et privé", "<p>Coutume n’écrit jamais dans Santé, et ne lit jamais ce que tu n’as pas autorisé. Les totaux quotidiens restent sur ton iPhone et dans ton iCloud privé : ils ne nous sont jamais envoyés et ne servent jamais à la publicité. Tu peux changer ce que lit Coutume en tout temps dans Réglages › Confidentialité et sécurité › Santé › Coutume.</p>"),
  ])),

dict(key="energy", layout="split", en_slug="quit-energy-drinks", fr_slug="arreter-boissons-energisantes",
en=dict(
  title="Quit Energy Drinks: Count Your Days Without — Coutume",
  desc="Trying to quit energy drinks? Coutume counts your days without, the money you save and the urges you resist, on iPhone. Free, private, no account.",
  crumb="Quit energy drinks", guide="Count your days without energy drinks and the money you save",
  h1="Quit energy drinks, one day at a time",
  lede="Coutume is a free habit tracker for iPhone with a habit made for quitting: it counts your days without energy drinks, the money you save and the urges you resist. No account, no ads.",
  sections=[
    ("quit", "Kept by default, logged only when you slip", "<p>Most trackers want you to check a box every day. A habit to quit works the other way: each day counts as kept unless you log a slip. On a good day, there is nothing to do.</p>"),
    ("quit", "Days without, money saved, urges resisted", "<p>Coutume counts your days without energy drinks, the money you didn’t spend on cans, and the urges you resisted, so you can see them add up week after week.</p>"),
    ("progress", "A slip restarts the count, not everything", "<p>If you slip, the count of days without starts over. Your level, your milestones and your month stay: they count every day you kept.</p>"),
    ("today", "Replace it with something", "<p>Quitting is easier with something in its place. Add a habit to build beside it, like 8 glasses of water or a walk, and fill its ring with a tap, or let Apple Health fill it for you.</p>"),
  ],
  extra="<p class=\"note\">Coutume is a habit tracker, not a medical app. If you are worried about your caffeine intake, talk to a doctor or a pharmacist.</p>"),
fr=dict(
  title="Arrêter les boissons énergisantes : compte tes jours sans — Coutume",
  desc="Arrêter les boissons énergisantes : Coutume compte tes jours sans, l’argent économisé et les envies résistées, sur iPhone. Gratuite et sans compte.",
  crumb="Arrêter les boissons énergisantes", guide="Compte tes jours sans boisson énergisante et l’argent économisé",
  h1="Arrêter les boissons énergisantes, un jour à la fois",
  lede="Coutume suit tes habitudes sur iPhone, gratuitement, avec un type d’habitude fait pour arrêter : elle compte tes jours sans boisson énergisante, l’argent économisé et les envies résistées. Sans compte, sans pub.",
  sections=[
    ("quit", "Tenue d’office, notée seulement quand tu craques", "<p>La plupart des apps veulent que tu coches une case chaque jour. Une habitude à éviter fonctionne à l’inverse : chaque journée compte comme tenue, sauf si tu notes un écart. Les bons jours, tu n’as rien à faire.</p>"),
    ("quit", "Jours sans, argent économisé, envies résistées", "<p>Coutume compte tes jours sans boisson énergisante, l’argent que tu n’as pas dépensé en canettes et les envies auxquelles tu as résisté : tu les vois s’additionner semaine après semaine.</p>"),
    ("progress", "Un écart remet le compteur à zéro, pas tout le reste", "<p>Si tu craques, le compteur de jours sans repart à zéro. Ton niveau, tes jalons et ton mois restent : ils comptent chaque journée tenue.</p>"),
    ("today", "La remplacer par autre chose", "<p>Arrêter est plus facile avec quelque chose à la place. Ajoute à côté une habitude à prendre, comme 8 verres d’eau ou une marche, et remplis son anneau d’un toucher, ou laisse Santé le remplir pour toi.</p>"),
  ],
  extra="<p class=\"note\">Coutume est une app d’habitudes, pas une app médicale. Si ta consommation de caféine t’inquiète, parles-en à un médecin ou à un pharmacien.</p>")),

dict(key="vaping", layout="split", en_slug="quit-vaping-tracker", fr_slug="arreter-de-vapoter",
en=dict(
  title="Quit Vaping Tracker for iPhone: Days Without, Money Saved — Coutume",
  desc="A free quit vaping tracker for iPhone: Coutume counts your days without vaping, the money you save and the urges you resist. No account, no ads.",
  crumb="Quit vaping tracker", guide="Track your days without vaping, the money saved and the urges resisted",
  h1="A quit vaping tracker that counts what you gain",
  lede="Set “No vaping” as a habit to quit, and Coutume counts every day without it, the money you save and the urges you get through. Free, private, on iPhone.",
  sections=[
    ("quit", "Nothing to log on a good day", "<p>A habit to quit is kept by default. You don’t check anything when you didn’t vape; you only log the day you slip. Coutume does the counting.</p>"),
    ("quit", "Watch the days and the savings grow", "<p>Your days without vaping, the money you didn’t spend, and the urges you resisted this week, side by side on the habit’s page.</p>"),
    ("progress", "Every day kept still counts", "<p>A slip restarts the count of days without, but never takes away your level or your milestones. Fifteen levels and eighteen milestones mark the way, one kept day after another.</p>"),
    ("calendar", "See your month", "<p>The calendar shows each day of the month, brighter as more of your habits were kept: a quiet way to see how far you’ve come.</p>"),
  ],
  extra="<p class=\"note\">Coutume is a habit tracker, not a medical app or a quit-smoking program. For help to stop vaping, talk to a doctor, a pharmacist or your local quit line.</p>"),
fr=dict(
  title="Arrêter de vapoter : tes jours sans et l’argent économisé — Coutume",
  desc="Une app gratuite pour arrêter de vapoter sur iPhone : Coutume compte tes jours sans vapoter, l’argent économisé et les envies résistées. Sans compte.",
  crumb="Arrêter de vapoter", guide="Tes jours sans vapoter, l’argent économisé et les envies résistées",
  h1="Arrêter de vapoter, en comptant ce que tu gagnes",
  lede="Crée « Zéro vapotage » comme habitude à éviter, et Coutume compte chaque journée sans, l’argent économisé et les envies que tu traverses. Gratuite, privée, sur iPhone.",
  sections=[
    ("quit", "Rien à noter les bons jours", "<p>Une habitude à éviter est tenue d’office. Tu ne coches rien quand tu n’as pas vapoté ; tu ne notes que le jour où tu craques. Coutume compte pour toi.</p>"),
    ("quit", "Regarde les jours et les économies grimper", "<p>Tes jours sans vapoter, l’argent que tu n’as pas dépensé et les envies résistées cette semaine, côte à côte sur la page de l’habitude.</p>"),
    ("progress", "Chaque journée tenue compte toujours", "<p>Un écart remet à zéro le compteur de jours sans, mais ne t’enlève jamais ton niveau ni tes jalons. Quinze niveaux et dix-huit jalons balisent le chemin, une journée tenue après l’autre.</p>"),
    ("calendar", "Vois ton mois", "<p>Le calendrier montre chaque journée du mois, plus vive quand plus d’habitudes ont été tenues : une façon tranquille de voir le chemin parcouru.</p>"),
  ],
  extra="<p class=\"note\">Coutume est une app d’habitudes, pas une app médicale ni un programme d’arrêt du tabac. Pour de l’aide à arrêter de vapoter, parles-en à un médecin, à un pharmacien ou à une ligne d’aide de ta région.</p>")),

dict(key="dayswithout", layout="split", en_slug="days-without-counter", fr_slug="compteur-jours-sans",
en=dict(
  title="Days Without Counter for iPhone: Track Any Habit You Quit — Coutume",
  desc="A free “days without” counter for iPhone: sugar, coffee, social media, energy drinks. Count your days without, the money saved and the urges resisted.",
  crumb="Days without counter", guide="A days-without counter for anything you want to quit",
  h1="A “days without” counter for anything you quit",
  lede="Sugar, coffee, late-night scrolling, energy drinks: name what you want to quit, and Coutume counts your days without it. A free habit tracker for iPhone, with no account and no ads.",
  sections=[
    ("quit", "Any habit you want to quit", "<p>Create a habit to quit and give it a name and an icon. From then on, every day counts as kept unless you log a slip, and the count of days without grows on its own.</p>"),
    ("quit", "More than a number of days", "<p>Coutume also counts the money you save and the urges you resist, so a hard afternoon you got through counts for something.</p>"),
    ("progress", "A slip isn’t the end", "<p>A slip restarts the count, never your month or your level. Your milestones stay earned, and every day you kept still counts.</p>"),
    ("calendar", "Several at once", "<p>Quit more than one thing, and build good habits beside them: they all share your day, your calendar and your levels.</p>"),
  ]),
fr=dict(
  title="Compteur de jours sans pour iPhone : tout ce que tu arrêtes — Coutume",
  desc="Un compteur de jours sans gratuit pour iPhone : sucre, café, réseaux sociaux. Coutume compte tes jours sans, l’argent économisé et les envies résistées.",
  crumb="Compteur de jours sans", guide="Un compteur de jours sans pour tout ce que tu veux arrêter",
  h1="Un compteur de « jours sans » pour tout ce que tu arrêtes",
  lede="Le sucre, le café, les réseaux le soir, les boissons énergisantes : nomme ce que tu veux arrêter, et Coutume compte tes jours sans. Une app d’habitudes gratuite pour iPhone, sans compte et sans pub.",
  sections=[
    ("quit", "N’importe quelle habitude à arrêter", "<p>Crée une habitude à éviter, donne-lui un nom et une icône. Dès lors, chaque journée compte comme tenue sauf si tu notes un écart, et le compteur de jours sans grimpe tout seul.</p>"),
    ("quit", "Plus qu’un nombre de jours", "<p>Coutume compte aussi l’argent économisé et les envies résistées : un après-midi difficile que tu as traversé compte pour quelque chose.</p>"),
    ("progress", "Un écart n’est pas la fin", "<p>Un écart remet le compteur à zéro, jamais ton mois ni ton niveau. Tes jalons restent gagnés, et chaque journée tenue compte toujours.</p>"),
    ("calendar", "Plusieurs à la fois", "<p>Arrête plus d’une chose, et prends de bonnes habitudes à côté : elles partagent toutes ta journée, ton calendrier et tes niveaux.</p>"),
  ])),

dict(key="water", layout="split", en_slug="water-tracker", fr_slug="suivi-eau",
en=dict(
  title="Water Tracker for iPhone: 8 Glasses a Day, in One Tap — Coutume",
  desc="Track your water on iPhone: tap a ring for each glass, or let Apple Health fill it in. Coutume is a free habit tracker with streaks, levels and no account.",
  crumb="Water tracker", guide="Count your glasses of water in one tap, or let Apple Health do it",
  h1="A water tracker that takes one tap per glass",
  lede="Set a daily target, like 8 glasses of water, and tap the ring each time you drink. Or let Apple Health fill it in. Coutume is a free habit tracker for iPhone, with no account and no ads.",
  sections=[
    ("today", "One tap, one glass", "<p>A habit you count adds one with each tap, and its ring fills toward your target. Touch and hold the ring to enter a number or undo the last glass.</p>"),
    ("detail", "Or let Apple Health count", "<p>If you already log water in Health, or with an app or a bottle that writes to it, link your water habit to Health and it fills itself in.</p>"),
    ("calendar", "A streak that forgives", "<p>Each day you reach your target extends your streak, and one missed day a week is forgiven. The calendar shows your month, brighter as more habits were kept.</p>"),
    ("today", "With your other habits", "<p>Water sits beside your steps, your reading or your bedtime, in the same day and on the same Home Screen widget.</p>"),
  ]),
fr=dict(
  title="Suivi de l’eau sur iPhone : 8 verres par jour, d’un toucher — Coutume",
  desc="Suis l’eau que tu bois sur iPhone : touche l’anneau à chaque verre, ou laisse Santé le remplir. Gratuite, avec séquences et niveaux, sans compte.",
  crumb="Suivi de l’eau", guide="Compte tes verres d’eau d’un toucher, ou laisse Santé le faire",
  h1="Suivre ton eau, un toucher par verre",
  lede="Fixe un objectif quotidien, comme 8 verres d’eau, et touche l’anneau chaque fois que tu bois. Ou laisse Santé le remplir. Coutume suit tes habitudes sur iPhone, gratuitement, sans compte et sans pub.",
  sections=[
    ("today", "Un toucher, un verre", "<p>Une habitude qui se compte en ajoute un à chaque toucher, et son anneau se remplit vers ton objectif. Maintiens l’anneau pour entrer un nombre ou annuler le dernier verre.</p>"),
    ("detail", "Ou laisse Santé compter", "<p>Si tu notes déjà ton eau dans Santé, ou avec une app ou une bouteille qui y écrit, relie ton habitude d’eau à Santé et elle se remplit seule.</p>"),
    ("calendar", "Une séquence qui pardonne", "<p>Chaque journée où tu atteins ton objectif allonge ta séquence, et un jour manqué par semaine est pardonné. Le calendrier montre ton mois, plus vif quand plus d’habitudes ont été tenues.</p>"),
    ("today", "Avec tes autres habitudes", "<p>L’eau côtoie tes pas, ta lecture ou ton coucher, dans la même journée et sur le même widget d’écran d’accueil.</p>"),
  ])),

dict(key="free", layout="split", en_slug="free-habit-tracker", fr_slug="application-habitudes-gratuite",
en=dict(
  title="Free Habit Tracker for iPhone: No Account, No Ads — Coutume",
  desc="A truly free habit tracker for iPhone: no subscription, no ads, no account, no habit limit. Habits to build and to quit, Apple Health and widgets.",
  crumb="Free habit tracker", guide="Free for real: no subscription, no ads, no account",
  h1="A habit tracker that is free for real",
  lede="No trial that ends, no fourth habit behind a paywall, no ads between your rings. Coutume is a free habit tracker for iPhone, with no account and no subscription.",
  sections=[
    ("today", "Everything, for free", "<p>Habits to build and to quit, Apple Health, forgiving streaks, levels, milestones, the calendar, widgets and iCloud sync: all of it, with no paid plan.</p>"),
    ("quit", "No account to create", "<p>Open the app and add your first habit. There is no sign-up, no email and no password, and nothing to delete later.</p>"),
    ("progress", "No ads, no tracking", "<p>Coutume has no ads, no analytics and no server of its own. Your habits stay on your iPhone and in your private iCloud, and we never receive them.</p>"),
    ("calendar", "Why it’s free", "<p>Coutume is made by Wibeset, a small studio in Canada that makes apps it wants to use itself, like Reliure for reading. It is free because a habit tracker shouldn’t cost you a subscription.</p>"),
  ]),
fr=dict(
  title="App d’habitudes gratuite pour iPhone : sans compte ni pub — Coutume",
  desc="Une app d’habitudes vraiment gratuite pour iPhone : sans abonnement, sans pub, sans compte ni limite. Habitudes à prendre et à éviter, Santé, widgets.",
  crumb="App d’habitudes gratuite", guide="Gratuite pour vrai : sans abonnement, sans pub, sans compte",
  h1="Une app d’habitudes gratuite pour vrai",
  lede="Pas d’essai qui se termine, pas de quatrième habitude derrière un paiement, pas de pub entre tes anneaux. Coutume suit tes habitudes sur iPhone, gratuitement, sans compte ni abonnement.",
  sections=[
    ("today", "Tout, gratuitement", "<p>Habitudes à prendre et à éviter, Santé, séquences indulgentes, niveaux, jalons, calendrier, widgets et synchro iCloud : tout, sans forfait payant.</p>"),
    ("quit", "Aucun compte à créer", "<p>Ouvre l’app et ajoute ta première habitude. Pas d’inscription, pas de courriel, pas de mot de passe, et rien à supprimer plus tard.</p>"),
    ("progress", "Sans pub, sans pistage", "<p>Coutume n’a ni pub, ni statistiques d’usage, ni serveur à elle. Tes habitudes restent sur ton iPhone et dans ton iCloud privé, et nous ne les recevons jamais.</p>"),
    ("calendar", "Pourquoi elle est gratuite", "<p>Coutume est faite par Wibeset, un petit studio au Canada qui fait les apps qu’il veut utiliser lui-même, comme Reliure pour la lecture. Elle est gratuite parce qu’une app d’habitudes ne devrait pas te coûter un abonnement.</p>"),
  ])),

dict(key="widget", layout="split", en_slug="habit-tracker-widget", fr_slug="widget-habitudes",
en=dict(
  title="Habit Tracker Widget for iPhone: Rings on Your Home Screen — Coutume",
  desc="See your habits without opening an app: Coutume’s widgets show the day’s rings and your streak of perfect days on the Home Screen and Lock Screen.",
  crumb="Habit tracker widget", guide="The day’s rings on your Home Screen and Lock Screen",
  h1="Your habits, right on your Home Screen",
  lede="Coutume’s widgets show the day’s rings and your streak of perfect days on your Home Screen, and fit on the Lock Screen too. A free habit tracker for iPhone, with no account and no ads.",
  sections=[
    ("today", "The day at a glance", "<p>Each habit’s ring, as full as your day: glasses of water, steps filled in by Apple Health, the habits you quit, kept by default.</p>"),
    ("calendar", "Your streak of perfect days", "<p>The widget also shows how many perfect days in a row you’ve kept, the days every habit was done.</p>"),
    ("today", "Add the widget", "<p>Touch and hold your Home Screen, tap <strong>Edit</strong> › <strong>Add Widget</strong>, then choose Coutume. On the Lock Screen, touch and hold it, tap <strong>Customize</strong>, then add Coutume to the widgets under the clock.</p>"),
  ]),
fr=dict(
  title="Widget d’habitudes : tes anneaux sur l’écran d’accueil — Coutume",
  desc="Vois tes habitudes sans ouvrir d’app : les widgets de Coutume montrent les anneaux du jour et ta séquence sur l’écran d’accueil et l’écran verrouillé.",
  crumb="Widget d’habitudes", guide="Les anneaux du jour sur ton écran d’accueil et ton écran verrouillé",
  h1="Tes habitudes, directement sur ton écran d’accueil",
  lede="Les widgets de Coutume montrent les anneaux du jour et ta séquence de journées parfaites sur ton écran d’accueil, et se placent aussi sur l’écran verrouillé. Une app d’habitudes gratuite pour iPhone, sans compte et sans pub.",
  sections=[
    ("today", "Ta journée d’un coup d’œil", "<p>L’anneau de chaque habitude, aussi plein que ta journée : les verres d’eau, les pas remplis par Santé, les habitudes que tu arrêtes, tenues d’office.</p>"),
    ("calendar", "Ta séquence de journées parfaites", "<p>Le widget montre aussi combien de journées parfaites tu as enchaînées, celles où chaque habitude a été tenue.</p>"),
    ("today", "Ajouter le widget", "<p>Maintiens ton écran d’accueil, touche <strong>Modifier</strong> › <strong>Ajouter un widget</strong>, puis choisis Coutume. Sur l’écran verrouillé, maintiens-le, touche <strong>Personnaliser</strong>, puis ajoute Coutume aux widgets sous l’heure.</p>"),
  ])),

# ---------------------------------------------------------------- Articles
dict(key="ideas", layout="plain", en_slug="habit-ideas", fr_slug="idees-habitudes",
en=dict(
  title="40 Habit Ideas: Good Habits to Build and Bad Ones to Quit — Coutume",
  desc="Looking for habits to track? 40 ideas of good habits to build and bad habits to quit, for health, sleep, mind and money, with a tip to make each one stick.",
  crumb="Habit ideas", guide="40 ideas of good habits to build and bad ones to quit",
  h1="40 habit ideas, to build and to quit",
  lede="Not sure which habits to track? Here are forty ideas, sorted by theme. Pick two or three, not ten: small habits you keep beat big ones you drop.",
  body="""
      <h2>Health and movement</h2>
      <ul>
        <li><strong>Drink 8 glasses of water.</strong> Count them one tap at a time, or let Apple Health fill them in.</li>
        <li><strong>Walk 10,000 steps</strong>, or 6,000 to start: a target you reach most days keeps the streak alive.</li>
        <li><strong>Move for 30 minutes.</strong> Apple Health counts your exercise minutes.</li>
        <li><strong>Stretch for 5 minutes</strong> after waking up.</li>
        <li><strong>Eat a fruit or a vegetable</strong> with every meal.</li>
        <li><strong>Take the stairs.</strong></li>
        <li><strong>Cook dinner at home.</strong></li>
        <li><strong>Take your vitamins or medication</strong> at the same time each day.</li>
      </ul>

      <h2>Sleep and evenings</h2>
      <ul>
        <li><strong>Be in bed by 11 p.m.</strong></li>
        <li><strong>No screens in bed.</strong></li>
        <li><strong>Prepare tomorrow’s bag or clothes</strong> the night before.</li>
        <li><strong>Get outside in the morning light.</strong></li>
        <li><strong>Write three lines</strong> about your day.</li>
      </ul>

      <h2>Mind and learning</h2>
      <ul>
        <li><strong>Read 20 pages.</strong> <a href="https://reliure.me/">Reliure</a>, from the same makers, keeps track of your books.</li>
        <li><strong>Meditate for 10 minutes.</strong> Apple Health counts your mindful minutes.</li>
        <li><strong>Practise a language</strong> for 15 minutes.</li>
        <li><strong>Play an instrument.</strong></li>
        <li><strong>Note one thing you’re grateful for.</strong></li>
        <li><strong>Call or write to someone</strong> you care about.</li>
        <li><strong>Make your bed.</strong></li>
        <li><strong>Tidy for 10 minutes.</strong></li>
      </ul>

      <h2>Bad habits to quit</h2>
      <p>In Coutume, a habit to quit is kept by default: you only log the day you slip, and it counts your <a href="../days-without-counter/">days without</a>, the money saved and the urges you resisted.</p>
      <ul>
        <li><strong><a href="../quit-energy-drinks/">No energy drinks.</a></strong></li>
        <li><strong><a href="../quit-vaping-tracker/">No vaping</a></strong>, or no smoking.</li>
        <li><strong>No sugary drinks.</strong></li>
        <li><strong>No snacking after dinner.</strong></li>
        <li><strong>No coffee after noon.</strong></li>
        <li><strong>No social media before 9 a.m.</strong></li>
        <li><strong>No phone at the table.</strong></li>
        <li><strong>No doomscrolling in bed.</strong></li>
        <li><strong>No takeout on weeknights.</strong></li>
        <li><strong>No impulse buys online.</strong></li>
        <li><strong>No nail biting.</strong></li>
        <li><strong>No hitting snooze.</strong></li>
      </ul>

      <h2>Money</h2>
      <ul>
        <li><strong>Write down every expense.</strong></li>
        <li><strong>Bring your lunch.</strong></li>
        <li><strong>Make your own coffee.</strong> As a habit to quit, “no café coffee” shows the money it saves.</li>
        <li><strong>Wait 24 hours</strong> before any purchase over $50.</li>
        <li><strong>Put aside $5 a day.</strong></li>
        <li><strong>Check your accounts</strong> once a week.</li>
        <li><strong>Cancel one subscription</strong> you don’t use.</li>
      </ul>

      <h2>Make them stick</h2>
      <ul>
        <li><strong>Start smaller than you think.</strong> Five minutes kept every day does more than an hour kept twice.</li>
        <li><strong>Tie it to something you already do</strong>: a glass of water with your coffee, a stretch after brushing your teeth.</li>
        <li><strong>Don’t chase a perfect streak.</strong> Missing one day barely matters; what matters is coming back the next one. That’s why Coutume forgives one missed day a week. Read <a href="../how-long-to-form-a-habit/">how long it takes to form a habit</a>.</li>
      </ul>
"""),
fr=dict(
  title="40 idées d’habitudes : bonnes à prendre, mauvaises à laisser — Coutume",
  desc="40 idées de bonnes habitudes à prendre et de mauvaises à laisser, pour la santé, le sommeil, la tête et l’argent, avec des astuces pour les garder.",
  crumb="Idées d’habitudes", guide="40 idées de bonnes habitudes à prendre et de mauvaises à laisser",
  h1="40 idées d’habitudes, à prendre et à laisser",
  lede="Tu ne sais pas quelles habitudes suivre ? Voici quarante idées, classées par thème. Choisis-en deux ou trois, pas dix : de petites habitudes que tu gardes valent mieux que de grandes que tu abandonnes.",
  body="""
      <h2>Santé et mouvement</h2>
      <ul>
        <li><strong>Boire 8 verres d’eau.</strong> Compte-les d’un toucher, ou laisse Santé les remplir.</li>
        <li><strong>Marcher 10 000 pas</strong>, ou 6 000 pour commencer : un objectif atteint la plupart des jours garde la séquence en vie.</li>
        <li><strong>Bouger 30 minutes.</strong> Santé compte tes minutes d’exercice.</li>
        <li><strong>T’étirer 5 minutes</strong> au réveil.</li>
        <li><strong>Manger un fruit ou un légume</strong> à chaque repas.</li>
        <li><strong>Prendre l’escalier.</strong></li>
        <li><strong>Cuisiner le souper à la maison.</strong></li>
        <li><strong>Prendre tes vitamines ou tes médicaments</strong> à la même heure chaque jour.</li>
      </ul>

      <h2>Sommeil et soirées</h2>
      <ul>
        <li><strong>Être au lit à 23 h.</strong></li>
        <li><strong>Pas d’écran au lit.</strong></li>
        <li><strong>Préparer ton sac ou tes vêtements</strong> la veille.</li>
        <li><strong>Sortir à la lumière du matin.</strong></li>
        <li><strong>Écrire trois lignes</strong> sur ta journée.</li>
      </ul>

      <h2>Tête et apprentissage</h2>
      <ul>
        <li><strong>Lire 20 pages.</strong> <a href="https://reliure.me/fr/">Reliure</a>, des mêmes créateurs, garde la trace de tes livres.</li>
        <li><strong>Méditer 10 minutes.</strong> Santé compte tes minutes de pleine conscience.</li>
        <li><strong>Pratiquer une langue</strong> 15 minutes.</li>
        <li><strong>Jouer d’un instrument.</strong></li>
        <li><strong>Noter une chose dont tu es reconnaissant ou reconnaissante.</strong></li>
        <li><strong>Appeler ou écrire à quelqu’un</strong> qui compte pour toi.</li>
        <li><strong>Faire ton lit.</strong></li>
        <li><strong>Ranger 10 minutes.</strong></li>
      </ul>

      <h2>Mauvaises habitudes à laisser</h2>
      <p>Dans Coutume, une habitude à éviter est tenue d’office : tu ne notes que le jour où tu craques, et elle compte tes <a href="../compteur-jours-sans/">jours sans</a>, l’argent économisé et les envies résistées.</p>
      <ul>
        <li><strong><a href="../arreter-boissons-energisantes/">Zéro boisson énergisante.</a></strong></li>
        <li><strong><a href="../arreter-de-vapoter/">Zéro vapotage</a></strong>, ou zéro cigarette.</li>
        <li><strong>Zéro boisson sucrée.</strong></li>
        <li><strong>Pas de grignotage après le souper.</strong></li>
        <li><strong>Pas de café après midi.</strong></li>
        <li><strong>Pas de réseaux sociaux avant 9 h.</strong></li>
        <li><strong>Pas de téléphone à table.</strong></li>
        <li><strong>Pas de défilement sans fin au lit.</strong></li>
        <li><strong>Pas de commande pour emporter en semaine.</strong></li>
        <li><strong>Pas d’achat impulsif en ligne.</strong></li>
        <li><strong>Ne plus te ronger les ongles.</strong></li>
        <li><strong>Ne plus repousser le réveil.</strong></li>
      </ul>

      <h2>Argent</h2>
      <ul>
        <li><strong>Noter chaque dépense.</strong></li>
        <li><strong>Apporter ton lunch.</strong></li>
        <li><strong>Faire ton café toi-même.</strong> En habitude à éviter, « pas de café acheté » montre l’argent économisé.</li>
        <li><strong>Attendre 24 heures</strong> avant tout achat de plus de 50 $.</li>
        <li><strong>Mettre 5 $ de côté par jour.</strong></li>
        <li><strong>Vérifier tes comptes</strong> une fois par semaine.</li>
        <li><strong>Annuler un abonnement</strong> que tu n’utilises pas.</li>
      </ul>

      <h2>Les garder</h2>
      <ul>
        <li><strong>Commence plus petit que tu penses.</strong> Cinq minutes tenues chaque jour font plus qu’une heure tenue deux fois.</li>
        <li><strong>Accroche-la à quelque chose que tu fais déjà</strong> : un verre d’eau avec ton café, un étirement après t’être brossé les dents.</li>
        <li><strong>Ne cours pas après la séquence parfaite.</strong> Manquer une journée ne change presque rien ; ce qui compte, c’est de revenir le lendemain. C’est pour ça que Coutume pardonne un jour manqué par semaine. Lis <a href="../combien-de-temps-pour-une-habitude/">combien de temps il faut pour prendre une habitude</a>.</li>
      </ul>
""")),

dict(key="howlong", layout="plain", en_slug="how-long-to-form-a-habit", fr_slug="combien-de-temps-pour-une-habitude",
en=dict(
  title="How Long Does It Take to Form a Habit? Not 21 Days — Coutume",
  desc="It takes 66 days on average to form a habit, not 21, and from 18 to 254 days. What the research says, and why missing one day doesn’t ruin your progress.",
  crumb="How long to form a habit", guide="What research says about the 21-day myth, and why one missed day doesn’t matter",
  h1="How long does it take to form a habit?",
  lede="About 66 days on average, not 21. And it varies a lot: from 18 days to more than 250, depending on the person and the habit. The good news: missing a day doesn’t send you back to zero.",
  body="""
      <h2>Where the 21 days come from</h2>
      <p>The “21 days” figure goes back to the 1960s, to a plastic surgeon, Maxwell Maltz, who noticed that his patients took a minimum of about 21 days to get used to a change. It was an observation, not a measurement of habits, and “a minimum of 21 days” became “21 days” over the years.</p>

      <h2>What the research found</h2>
      <p>In a study published online in 2009 (in print in 2010), a team at University College London led by Phillippa Lally followed 96 people for 84 days. Each chose a new daily behaviour, like drinking a glass of water with lunch or going for a run before dinner, and reported every day how automatic it felt.</p>
      <ul>
        <li>On average, it took <strong>66 days</strong> for the behaviour to become as automatic as it would get.</li>
        <li>The range was wide: from <strong>18 days</strong> to an estimated <strong>254 days</strong>.</li>
        <li>Simple habits, like drinking water, became automatic sooner than demanding ones, like exercising.</li>
        <li><strong>Missing one opportunity didn’t meaningfully affect the process.</strong> What prevented a habit from forming was being inconsistent, not missing a day.</li>
      </ul>
      <p class="note">Source: Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W. and Wardle, J. (2010). How are habits formed: Modelling habit formation in the real world. <em>European Journal of Social Psychology</em>, 40(6), 998–1009.</p>

      <h2>What it means for you</h2>
      <ul>
        <li><strong>Plan for two months, not three weeks.</strong> If a habit still takes effort after 21 days, nothing is wrong with you.</li>
        <li><strong>Make it easy.</strong> The simpler the behaviour, the sooner it becomes automatic: start with a glass of water or 5 minutes, then grow.</li>
        <li><strong>Same time, same cue.</strong> Repeating a behaviour in the same situation, after coffee or before bed, is what makes it automatic.</li>
        <li><strong>Forgive the missed day, then come back.</strong> One miss barely matters; a long break does.</li>
      </ul>

      <h2>How Coutume follows the research</h2>
      <p>Coutume’s streaks forgive one missed day a week, so one off day doesn’t erase weeks of effort. Your level counts every day you kept, not just your current streak, and the fifteen levels go well past 66 days, from Good intention to Legend.</p>
"""),
fr=dict(
  title="Combien de temps pour prendre une habitude ? Pas 21 jours — Coutume",
  desc="En moyenne 66 jours pour prendre une habitude, pas 21, et de 18 à 254 jours. Ce que dit la recherche, et pourquoi un jour manqué ne ruine pas tes progrès.",
  crumb="Combien de temps pour une habitude", guide="Ce que dit la recherche sur le mythe des 21 jours, et pourquoi un jour manqué ne compte pas",
  h1="Combien de temps faut-il pour prendre une habitude ?",
  lede="Environ 66 jours en moyenne, pas 21. Et ça varie beaucoup : de 18 jours à plus de 250, selon la personne et l’habitude. La bonne nouvelle : manquer une journée ne te ramène pas à zéro.",
  body="""
      <h2>D’où viennent les 21 jours</h2>
      <p>Le chiffre de « 21 jours » remonte aux années 1960, à un chirurgien plastique, Maxwell Maltz, qui avait remarqué que ses patients mettaient au moins 21 jours environ à s’habituer à un changement. C’était une observation, pas une mesure des habitudes, et « au moins 21 jours » est devenu « 21 jours » avec les années.</p>

      <h2>Ce que la recherche a trouvé</h2>
      <p>Dans une étude publiée en ligne en 2009 (sur papier en 2010), une équipe de l’University College London menée par Phillippa Lally a suivi 96 personnes pendant 84 jours. Chacune avait choisi un nouveau geste quotidien, comme boire un verre d’eau au dîner ou courir avant le souper, et notait chaque jour à quel point il lui semblait automatique.</p>
      <ul>
        <li>En moyenne, il a fallu <strong>66 jours</strong> pour que le geste devienne aussi automatique qu’il allait l’être.</li>
        <li>L’écart était grand : de <strong>18 jours</strong> à environ <strong>254 jours</strong>, selon les estimations.</li>
        <li>Les habitudes simples, comme boire de l’eau, sont devenues automatiques plus vite que les exigeantes, comme faire de l’exercice.</li>
        <li><strong>Manquer une occasion n’a pas vraiment nui au processus.</strong> Ce qui empêchait l’habitude de se former, c’était l’irrégularité, pas un jour manqué.</li>
      </ul>
      <p class="note">Source : Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W. et Wardle, J. (2010). How are habits formed: Modelling habit formation in the real world. <em>European Journal of Social Psychology</em>, 40(6), 998–1009.</p>

      <h2>Ce que ça veut dire pour toi</h2>
      <ul>
        <li><strong>Prévois deux mois, pas trois semaines.</strong> Si une habitude demande encore un effort après 21 jours, tout va bien.</li>
        <li><strong>Rends-la facile.</strong> Plus le geste est simple, plus vite il devient automatique : commence par un verre d’eau ou 5 minutes, puis augmente.</li>
        <li><strong>Même moment, même signal.</strong> Répéter un geste dans la même situation, après le café ou avant le coucher, est ce qui le rend automatique.</li>
        <li><strong>Pardonne le jour manqué, puis reviens.</strong> Une absence compte à peine ; une longue pause, oui.</li>
      </ul>

      <h2>Comment Coutume suit la recherche</h2>
      <p>Les séquences de Coutume pardonnent un jour manqué par semaine : une mauvaise journée n’efface pas des semaines d’effort. Ton niveau compte chaque journée tenue, pas seulement ta séquence en cours, et les quinze niveaux vont bien au-delà de 66 jours, de Bonne intention à Légende.</p>
""")),
]

# Which guides each page links to at its end.
RELATED = {
    **ALT_RELATED,
    "health": ["water", "widget", "streaks", "ideas"],
    "energy": ["dayswithout", "vaping", "water", "howlong"],
    "vaping": ["dayswithout", "energy", "howlong", "ideas"],
    "dayswithout": ["energy", "vaping", "ideas", "howlong"],
    "water": ["health", "widget", "ideas", "free"],
    "free": ["streaks", "habitify", "habitica", "health"],
    "widget": ["health", "water", "free", "ideas"],
    "ideas": ["howlong", "dayswithout", "health", "water"],
    "howlong": ["ideas", "dayswithout", "free", "habitica"],
}
