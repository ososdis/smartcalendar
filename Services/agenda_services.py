from datetime import date, time
from typing import List, Optional

from Models.data import SeanceDTO, CoursDTO
from DAO.DAO import EventDAO


class AgendaService:

    def __init__(self, event_dao: EventDAO):
        self.event_dao = event_dao

    # ==========================================
    # AJOUT SEANCE
    # ==========================================
    def ajouter_seance(self, seance: SeanceDTO) -> None:
        self.event_dao.save(seance)

    # ==========================================
    # SUPPRESSION
    # ==========================================
    def supprimer_seance(self, id_seance: int) -> None:
        self.event_dao.delete(id_seance)

    # ==========================================
    # LISTE PAR DATE
    # ==========================================
    def get_seances_par_date(self, jour: date) -> List[SeanceDTO]:

        toutes = self.event_dao.get_all()

        return [
            s for s in toutes
            if s.date_seance == jour
        ]

    # ==========================================
    # CONFLIT HORAIRE
    # ==========================================
    def verifier_conflit(self, nouvelle: SeanceDTO, existante: SeanceDTO) -> bool:

        if nouvelle.date_seance != existante.date_seance:
            return False

        return not (
            nouvelle.heure_fin <= existante.heure_debut
            or nouvelle.heure_debut >= existante.heure_fin
        )

    # ==========================================
    # DETECTION CONFLITS GLOBAL
    # ==========================================
    def a_conflit(self, nouvelle: SeanceDTO) -> bool:

        seances = self.event_dao.get_all()

        for s in seances:
            if self.verifier_conflit(nouvelle, s):
                return True

        return False