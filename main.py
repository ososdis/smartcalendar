import flet as ft
import sqlite3

# =========================
# IMPORTS DTO / DAO / SERVICES / VIEWS
# =========================

from Models.data import UserDTO
from DAO.dao import UserDAO, EventDAO
from Services.agenda_services import AgendaService
from Services.notify_services import NotifyService

from Views.calendrier_view import CalendrierView
from Views.app_layout import AppLayout


# =========================
# MAIN APP
# =========================

def main(page: ft.Page):

    # -------------------------
    # CONFIG PAGE
    # -------------------------
    page.title = "Smart Calendar"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 1200
    page.window_height = 800

    # -------------------------
    # DATABASE CONNECTION
    # -------------------------
    conn = sqlite3.connect("database.db")

    # -------------------------
    # DAOs
    # -------------------------
    user_dao = UserDAO(conn)
    event_dao = EventDAO(conn)

    # -------------------------
    # SERVICES
    # -------------------------
    agenda_service = AgendaService(event_dao)
    notify_service = NotifyService()

    # -------------------------
    # USER TEST (TEMPORAIRE)
    # -------------------------
    user = UserDTO(
        id_user=1,
        role="Etudiant",
        email="test@gmail.com",
        logged_in=True
    )

    # -------------------------
    # VIEWS
    # -------------------------
    calendrier_view = CalendrierView(agenda_service)

    # sidebar simple (temporaire)
    sidebar = ft.Container(
        width=200,
        bgcolor="#111827",
        content=ft.Column(
            controls=[
                ft.Text("MENU", color="white"),
                ft.Text("Calendrier", color="white"),
            ]
        )
    )

    app = AppLayout(
        sidebar=sidebar,
        content=calendrier_view
    )

    # -------------------------
    # AJOUT UI
    # -------------------------
    page.add(app)


# =========================
# RUN APP
# =========================

ft.app(target=main)