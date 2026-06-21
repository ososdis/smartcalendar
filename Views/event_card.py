import flet as ft


class EventCard(ft.Card):

    def __init__(
        self,
        titre,
        horaire,
        salle
    ):

        super().__init__()

        self.content = ft.Container(
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text(
                        titre,
                        size=18,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Text(horaire),

                    ft.Text(f"Salle : {salle}")
                ]
            )
        )