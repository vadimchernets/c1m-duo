# Qu’est-ce que Poly ?

C1M, c’est le projet ; **Poly**, c’est ce que tu obtiens vraiment sur ton téléphone. Cette page l’explique en langage simple.

## Ce que c’est concrètement

Poly est un bouton sur ton iPhone, avec deux IA derrière. Tu poses une seule question et ChatGPT et Claude la traitent en duo : l’un répond, l’autre vérifie et améliore — ou les deux répondent indépendamment et leurs réponses sont fusionnées, selon le mode choisi. Le résultat arrive à l’écran, dans ton presse-papiers et dans un journal.

L’idée, c’est la compression. L’ancienne séquence — ouvrir ChatGPT, demander, copier, ouvrir Claude, coller, lui demander de vérifier, copier la version finale — se réduit à une pression et environ une minute et demie d’attente. Et ce n’est pas seulement plus rapide, c’est meilleur : une seconde IA attrape vraiment les erreurs de la première. C’est toute la raison pour laquelle un duo bat un modèle seul.

Ce n’est pas une app de l’App Store. C’est un **raccourci** pour l’app Raccourcis intégrée d’Apple — d’où son installation en une pression sur un fichier, et sa présence sur ton écran d’accueil comme une icône ordinaire.

## Ce que ça coûte

- **Poly en lui-même est gratuit.** C’est un fichier, pas un service — aucun abonnement à Poly, aucune publicité, aucune collecte de données.
- **Le coût est prélevé sur tes abonnements ChatGPT et Claude.** Chaque exécution dépense de 1 à 4 messages (le prix est affiché dans le menu avec l’icône ✉). Elle partage les mêmes limites que tes conversations habituelles dans ces apps.
- **Un abonnement Claude est indispensable** — sur un compte gratuit, l’action peut répondre « model isn't available ». ChatGPT fonctionne dans les deux cas, dans la limite de ses propres quotas.
- **Pas besoin d’iCloud payant :** le journal pèse quelques kilo-octets ; les 5 Go gratuits en couvrent des décennies. Coupe iCloud et la réponse arrive quand même — seule l’entrée du journal est ignorée.

## Ce qu’il te faut avant d’installer

Un iPhone sous iOS 18 ou ultérieur, avec les apps ChatGPT et Claude installées et la session ouverte. C’est tout. L’installation, c’est une pression sur le fichier `dist/fr/Poly.shortcut` — le guide pas à pas pour les utilisateurs non techniques est dans `install.md`.

## Là où Poly justifie sa place

- **Écriture :** relire avant d’envoyer, décoder un message désagréable reçu, traduire et polir.
- **Décisions :** « est-ce que j’achète », « est-ce que je change », « est-ce que je lance » — un regard rapide face à un regard prudent, puis un plan et les risques.
- **Questions à fort enjeu** (médicales, juridiques, financières) : deux avis indépendants et une carte honnête de leurs désaccords, au lieu d’une seule voix sûre d’elle.
- **Ton propre texte, intact :** le mode Conseil relit sans se transformer en coauteur.
- **En déplacement :** le compagnon Voice — tu dictes la question, tu écoutes la réponse lue à voix haute.
- **Images :** deux croquis vectoriels de deux artistes IA différents, à toi de choisir.

Des formulations toutes prêtes pour plus de 20 tâches se trouvent dans `recipes.md`.

## Les défauts, en toute honnêteté

- **Pendant que Poly tourne, laisse ton téléphone tranquille** (environ 1 à 2 minutes) — toucher l’écran annule l’exécution. C’est une limite de la plateforme d’Apple, pas de Poly. L’exception est le mode Clarification, qui ouvre une fenêtre de lui-même et te demande de répondre.
- **Ce n’est pas de la magie en arrière-plan.** Le téléphone doit être déverrouillé, les apps passent au premier plan une par une, dans un ordre strict. Poly est un bouton sur lequel on appuie et qu’on attend, pas un robot programmé.
- **L’action ChatGPT peut avoir des ratés :** elle affirme parfois que « you are logged out » alors que tu es manifestement connecté. Toujours réparable : ouvre l’app ChatGPT, ferme-la, relance Poly.
- **Les questions longues sont risquées :** l’action Claude a un délai d’expiration — sur une question très longue, le résultat final peut revenir vide et tu dois aller chercher la réponse complète dans l’app Claude elle-même. Les questions plus courtes reviennent plus sûrement.
- **Le modèle ne se choisit pas depuis Poly :** il utilise celui défini par défaut dans chaque app. Vérifie le modèle dans Claude avant une exécution qui compte.
- **Une grosse mise à jour d’iOS peut appeler une exécution de test** — une mise à jour importante peut redemander les autorisations.

## Perdu au moment de choisir un mode ?

Dans le menu de Poly, ouvre **📂 Plus…** → **ℹ️ Qu’est-ce que Poly** — une explication courte de chaque mode, directement sur ton téléphone et gratuitement. Ensuite, Poly propose de te ramener au choix du mode avec la même question.

## Et les autres IA — la moitié du travail t’est déjà retirée des mains

Tout ce qui précède parle du duo, parce que c’est le duo qui tourne tout seul. Mais tu as sans doute plus de deux IA sur ton téléphone : Gemini, Grok, DeepSeek, Qwen, Copilot, celle que tu veux. Poly sait les faire entrer elles aussi — en semi-manuel, et il vaut mieux savoir exactement ce que ça veut dire.

Jusqu’ici, poser la même question à cinq IA voulait dire tout faire à la main : écrire la question cinq fois, garder cinq réponses en tête, puis les fusionner soi-même. **Poly Multi t’enlève à peu près la moitié de ce travail.** Il rédige le prompt, le met dans ton presse-papiers, te fait passer d’une app à l’autre dans l’ordre, récupère chaque réponse dès que tu l’as copiée et remet toute la pile à Claude, qui la fond en un seul document en gardant les désaccords. Il te reste ce que toi seul peux faire : ouvrir ton app, coller, envoyer, copier la réponse, revenir.

Ce n’est donc pas « Poly pilote tes autres apps » — rien ici n’automatise un logiciel qui n’est pas le tien. Ce sont tes propres trois pressions par IA, sauf que réfléchir, tenir la file et fusionner, c’est Poly qui le fait pour toi. Si tu le faisais à la main, c’est environ deux fois plus rapide, et tu obtiens un document au lieu de cinq onglets.

C’est là que va le projet : plus de chœur, moins de manuel, à mesure que les apps s’ouvriront. Pour l’instant le duo tourne seul et le reste est semi-manuel — et nous préférons le dire franchement plutôt que promettre autre chose. Poly Multi est livré à côté du raccourci principal ; prends-le quand le duo te sera devenu naturel.

## En une phrase

Un bouton gratuit qui met deux de tes abonnements payants au travail ensemble, à se vérifier l’un l’autre : un seul prix — de 1 à 4 messages par exécution — et une seule habitude : appuyer, puis laisser le téléphone tranquille une minute et demie.
