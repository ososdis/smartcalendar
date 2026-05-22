# services.py
# Couche services : logique métier de l'application SmartCalendar
# Auteur : Toussaint Kitsa
# Projet : SmartCalendar
# Description : Implémentation DAO + Services
from dao.DAO import (
    EventDAO,
    CoursDAO,
    NotificationDAO,
    UniteEnseignementDAO,
    EtudiantDAO
)


class CalendarManager:
    def __init__(self):
        self.event_dao = EventDAO()
        self.cours_dao = CoursDAO()
        self.ue_dao = UniteEnseignementDAO()
        self.etudiant_dao = EtudiantDAO()

    def afficher_tous_les_evenements(self):
        return self.event_dao.get_all()

    def afficher_evenements_par_cours(self, id_cours: int):
        return self.event_dao.get_by_cours(id_cours)

    def afficher_cours_par_ue(self, id_ue: int):
        return self.cours_dao.get_by_ue(id_ue)

    def emploi_du_temps_etudiant(self, id_etudiant: int):
        etudiant = self.etudiant_dao.get_by_id(id_etudiant)

        if etudiant is None:
            return []

        id_promo = etudiant.id_promotion
        unites = self.ue_dao.get_by_promotion(id_promo)

        emploi_du_temps = []

        for ue in unites:
            cours_list = self.cours_dao.get_by_ue(ue.id_ue)

            for cours in cours_list:
                events = self.event_dao.get_by_cours(cours.id_cours)
                emploi_du_temps.extend(events)

        emploi_du_temps.sort(key=lambda event: event.date)

        return emploi_du_temps


class NotificationService:
    def __init__(self):
        self.notification_dao = NotificationDAO()

    def afficher_historique_notifications(self):
        return self.notification_dao.get_history()