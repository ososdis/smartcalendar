from dao.base_dao import BaseDAO
from modeles.models import Seance, TypeSeance


class SeanceDAO(BaseDAO):
    def __init__(self):
        super().__init__()

        
        self.save(
            Seance(
                1,
                "2026-05-10",
                "08:00",
                "10:00",
                "Salle B12",
                False,
                1,
                TypeSeance.COURS_MAGISTRAL
            )
        )

        self.save(
            Seance(
                2,
                "2026-05-11",
                "10:00",
                "12:00",
                "Labo Informatique",
                False,
                1,
                TypeSeance.TP
            )
        )

        self.save(
            Seance(
                3,
                "2026-05-12",
                "13:00",
                "15:00",
                "Salle A5",
                True,
                2,
                TypeSeance.TD
            )
        )

    def get_by_date(self, date_seance):
        """
        Retourne les séances prévues à une date donnée
        """
        return [
            seance for seance in self.data
            if seance.date_seance == date_seance
        ]

    def get_non_synchronisees(self):
        """
        Retourne les séances qui ne sont pas encore synchronisées
        """
        return [
            seance for seance in self.data
            if seance.est_synchronise is False
        ]

    def synchroniser(self, id_seance):
        """
        Change le statut d'une séance en synchronisé
        """
        seance = self.get_by_id(id_seance)

        if seance is None:
            return False

        seance.est_synchronise = True
        return True