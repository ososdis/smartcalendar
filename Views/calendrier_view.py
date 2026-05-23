import flet as ft
from datetime import date


class CalendrierView(ft.Container):

    def __init__(self, agenda_service):
        super().__init__()

        self.agenda_service = agenda_service

        self.expand = True
        self.build()

    def build(self):

        seances = self.agenda_service.get_seances_par_date(date.today())

        self.content = ft.Column(
            controls=[
                ft.Text(
                    "Calendrier du jour",
                    size=24,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Column(
                    controls=[
                        ft.Text(f"{s.salle} - {s.heure_debut} à {s.heure_fin}")
                        for s in seances
                    ]
                )
            ]
        )