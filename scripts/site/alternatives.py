# The "best alternatives to <competitor>" pages, in English, French and Spanish: Coutume first, then three other picks.
# content.py and guides_es.py turn ALTS into guide pages. Facts about the competitors come from their US App Store listings
# and websites as of November 2026: re-check them before changing a page (see "Before updating" in scripts/README.md).
# A dash in a table means the listing doesn't say. French: ordinary spaces before ? ! : ; (the generator adds no-break spaces).

NAMES = {
    "streaks": "Streaks", "habitify": "Habitify", "habitica": "Habitica", "wayoflife": "Way of Life",
    "productive": "Productive", "strides": "Strides", "finch": "Finch", "habitkit": "HabitKit",
    "atoms": "Atoms", "fabulous": "Fabulous",
}
SLUG = {"streaks": "streaks", "habitify": "habitify", "habitica": "habitica", "wayoflife": "way-of-life",
        "productive": "productive", "strides": "strides", "finch": "finch", "habitkit": "habitkit",
        "atoms": "atoms", "fabulous": "fabulous"}

L = {
    "en": dict(
        title="The Best {n} Alternatives for iPhone (2026) — Coutume", h1="The best alternatives to {n}",
        crumb="{n} alternative", guide="The best alternatives to {n}, {t}",
        first="1. Coutume: the best free alternative to {n}", glance="Coutume and {n} at a glance", why="Why choose Coutume",
        better="When {n} may suit you better", moving="Moving from {n} to Coutume",
        move="Coutume doesn’t import from {n}: add your habits again, it takes a few seconds each. Habits filled in by Apple Health catch up on their own, since Coutume reads the last seven days each time you open it.",
        feature="Feature", rows=["Price", "Account", "Habits to quit", "Apple Health", "Rewards", "Platforms"],
        coutume=["Free, no ads", "None", "Days without, money saved, urges resisted", "Steps, exercise, mindful minutes and water, read only", "11 levels and 18 milestones, by days kept", "iPhone"],
        best="Best for",
        note="Based on each app’s US App Store listing and website as of November 2026; prices are in US dollars and vary by country and offer. A dash means the listing doesn’t say. {n} and the other apps named here are trademarks of their owners; Coutume is not affiliated with them."),
    "fr": dict(
        title="Les meilleures alternatives à {n} sur iPhone (2026) — Coutume", h1="Les meilleures alternatives à {n}",
        crumb="Alternative à {n}", guide="Les meilleures alternatives à {n}, {t}",
        first="1. Coutume : la meilleure alternative gratuite à {n}", glance="Coutume et {n} en un coup d’œil", why="Pourquoi choisir Coutume",
        better="Quand {n} te conviendra mieux", moving="Passer de {n} à Coutume",
        move="Coutume n’importe pas les données de {n} : ajoute de nouveau tes habitudes, ça prend quelques secondes chacune. Celles que Santé remplit se rattrapent seules, puisque Coutume relit les sept derniers jours chaque fois que tu l’ouvres.",
        feature="Fonctionnalité", rows=["Prix", "Compte", "Habitudes à éviter", "Santé", "Récompenses", "Appareils"],
        coutume=["Gratuite, sans pub", "Aucun", "Jours sans, argent économisé, envies résistées", "Pas, exercice, pleine conscience et eau, en lecture seule", "11 niveaux et 18 jalons, selon les jours tenus", "iPhone"],
        best="Idéale pour",
        note="D’après la fiche App Store américaine et le site de chaque app en novembre 2026 ; les prix sont en dollars américains et varient selon le pays et l’offre. Un tiret veut dire que la fiche ne le précise pas. {n} et les autres apps citées sont des marques de leurs propriétaires ; Coutume n’y est pas affiliée."),
    "es": dict(
        title="Las mejores alternativas a {n} para iPhone (2026) — Coutume", h1="Las mejores alternativas a {n}",
        crumb="Alternativa a {n}", guide="Las mejores alternativas a {n}, {t}",
        first="1. Coutume: la mejor alternativa gratis a {n}", glance="Coutume y {n} de un vistazo", why="Por qué elegir Coutume",
        better="Cuándo te puede convenir más {n}", moving="Pasar de {n} a Coutume",
        move="Coutume no importa datos de {n}: vuelve a añadir tus hábitos, cada uno lleva unos segundos. Los que completa Salud se ponen al día solos, porque Coutume vuelve a leer los últimos siete días cada vez que la abres.",
        feature="Función", rows=["Precio", "Cuenta", "Hábitos por dejar", "Salud", "Recompensas", "Dispositivos"],
        coutume=["Gratis, sin anuncios", "Ninguna", "Días sin, dinero ahorrado, impulsos resistidos", "Pasos, ejercicio, atención plena y agua, solo lectura", "11 niveles y 18 logros, por días cumplidos", "iPhone"],
        best="Ideal para",
        note="Según la ficha del App Store de EE. UU. y el sitio de cada app a noviembre de 2026; los precios están en dólares estadounidenses y varían según el país y la oferta. Un guion significa que la ficha no lo indica. {n} y las demás apps citadas son marcas de sus propietarios; Coutume no está afiliada a ellas."),
}

