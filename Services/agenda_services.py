from Models.data import EventDTO


class CalendarManager:

    def __init__(self, event_dao):
        self.event_dao = event_dao

    def import_from_csv(self, csv_path):
        print(f"Import du fichier : {csv_path}")
        # TODO : lecture du CSV

    def reschedule_event(
        self,
        event: EventDTO,
        nouvelle_date,
        nouvelle_heure_debut,
        nouvelle_heure_fin
    ):
        event.date = nouvelle_date
        event.heure_debut = nouvelle_heure_debut
        event.heure_fin = nouvelle_heure_fin

        self.event_dao.update(event)

        return event