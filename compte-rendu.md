# Compte Rendu

## Partie 0 — État des lieux et préparation

### Question 1

#### Quelle est la différence entre un linter et un formatter ? Donnez un exemple de chaque en Python. <!-- rumdl-disable-line MD013 -->

Là ou un Linter va relever et notifier les erreurs de codes et mauvaises pratiques,
un formatter va venir corriger ce dernier.

Un linter populaire python est flake8 ou pylint.
Un formatter populaire est ruff ou black.

## Partie 1 — Formatage automatique avec Black

### Question 2

#### Pourquoi utilise-t-on --check dans la CI plutôt que de laisser la CI formater le code directement ? <!-- rumdl-disable-line MD013 -->

Le paramètre `--check` permet de mettre en place la partie linting de ruff et non
la partie formatter.

Effectuer un formattage ne serait pas utile car il serait perdu dans la CI actuelle.

Si on voulait vraiment l'implémenter, il faudrait effectuer un nouveau push en
fin de CI, il vaut mieux par simplicité l'avoir dans un hook.

## Partie 2 — Linting avancé avec Ruff

### Question 3

#### Quels avantages a Ruff par rapport à flake8 ? Pourquoi le fichier pyproject.toml est-il préférable à des arguments en ligne de commande ? <!-- rumdl-disable-line MD013 -->

Ruff est écrit en Rust, et donc il est plus rapide de base que flake8 qui est écrit
en python.

De plus, il permet de faire à la fois du lint et du formattage.

L'avantage de `pyproject.toml` réside dans sa portabilité, un projet initialisé
peut simplement reprendre ce fichier au lieu de passer des commandes et il sera
pareil peu importe le projet.

À noter que `pyproject.toml` peut aussi être utilisé pour `uv`, un manager de paquets
écrit en Rust bien plus rapide et modulaire que pip.

## Partie 3 — Analyse de sécurité avec Bandit et Semgrepe

### Question 4

#### Quelle est la différence entre Bandit et Semgrep ? Dans quel cas utiliseriez-vous l'un ou l'autre ? <!-- rumdl-disable-line MD013 -->

Bandit est limité à Python et utilise des règles par défaut.

Semgrep lui supporte plusieurs langages et on peut soit lui fournir des règles internes
soit télécharger des règles spécifiques.

Si l'application est entièrement codée en python, Bandit peut suffire.

À noter qu'une version OpenSource de Semgrep (Opengrep) existe.

### Question 5

#### Qu'est-ce que l'analyse statique ? En quoi diffère-t-elle des tests unitaires ? <!-- rumdl-disable-line MD013 -->

Un test statique va relever les failles de sécurité et structuelles du code
avant son exécution.

La différence est qu'un test unitaire s'assure du bon fonctionnement du code.

## Partie 4 — Pre-commit hooks

### Question 6

#### Quel est l'intérêt des pre-commit hooks par rapport à la CI ? Pourquoi utiliser les deux ? <!-- rumdl-disable-line MD013 -->

L'intérêt des pre-commits réside dans le fait de ne pas pousser de code invalide,
bien qu'il puisse être attrapé par la CI, le commit salirait l'historique, et parfois
même de manière critique (.env poussé par exemple).

La CI reste importante comme double sécurité malgré tout, et elle ne se limite pas
à ce que fait un hook, elle peut faire beaucoup d'autres taches comme du build
par exemple.

### Question 7

#### Un collègue fait un git commit --no-verify pour contourner les pre-commit hooks. Est-ce un problème ? Pourquoi ? <!-- rumdl-disable-line MD013 -->

C'est effectivement un problème, comme dit dans la question plus haut, un pre-commit
peut relever des erreurs critiques comme un .env poussé, ou des formattage de code
ne respectant pas les règles ou les standards d'entreprise.

## Partie 5 — Pipeline final et Quality Gate

### Question 8

#### Qu'est-ce qu'un Quality Gate ? Donnez 3 exemples de conditions qu'on pourrait y mettre. <!-- rumdl-disable-line MD013 -->

Selon la [documentation Sonar](https://www.sonarsource.com/resources/library/quality-gate/)
Un Quality Gate est un checkpoint qui assure que le code soit conforme aux standards
de l'entreprise et passe un pourcentage de réussite suffisant avant de passer
au prochain stade de son cycle de vie.

On peut controller par exemple:

- La documentation créée pour ce projet
- Les failles de sécurité remontées
- La validité syntaxique et structurelle du code

### Question 9

#### Décrivez l'ordre des vérifications dans votre pipeline final et expliquez pourquoi cet ordre est important. <!-- rumdl-disable-line MD013 -->

La pipeline effectue les actions suivantes de manière séquentielle:

**Job tests**:

- `actions/checkout` pour que Github accède au workspace
- `Installer Python` pour agir sur le projet codé en python
- `Cache Pip` afin de ne pas réinstaller toutes les dépendances à chaque exécution
  de la CI
- `Installer les dépendances` pour installer les dépendances
- `Formatage (black)` et `Linting (ruff)` Lint du code python
- `Sécurité (bandit) et Sécurité (bandit)` Effectue les tests de sécurité en check
  only
- `Tests + couverture` Fait une couverture du code de src grace à Pytest
- `Générer rapport couverture XML` Génère un rapport XML de ce test
- `SonarCloud Scan` Génère un rapport sur SonarCloud du dépôt
- `Sauvegarder le rapport`

**Job security**:

Vérifie les failles de dépendances au `requirements.txt` python.

### Question 10

#### Décrivez ce que vous voyez sur le tableau de bord SonarCloud de votre projet. Quel est le résultat du Quality Gate ? Quels problèmes ont été détectés ? <!-- rumdl-disable-line MD013 -->

Le dashboard présente plusieurs métriques,
Par exemple, il propose une notation de A à E sur la sécurité, fiabilité et
maintenabilité.

Le résultat de la Quality Gate est n'est pas passée car:

- La CI pointe sur la branche master du scan de SonarQube
- L'application Flask ne spécifie pas les méthodes HTTP (GET) explicitement

### Question 11

#### Comparez SonarCloud avec les outils locaux (Bandit, Semgrep, Ruff). Quels sont les avantages d'un outil centralisé comme SonarCloud en entreprise ? <!-- rumdl-disable-line MD013 -->

L'avantage d'un outil centralisé comme SonarCloud en entreprise résite surtout
dans sa partie de policies et scan.

Il est possible de faire pointer les applications vers SonarQube et ainsi imposer
des standards d'entreprise en matière de gestion de la sécurité et maintenabilité.

De cette manière, le cycle de développement devient plus résilient.

## Partie 7 — Recherche autonome

### Question 12

#### Quelles catégories de règles Ruff avez-vous ajoutées ? Pourquoi les avez-vous choisies ? Quelles erreurs ont-elles détectées dans votre code ? Indiquez le lien vers la page de documentation de chaque catégorie <!-- rumdl-disable-line MD013 -->

Ajout de la règle [PLE](https://docs.astral.sh/ruff/rules/#error-ple) pour gérer les erreurs des décorateurs, beaucoup
utilisés sur Flask.

Ajout de la règle [T20](https://docs.astral.sh/ruff/rules/#flake8-print-t20) pour éviter d'avoir des prints, il vaut mieux utiliser
`logging()`.
