import flet as ft

from Services.agenda_services import AgendaService
from Views.event_card import EventCard


class CalendrierView(ft.Column):

    def __init__(self):

        super().__init__()

        self.agenda_service = AgendaService()

        self.controls.append(
            ft.Text(
                "Calendrier pédagogique",
                size=28,
                weight=ft.FontWeight.BOLD
            )
        )

        self.charger_evenements()

    def charger_evenements(self):

        events = self.agenda_service.seance_dao.get_all()

        for e in events:

            card = EventCard(
                titre=f"Cours ID {e[6]}",
                horaire=f"{e[2]} - {e[3]}",
                salle=e[4]
            )

            self.controls.append(card)