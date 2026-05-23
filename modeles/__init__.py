from enum import Enum


class TypeSeance(Enum):
    COURS_MAGISTRAL = "COURS_MAGISTRAL"
    TD = "TD"
    TP = "TP"
    EXAMEN = "EXAMEN"
    AUTRE = "AUTRE"


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