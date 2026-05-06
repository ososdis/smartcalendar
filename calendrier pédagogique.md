# Calendrier Pédagogique 2025-2026

Voici un Tableur  servant de référentiel pour la planification annuelle d'un cursus de formation (mention "X3" pour l'année 2025-2026).

### 1. Structure Temporelle et Axes de Lecture

Le document s'organise verticalement par une progression chronologique et horizontalement par types d'activités :

- **La Colonne B (Semaines) :** Indique le numéro de la semaine de l'année (ex: 33 à 40 visibles).
- **La Colonne C (Dates) :** Détaille chaque jour de la semaine (lundi à vendredi), utilisant un code couleur bleu pour les en-têtes de semaine.
- **L'Unité de temps :** La ligne représente la journée, mais de nombreuses cellules sont **fusionnées verticalement** pour indiquer des activités s'étalant sur plusieurs jours ou une semaine complète.

### 2. Segmentation des Contenus (Colonnes Métier)

Le calendrier répartit les informations en quatre zones de responsabilités distinctes :

- **Module (Col. F) :** Identifie l'unité d'enseignement ou la thématique majeure (ex: _INFO381 Informatique et société_, _Statistiques_). Ces cellules sont largement fusionnées, indiquant la dominance d'un sujet sur une période donnée.
- **CCTL / WS (Col. G) :** Détaille le contenu spécifique, les types de travaux (Workshops) ou les modalités de contrôle (Contrôle Continu à Temps Limité).
- **FHS (Col. H) :** Gère les Formations Humaines et Sociales, incluant les cours de langues (ex: _Anglais 3h_) ou de sciences humaines.
- **Événements & Échéancier (Col. J-K) :** Répertorie les moments clés hors-cours (rentrée, séminaires, fresque du climat, jours fériés comme l'Assomption).

### 3. Système de Codification Visuelle (La Légende)

L'efficacité du document repose sur un **code couleur strict** (présenté dans le bloc de légende en haut à droite) :

- **Jaune :** Événements de rentrée ou sessions administratives.
- **Marron/Ocre :** Projets et Workshops (WS).
- **Vert :** Cours de langues ou FHS.
- **Bleu :** Activités de promotion ou jalons temporels.
- **Gris :** Périodes de vacances ou de stages.

### 4. Caractéristiques Techniques pour l'Automatisation

Afin de réaliser l'extraction de données (Parsing), voici les défis spécifiques qui en ressortent :

- **Données Implicites :** L'année (2025/2026) est globale ; chaque ligne doit hériter de l'année et du mois de son bloc.
- **Relations Parent-Enfant :** Une ligne "Mardi" en colonne C doit être rattachée au "Module" défini dans la cellule fusionnée de la colonne F, même si la ligne correspondante en F est techniquement vide.
- **Absence d'Horaires Précis :** Les créneaux sont définis par la journée entière ou des mentions textuelles (ex: "3h"), nécessitant une logique de conversion pour les outils de calendrier (Google Calendar).
