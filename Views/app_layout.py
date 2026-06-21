import flet as ft

from Views.calendrier_view import CalendrierView


class AppLayout(ft.Row):

    def __init__(self):

        super().__init__(expand=True)

        sidebar = ft.Container(
            width=220,
            bgcolor=ft.Colors.BLUE_100,
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "SMARTCALENDAR",
                        size=22,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Divider(),

                    ft.Text("Tableau de bord"),
                    ft.Text("Calendrier"),
                    ft.Text("Cours"),
                    ft.Text("Promotions")
                ]
            )
        )

        main_content = ft.Container(
            expand=True,
            padding=20,
        ]