# Installer Poly — 2 minutes, aucune compétence technique

Poly est un « raccourci » pour iPhone : tu poses une seule question et elle est traitée par deux IA à la fois — ChatGPT et Claude — dans l’un des onze modes. La réponse arrive à l’écran et dans ton presse-papiers.

## Avant d’installer (une seule fois)

1. **Un iPhone sous iOS 18 ou ultérieur.** C’est le minimum officiel de l’action « Ask Claude » sur laquelle Poly est bâti (la documentation d’Anthropic dit elle-même « iOS 18 and later »). Par ailleurs, sous iOS 26, Apple donne comme compatibles l’iPhone 11 et ultérieurs, ainsi que le SE de 2ᵉ génération et ultérieurs. Poly lui-même n’exige pas Apple Intelligence — seulement iOS 18+. L’iPad devrait fonctionner sous iPadOS 18+/26, mais cela n’a pas été vérifié sur le terrain. Le compagnon **Poly Compress**, lui, réclame du matériel Apple Intelligence : une puce A17 Pro / série M ou plus récente (iPhone 15 Pro/Pro Max, tous les 16/16e et ultérieurs, iPad avec M1+ ou le mini à A17 Pro).
2. **Les apps ChatGPT et Claude**, installées depuis l’App Store, avec la session ouverte dans les deux. Claude exige un abonnement payant — sur un compte gratuit, l’action peut échouer avec « model isn't available ».

## Installation (une seule pression)

1. Récupère le fichier **`dist/fr/Poly.shortcut`** comme tu veux : AirDrop, WhatsApp/Telegram, e-mail, une clé USB — peu importe.
2. Touche le fichier. L’app Raccourcis s’ouvre sur une fiche « Poly » — appuie sur **Ajouter le raccourci**. Voilà, Poly est installé.
   - Si le fichier est arrivé dans une messagerie, touche-le d’abord là-bas, choisis Partager/« Ouvrir dans… », puis sélectionne Raccourcis.
3. **Première exécution :** le raccourci demande des autorisations — « Autoriser les actions ChatGPT ? » → Autoriser ; « …envoyer du texte à Claude ? » → **Toujours autoriser** ; « …copier dans le presse-papiers ? » → **Toujours autoriser**. Cela n’arrive qu’une fois.

## Icône sur l’écran d’accueil (30 secondes, facultatif)

1. Ouvre Raccourcis → appui long sur la vignette Poly → si aucun menu n’apparaît, touche « ··· » sur la vignette → touche le nom **Poly ⌄** en haut → **« Sur l’écran d’accueil »**.
2. Tu veux l’icône de la marque ? Touche la miniature → onglet « Image » → « Choisir une photo/un fichier » → sélectionne `assets/poly.jpg` (envoie-le sur ton téléphone en même temps que le raccourci).
3. Appuie sur **Ajouter**. L’icône Poly apparaît sur ton écran d’accueil — une pression pour la lancer. À la voix : « Dis Siri, Poly ».

## Comment s’en servir

Touche l’icône → « Que veux-tu demander à Poly ? » → tape ta question → « Terminé » → choisis un mode. Le menu a deux niveaux : les cinq modes courants en haut, tout le reste rangé dans **📂 Plus…** (rien n’est supprimé — un mode rare coûte simplement une pression de plus). Plus… contient aussi **ℹ️ Qu’est-ce que Poly** — une explication gratuite de chaque mode, directement sur l’appareil. Perdu au moment de choisir ? Ouvre-la — elle ne dépense pas un seul message.

**Menu principal (modes courants) :**

| Mode | Ce qui se passe | Coût |
|---|---|---|
| **⚖️ Critique · 2✉** | ChatGPT répond, Claude vérifie et livre une version finale améliorée. Ton mode de tous les jours. | 2 messages |
| **🩺 Conseil · 1✉** | Claude relit TON texte déjà terminé sans le réécrire : un verdict en une ligne, l’objection la plus forte d’abord, ce qu’il faut revérifier. Le mode le moins cher. | 1 message |
| **👀 Côte à côte · 2✉** | Les deux répondent indépendamment ; les réponses sont placées l’une à côté de l’autre. | 2 messages |
| **🔀 Synthèse · 3✉** | Les deux répondent à l’aveugle, puis on fusionne en un résultat « ancre + delta ». On te demandera qui sert d’ancre : Claude (faits/structure) ou ChatGPT (ton/créativité). Pour tout ce qui compte. | 3 messages |
| **🧭 Auto · +1✉** | Tu ne sais pas quel mode prendre ? ChatGPT en choisit un pour toi (+1 message), puis Poly redémarre avec la même question pour que tu sélectionnes le mode recommandé. | 1 message + le mode |

