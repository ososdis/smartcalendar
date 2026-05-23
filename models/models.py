# ==========================================================
# Représenter les DTO du système SmartCalendar
# ==========================================================

from enum import Enum


# ==========================================================
# ENUM : TYPE DE SÉANCE
# ==========================================================

class TypeSeance(Enum):
    COURS_MAGISTRAL = "COURS_MAGISTRAL"
    TD = "TD"
    TP = "TP"
    EXAMEN = "EXAMEN"
    AUTRE_EVENEMENT = "AUTRE_EVENEMENT"


# ==========================================================
# DTO : PROMOTION
# ==========================================================

class Promotion:
    def __init__(self, id_promotion, nom_promo, annee_academique):
        self.id_promotion = id_promotion
        self.nom_promo = nom_promo
        self.annee_academique = annee_academique


# ==========================================================
# DTO : ÉTUDIANT
# ==========================================================

class Etudiant:
    def __init__(self, id_etudiant, matricule, nom, prenom, email, id_promotion):
        self.id_etudiant = id_etudiant
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.id_promotion = id_promotion


# ==========================================================
# DTO : ENSEIGNANT
# ==========================================================

class Enseignant:
    def __init__(self, id_enseignant, nom, prenom, email):
        self.id_enseignant = id_enseignant
        self.nom = nom
        self.prenom = prenom
        self.email = email


# ==========================================================
# DTO : UNITÉ D’ENSEIGNEMENT
# ==========================================================

class UniteEnseignement:
    def __init__(self, id_ue, code_ue, intitule, credits_ects, id_promotion):
        self.id_ue = id_ue
        self.code_ue = code_ue
        self.intitule = intitule
        self.credits_ects = credits_ects
        self.id_promotion = id_promotion


# ==========================================================
# DTO : COURS
# ==========================================================

class Cours:
    def __init__(self, id_cours, intitule_cours, volume_horaire, id_ue, id_enseignant):
        self.id_cours = id_cours
        self.intitule_cours = intitule_cours
        self.volume_horaire = volume_horaire
        self.id_ue = id_ue
        self.id_enseignant = id_enseignant


# ==========================================================
# DTO : SÉANCE / ÉVÉNEMENT
# ==========================================================

class Seance:
    def __init__(
        self,
        id_seance,
        date_seance,
        heure_debut,
        heure_fin,
        salle,
        est_synchronise,
        id_cours,
        type_seance
    ):
        self.id_seance = id_seance
        self.date_seance = date_seance
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
        self.salle = salle
        self.est_synchronise = est_synchronise
        self.id_cours = id_cours
        self.type_seance = type_seance