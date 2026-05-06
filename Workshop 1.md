# TP : Conception Orientée Objet - Du Google Sheet à SQLite

## Contexte du Projet

L'université gère son calendrier pédagogique annuel via un fichier Google Sheets très visuel. Ce format, bien que lisible par un humain (cellules fusionnées, codes couleurs), est inexploitable directement par un système d'information informatisé.

**Votre mission :** Concevoir et développer un programme Python orienté objet capable de lire ce tableur (fourni sous forme de fichier Excel) et de transformer cette représentation visuelle en données relationnelles structurées dans une base de données SQLite.

## Étape 1 : Analyse et Modélisation (Sur Papier/Tableau)

_Objectif : Identifier les entités du système et leurs relations avant d'écrire la moindre ligne de code._

En observant la capture d'écran du calendrier pédagogique, identifiez les concepts clés de notre système d'information.

### 1.1 Identification des Classes Métier

Répondez aux questions suivantes pour définir vos classes :

1. **L'Unité de Temps :** Le calendrier est divisé en blocs logiques (les semaines). Quelles informations caractérisent une semaine ? (Proposez une classe `Semaine`).
    
2. **Le Conteneur Pédagogique :** De nombreuses cellules fusionnées dans la colonne F représentent de grands ensembles d'enseignements (ex: _INFO381 Informatique et société_). Comment modéliser cela ? (Proposez une classe `Module`).
    
3. **L'Événement Atomique :** Qu'est-ce qui se passe un jour précis (ex: un cours spécifique, un projet, un jour férié) ? C'est ce qui finira dans un agenda. Quelles informations définissent cette action ? (Proposez une classe abstraite `Evenement` et des sous-classes comme `Cours`, `ActiviteSpe`).
    

### 1.2 Conception de la Base de Données (MCD)

Traduisez vos classes en tables SQLite.

- Quelles seront les clés primaires ?
    
- Quelles sont les relations (clés étrangères) ? Par exemple : Un module contient plusieurs cours, un cours appartient à une semaine spécifique.
    

**Livrable Étape 1 :** Un diagramme de classes (UML simple) et un schéma relationnel de la base de données.

## Étape 2 : Préparation de la Persistance (Python & SQLite)

_Objectif : Implémenter les classes métiers et le service de base de données._

### 2.1 Les Classes Métier (Data Transfer Objects)

Créez un fichier `models.py`. Implémentez les classes définies à l'étape 1. Utilisez des classes Python simples (ou des `dataclasses`).

```
# Exemple de structure attendue dans models.py
class Module:
    def __init__(self, id_module, nom):
        self.id_module = id_module
        self.nom = nom

class Cours:
    def __init__(self, id_cours, date_jour, module_id, description, type_activite):
        pass # À compléter

```

### 2.2 Le Service de Base de Données

Créez un fichier `database.py`. Nous allons utiliser le pattern **DAO (Data Access Object)** ou un **Repository** simple pour isoler la logique SQL.

1. Créez une classe `DatabaseManager`.
    
2. Ajoutez une méthode `initialiser_base()` qui exécute les `CREATE TABLE` définis à l'étape 1.2.
    
3. Ajoutez des méthodes pour insérer vos objets : `inserer_module(module: Module)`, `inserer_cours(cours: Cours)`.
    

**Livrable Étape 2 :** Un script capable de créer une base SQLite vide avec les bonnes tables et des méthodes prêtes à recevoir des données.

## Étape 3 : Le Cœur du Réacteur - Le Parser

_Objectif : Créer l'algorithme capable de "lire" le tableau en gérant l'implicite (cellules fusionnées)._

_Pour simplifier ce TP, nous simulerons la lecture de la colonne "Dates" (C), "Module" (F) et "CCTL/WS" (G) via une liste de listes (représentant les lignes)._

### Le Problème des Cellules Fusionnées

Dans le tableau, la cellule "INFO381 Informatique et société" s'étale de la ligne du Lundi 15 sept. jusqu'au Vendredi 26 sept.

Lorsqu'un script lit ligne par ligne, la ligne du Lundi contient "INFO381", mais la ligne du Mardi aura une case "Module" vide !

