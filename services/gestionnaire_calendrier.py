from dao.seance_dao import SeanceDAO


class GestionnaireCalendrier:
    def __init__(self):
        self.dao = SeanceDAO()

    def get_all_seances(self):
        return self.dao.get_all()