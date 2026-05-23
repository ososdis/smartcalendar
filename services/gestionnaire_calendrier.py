from dao.seance_dao import SeanceDAO


class GestionnaireCalendrier:
    def __init__(self):
        self.seance_dao = SeanceDAO()

    def get_all_seances(self):
        return self.seance_dao.get_all()

    def rechercher_par_date(self, date_seance):
        return self.seance_dao.get_by_date(date_seance)

    def get_seances_non_synchronisees(self):
        return self.seance_dao.get_non_synchronisees()

    def synchroniser_seance(self, id_seance):
        return self.seance_dao.synchroniser(id_seance)