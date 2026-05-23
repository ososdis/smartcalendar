from __future__ import annotations

from datetime import date, time
from enum import Enum, auto
from typing import List


# ==========================================
# ENUMS
# ==========================================

class TypeSeance(Enum):
    COURS_MAGISTRAL = auto()
    TD = auto()
    TP = auto()
    EXAMEN = auto()
    AUTRE_EVENEMENT = auto()


# ==========================================
# USER DTO
# ==========================================

class UserDTO:

    def __init__(
        self,
        id_user: int,
        role: str,
        email: str,
        logged_in: bool = False,
    ):

        self.id_user = id_user
        self.role = role
        self.email = email
        self.logged_in = logged_in


# ==========================================
# PROMOTION DTO
# ==========================================

class PromotionDTO:

    def __init__(
        self,
        id_promotion: int,
        nom_promo: str,
        annee_academique: str,
    ):

        self.id_promotion = id_promotion
        self.nom_promo = nom_promo
        self.annee_academique = annee_academique

        self.etudiants: List[EtudiantDTO] = []
        self.unites_enseignement: List[UniteEnseignementDTO] = []


# ==========================================
# ETUDIANT DTO
# ==========================================

class EtudiantDTO:

    def __init__(
        self,
        id_etudiant: int,
        matricule: str,
        nom: str,
        prenom: str,
        email: str,
        promotion_id: int,
    ):

        self.id_etudiant = id_etudiant
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.promotion_id = promotion_id


# ==========================================
# ENSEIGNEMENT DTO
# ==========================================

class UniteEnseignementDTO:

    def __init__(
        self,
        id_ue: int,
        code_ue: str,
        intitule: str,
        credits_ects: int,
        promotion_id: int,
    ):

        self.id_ue = id_ue
        self.code_ue = code_ue
        self.intitule = intitule
        self.credits_ects = credits_ects
        self.promotion_id = promotion_id

        self.cours: List[CoursDTO] = []


# ==========================================
# ENSEIGNANT DTO
# ==========================================

class EnseignantDTO:

    def __init__(
        self,
        id_enseignant: int,
        nom: str,
        prenom: str,
        email: str,
    ):

        self.id_enseignant = id_enseignant
        self.nom = nom
        self.prenom = prenom
        self.email = email

        self.cours: List[CoursDTO] = []


# ==========================================
# COURS DTO
# ==========================================

class CoursDTO:

    def __init__(
        self,
        id_cours: int,
        intitule: str,
        volume_horaire: int,
        ue_id: int,
        enseignant_id: int,
    ):

        self.id_cours = id_cours
        self.intitule = intitule
        self.volume_horaire = volume_horaire
        self.ue_id = ue_id
        self.enseignant_id = enseignant_id

        self.seances: List[SeanceDTO] = []


# ==========================================
# SEANCE DTO
# ==========================================

class SeanceDTO:

    def __init__(
        self,
        id_seance: int,
        date_seance: date,
        heure_debut: time,
        heure_fin: time,
        salle: str,
        est_synchro: bool,
        cours_id: int,
        type_seance: TypeSeance,
    ):

        self.id_seance = id_seance
        self.date_seance = date_seance
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
        self.salle = salle
        self.est_synchro = est_synchro
        self.cours_id = cours_id
        self.type_seance = type_seance