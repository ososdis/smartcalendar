from dao.base_dao import BaseDAO
from modeles.models import Seance, TypeSeance


class SeanceDAO(BaseDAO):
    def __init__(self):
        super().__init__()

        self.save(
            Seance(
                1, "2026-05-10", "08:00", "10:00",
                "Salle B12", False, 1, TypeSeance.COURS_MAGISTRAL
            )
        )

        self.save(
            Seance(
                2, "2026-05-11", "10:00", "12:00",
                "Labo Informatique", False, 1, TypeSeance.TP
            )
        )

    def get_by_date(self, date):
        return [s for s in self.data if s.date_seance == date]