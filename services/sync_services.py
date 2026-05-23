# ==========================================================
# Le service de synchronisation des séances
# ==========================================================


class SyncService:

    def __init__(self, seance_dao):
        self.seance_dao = seance_dao

    def synchroniser_seance(self, id_seance):
        """
        Marque une séance comme synchronisée.
        """

        seance = self.seance_dao.get_by_id(id_seance)

        if seance is None:
            return False

        seance.est_synchronise = True
        return True

    def synchroniser_toutes_les_seances(self):
        """
        Synchronise toutes les séances non synchronisées.
        """

        seances = self.seance_dao.get_non_synchronisees()

        for seance in seances:
            seance.est_synchronise = True

        return len(seances)