**📂 Plus… (modes occasionnels + aide gratuite) :**

| Mode | Ce qui se passe | Coût |
|---|---|---|
| **⚔️ Décision · 3✉** | Un regard rapide (ChatGPT) rencontre un regard prudent (Claude), puis un arbitre expose les premières étapes et les risques. Pour décider. | 3 messages |
| **🗺 Carte des désaccords · 3✉** | Les deux répondent à l’aveugle, puis on dresse la carte : où ils s’accordent, où ils divergent, les angles morts, ce qu’il faut vérifier. Aucune conclusion imposée — c’est toi qui tranches. | 3 messages |
| **🥊 Débat · 4✉** | Un brouillon, un opposant à la chasse aux faiblesses, une révision, puis le verdict d’un juge. Pour les problèmes les plus durs. | 4 messages |
| **❓ Clarification · 2✉** | ChatGPT demande d’abord ce qui manque → tu réponds dans une fenêtre qui s’ouvre → Claude donne une réponse précise. Pour les questions floues. C’est le seul mode où tu es censé toucher l’écran en cours de route — mais uniquement dans sa propre fenêtre, nulle part ailleurs. | 2 messages |
| **➕ Delta · 2✉** | Claude écrit la réponse d’ancrage → ChatGPT renvoie UNIQUEMENT une liste d’améliorations, sans tout réécrire. Une alternative moins chère à la Synthèse quand tu surveilles ton budget de messages. | 2 messages |
| **🎨 Image · 2–3✉** | Décris ce qu’il faut dessiner → les deux artistes IA le croquent à l’aveugle (SVG vectoriel, chacun dans une session propre — sans regarder chez l’autre) → une page s’ouvre avec les deux croquis côte à côte, ◆ CLAUDE et ◆ CHATGPT — à toi de choisir (on te demandera : croquis seuls · 2✉ ou + le verdict d’un juge comparateur · 3✉ — le juge compare le code des croquis ; les rendus, tu les vois déjà toi-même). L’image est enregistrée (Fichiers → iCloud Drive → Raccourcis → `Poly-image.html`) et le code SVG atterrit dans ton presse-papiers : colle-le dans n’importe quel convertisseur ou site pour obtenir un fichier image à la taille que tu veux. | 2–3 messages |
| **ℹ️ Qu’est-ce que Poly** | Une explication à l’écran de ce qu’est Poly et du mode à utiliser selon les cas — sans aucun appel à l’IA. De là, « 🔁 Autre mode » te ramène au choix du mode avec la même question. | 0 message |

**Un raccourci vers le menu lui-même** (facultatif) : garde le compagnon **Poly Quiet** sous la main — c’est une exécution de Critique toute prête en une pression, sans sélecteur de mode (le résultat part directement dans le presse-papiers et le journal, sans aucun écran), ou **Poly Voice** — la même chose à la voix, avec le résultat lu à voix haute. L’icône de l’un comme de l’autre peut aller sur ton écran d’accueil, tout comme celle de Poly : tu as ainsi un « bouton rapide » à côté du menu complet.

Le prix est affiché dans le menu même (l’icône ✉). Les notifications de progression arrivent au fil de l’exécution — « [étape 2/4]… ». Le journal consigne à la fois le mode et les réponses intermédiaires brutes : si le résultat final se retrouve coupé, les brouillons ne sont pas perdus. La réponse finale s’ouvre en plein écran avec un bouton de partage (Coup d’œil).

**Deux niveaux.** Le niveau 1, c’est le cœur : le duo Poly entièrement automatique et ses compagnons automatiques ci-dessous — installe-le sans hésiter, c’est là qu’est l’innovation. Le niveau 2 est une extension PRO pour utilisateurs avancés : **🎼 Poly Multi** (un chœur manuel de 10 IA américaines et chinoises avec une synthèse Est-Ouest) est distribué à part et n’est pas nécessaire à l’expérience de base — prends-le quand tu seras à l’aise avec l’essentiel.

