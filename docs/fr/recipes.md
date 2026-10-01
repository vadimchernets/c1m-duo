# Recettes Poly — quoi demander, et avec quel mode

Poly est un généraliste : toute tâche se ramène à la bonne formulation plus le bon mode. Voici une bibliothèque de recettes éprouvées. Le chemin le plus rapide pour un texte existant : **sélectionne le texte → Partager → Poly** — il atterrit directement dans la zone de question, il ne te reste qu’à ajouter la consigne devant.

| Tâche | Quoi écrire dans la question | Mode |
|---|---|---|
| Relire un e-mail avant de l’envoyer | « Vérifie et améliore cet e-mail, garde un ton chaleureux et professionnel : [texte] » | ⚖️ Critique · 2✉ (déjà définitif et à ne pas réécrire ? Prends plutôt 🩺 Conseil — voir plus bas) |
| Répondre à un message difficile ou désagréable | « Voici un message reçu. Analyse le ton et l’intention, et propose 3 réponses sur des tons différents : [texte] » | ⚖️ Critique · 2✉ |
| Écrire du code et le faire relire | « Écris [ce dont tu as besoin]. Exigences : … » | ⚖️ Critique · 2✉ (🥊 Débat · 4✉ uniquement pour du code critique, quand tu veux expressément quelqu’un qui cherche les trous) |
| Relire du code existant | « Trouve les bugs, les risques et ce qu’il faut améliorer : [code] » | 👀 Côte à côte · 2✉ |
| Prendre une décision (acheter / changer / lancer ?) | « Est-ce que je devrais [idée/décision] ? Contexte : … » | ⚔️ Décision · 3✉ |
| Évaluer le risque d’un projet ou d’un accord | « Quels sont les risques de [sujet] et comment les refermer ? » | ⚔️ Décision · 3✉ |
| Vérifier un texte ou un article d’actualité | « Vérifie ces affirmations pour y trouver des erreurs factuelles : [texte] » | 🔀 Synthèse · 3✉ |
| Question à fort enjeu (médicale / juridique / financière) | Pose-la telle quelle | 🔀 Synthèse · 3✉ (🥊 Débat n’est pas un substitut : c’est pour quand tu veux expressément mettre la conclusion à l’épreuve) |
| Comprendre vite un sujet nouveau | « Explique ça pour un non-spécialiste, sans blabla : [sujet] » | ⚖️ Critique · 2✉ |
| Apprendre quelque chose en s’auto-testant | « Explique [sujet] et donne-moi 3 questions d’auto-évaluation avec leurs réponses » | ⚖️ Critique · 2✉ |
| Préparer une réunion ou une négociation | « Réunion sur [sujet] avec [qui]. Quelles questions poser, et quelles objections prévoir, avec les réponses ? » | ⚔️ Décision · 3✉ |
| Noms, accroches, pistes créatives | « Donne-moi 10 variantes de [chose] dans des styles différents, puis choisis ton top 3 en justifiant » | 👀 Côte à côte · 2✉ |
| Résumer un article | sélectionne l’article → Partager → « Résume : les points principaux et la conclusion » | ⚖️ Critique · 2✉ |
| Organiser sa journée / prioriser ses tâches | « Voici mes tâches : […]. Priorise-les et propose un ordre » | ⚔️ Décision · 3✉ |
| Traduire et polir | « Traduis en [langue] et soigne le style : [texte] » | ⚖️ Critique · 2✉ |
| Brainstorming | « Propose 5 solutions non évidentes à ce problème : […], puis évalue lesquelles sont réalistes » | ⚖️ Critique · 2✉ (c’est « générer et filtrer », pas « mettre à l’épreuve » — le Débat est inutile) |
| Longue explication → résumé court | « Explique […] en détail, puis condense le tout en 3 points d’une phrase à la fin » | ⚖️ Critique · 2✉ |
| Message embarrassant → brouillon de réponse | sélectionne la conversation → Partager → « Analyse le ton et propose une réponse » | ⚔️ Décision · 3✉ |
| Vérifier TON PROPRE texte sans réécriture | sélectionne ton brouillon → Partager → (n’ajoute rien) | 🩺 Conseil · 1✉ |
| Sujet contesté — qu’est-ce qui est vrai au juste ? | pose-la telle quelle — tu obtiendras une carte des accords et des désaccords, sans conclusion imposée | 🗺 Carte des désaccords · 3✉ |
| Question floue, tu ne sais pas bien ce que tu veux | pose-la telle quelle — on te posera d’abord des questions complémentaires | ❓ Clarification · 2✉ |
| Logo, schéma, carte de vœux, illustration | « Dessine [quoi, dans quel style] » — deux croquis vectoriels au choix | 🎨 Image · 2–3✉ |
| Photo d’un document, d’un panneau ou d’un menu | Partage la photo → Poly Photo (l’OCR s’occupe du reste) | compagnon Poly Photo |
| Petit écran / en déplacement | demande à la voix — la réponse est lue à voix haute et le texte arrive dans ton presse-papiers | compagnon Poly Voice |
| Tu ne sais pas quel mode prendre | pose-la telle quelle — ne choisis pas de mode toi-même | 🧭 Auto · +1✉ (ChatGPT en recommande un ; Poly redémarre avec la même question) |
| Budget de messages serré, mais tu veux deux points de vue | pose-la telle quelle | ➕ Delta · 2✉ (alternative moins chère à 🔀 Synthèse : l’ancre de Claude + la liste d’améliorations de ChatGPT — 2 messages au lieu de 3) |

## Notes de technique

- **Le Débat est un outil rare, pas un réglage par défaut.** Garde-le pour les cas où tu as vraiment besoin que quelqu’un tente de casser la conclusion : code critique, décisions où l’erreur coûte cher. L’écriture du quotidien passe par Critique ou Conseil ; les questions à fort enjeu passent par la Synthèse.
- **La touche micro** du clavier, dans la zone de question, te donne la saisie vocale sans aucun réglage.
- **Les mots modificateurs** en fin de question fonctionnent : « réponds de façon concise », « en détail », « uniquement en puces » — les modèles les suivent.
- Pour une recette que tu utilises souvent, tu peux monter un **petit raccourci dédié** : un bloc de texte contenant déjà la tâche, suivi de « Exécuter le raccourci » pointant sur Poly (la tâche devient la question pré-remplie).
- Le résultat de chaque exécution est déjà dans ton **presse-papiers** — colle-le directement dans un e-mail ou une conversation — et il est aussi enregistré dans le **journal**, `Poly-journal.md`.
