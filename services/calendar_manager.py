# ==========================================================
# C'est le service de gestion du calendrier
# ==========================================================


class CalendarManager:

    def __init__(self, seance_dao):
        self.seance_dao = seance_dao

    def ajouter_seance(self, seance):
        """
        Ajoute une séance dans le calendrier.
        """
        return self.seance_dao.save(seance)

    def afficher_toutes_les_seances(self):
        """
        Retourne toutes les séances.
        """
        return self.seance_dao.get_all()

    def rechercher_par_date(self, date_seance):
        """
        Recherche les séances d'une date donnée.
        """
        return self.seance_dao.get_by_date(date_seance)

    def obtenir_seances_non_synchronisees(self):
        """
        Retourne les séances qui ne sont pas encore synchronisées.
        """
        return self.seance_dao.get_non_synchronisees()