# Reasons to choose Coutume; each page picks its own, in its own order.
WHY = {
    "en": dict(
        free="<strong>Free, for good.</strong> No purchase, no subscription, no ads, and no habit limit behind a paywall.",
        noaccount="<strong>No account, no sign-up.</strong> Open the app and add your first habit. No password to remember, no profile to manage.",
        private="<strong>Private by default.</strong> No server, no analytics: your habits stay on your iPhone and in your private iCloud. We never receive them.",
        quit="<strong>Bad habits get their own logic.</strong> A habit to quit is kept by default: you only log the day you slip. Coutume counts your days without, the money saved and the urges you resisted.",
        forgive="<strong>A streak that forgives.</strong> One missed day a week doesn’t break your streak, so one off day doesn’t erase weeks of effort.",
        levels="<strong>Something to aim for.</strong> Eleven levels, from Good intention to Legend, and eighteen milestones, earned with every day kept.",
        health="<strong>Apple Health does the logging.</strong> Steps, exercise minutes, mindful minutes and water fill in your habits on their own.",
        simple="<strong>Quick to log.</strong> Tap a ring and the day is logged; touch and hold it to enter a number or undo.",
        calm="<strong>Progress without a game to manage.</strong> No avatar to equip, no pet to look after: every day kept moves you toward the next level.",
    ),
    "fr": dict(
        free="<strong>Gratuite, pour de bon.</strong> Pas d’achat, pas d’abonnement, pas de pub, et pas de limite d’habitudes cachée derrière un paiement.",
        noaccount="<strong>Sans compte ni inscription.</strong> Ouvre l’app et ajoute ta première habitude. Aucun mot de passe à retenir, aucun profil à gérer.",
        private="<strong>Privée d’office.</strong> Pas de serveur, pas de statistiques d’usage : tes habitudes restent sur ton iPhone et dans ton iCloud privé. Nous ne les recevons jamais.",
        quit="<strong>Les mauvaises habitudes ont leur propre logique.</strong> Une habitude à éviter est tenue d’office : tu ne notes que le jour où tu craques. Coutume compte tes jours sans, l’argent économisé et les envies résistées.",
        forgive="<strong>Une séquence qui pardonne.</strong> Un jour manqué par semaine ne brise pas ta séquence : une mauvaise journée n’efface pas des semaines d’effort.",
        levels="<strong>Quelque chose à viser.</strong> Onze niveaux, de Bonne intention à Légende, et dix-huit jalons, gagnés avec chaque journée tenue.",
        health="<strong>Santé note pour toi.</strong> Tes pas, tes minutes d’exercice, ta pleine conscience et ton eau remplissent tes habitudes tout seuls.",
        simple="<strong>Rapide à noter.</strong> Touche un anneau et la journée est notée ; garde le doigt dessus pour entrer un nombre ou annuler.",
        calm="<strong>Du progrès sans jeu à gérer.</strong> Pas d’avatar à équiper, pas d’animal à soigner : chaque journée tenue te rapproche du niveau suivant.",
    ),
    "es": dict(
        free="<strong>Gratis, de verdad.</strong> Sin compra, sin suscripción, sin anuncios y sin límite de hábitos escondido tras un pago.",
        noaccount="<strong>Sin cuenta ni registro.</strong> Abre la app y añade tu primer hábito. Sin contraseña que recordar ni perfil que gestionar.",
        private="<strong>Privada por defecto.</strong> Sin servidor ni estadísticas de uso: tus hábitos se quedan en tu iPhone y en tu iCloud privado. Nunca los recibimos.",
        quit="<strong>Los malos hábitos tienen su propia lógica.</strong> Un hábito por dejar se da por cumplido: solo registras el día que recaes. Coutume cuenta tus días sin, el dinero ahorrado y los impulsos que resististe.",
        forgive="<strong>Una racha que perdona.</strong> Un día perdido por semana no rompe tu racha, así que un mal día no borra semanas de esfuerzo.",
        levels="<strong>Algo a lo que aspirar.</strong> Once niveles, de Buena intención a Leyenda, y dieciocho logros, que se ganan con cada día cumplido.",
        health="<strong>Salud registra por ti.</strong> Los pasos, los minutos de ejercicio, la atención plena y el agua completan tus hábitos solos.",
        simple="<strong>Rápida de registrar.</strong> Toca un anillo y el día queda anotado; mantenlo pulsado para introducir un número o deshacer.",
        calm="<strong>Progreso sin un juego que gestionar.</strong> Sin avatar que equipar ni mascota que cuidar: cada día cumplido te acerca al siguiente nivel.",
    ),
}

# The other picks: (best for, what it is and what it costs).
OTHER = {
    "streaks": dict(
        en=("a polished app across your Apple devices", "A one-time purchase that runs on iPhone, iPad, Apple Watch and Mac, with deep Apple Health support and up to 24 tasks, negative ones included. US$5.99, with no subscription."),
        fr=("une app soignée sur tous tes appareils Apple", "Un achat unique qui fonctionne sur iPhone, iPad, Apple Watch et Mac, avec une intégration poussée à Santé et jusqu’à 24 tâches, négatives comprises. 5,99 $ US, sans abonnement."),
        es=("una app cuidada en todos tus dispositivos Apple", "Una compra única que funciona en iPhone, iPad, Apple Watch y Mac, con una integración profunda con Salud y hasta 24 tareas, incluidas las negativas. 5,99 US$, sin suscripción.")),
    "habitify": dict(
        en=("tracking on iPhone, Android and the web", "Your habits live in an online account and sync everywhere, with detailed statistics. Free for 3 habits; the Plus and Pro plans unlock the rest, and Apple Health is in Pro."),
        fr=("suivre tes habitudes sur iPhone, Android et le web", "Tes habitudes vivent dans un compte en ligne et se synchronisent partout, avec des statistiques détaillées. Gratuite pour 3 habitudes ; les forfaits Plus et Pro débloquent le reste, et Santé fait partie de Pro."),
        es=("seguir tus hábitos en iPhone, Android y la web", "Tus hábitos viven en una cuenta en línea y se sincronizan en todas partes, con estadísticas detalladas. Gratis para 3 hábitos; los planes Plus y Pro desbloquean el resto, y Salud está en Pro.")),
    "habitica": dict(
        en=("people who want a role-playing game", "Your habits and to-dos become a game: an avatar earns experience and gold, and a party of friends keeps you accountable. Free with an account; a subscription adds extras."),
        fr=("ceux qui veulent un jeu de rôle", "Tes habitudes et tes tâches deviennent un jeu : un avatar gagne de l’expérience et de l’or, et une équipe d’amis te tient responsable. Gratuite avec un compte ; un abonnement ajoute des extras."),
        es=("quien quiere un juego de rol", "Tus hábitos y tareas se vuelven un juego: un avatar gana experiencia y oro, y un grupo de amigos te mantiene al día. Gratis con una cuenta; una suscripción añade extras.")),
    "wayoflife": dict(
        en=("a quick yes-or-no diary with strong charts", "Each day you mark a habit green or red, and the charts show the trend over months. Around since 2010, on iPhone, iPad and Android. Free with a habit limit; Premium unlocks the rest."),
        fr=("un journal rapide, oui ou non, avec de bons graphiques", "Chaque jour, tu marques une habitude en vert ou en rouge, et les graphiques montrent la tendance sur des mois. Elle existe depuis 2010, sur iPhone, iPad et Android. Gratuite avec une limite d’habitudes ; Premium débloque le reste."),
        es=("un diario rápido de sí o no con buenos gráficos", "Cada día marcas un hábito en verde o en rojo, y los gráficos muestran la tendencia durante meses. Existe desde 2010, en iPhone, iPad y Android. Gratis con un límite de hábitos; Premium desbloquea el resto.")),
    "productive": dict(
        en=("planning routines by time of day", "Habits are grouped into morning, afternoon and evening, with guided programs and challenges, on iPhone, Apple Watch and Android. Free with a habit limit; unlimited habits need a Premium subscription."),
        fr=("planifier tes routines selon le moment de la journée", "Les habitudes sont regroupées en matin, après-midi et soir, avec des programmes guidés et des défis, sur iPhone, Apple Watch et Android. Gratuite avec une limite d’habitudes ; il faut un abonnement Premium pour en avoir autant que tu veux."),
        es=("planificar rutinas según el momento del día", "Los hábitos se agrupan en mañana, tarde y noche, con programas guiados y retos, en iPhone, Apple Watch y Android. Gratis con un límite de hábitos; los hábitos ilimitados requieren una suscripción Premium.")),
    "strides": dict(
        en=("mixing habits with goals and targets", "Besides habits, it tracks targets by a date, averages and projects, with over 150 templates, Apple Health, a Mac app and a web app. Free for 3 trackers; Strides Plus is a subscription or a lifetime purchase."),
        fr=("combiner habitudes, objectifs et cibles", "En plus des habitudes, elle suit des cibles à atteindre avant une date, des moyennes et des projets, avec plus de 150 modèles, Santé, une app Mac et une app web. Gratuite pour 3 suivis ; Strides Plus est un abonnement ou un achat à vie."),
        es=("combinar hábitos con metas y objetivos", "Además de hábitos, sigue objetivos con fecha, promedios y proyectos, con más de 150 plantillas, Salud, una app para Mac y una app web. Gratis para 3 seguimientos; Strides Plus es una suscripción o una compra de por vida.")),
    "finch": dict(
        en=("gentle self-care with a virtual pet", "You look after a little bird that grows as you finish your self-care goals, with mood check-ins, journaling and breathing exercises. Free, with an optional Finch Plus subscription."),
        fr=("prendre soin de toi en douceur, avec un animal virtuel", "Tu t’occupes d’un petit oiseau qui grandit à mesure que tu atteins tes objectifs de bien-être, avec suivi de l’humeur, journal et exercices de respiration. Gratuite, avec un abonnement Finch Plus optionnel."),
        es=("cuidarte con calma, con una mascota virtual", "Cuidas a un pajarito que crece a medida que cumples tus metas de autocuidado, con registro del ánimo, diario y ejercicios de respiración. Gratis, con una suscripción Finch Plus opcional.")),
    "habitkit": dict(
        en=("a private grid of your habits", "No account, your data on your device, and a tile grid that fills in like a contribution graph. Free for 4 habits; Pro is monthly, yearly or lifetime."),
        fr=("une grille privée de tes habitudes", "Pas de compte, tes données sur ton appareil, et une grille de cases qui se remplit jour après jour. Gratuite pour 4 habitudes ; Pro au mois, à l’année ou à vie."),
        es=("una cuadrícula privada de tus hábitos", "Sin cuenta, tus datos en tu dispositivo y una cuadrícula de casillas que se llena día a día. Gratis para 4 hábitos; Pro mensual, anual o de por vida.")),
    "atoms": dict(
        en=("readers of Atomic Habits", "James Clear’s app helps you start small and tie each habit to a time and place, with short daily lessons. Atoms Pro costs US$4.99 a month or US$39.99 a year."),
        fr=("les lecteurs d’Atomic Habits", "L’app de James Clear t’aide à commencer petit et à lier chaque habitude à un moment et à un lieu, avec de courtes leçons quotidiennes. Atoms Pro coûte 4,99 $ US par mois ou 39,99 $ US par année."),
        es=("quienes leyeron Hábitos atómicos", "La app de James Clear te ayuda a empezar poco a poco y a unir cada hábito a un momento y un lugar, con lecciones diarias breves. Atoms Pro cuesta 4,99 US$ al mes o 39,99 US$ al año.")),
    "fabulous": dict(
        en=("guided morning routines and coaching", "Coaching journeys build a routine step by step, alongside journaling, meditation and workouts. Free to start; most of it is in a Premium subscription."),
        fr=("des routines du matin guidées et du coaching", "Des parcours de coaching bâtissent une routine étape par étape, avec journal, méditation et entraînements. Gratuite pour commencer ; l’essentiel est dans un abonnement Premium."),
        es=("rutinas de mañana guiadas y coaching", "Recorridos de coaching construyen una rutina paso a paso, junto con diario, meditación y entrenamientos. Gratis para empezar; casi todo está en una suscripción Premium.")),
}