### 3.1 La Classe `SheetParser`

Créez un fichier `parser.py` et une classe `SheetParser`.

**La Logique de l'État :**

Votre parser doit avoir une "mémoire" (des attributs de classe) pour se souvenir du contexte de la ligne précédente.

```
class SheetParser:
    def __init__(self):
        # Ces attributs conservent l'état ("l'implicite")
        self.module_courant = None
        self.semaine_courante = None

    def analyser_ligne(self, numero_ligne, date_jour, texte_module, texte_cours):
        """
        Analyse une ligne et retourne un objet Cours (ou None s'il n'y a rien).
        """
        # 1. Mise à jour du contexte (Gestion de la fusion)
        if texte_module.strip() != "":
            self.module_courant = texte_module
            # (Bonus) Gérer la création du module en BDD si c'est un nouveau
        
        # Si aucun module n'est défini et la case est vide, on ignore (ex: Lignes de week-end)
        if self.module_courant is None and texte_cours.strip() == "":
            return None
            
        # 2. Création de l'événement si du texte est présent dans la colonne cours
        if texte_cours.strip() != "":
            # On utilise le module_courant (même si texte_module est vide sur cette ligne)
            nouveau_cours = Cours(
                date_jour=date_jour,
                module_nom=self.module_courant, 
                description=texte_cours
            )
            return nouveau_cours
            
        return None

```

### 3.2 Exercice d'application du Parser

Implémentez la méthode `analyser_ligne` et testez-la avec le jeu d'essai suivant :

```
# Jeu d'essai simulant les lignes 38 à 40 du Sheet
lignes_test = [
    # [numero, date, module (Col F), cours (Col G)]
    [32, "Lundi 15 sept", "INFO381 Info et Soc", "Prosit 1 : Généralités"],
    [33, "Mardi 16 sept", "", "Prosit 2 : Principes éthiques"],
    [34, "Mercredi 17 sept", "", "[X3] CE : Histoire de l'informatique"],
    [35, "Jeudi 18 sept", "", ""], # Journée sans cours de module
    [41, "Lundi 29 sept", "Statistiques", "Statistique descriptive"],
    [42, "Mardi 30 sept", "", "Variable qualitative discrète"],
]

parser = SheetParser()
cours_extraits = []

for ligne in lignes_test:
    cours = parser.analyser_ligne(ligne[0], ligne[1], ligne[2], ligne[3])
    if cours:
        cours_extraits.append(cours)

# Vérification : Le cours "Variable qualitative discrète" doit être rattaché au module "Statistiques" et non "INFO381".

```

**Livrable Étape 3 :** Un script `parser.py` fonctionnel capable d'associer correctement un événement à son module "parent" même si la case module est vide sur sa ligne.

## Étape 4 : L'Orchestration (Le Contrôleur)

_Objectif : Lier le parser à la base de données._

Créez le point d'entrée de votre application, par exemple un fichier `main.py`.

1. Instanciez votre `DatabaseManager` et initialisez la base.
    
2. Instanciez votre `SheetParser`.
    
3. Simulez la lecture complète d'un calendrier (utilisez le jeu de données de l'étape 3 enrichi).
    
4. Pour chaque `Cours` retourné par le parser, utilisez le `DatabaseManager` pour le sauvegarder dans SQLite.
    
5. **Validation :** Écrivez une requête SQL simple à la fin du script pour afficher : "Liste de tous les cours appartenant au module INFO381".
    

## Étape 5 (Bonus : Pour aller plus loin)

Si vous avez terminé en avance :

1. **Parsing des Dates :** Actuellement, la date est un texte ("Lundi 15 sept"). Utilisez la bibliothèque `datetime` pour essayer de la convertir en vrai format date exploitable par SQLite (YYYY-MM-DD). _Astuce : il faudra utiliser l'année du calendrier !_
    
2. **Types d'activités :** En analysant le texte de la colonne G (ex: "
    
    $$X3$$
    
    CE : ..." ou "Prosit"), essayez d'extraire automatiquement le type d'activité (CE, Prosit, WS) et de le sauvegarder dans une colonne spécifique de votre base.