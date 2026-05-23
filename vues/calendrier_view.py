import flet as ft


def afficher_calendrier(page, seances):
    page.add(ft.Text("Calendrier des séances", size=20, weight="bold"))

    for s in seances:
        page.add(
            ft.Text(
                f"ID: {s.id_seance} | Date: {s.date_seance} | "
                f"{s.heure_debut}-{s.heure_fin} | Salle: {s.salle}"
            )
        )