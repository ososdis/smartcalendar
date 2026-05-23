from enum import Enum


class TypeSeance(Enum):
    COURS_MAGISTRAL = "Cours magistral"
    TD = "Travaux dirigés"
    TP = "Travaux pratiques"
    EXAMEN = "Examen"
    AUTRE = "Autre événement"


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

    def afficher_resume(self):
        return (
            f"{self.date_seance} | "
            f"{self.heure_debut}-{self.heure_fin} | "
            f"{self.salle} | "
            f"{self.type_seance.value}"
        )