# One page per competitor. "col": the competitor's column, in the order of L[lang]["rows"]. "others": the three other picks.
ALTS = [
dict(key="streaks", why=["free", "quit", "forgive", "levels", "private"], others=["wayoflife", "habitkit", "strides"],
  col=dict(
    en=["One-time purchase, US$5.99", "No", "Yes, as negative tasks", "Yes, reads and writes", "Streaks", "iPhone, iPad, Apple Watch, Mac, Vision Pro"],
    fr=["Achat unique, 5,99 $ US", "Non", "Oui, en tâches négatives", "Oui, en lecture et en écriture", "Les séquences", "iPhone, iPad, Apple Watch, Mac, Vision Pro"],
    es=["Compra única, 5,99 US$", "No", "Sí, como tareas negativas", "Sí, lectura y escritura", "Las rachas", "iPhone, iPad, Apple Watch, Mac, Vision Pro"]),
  en=dict(t="the paid habit tracker for Apple devices",
    desc="The best Streaks alternatives for iPhone in 2026: Coutume is free, tracks habits to quit, reads Apple Health and forgives a missed day. Plus three more picks.",
    lede="Streaks is a polished one-time purchase. If you’d rather pay nothing, count bad habits in days without, or keep a streak that forgives an off day, here are the best alternatives, starting with Coutume.",
    pitch="Coutume keeps what people like about Streaks, one tap to log, Apple Health and streaks, and adds habits to quit counted in days without, levels and milestones. Free, with no account, no ads and no subscription.",
    better="Streaks has been around for years and runs on more devices. You may prefer it if you want to log from your Apple Watch, iPad or Mac, if you need habits due only on some days of the week, or if you already own it and it works for you."),
  fr=dict(t="l’app d’habitudes payante pour appareils Apple",
    desc="Les meilleures alternatives à Streaks sur iPhone en 2026 : Coutume est gratuite, suit les habitudes à éviter, lit Santé et pardonne un jour manqué.",
    lede="Streaks est un achat unique soigné. Si tu préfères ne rien payer, compter tes mauvaises habitudes en jours sans, ou garder une séquence qui pardonne une mauvaise journée, voici les meilleures alternatives, à commencer par Coutume.",
    pitch="Coutume garde ce qu’on aime de Streaks, un toucher pour noter, Santé et les séquences, et y ajoute les habitudes à éviter comptées en jours sans, des niveaux et des jalons. Gratuite, sans compte, sans pub et sans abonnement.",
    better="Streaks existe depuis des années et fonctionne sur plus d’appareils. Tu la préféreras peut-être si tu veux noter depuis ton Apple Watch, ton iPad ou ton Mac, si certaines habitudes ne reviennent que certains jours de la semaine, ou si tu l’as déjà achetée et qu’elle te va."),
  es=dict(t="la app de hábitos de pago para dispositivos Apple",
    desc="Las mejores alternativas a Streaks para iPhone en 2026: Coutume es gratis, sigue hábitos por dejar, lee Salud y perdona un día perdido. Y tres opciones más.",
    lede="Streaks es una compra única muy cuidada. Si prefieres no pagar nada, contar tus malos hábitos en días sin o tener una racha que perdona un mal día, estas son las mejores alternativas, empezando por Coutume.",
    pitch="Coutume conserva lo que gusta de Streaks, un toque para registrar, Salud y las rachas, y añade hábitos por dejar contados en días sin, niveles y logros. Gratis, sin cuenta, sin anuncios y sin suscripción.",
    better="Streaks existe desde hace años y funciona en más dispositivos. Quizá la prefieras si quieres registrar desde tu Apple Watch, iPad o Mac, si necesitas hábitos que solo tocan algunos días de la semana, o si ya la compraste y te funciona.")),

dict(key="habitify", why=["free", "noaccount", "private", "quit", "forgive"], others=["streaks", "wayoflife", "strides"],
  col=dict(
    en=["Free for 3 habits; Plus US$29.99/year; Pro from US$8.99/month, US$49.99/year or lifetime", "Optional, suggested at setup", "Yes, habits to break", "Pro plan only", "Challenges, streaks", "iOS, Android, Mac, web"],
    fr=["Gratuite pour 3 habitudes ; Plus 29,99 $ US/an ; Pro dès 8,99 $ US/mois, 49,99 $ US/an ou à vie", "Facultatif, proposé au départ", "Oui, des habitudes à briser", "Forfait Pro seulement", "Défis, séquences", "iOS, Android, Mac, web"],
    es=["Gratis para 3 hábitos; Plus 29,99 US$/año; Pro desde 8,99 US$/mes, 49,99 US$/año o de por vida", "Opcional, se sugiere al empezar", "Sí, hábitos por romper", "Solo en el plan Pro", "Retos, rachas", "iOS, Android, Mac, web"]),
  en=dict(t="the habit tracker with free and paid plans",
    desc="The best Habitify alternatives in 2026: Coutume is a free iPhone habit tracker with no habit limit, no account and no subscription. Plus three more picks.",
    lede="Habitify’s free plan stops at three habits, and Apple Health is part of its Pro plan. If you want every habit for free, without an account, here are the best alternatives, starting with Coutume.",
    pitch="Coutume is a free habit tracker for iPhone. No account to create, no plan to choose and no subscription: your habits stay on your iPhone and in your private iCloud.",
    better="Habitify works on Android, Mac and the web, and keeps your habits in an online account. You may prefer it if you switch between an iPhone and an Android phone or a computer, or if you want the detailed reports of its paid plans."),
  fr=dict(t="l’app d’habitudes aux forfaits gratuit et payants",
    desc="Les meilleures alternatives à Habitify en 2026 : Coutume suit tes habitudes sur iPhone gratuitement, sans limite, sans compte ni abonnement.",
    lede="Le forfait gratuit de Habitify s’arrête à trois habitudes, et Santé fait partie de son forfait Pro. Si tu veux toutes tes habitudes gratuitement, sans compte, voici les meilleures alternatives, à commencer par Coutume.",
    pitch="Coutume suit tes habitudes sur iPhone, gratuitement. Pas de compte à créer, pas de forfait à choisir, pas d’abonnement : tes habitudes restent sur ton iPhone et dans ton iCloud privé.",
    better="Habitify fonctionne sur Android, Mac et le web, et garde tes habitudes dans un compte en ligne. Tu la préféreras peut-être si tu passes d’un iPhone à un téléphone Android ou à un ordinateur, ou si tu veux les rapports détaillés de ses forfaits payants."),
  es=dict(t="la app de hábitos con planes gratis y de pago",
    desc="Las mejores alternativas a Habitify en 2026: Coutume es una app de hábitos gratis para iPhone, sin límite de hábitos, sin cuenta y sin suscripción.",
    lede="El plan gratis de Habitify se queda en tres hábitos, y Salud forma parte de su plan Pro. Si quieres todos tus hábitos gratis y sin cuenta, estas son las mejores alternativas, empezando por Coutume.",
    pitch="Coutume es una app de hábitos gratis para iPhone. Sin cuenta que crear, sin plan que elegir y sin suscripción: tus hábitos se quedan en tu iPhone y en tu iCloud privado.",
    better="Habitify funciona en Android, Mac y la web, y guarda tus hábitos en una cuenta en línea. Quizá la prefieras si alternas entre un iPhone y un teléfono Android o un ordenador, o si quieres los informes detallados de sus planes de pago.")),

dict(key="habitica", why=["calm", "forgive", "simple", "health", "noaccount"], others=["finch", "productive", "streaks"],
  col=dict(
    en=["Free; optional subscription and gems", "Yes", "Negative habits cost your avatar health", "—", "Avatar, experience, gold, gear, pets, quests", "iOS, Android, web"],
    fr=["Gratuite ; abonnement et gemmes en option", "Oui", "Les habitudes négatives coûtent de la vie à ton avatar", "—", "Avatar, expérience, or, équipement, animaux, quêtes", "iOS, Android, web"],
    es=["Gratis; suscripción y gemas opcionales", "Sí", "Los hábitos negativos le quitan vida a tu avatar", "—", "Avatar, experiencia, oro, equipo, mascotas, misiones", "iOS, Android, web"]),
  en=dict(t="the habit tracker played as a role-playing game",
    desc="The best Habitica alternatives in 2026: Coutume keeps the levels and drops the avatar, the gold and the account. A free, quiet habit tracker for iPhone.",
    lede="Habitica turns your habits into a role-playing game. If the avatar, the gold and the party have become one more thing to manage, here are the best alternatives, starting with Coutume.",
    pitch="Coutume keeps the reward of levelling up, and drops the avatar, the gold and the account: a free habit tracker for iPhone, quiet and private.",
    better="Habitica shines if the game is what keeps you going: if you enjoy an avatar to dress, quests to finish and friends counting on you in a party. It also works on Android and the web, and mixes habits with to-dos."),
  fr=dict(t="l’app d’habitudes en forme de jeu de rôle",
    desc="Les meilleures alternatives à Habitica en 2026 : Coutume garde les niveaux et laisse tomber l’avatar, l’or et le compte. Gratuite et calme, sur iPhone.",
    lede="Habitica transforme tes habitudes en jeu de rôle. Si l’avatar, l’or et l’équipe sont devenus une chose de plus à gérer, voici les meilleures alternatives, à commencer par Coutume.",
    pitch="Coutume garde le plaisir de monter de niveau, et laisse tomber l’avatar, l’or et le compte : une app d’habitudes gratuite pour iPhone, calme et privée.",
    better="Habitica brille si c’est le jeu qui te motive : si tu aimes habiller un avatar, finir des quêtes et savoir que des amis comptent sur toi dans ton équipe. Elle fonctionne aussi sur Android et le web, et mêle habitudes et tâches."),
  es=dict(t="la app de hábitos en forma de juego de rol",
    desc="Las mejores alternativas a Habitica en 2026: Coutume conserva los niveles y deja el avatar, el oro y la cuenta. Una app de hábitos gratis y tranquila para iPhone.",
    lede="Habitica convierte tus hábitos en un juego de rol. Si el avatar, el oro y el grupo se han vuelto una cosa más que gestionar, estas son las mejores alternativas, empezando por Coutume.",
    pitch="Coutume conserva el gusto de subir de nivel y deja el avatar, el oro y la cuenta: una app de hábitos gratis para iPhone, tranquila y privada.",
    better="Habitica brilla si el juego es lo que te motiva: si te gusta vestir a un avatar, terminar misiones y saber que tus amigos cuentan contigo en el grupo. También funciona en Android y en la web, y mezcla hábitos con tareas.")),

dict(key="wayoflife", why=["free", "health", "quit", "forgive", "levels"], others=["streaks", "habitkit", "habitify"],
  col=dict(
    en=["Free with a habit limit; Premium unlocks unlimited habits", "—", "Yes, days marked green or red", "—", "Chains, scoreboard", "iPhone, iPad, Android"],
    fr=["Gratuite avec une limite d’habitudes ; Premium les débloque toutes", "—", "Oui, des jours marqués en vert ou en rouge", "—", "Chaînes, tableau des scores", "iPhone, iPad, Android"],
    es=["Gratis con un límite de hábitos; Premium los desbloquea todos", "—", "Sí, días marcados en verde o rojo", "—", "Cadenas, marcador", "iPhone, iPad, Android"]),
  en=dict(t="the green-and-red habit diary",
    desc="The best Way of Life alternatives in 2026: Coutume is free with every habit, fills in steps and water from Apple Health, and forgives a missed day.",
    lede="Way of Life is a fast green-or-red diary with good charts, but its free version limits your habits and you log everything yourself. Here are the best alternatives, starting with Coutume.",
    pitch="Coutume logs a habit in one tap too, and lets Apple Health fill in your steps, exercise, mindful minutes and water. Every habit is free, and levels and milestones reward each day kept.",
    better="Way of Life has been around since 2010, runs on iPad and Android, and its charts and exports (CSV, Excel, JSON) go further. You may prefer it if you want to study trends over years, export your data or log from an Android phone."),
  fr=dict(t="le journal d’habitudes en vert et en rouge",
    desc="Les meilleures alternatives à Way of Life en 2026 : Coutume est gratuite pour toutes tes habitudes, se remplit avec Santé et pardonne un jour manqué.",
    lede="Way of Life est un journal rapide, en vert ou en rouge, avec de bons graphiques, mais sa version gratuite limite tes habitudes et tu notes tout toi-même. Voici les meilleures alternatives, à commencer par Coutume.",
    pitch="Coutume note une habitude d’un toucher, elle aussi, et laisse Santé remplir tes pas, ton exercice, ta pleine conscience et ton eau. Toutes tes habitudes sont gratuites, et des niveaux et des jalons récompensent chaque journée tenue.",
    better="Way of Life existe depuis 2010, fonctionne sur iPad et Android, et ses graphiques et exportations (CSV, Excel, JSON) vont plus loin. Tu la préféreras peut-être si tu veux étudier tes tendances sur des années, exporter tes données ou noter depuis un téléphone Android."),
  es=dict(t="el diario de hábitos en verde y rojo",
    desc="Las mejores alternativas a Way of Life en 2026: Coutume es gratis para todos tus hábitos, completa pasos y agua con Salud y perdona un día perdido.",
    lede="Way of Life es un diario rápido en verde o rojo con buenos gráficos, pero su versión gratis limita tus hábitos y lo registras todo a mano. Estas son las mejores alternativas, empezando por Coutume.",
    pitch="Coutume también registra un hábito con un toque, y deja que Salud complete tus pasos, tu ejercicio, tu atención plena y tu agua. Todos los hábitos son gratis, y niveles y logros premian cada día cumplido.",
    better="Way of Life existe desde 2010, funciona en iPad y Android, y sus gráficos y exportaciones (CSV, Excel, JSON) llegan más lejos. Quizá la prefieras si quieres estudiar tendencias durante años, exportar tus datos o registrar desde un teléfono Android.")),

dict(key="productive", why=["free", "noaccount", "health", "quit", "forgive"], others=["streaks", "habitify", "atoms"],
  col=dict(
    en=["Free with a habit limit; Premium subscription (US$10.99/month)", "—", "No dedicated mode", "—", "Streaks, perfect days, challenges", "iPhone, iPad, Apple Watch, Android"],
    fr=["Gratuite avec une limite d’habitudes ; abonnement Premium (10,99 $ US/mois)", "—", "Pas de mode dédié", "—", "Séquences, journées parfaites, défis", "iPhone, iPad, Apple Watch, Android"],
    es=["Gratis con un límite de hábitos; suscripción Premium (10,99 US$/mes)", "—", "Sin modo dedicado", "—", "Rachas, días perfectos, retos", "iPhone, iPad, Apple Watch, Android"]),
  en=dict(t="the routine planner with a subscription",
    desc="The best Productive alternatives in 2026: Coutume tracks every habit for free on iPhone, with Apple Health, habits to quit, and no subscription or account.",
    lede="Productive plans your habits by time of day, but unlimited habits need its Premium subscription. If you want a simpler tracker that costs nothing, here are the best alternatives, starting with Coutume.",
    pitch="Coutume is a free habit tracker for iPhone: every habit, levels, milestones, widgets and Apple Health, with no subscription, no account and no ads.",
    better="Productive groups habits into morning, afternoon and evening, offers guided programs and challenges, and runs on Apple Watch and Android. You may prefer it if you plan your day around routines or want to log from your wrist."),
  fr=dict(t="le planificateur de routines avec abonnement",
    desc="Les meilleures alternatives à Productive en 2026 : Coutume suit toutes tes habitudes gratuitement sur iPhone, avec Santé, sans abonnement ni compte.",
    lede="Productive planifie tes habitudes selon le moment de la journée, mais il faut son abonnement Premium pour en avoir autant que tu veux. Si tu cherches plus simple et gratuit, voici les meilleures alternatives, à commencer par Coutume.",
    pitch="Coutume suit tes habitudes sur iPhone, gratuitement : toutes tes habitudes, les niveaux, les jalons, les widgets et Santé, sans abonnement, sans compte et sans pub.",
    better="Productive regroupe les habitudes en matin, après-midi et soir, propose des programmes guidés et des défis, et fonctionne sur Apple Watch et Android. Tu la préféreras peut-être si tu organises ta journée en routines ou si tu veux noter depuis ton poignet."),
  es=dict(t="el planificador de rutinas con suscripción",
    desc="Las mejores alternativas a Productive en 2026: Coutume sigue todos tus hábitos gratis en iPhone, con Salud, hábitos por dejar y sin suscripción ni cuenta.",
    lede="Productive organiza tus hábitos según el momento del día, pero los hábitos ilimitados requieren su suscripción Premium. Si buscas algo más simple y gratis, estas son las mejores alternativas, empezando por Coutume.",
    pitch="Coutume es una app de hábitos gratis para iPhone: todos los hábitos, niveles, logros, widgets y Salud, sin suscripción, sin cuenta y sin anuncios.",
    better="Productive agrupa los hábitos en mañana, tarde y noche, ofrece programas guiados y retos, y funciona en Apple Watch y Android. Quizá la prefieras si organizas tu día en rutinas o quieres registrar desde la muñeca.")),

dict(key="strides", why=["free", "noaccount", "quit", "levels", "private"], others=["streaks", "habitify", "wayoflife"],
  col=dict(
    en=["Free for 3 trackers; Strides Plus subscription or lifetime", "Needed to sync", "Yes, bad-habit trackers with a limit", "Yes", "Streaks, success rate", "iPhone, iPad, Apple Watch, Mac, web"],
    fr=["Gratuite pour 3 suivis ; Strides Plus en abonnement ou à vie", "Nécessaire pour synchroniser", "Oui, des suivis de mauvaises habitudes avec une limite", "Oui", "Séquences, taux de réussite", "iPhone, iPad, Apple Watch, Mac, web"],
    es=["Gratis para 3 seguimientos; Strides Plus por suscripción o de por vida", "Necesaria para sincronizar", "Sí, seguimientos de malos hábitos con un límite", "Sí", "Rachas, tasa de éxito", "iPhone, iPad, Apple Watch, Mac, web"]),
  en=dict(t="the habit and goal tracker",
    desc="The best Strides alternatives in 2026: Coutume is a free iPhone habit tracker with no tracker limit, no account, habits to quit, levels and Apple Health.",
    lede="Strides tracks habits and goals side by side, but its free version stops at three trackers. If daily habits are what you need, here are the best alternatives, starting with Coutume.",
    pitch="Coutume focuses on daily habits, and gives you all of them for free: habits to build, habits to quit, Apple Health, forgiving streaks, levels and widgets, without an account.",
    better="Strides goes beyond habits: targets by a date, averages and projects, with a Mac app, a web app and Apple Watch. You may prefer it if you track goals like savings or weight alongside your habits, or if you work from a computer."),
  fr=dict(t="l’app d’habitudes et d’objectifs",
    desc="Les meilleures alternatives à Strides en 2026 : Coutume suit tes habitudes sur iPhone gratuitement, sans limite ni compte, avec Santé et des niveaux.",
    lede="Strides suit habitudes et objectifs côte à côte, mais sa version gratuite s’arrête à trois suivis. Si ce sont tes habitudes quotidiennes qui comptent, voici les meilleures alternatives, à commencer par Coutume.",
    pitch="Coutume se concentre sur les habitudes quotidiennes, et te les offre toutes gratuitement : habitudes à prendre et à éviter, Santé, séquences indulgentes, niveaux et widgets, sans compte.",
    better="Strides va au-delà des habitudes : des cibles à atteindre avant une date, des moyennes et des projets, avec une app Mac, une app web et l’Apple Watch. Tu la préféreras peut-être si tu suis des objectifs comme ton épargne ou ton poids en plus de tes habitudes, ou si tu travailles à l’ordinateur."),
  es=dict(t="la app de hábitos y metas",
    desc="Las mejores alternativas a Strides en 2026: Coutume es una app de hábitos gratis para iPhone, sin límite ni cuenta, con hábitos por dejar, niveles y Salud.",
    lede="Strides sigue hábitos y metas a la vez, pero su versión gratis se queda en tres seguimientos. Si lo que necesitas son hábitos diarios, estas son las mejores alternativas, empezando por Coutume.",
    pitch="Coutume se centra en los hábitos diarios y te los da todos gratis: hábitos por crear y por dejar, Salud, rachas que perdonan, niveles y widgets, sin cuenta.",
    better="Strides va más allá de los hábitos: objetivos con fecha, promedios y proyectos, con app para Mac, app web y Apple Watch. Quizá la prefieras si sigues metas como el ahorro o el peso junto a tus hábitos, o si trabajas desde un ordenador.")),

dict(key="finch", why=["calm", "quit", "health", "private", "free"], others=["habitica", "fabulous", "streaks"],
  col=dict(
    en=["Free; optional Finch Plus subscription", "Optional", "Not its focus", "—", "A virtual pet that grows, outfits, adventures", "iPhone, iPad, Android"],
    fr=["Gratuite ; abonnement Finch Plus optionnel", "Facultatif", "Ce n’est pas son but", "—", "Un animal virtuel qui grandit, des tenues, des aventures", "iPhone, iPad, Android"],
    es=["Gratis; suscripción Finch Plus opcional", "Opcional", "No es su enfoque", "—", "Una mascota virtual que crece, ropa, aventuras", "iPhone, iPad, Android"]),
  en=dict(t="the self-care app with a virtual pet",
    desc="The best Finch alternatives in 2026: Coutume is a calm, free habit tracker for iPhone, with levels instead of a pet, habits to quit and Apple Health.",
    lede="Finch wraps self-care around a little bird to look after. If you’d rather track your habits plainly, without a pet to dress or adventures to follow, here are the best alternatives, starting with Coutume.",
    pitch="Coutume keeps the warmth of small rewards, levels and milestones earned with every day kept, and leaves out the pet. It’s a habit tracker for iPhone, free, with no account.",
    better="Finch is gentler than a habit tracker: mood check-ins, journaling, breathing exercises and a pet that keeps you company, with friends who can cheer you on. You may prefer it if self-care and your mood matter more to you than counting habits."),
  fr=dict(t="l’app de bien-être avec un animal virtuel",
    desc="Les meilleures alternatives à Finch en 2026 : Coutume suit tes habitudes sur iPhone, calme et gratuite, avec des niveaux plutôt qu’un animal, et Santé.",
    lede="Finch enveloppe le bien-être autour d’un petit oiseau à soigner. Si tu préfères suivre tes habitudes simplement, sans animal à habiller ni aventures à suivre, voici les meilleures alternatives, à commencer par Coutume.",
    pitch="Coutume garde la douceur des petites récompenses, des niveaux et des jalons gagnés avec chaque journée tenue, et laisse de côté l’animal. C’est une app d’habitudes pour iPhone, gratuite et sans compte.",
    better="Finch est plus douce qu’une app d’habitudes : suivi de l’humeur, journal, exercices de respiration et un animal qui te tient compagnie, avec des amis qui peuvent t’encourager. Tu la préféreras peut-être si ton bien-être et ton humeur comptent plus pour toi que le suivi de tes habitudes."),
  es=dict(t="la app de autocuidado con una mascota virtual",
    desc="Las mejores alternativas a Finch en 2026: Coutume es una app de hábitos tranquila y gratis para iPhone, con niveles en vez de mascota, hábitos por dejar y Salud.",
    lede="Finch envuelve el autocuidado en un pajarito que cuidar. Si prefieres seguir tus hábitos sin más, sin mascota que vestir ni aventuras que seguir, estas son las mejores alternativas, empezando por Coutume.",
    pitch="Coutume conserva la calidez de las pequeñas recompensas, niveles y logros ganados con cada día cumplido, y deja fuera la mascota. Es una app de hábitos para iPhone, gratis y sin cuenta.",
    better="Finch es más suave que una app de hábitos: registro del ánimo, diario, ejercicios de respiración y una mascota que te acompaña, con amigos que pueden animarte. Quizá la prefieras si tu autocuidado y tu ánimo te importan más que contar hábitos.")),

dict(key="habitkit", why=["free", "health", "forgive", "levels"], others=["streaks", "wayoflife", "habitify"],
  col=dict(
    en=["Free for 4 habits; Pro monthly, yearly or lifetime", "No", "Yes, clean days until a slip", "—", "Streaks, a tile grid", "iPhone, Android"],
    fr=["Gratuite pour 4 habitudes ; Pro au mois, à l’année ou à vie", "Non", "Oui, des jours sans jusqu’au faux pas", "—", "Séquences, une grille de cases", "iPhone, Android"],
    es=["Gratis para 4 hábitos; Pro mensual, anual o de por vida", "No", "Sí, días limpios hasta una recaída", "—", "Rachas, una cuadrícula de casillas", "iPhone, Android"]),
  en=dict(t="the habit grid with a Pro upgrade",
    desc="The best HabitKit alternatives in 2026: Coutume is free with every habit, reads Apple Health, forgives a missed day and rewards you with levels.",
    lede="HabitKit is private and simple, and Coutume shares that spirit. But HabitKit’s free version stops at four habits, and Apple Health isn’t among its features. Here are the best alternatives, starting with Coutume.",
    pitch="Like HabitKit, Coutume works without an account and keeps your habits on your iPhone. It adds Apple Health, levels, milestones and a streak that forgives, and every habit is free.",
    better="HabitKit runs on Android too, and its tile grid shows months of habits at a glance. You may prefer it if you switch between an iPhone and an Android phone, or if that grid is what keeps you going."),
  fr=dict(t="la grille d’habitudes avec une version Pro",
    desc="Les meilleures alternatives à HabitKit en 2026 : Coutume est gratuite pour toutes tes habitudes, lit Santé, pardonne un jour manqué et a des niveaux.",
    lede="HabitKit est privée et simple, et Coutume partage cet esprit. Mais la version gratuite de HabitKit s’arrête à quatre habitudes, et Santé ne fait pas partie de ses fonctions. Voici les meilleures alternatives, à commencer par Coutume.",
    pitch="Comme HabitKit, Coutume fonctionne sans compte et garde tes habitudes sur ton iPhone. Elle y ajoute Santé, des niveaux, des jalons et une séquence qui pardonne, et toutes tes habitudes sont gratuites.",
    better="HabitKit fonctionne aussi sur Android, et sa grille montre des mois d’habitudes d’un coup d’œil. Tu la préféreras peut-être si tu passes d’un iPhone à un téléphone Android, ou si c’est cette grille qui te motive."),
  es=dict(t="la cuadrícula de hábitos con versión Pro",
    desc="Las mejores alternativas a HabitKit en 2026: Coutume es gratis para todos tus hábitos, lee Salud, perdona un día perdido y te premia con niveles.",
    lede="HabitKit es privada y sencilla, y Coutume comparte ese espíritu. Pero la versión gratis de HabitKit se queda en cuatro hábitos, y Salud no está entre sus funciones. Estas son las mejores alternativas, empezando por Coutume.",
    pitch="Como HabitKit, Coutume funciona sin cuenta y guarda tus hábitos en tu iPhone. Añade Salud, niveles, logros y una racha que perdona, y todos los hábitos son gratis.",
    better="HabitKit también funciona en Android, y su cuadrícula muestra meses de hábitos de un vistazo. Quizá la prefieras si alternas entre un iPhone y un teléfono Android, o si esa cuadrícula es lo que te motiva.")),

dict(key="atoms", why=["free", "quit", "health", "forgive", "levels"], others=["streaks", "productive", "habitkit"],
  col=dict(
    en=["Free with limits; Atoms Pro US$4.99/month or US$39.99/year", "—", "No dedicated counter", "—", "Milestones", "iPhone, iPad, Apple Watch, Android"],
    fr=["Gratuite avec des limites ; Atoms Pro 4,99 $ US/mois ou 39,99 $ US/an", "—", "Pas de compteur dédié", "—", "Jalons", "iPhone, iPad, Apple Watch, Android"],
    es=["Gratis con límites; Atoms Pro 4,99 US$/mes o 39,99 US$/año", "—", "Sin contador dedicado", "—", "Hitos", "iPhone, iPad, Apple Watch, Android"]),
  en=dict(t="the app from Atomic Habits",
    desc="The best Atoms alternatives in 2026: Coutume is a free habit tracker for iPhone, with habits to quit, Apple Health, forgiving streaks and levels.",
    lede="Atoms brings James Clear’s method to your phone, with lessons and a Pro subscription. If you already know the method and just want to track, here are the best alternatives, starting with Coutume.",
    pitch="Coutume is built on the same idea of small daily steps: make it easy, and count every day. It’s free, with no subscription and no account, and it counts the habits you quit, too.",
    better="Atoms teaches as it tracks: daily lessons from Atomic Habits and a guided way to shape each habit around who you want to become. It also runs on Apple Watch and Android. You may prefer it if you want the method explained along the way."),
  fr=dict(t="l’app d’Atomic Habits",
    desc="Les meilleures alternatives à Atoms en 2026 : Coutume suit tes habitudes sur iPhone gratuitement, avec habitudes à éviter, Santé, séquences et niveaux.",
    lede="Atoms met la méthode de James Clear dans ton téléphone, avec des leçons et un abonnement Pro. Si tu connais déjà la méthode et veux simplement suivre tes habitudes, voici les meilleures alternatives, à commencer par Coutume.",
    pitch="Coutume repose sur la même idée de petits pas quotidiens : rends-la facile, et compte chaque journée. Elle est gratuite, sans abonnement ni compte, et elle compte aussi les habitudes que tu laisses tomber.",
    better="Atoms enseigne en même temps qu’elle suit : des leçons quotidiennes tirées d’Atomic Habits et une façon guidée de bâtir chaque habitude autour de la personne que tu veux devenir. Elle fonctionne aussi sur Apple Watch et Android. Tu la préféreras peut-être si tu veux qu’on t’explique la méthode en chemin."),
  es=dict(t="la app de Hábitos atómicos",
    desc="Las mejores alternativas a Atoms en 2026: Coutume es una app de hábitos gratis para iPhone, con hábitos por dejar, Salud, rachas que perdonan y niveles.",
    lede="Atoms lleva el método de James Clear a tu teléfono, con lecciones y una suscripción Pro. Si ya conoces el método y solo quieres registrar, estas son las mejores alternativas, empezando por Coutume.",
    pitch="Coutume parte de la misma idea de pequeños pasos diarios: hazlo fácil y cuenta cada día. Es gratis, sin suscripción ni cuenta, y también cuenta los hábitos que dejas.",
    better="Atoms enseña mientras registra: lecciones diarias de Hábitos atómicos y una forma guiada de construir cada hábito en torno a la persona que quieres ser. También funciona en Apple Watch y Android. Quizá la prefieras si quieres que te expliquen el método por el camino.")),

dict(key="fabulous", why=["free", "private", "simple", "quit", "health"], others=["productive", "finch", "atoms"],
  col=dict(
    en=["Free to start; Premium subscription (US$49.99/year among its offers)", "—", "Not its focus", "—", "Guided journeys, challenges", "iPhone, iPad, Apple Watch, Android"],
    fr=["Gratuite pour commencer ; abonnement Premium (49,99 $ US/an parmi ses offres)", "—", "Ce n’est pas son but", "—", "Parcours guidés, défis", "iPhone, iPad, Apple Watch, Android"],
    es=["Gratis para empezar; suscripción Premium (49,99 US$/año entre sus ofertas)", "—", "No es su enfoque", "—", "Recorridos guiados, retos", "iPhone, iPad, Apple Watch, Android"]),
  en=dict(t="the coaching and routine app",
    desc="The best Fabulous alternatives in 2026: Coutume is a free, private habit tracker for iPhone, with no subscription, no account and no tracking.",
    lede="Fabulous coaches you through routines, but much of it sits behind a subscription. If you want to track your habits simply, for free and privately, here are the best alternatives, starting with Coutume.",
    pitch="Coutume doesn’t coach you: it keeps count. Tap a ring, let Apple Health fill in the rest, and watch your days add up to levels and milestones. Free, with no account and no subscription.",
    better="Fabulous is a coaching app as much as a tracker: guided journeys, morning routines, meditation, workouts and coaching sessions. You may prefer it if you want to be guided on what to do next."),
  fr=dict(t="l’app de coaching et de routines",
    desc="Les meilleures alternatives à Fabulous en 2026 : Coutume suit tes habitudes sur iPhone, gratuite et privée, sans abonnement, sans compte ni pistage.",
    lede="Fabulous te guide dans tes routines, mais une bonne partie est derrière un abonnement. Si tu veux suivre tes habitudes simplement, gratuitement et en privé, voici les meilleures alternatives, à commencer par Coutume.",
    pitch="Coutume ne te coache pas : elle tient le compte. Touche un anneau, laisse Santé remplir le reste, et regarde tes journées s’additionner en niveaux et en jalons. Gratuite, sans compte et sans abonnement.",
    better="Fabulous est une app de coaching autant qu’une app d’habitudes : parcours guidés, routines du matin, méditation, entraînements et séances de coaching. Tu la préféreras peut-être si tu veux qu’on te guide vers la prochaine chose à faire."),
  es=dict(t="la app de coaching y rutinas",
    desc="Las mejores alternativas a Fabulous en 2026: Coutume es una app de hábitos gratis y privada para iPhone, sin suscripción, sin cuenta y sin rastreo.",
    lede="Fabulous te guía en tus rutinas, pero buena parte está tras una suscripción. Si quieres seguir tus hábitos de forma sencilla, gratis y en privado, estas son las mejores alternativas, empezando por Coutume.",
    pitch="Coutume no te entrena: lleva la cuenta. Toca un anillo, deja que Salud complete el resto y mira cómo tus días se suman en niveles y logros. Gratis, sin cuenta y sin suscripción.",
    better="Fabulous es tanto una app de coaching como de hábitos: recorridos guiados, rutinas de mañana, meditación, entrenamientos y sesiones de coaching. Quizá la prefieras si quieres que te guíen en lo siguiente que hacer.")),
]


