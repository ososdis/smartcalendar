import flet as ft


def afficher_calendrier(page, gestionnaire):
    page.clean()  

    page.add(
        ft.Text("Calendrier des séances", size=24, weight="bold")
    )
    champ_date = ft.TextField(label="Rechercher par date (YYYY-MM-DD)")

    liste_seances = ft.Column()

    def afficher_seances(seances):
        liste_seances.controls.clear()

        if not seances:
            liste_seances.controls.append(ft.Text("Aucune séance trouvée"))
        else:
            for s in seances:
                statut = "Synchronisée" if s.est_synchronise else " Non synchronisée"

                carte = ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text(f"ID: {s.id_seance}", weight="bold"),
                            ft.Text(f"Date: {s.date_seance}"),
                            ft.Text(f"Heure: {s.heure_debut} - {s.heure_fin}"),
                            ft.Text(f"Salle: {s.salle}"),
                            ft.Text(f"Type: {s.type_seance.value}"),
                            ft.Text(statut),

                            ft.ElevatedButton(
                                "Synchroniser",
                                on_click=lambda e, id=s.id_seance: synchroniser(id)
                            )
                        ]),
                        padding=10
                    )
                )

                liste_seances.controls.append(carte)

        page.update()

    def rechercher(e):
        date = champ_date.value
        resultats = gestionnaire.rechercher_par_date(date)
        afficher_seances(resultats)

    def afficher_tout(e):
        seances = gestionnaire.get_all_seances()
        afficher_seances(seances)

    def synchroniser(id_seance):
        gestionnaire.synchroniser_seance(id_seance)
        afficher_seances(gestionnaire.get_all_seances())

    page.add(
        champ_date,
        ft.Row([
            ft.ElevatedButton("Rechercher", on_click=rechercher),
            ft.ElevatedButton("Afficher tout", on_click=afficher_tout),
        ]),
        liste_seances
    )


    afficher_seances(gestionnaire.get_all_seances())