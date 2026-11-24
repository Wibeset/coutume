# Travailler sur le site de Coutume

Du HTML statique, une feuille de style et un petit script, publiés par GitHub Pages sur `coutume.app` (`CNAME`). La structure et le design
reprennent ceux de Reliure (`../reliure`) : fond encre `#0a0a0b` sous un grain léger, titres en Headland One
(`assets/fonts/`), texte en Helvetica, liens marqués par leur soulignement. L’accent est la flamme de l’app, éclaircie
en `#f29a5c` pour se lire sur l’encre (contours de focus, trait de surligneur du titre, halo derrière le téléphone).
L’accueil et les guides avec captures sont coupés en deux : le texte à gauche, un grand iPhone fixe à droite dont
l’écran suit la section lue (`main.js`).

## Pages

| English | Français | Español |
| --- | --- | --- |
| `/` | `/fr/` | `/es/` |
| `/support/` | `/fr/assistance/` | `/es/soporte/` |
| `/privacy/` | `/fr/confidentialite/` | `/es/privacidad/` |
| `/streaks-alternative/` | `/fr/alternative-streaks/` | `/es/alternativa-streaks/` |
| `/habitify-alternative/` | `/fr/alternative-habitify/` | `/es/alternativa-habitify/` |
| `/habitica-alternative/` | `/fr/alternative-habitica/` | `/es/alternativa-habitica/` |
| `/habit-tracker-apple-health/` | `/fr/suivi-habitudes-sante/` | `/es/seguimiento-habitos-salud/` |
| `/quit-energy-drinks/` | `/fr/arreter-boissons-energisantes/` | `/es/dejar-bebidas-energeticas/` |
| `/quit-vaping-tracker/` | `/fr/arreter-de-vapoter/` | `/es/dejar-de-vapear/` |
| `/days-without-counter/` | `/fr/compteur-jours-sans/` | `/es/contador-dias-sin/` |
| `/water-tracker/` | `/fr/suivi-eau/` | `/es/seguimiento-agua/` |
| `/free-habit-tracker/` | `/fr/application-habitudes-gratuite/` | `/es/app-habitos-gratis/` |
| `/habit-tracker-widget/` | `/fr/widget-habitudes/` | `/es/widget-habitos/` |
| `/habit-ideas/` | `/fr/idees-habitudes/` | `/es/ideas-habitos/` |
| `/how-long-to-form-a-habit/` | `/fr/combien-de-temps-pour-une-habitude/` | `/es/cuanto-tarda-un-habito/` |
| `/habit-ideas/<article>/` (38) | `/fr/idees-habitudes/<article>/` | `/es/ideas-habitos/<article>/` |

L’anglais est la langue par défaut (`x-default`). Chaque page déclare ses équivalents (`hreflang`) et
le pied de page mène à la même page dans les deux autres langues. L’espagnol est tutoyé, en espagnol neutre, comme
l’app (`../coutume-ios`), qui parle français, anglais et espagnol. Les liens sont relatifs
(`../assets/…`), donc les pages s’ouvrent aussi bien depuis le disque que servies d’un sous-dossier ;
seule `404.html` garde des liens depuis la racine, puisque GitHub Pages la sert à n’importe quelle adresse. Le français est tutoyé, comme
l’app, avec des espaces insécables avant `? ! : ;` et dans les « guillemets ». Coutume est « une app » : on l’accorde au féminin.

## Au quotidien

- **Pages générées** : `python3 scripts/site/build.py .` refait les trois accueils, les guides, les 38 articles
  « idées d’habitudes », les pieds de page et les langues de l’assistance et de la confidentialité, `404.html`,
  `sitemap.xml` et `llms.txt`. Les textes sont dans `scripts/site/` : `content.py` (guides en anglais et en français),
  `guides_es.py` (guides en espagnol), `articles/*.py` (un article = trois langues), `build_home.py` et `HOME_ES` dans
  `build.py` (les accueils). Modifier ces fichiers puis relancer, plutôt que de retoucher le HTML des pages générées.
  Le corps de l’assistance et de la confidentialité reste écrit à la main. `articles/README.md` décrit le format et
  les règles d’un article (dont les seules fonctions de l’app qu’on a le droit de citer).
- **Styles** : modifier `assets/style.css`, puis `scripts/build-css.sh` pour produire `style.min.css`,
  que les pages chargent.
- **Script** : `assets/main.js` montre dans le téléphone de droite l’écran de la section lue (`data-screen`) et ajoute
  un point par écran à côté ; sans JavaScript, le premier écran reste affiché.
- **Guides** : chaque guide existe en anglais et en français, se termine par des guides liés, et figure dans la liste
  « Guides » de l’accueil, `sitemap.xml` et `llms.txt`. Les pages comparatives (Streaks, Habitify, Habitica) datent
  leurs informations sur les concurrents : les revérifier avant de les mettre à jour.
- **Captures de l’app** : `scripts/capture-screens.sh fr` (ou `en`, `es`) compile `../coutume-ios`, la lance dans le
  simulateur avec les habitudes d’exemple et les chiffres Santé d’exemple, et capture les cinq écrans du téléphone,
  en sombre, en AVIF et WebP, dans `assets/screens/<langue>/` ; chaque langue du site montre les siennes. `SCREENS="today:"` n’en refait qu’une partie.
- **Icône et images** : `python3 scripts/make-images.py` dessine l’icône (`assets/icon.svg`, `icon-1024.png` pour
  l’App Store), les favicons et les images Open Graph (`icons` ou `og` pour n’en refaire qu’une partie). Il lui faut
  Google Chrome.
- **Prévisualiser** : ouvrir `index.html`, ou `python3 -m http.server` à la racine puis http://localhost:8000.
- **Publier** : un push sur `main` déploie avec `.github/workflows/pages.yml`.

## Avant le lancement

- **Icône** : la flamme (`assets/icon.svg`) est l’icône de l’app. Elle est dessinée deux fois, ici et dans
  `AppIcon` de `../coutume-ios` (avec ses variantes sombre et teintée) : changer les deux ensemble.
- **Fonctionnalités** : le texte suppose une app gratuite, sans compte, la lecture seule de Santé (pas, exercice,
  pleine conscience, eau), la synchro iCloud, le joker hebdomadaire, 11 niveaux, 18 jalons et les widgets.
  Ajuster les pages, les guides, le JSON-LD, `llms.txt` et la politique de confidentialité si l’app diffère.
- **App Store** : à la sortie, transformer la pastille « Coming soon to the App Store » / « Bientôt sur l’App Store »
  (`<span class="store">`) en lien `<a class="store">` vers l’App Store, comme sur Reliure, ajouter un lien « App Store ↗ »
  au pied de page, `apple-itunes-app` et `installUrl` dans le JSON-LD, et mettre à jour la phrase « arrive bientôt »
  à la fin des guides. Ajouter alors une page Nouveautés (`/whats-new/`, `/fr/nouveautes/`) comme celle de Reliure.
- **Pubs** : une liste « You may also like / Tu aimeras aussi » (Reliure, Arpente, Porcom, Dernier Verre), comme sur
  Reliure. Arpente et Dernier Verre y sont encore « coming soon / bientôt » ; à mettre à jour à leur sortie. Penser aussi à ajouter Coutume aux pubs de Reliure, d’Arpente, de Porcom et de Dernier Verre.
