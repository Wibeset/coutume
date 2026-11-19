# Travailler sur le site de Coutume

Du HTML statique, une feuille de style et un petit script, publiés par GitHub Pages sur `coutume.app` (`CNAME`). La structure et le design
reprennent ceux d’Arpente (`../arpente`) et de Porcom (`../porcom`), en mode clair seulement, aux couleurs de
l’app : papier `#f5f3ee`, encre `#17212b` et la flamme des séquences, foncée en `#a8501a` pour se lire en texte.
Les habitudes d’exemple gardent leurs propres couleurs (bleu pour l’eau, orange pour les énergisants).

## Pages

| English | Français |
| --- | --- |
| `/` | `/fr/` |
| `/support/` | `/fr/assistance/` |
| `/privacy/` | `/fr/confidentialite/` |

L’anglais est la langue par défaut (`x-default`). Chaque page déclare son équivalent (`hreflang`) et
le lien de langue mène à la même page dans l’autre langue. Les liens sont relatifs
(`../assets/…`), donc les pages s’ouvrent aussi bien depuis le disque que servies d’un sous-dossier ;
seule `404.html` garde des liens depuis la racine, puisque GitHub Pages la sert à n’importe quelle adresse. Le français est tutoyé, comme
l’app, avec des espaces insécables avant `? ! : ;` et dans les « guillemets ». Coutume est « une app » : on l’accorde au féminin.

## Au quotidien

- **Styles** : modifier `assets/style.css`, puis `scripts/build-css.sh` pour produire `style.min.css`,
  que les pages chargent.
- **Script** : `assets/main.js` fait apparaître les sections au défilement (et remplit les deux anneaux de la
  section « à prendre, à laisser ») ; sans JavaScript, tout reste visible.
- **Captures de l’app** : `scripts/capture-screens.sh fr` compile `../habitudes-ios`, la lance dans le simulateur
  avec les habitudes d’exemple et les chiffres Santé d’exemple, et capture les cinq écrans de la rangée, en clair,
  en AVIF et WebP. `SCREENS="today:"` n’en refait qu’une partie.
- **Icône et images** : `python3 scripts/make-images.py` dessine l’icône (`assets/icon.svg`, `icon-1024.png` pour
  l’App Store), les favicons et les images Open Graph (`icons` ou `og` pour n’en refaire qu’une partie). Il lui faut
  Google Chrome.
- **Prévisualiser** : ouvrir `index.html`, ou `python3 -m http.server` à la racine puis http://localhost:8000.
- **Publier** : un push sur `main` déploie avec `.github/workflows/pages.yml`.

## Avant le lancement

- **Captures en anglais** : l’app n’a pas encore de catalogue de chaînes anglais, donc les pages anglaises montrent
  les captures françaises (`assets/screens/fr/`). Quand l’app parlera anglais, lancer
  `scripts/capture-screens.sh en` et faire pointer la rangée et le JSON-LD de `index.html` vers `assets/screens/en/`.
- **Icône** : `assets/icon.svg` (un anneau presque fermé et une coche) est une proposition ; l’app n’a pas encore
  d’icône. Si elle est retenue, `assets/icon-1024.png` va dans `AppIcon` de `../habitudes-ios`.
- **Fonctionnalités** : le texte suppose une app gratuite, sans compte, la lecture seule de Santé (pas, exercice,
  pleine conscience, eau), la synchro iCloud, le joker hebdomadaire, 11 niveaux, 18 jalons et les widgets.
  Ajuster les pages, le JSON-LD, `llms.txt` et la politique de confidentialité si l’app diffère.
- **App Store** : à la sortie, transformer « Coming soon to the App Store » / « Bientôt sur l’App Store » (en-tête,
  titre, appel à l’action) en lien vers l’App Store, régénérer le QR code (il mène à coutume.app pour l’instant :
  `printf <lien> | npx qrcode -t svg -d '#17212b' -l '#0000' -m 0 -o assets/qr.svg`, qui lit le lien sur l’entrée standard) et ajouter `apple-itunes-app` et
  `installUrl` dans le JSON-LD.
- **Pubs** : quatre cartes, deux par deux (Reliure, Arpente, Porcom, Dernier Verre). Arpente et Dernier Verre y sont
  encore « bientôt sur iPhone » ; à mettre à jour à leur sortie. La capture de Dernier Verre
  (`assets/ads/dernierverre-feed-fr.webp`, tirée de `../dernierverre-ios/assets/screen-feed.png`) est en français
  sur les deux pages. Penser aussi à ajouter Coutume aux pubs de Reliure, d’Arpente, de Porcom et de Dernier Verre.
