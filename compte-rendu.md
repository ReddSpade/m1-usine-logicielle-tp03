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

## Partie 3 — Analyse de sécurité avec Bandit et Semgrepe

### Question 4

#### Quelle est la différence entre Bandit et Semgrep ? Dans quel cas utiliseriez-vous l'un ou l'autre ? <!-- rumdl-disable-line MD013 -->

### Question 5

#### Qu'est-ce que l'analyse statique ? En quoi diffère-t-elle des tests unitaires ? <!-- rumdl-disable-line MD013 -->

## Partie 4 — Pre-commit hooks

### Question 6

#### Quel est l'intérêt des pre-commit hooks par rapport à la CI ? Pourquoi utiliser les deux ? <!-- rumdl-disable-line MD013 -->

### Question 7

#### Un collègue fait un git commit --no-verify pour contourner les pre-commit hooks. Est-ce un problème ? Pourquoi ? <!-- rumdl-disable-line MD013 -->

## Partie 5 — Pipeline final et Quality Gate

### Question 8

#### Qu'est-ce qu'un Quality Gate ? Donnez 3 exemples de conditions qu'on pourrait y mettre. <!-- rumdl-disable-line MD013 -->

### Question 9

#### Décrivez l'ordre des vérifications dans votre pipeline final et expliquez pourquoi cet ordre est important. <!-- rumdl-disable-line MD013 -->

### Question 10

#### Décrivez ce que vous voyez sur le tableau de bord SonarCloud de votre projet. Quel est le résultat du Quality Gate ? Quels problèmes ont été détectés ? <!-- rumdl-disable-line MD013 -->

### Question 11

#### Comparez SonarCloud avec les outils locaux (Bandit, Semgrep, Ruff). Quels sont les avantages d'un outil centralisé comme SonarCloud en entreprise ? <!-- rumdl-disable-line MD013 -->

## Partie 7 — Recherche autonome

### Question 12

#### Quelles catégories de règles Ruff avez-vous ajoutées ? Pourquoi les avez-vous choisies ? Quelles erreurs ont-elles détectées dans votre code ? Indiquez le lien vers la page de documentation de chaque catégorie <!-- rumdl-disable-line MD013 -->
