# ==========================================================
# Vue simple pour afficher les séances du calendrier
# ==========================================================


class CalendrierView:

    def __init__(self, calendar_manager):
        self.calendar_manager = calendar_manager

    def afficher_calendrier(self):
        """
        Affiche toutes les séances enregistrées.
        """

        seances = self.calendar_manager.afficher_toutes_les_seances()

        print("\n===================================")
        print(" CALENDRIER DES SÉANCES ")
        print("===================================\n")

        if not seances:
            print("Aucune séance disponible.")
            return

        for seance in seances:
            print(
                f"ID : {seance.id_seance} | "
                f"Date : {seance.date_seance} | "
                f"Heure : {seance.heure_debut} - {seance.heure_fin} | "
                f"Salle : {seance.salle} | "
                f"Cours ID : {seance.id_cours} | "
                f"Type : {seance.type_seance.value} | "
                f"Synchronisée : {seance.est_synchronise}"
            )