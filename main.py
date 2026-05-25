import flet as ft

from Views.app_layout import AppLayout


def main(page: ft.Page):

    page.title = "SMARTCALENDAR"

    page.window_width = 1200
    page.window_height = 700

    page.padding = 0

    page.add(
        AppLayout()
    )


ft.app(target=main)== "__main__":
    main()