**Les compagnons automatiques de Poly** (inclus) : **Poly Voice** — tu touches, tu dictes, la chaîne Critique s’exécute, la réponse est lue à voix haute (pratique en marchant ou en cuisinant) ; **Poly Photo** — tu partages une photo ou un PDF, l’OCR de l’appareil lit le texte (gratuit, sans réseau) et l’envoie directement dans Poly ; **Poly Quiet** — la même chaîne que Critique mais sans notifications ni écran final : le résultat part uniquement dans le presse-papiers et le journal (pour des exécutions rapides en arrière-plan) ; **Poly Compress** (appareils Apple Intelligence uniquement : iPhone 15 Pro et ultérieurs, toute la gamme 16/16e/17) — tu sélectionnes un mur de texte → Partager → Compress : le modèle gratuit qui tourne sur l’appareil le condense et lance Poly automatiquement (protection contre les expirations sur les textes longs).

Juste après le choix du mode arrive une **notification d’état** (« ce qui se passe et combien de temps attendre »). Ensuite, comptez environ 1 à 2 minutes avant que la réponse n’apparaisse à l’écran et dans le presse-papiers. Des formulations toutes prêtes pour plus de 20 tâches courantes se trouvent dans `recipes.md`. La réponse finale commence toujours par l’essentiel en une ligne et se termine par « Confiance : élevée/moyenne/faible ». **Pendant que le raccourci tourne, laisse ton téléphone tranquille** — toucher l’écran l’annule (s’il semble mourir en silence, relance-le tout simplement). L’exception, c’est **❓ Clarification** : par construction, elle ouvre une seconde fenêtre et te demande de répondre à des questions complémentaires (ou de taper « passer ») — ce n’est pas un bug, cela fait partie du déroulé. Réponds et le raccourci continue tout seul.

## Super-pouvoirs

- **Depuis n’importe quelle app :** sélectionne du texte → Partager → Poly — ta zone de question contient déjà le texte ; ajoute « traduis/vérifie/explique » et lance.
- **Journal :** chaque exécution s’ajoute à `Poly-journal.md` (Fichiers → iCloud Drive → Raccourcis). Tout ton historique de questions et de verdicts vit au même endroit ; à la première exécution, autorise l’accès aux fichiers avec **Toujours autoriser**.
- **Lancement mains libres :** Réglages → bouton Action → « Exécuter un raccourci » → Poly. Ou un double tapotement à l’arrière du téléphone : Réglages → Accessibilité → Toucher → Toucher l’arrière de l’appareil → Poly. À la voix : « Dis Siri, Poly ».
- **D’autres points d’entrée :** un widget sur l’écran d’accueil ou l’écran verrouillé (appui long sur l’écran d’accueil → + → Raccourcis → Poly) ; le centre de contrôle (Réglages → Centre de contrôle → ajoute « Raccourcis ») ; un tag NFC sur ton bureau ou dans ta voiture (Raccourcis → Automatisation → NFC → exécuter Poly).
- **Des photos dans le duo :** la voie principale, c’est le compagnon **Poly Photo** (tu partages une photo/un PDF → OCR → il lance Poly pour toi). Pour une lecture *visuelle* d’une image (et non du texte qu’elle contient), utilise le widget appareil photo de Claude → analyse → Copier → partage ce texte dans Poly.
- **Vérifier ce que tu écris toi-même :** sélectionne ton brouillon n’importe où → Partager → Poly → mode **🩺 Conseil** — il relit sans réécrire (et ne devient jamais coauteur).
- **Sur iPhone 15 Pro et ultérieurs :** Raccourcis dispose d’une action « Utiliser le modèle » (Apple Intelligence, gratuite, sans internet) capable d’étendre Poly — par exemple pour choisir un mode automatiquement. Sur iPhone 14 et antérieurs, l’action n’existe pas ; Poly fonctionne très bien sans elle.
- **Écouter immédiatement (facultatif) :** dans l’éditeur du raccourci, déplie la première action « Demander » et active l’option de dictée immédiate — toucher l’icône lancera alors tout de suite l’écoute de ta question. Désactivée par défaut, parce que c’est plus pratique à la fois pour le texte tapé et pour la feuille de partage.

## À propos d’iCloud — aucun forfait payant nécessaire

