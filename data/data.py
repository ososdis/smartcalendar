# data.py
# Ce fichier simule une base de données avec des objets (DTO)
# Auteur : Toussaint Kitsa
# Projet : SmartCalendar
# Description : Implémentation DAO + Services
from datetime import datetime


# ================================
# ENUM (TypeSeance)
# ================================
class TypeSeance:
    COURS_MAGISTRAL = "COURS_MAGISTRAL"
    TD = "TD"
    TP = "TP"
    EXAMEN = "EXAMEN"
    AUTRE = "AUTRE_EVENEMENT"


# ================================
# DTO CLASSES
# ================================

class UserDTO:
    def __init__(self, id: int, email: str, role: str, google_linked: bool = False):
        self.id = id
        self.email = email
        self.role = role
        self.google_linked = google_linked
        self.token = None

    def __repr__(self):
        return f"UserDTO(id={self.id}, email='{self.email}', role='{self.role}')"


class EtudiantDTO:
    def __init__(self, id_etudiant: int, matricule: str, nom: str, prenom: str, email: str, id_promotion: int):
        self.id_etudiant = id_etudiant
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.id_promotion = id_promotion

    def __repr__(self):
        return f"EtudiantDTO(id={self.id_etudiant}, nom='{self.nom}', prenom='{self.prenom}')"


class EnseignantDTO:
    def __init__(self, id_enseignant: int, nom: str, prenom: str, email: str, id_ue: int):
        self.id_enseignant = id_enseignant
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.id_ue = id_ue

    def __repr__(self):
        return f"EnseignantDTO(id={self.id_enseignant}, nom='{self.nom}', prenom='{self.prenom}')"


class PromotionDTO:
    def __init__(self, id_promotion: int, nom_promo: str, annee_academique: str):
        self.id_promotion = id_promotion
        self.nom_promo = nom_promo
        self.annee_academique = annee_academique

    def __repr__(self):
        return f"PromotionDTO(id={self.id_promotion}, nom='{self.nom_promo}')"


class UniteEnseignementDTO:
    def __init__(self, id_ue: int, code_ue: str, intitule: str, credits: int, id_promotion: int):
        self.id_ue = id_ue
        self.code_ue = code_ue
        self.intitule = intitule
        self.credits = credits
        self.id_promotion = id_promotion

    def __repr__(self):
        return f"UE(id={self.id_ue}, code='{self.code_ue}', intitule='{self.intitule}')"


class CoursDTO:
    def __init__(self, id_cours: int, intitule: str, volume_horaire: int, id_ue: int):
        self.id_cours = id_cours
        self.intitule = intitule
        self.volume_horaire = volume_horaire
        self.id_ue = id_ue

    def __repr__(self):
        return f"CoursDTO(id={self.id_cours}, intitule='{self.intitule}')"


class EventDTO:
    def __init__(self, id_seance: int, titre: str, date: datetime,
                 heure_debut: str, heure_fin: str, salle: str,
                 status_synchro: str, type_seance: str, id_cours: int):
        self.id_seance = id_seance
        self.titre = titre
        self.date = date
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
        self.salle = salle
        self.status_synchro = status_synchro
        self.type = type_seance
        self.id_cours = id_cours

    def __repr__(self):
        return f"EventDTO(id={self.id_seance}, titre='{self.titre}', date={self.date.date()})"


class NotificationDTO:
    def __init__(self, id_notif: int, type: str, destinataires: list, message: str, date_envoi: datetime):
        self.id_notif = id_notif
        self.type = type
        self.destinataires = destinataires
        self.message = message
        self.date_envoi = date_envoi

    def __repr__(self):
        return f"NotificationDTO(id={self.id_notif}, message='{self.message}')"


# ================================
# DONNÉES (Simulation BD)
# ================================
# ================================
# DONNÉES (Simulation BD enrichie)
# ================================

users = [
    UserDTO(1, "admin@gmail.com", "admin"),
    UserDTO(2, "etudiant1@gmail.com", "etudiant"),
    UserDTO(3, "etudiant2@gmail.com", "etudiant"),
]

promotions = [
    PromotionDTO(1, "L2 Génie Industriel", "2025-2026"),
    PromotionDTO(2, "L3 Génie Industriel", "2025-2026"),
]

etudiants = [
    EtudiantDTO(1, "MAT001", "Kitsa", "Toussaint", "kitsatoussaint@gmail.com", 1),
    EtudiantDTO(2, "MAT002", "Mbemba", "Paul", "paul@gmail.com", 1),
    EtudiantDTO(3, "MAT003", "Ngoma", "Sarah", "sarah@gmail.com", 2),
]

enseignants = [
    EnseignantDTO(1, "Mukendi", "Jean", "jean@gmail.com", 1),
    EnseignantDTO(2, "Tshibangu", "Pierre", "pierre@gmail.com", 2),
]

unites_enseignement = [
    UniteEnseignementDTO(1, "UE101", "Electronique de puissance", 5, 1),
    UniteEnseignementDTO(2, "UE102", "Automatique", 4, 1),
    UniteEnseignementDTO(3, "UE201", "Maintenance industrielle", 5, 2),
]

cours = [
    CoursDTO(1, "Onduleur et moteurs", 30, 1),
    CoursDTO(2, "Asservissement", 25, 2),
    CoursDTO(3, "Maintenance des systèmes", 35, 3),
]

events = [
    EventDTO(1, "Cours Onduleur", datetime(2026, 5, 20), "08:00", "10:00", "Salle A", "non_sync", TypeSeance.COURS_MAGISTRAL, 1),
    EventDTO(2, "TD Onduleur", datetime(2026, 5, 21), "10:00", "12:00", "Salle B", "non_sync", TypeSeance.TD, 1),
    EventDTO(3, "Cours Automatique", datetime(2026, 5, 22), "08:00", "10:00", "Salle C", "sync", TypeSeance.COURS_MAGISTRAL, 2),
    EventDTO(4, "TP Automatique", datetime(2026, 5, 23), "13:00", "15:00", "Labo 1", "non_sync", TypeSeance.TP, 2),
    EventDTO(5, "Cours Maintenance", datetime(2026, 5, 24), "09:00", "11:00", "Salle D", "sync", TypeSeance.COURS_MAGISTRAL, 3),
]

notifications = [
    NotificationDTO(1, "INFO", ["kitsatoussaint@gmail.com"], "Cours Onduleur demain", datetime.now()),
    NotificationDTO(2, "ALERTE", ["paul@gmail.com"], "TP Automatique déplacé", datetime.now()),
]