def slug(key, lang):
    return {"en": f"{SLUG[key]}-alternative", "fr": f"alternative-{SLUG[key]}", "es": f"alternativa-{SLUG[key]}"}[lang]


def body(a, lang):
    t, c, n = L[lang], a[lang], NAMES[a["key"]]
    rows = "\n".join(f'            <tr><th scope="row">{r}</th><td>{x}</td><td>{y}</td></tr>'
                     for r, x, y in zip(t["rows"], t["coutume"], a["col"][lang]))
    why = "\n".join(f"        <li>{WHY[lang][k]}</li>" for k in a["why"])
    others = "".join(f'''
      <h2>{i}. {NAMES[k]}</h2>
      <p><strong>{t["best"]} {OTHER[k][lang][0]}.</strong> {OTHER[k][lang][1]}</p>
''' for i, k in enumerate(a["others"], 2))
    return f'''
      <h2>{t["first"].format(n=n)}</h2>
      <p>{c["pitch"]}</p>
      <h3>{t["glance"].format(n=n)}</h3>
      <div class="table-scroll">
        <table class="compare">
          <thead>
            <tr><th scope="col"><span class="sr-only">{t["feature"]}</span></th><th scope="col">Coutume</th><th scope="col">{n}</th></tr>
          </thead>
          <tbody>
{rows}
          </tbody>
        </table>
      </div>
      <p class="note">{t["note"].format(n=n)}</p>
      <h3>{t["why"]}</h3>
      <ul>
{why}
      </ul>
{others}
      <h2>{t["better"].format(n=n)}</h2>
      <p>{c["better"]}</p>

      <h2>{t["moving"].format(n=n)}</h2>
      <p>{t["move"].format(n=n)}</p>
'''


def page_text(a, lang):
    t, c, n = L[lang], a[lang], NAMES[a["key"]]
    return dict(title=t["title"].format(n=n), desc=c["desc"], crumb=t["crumb"].format(n=n),
                guide=t["guide"].format(n=n, t=c["t"]), h1=t["h1"].format(n=n), lede=c["lede"], body=body(a, lang))


# In the shapes content.py (PAGES) and guides_es.py (ES) use.
ALT_PAGES = [dict(key=a["key"], layout="plain", en_slug=slug(a["key"], "en"), fr_slug=slug(a["key"], "fr"),
                  en=page_text(a, "en"), fr=page_text(a, "fr")) for a in ALTS]
ALT_ES = {a["key"]: dict(slug=slug(a["key"], "es"), **page_text(a, "es")) for a in ALTS}
# Each page ends with its three other picks' pages and the free habit tracker guide.
ALT_RELATED = {a["key"]: a["others"] + ["free"] for a in ALTS}