Poly n’exige pas d’iCloud payant. Le flux principal (question → les deux IA → réponse à l’écran et dans le presse-papiers) ne touche jamais à iCloud. Seules deux commodités facultatives l’utilisent : le journal d’exécutions et le fichier image — l’un comme l’autre se comptent en kilo-octets, et les 5 Go gratuits de n’importe quel identifiant Apple couvrent des décennies. Si iCloud Drive est désactivé ou plein, la réponse arrive quand même à l’écran et dans le presse-papiers (c’est garanti par construction) — seule l’entrée du journal est ignorée. Tu ne veux pas de journal du tout ? Voir la confidentialité ci-dessous.

## Confidentialité

`Poly-journal.md` conserve chaque question et chaque réponse en texte brut dans iCloud Drive. Tu ne veux pas d’historique ? Supprime l’action de journal dans l’éditeur du raccourci. Pour effacer ce qui existe déjà, supprime le fichier `Poly-journal.md` dans Fichiers. Si le journal devient trop gros, renomme simplement le fichier (par exemple en `Poly-journal-aout.md`) — un nouveau est créé automatiquement à l’exécution suivante.

## Si quelque chose cloche

- **ChatGPT dit « You are logged out »** (alors que tu es manifestement connecté) — ouvre l’app ChatGPT, ferme-la, relance Poly. Un bug connu qui se règle toujours ainsi.
- **Claude dit « This model isn't available right now »** — ton compte Claude n’a pas d’abonnement, ou tu as atteint une limite. Connecte-toi à un compte payant dans l’app Claude.
- **Claude reste muet / réponse vide sur une longue question** — l’action Claude a un délai d’expiration : elle peut rendre la main avant que Claude ait fini, pendant que Claude continue d’écrire la réponse dans sa propre app. Ouvre Claude, la réponse y est — copie-la avec le bouton de l’app. Pour la prochaine fois : une question plus courte revient plus sûrement. Si l’exécution a carrément échoué, balaie Raccourcis hors des apps récentes et relance.
- **Partager Poly avec quelqu’un :** envoie `Poly.shortcut` comme fichier autonome, pas dans un zip (un zip sur téléphone, ce sont des étapes en plus). Dans Telegram : appui long sur le fichier → Partager/Enregistrer dans Fichiers, pas une simple pression.
- **Ne renomme pas le raccourci Poly.** Les compagnons Photo et Compress, ainsi que le bouton « 🔁 Autre mode », l’appellent par son nom exact « Poly ». Renomme-le (ou réimporte-le et tu te retrouves avec « Poly 1 ») et ces trois chemins cessent silencieusement de fonctionner. Si une réinstallation crée un doublon, supprime l’ancien raccourci et garde exactement un « Poly ».
- **Des réponses plus faibles que prévu** — l’action utilise le modèle défini par défaut dans l’app Claude : ouvre Claude, change de modèle, ferme, relance Poly. Bonne habitude : vérifier le modèle dans l’en-tête de Claude avant une exécution importante.
- **Un partage n’a apporté qu’un lien nu et rien ne s’est passé** — les actions ne vont pas chercher les pages web elles-mêmes : ouvre la page, sélectionne une partie du texte et partage ce texte.
- **Bonus :** la réponse finale part aussi dans le presse-papiers partagé (presse-papiers universel) — sur un Mac ou un iPad, tu peux la coller avec Cmd+V sans toucher à ton téléphone.
- **Après une grosse mise à jour d’iOS** (vers iOS 27, par exemple), fais une exécution de test en Critique. Une mise à jour importante de Raccourcis peut redemander les autorisations ou afficher une fiche « Terminé » supplémentaire — une exécution suffit à le révéler et à le régler.
- Le coût en messages est prélevé sur tes **abonnements** à chaque service (pas sur une API) et partage les mêmes limites que tes conversations habituelles. Le modèle utilisé est celui défini par défaut dans chaque app.

## Ce qui vient après la réponse finale

Sous l’écran final, Poly demande : **« ✅ Terminé »** ou **« 🔁 Autre mode — même question »**. La seconde option relance Poly avec ta question déjà saisie (tu peux la modifier) et te laisse choisir un autre mode. Pratique pour lancer Critique puis, dans la foulée, Carte des désaccords sur la même question sans la retaper.
