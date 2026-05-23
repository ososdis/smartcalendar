# ==========================================================
# Point d’entrée de l’application SmartCalendar
# ==========================================================

from data import (
    Promotion,
    Etudiant,
    Enseignant,
    UniteEnseignement,
    Cours,
    Seance,
    TypeSeance
)

from dao import EtudiantDAO
from dao import EnseignantDAO
from dao import UniteEnseignementDAO
from dao import CoursDAO
from dao import SeanceDAO

from data import CalendarManager
from data import SyncService

from data import CalendrierView


def main():

    # ======================================================
    # CRÉATION DES DAO
    # ======================================================

    etudiant_dao = EtudiantDAO()
    enseignant_dao = EnseignantDAO()
    ue_dao = UniteEnseignementDAO()
    cours_dao = CoursDAO()
    seance_dao = SeanceDAO()

    # ======================================================
    # CRÉATION DES OBJETS DTO
    # ======================================================

    promotion = Promotion(
        1,
        "Licence 2 Maintenance et Génie Industriel",
        "2025-2026"
    )

    etudiant1 = Etudiant(
        1,
        "2023/486",
        "IDY",
        "Landry",
        "idylandry03@gmail.com",
        promotion.id_promotion
    )

    enseignant1 = Enseignant(
        1,
        "EMOWA",
        "Cedric",
        "cedric.emowa@2025.ulc-icam.com"
    )

    ue1 = UniteEnseignement(
        1,
        "INFO381",
        "Programmation et Base de Données",
        5,
        promotion.id_promotion
    )

    cours1 = Cours(
        1,
        "Programmation Orientée Objet",
        45,
        ue1.id_ue,
        enseignant1.id_enseignant
    )

    seance1 = Seance(
        1,
        "2026-05-10",
        "08:00",
        "10:00",
        "Salle B12",
        False,
        cours1.id_cours,
        TypeSeance.COURS_MAGISTRAL
    )

    seance2 = Seance(
        2,
        "2026-05-11",
        "10:00",
        "12:00",
        "Labo Informatique",
        False,
        cours1.id_cours,
        TypeSeance.TP
    )

    # ======================================================
    # ENREGISTREMENT DANS LES DAO
    # ======================================================

    etudiant_dao.save(etudiant1)
    enseignant_dao.save(enseignant1)
    ue_dao.save(ue1)
    cours_dao.save(cours1)
    seance_dao.save(seance1)
    seance_dao.save(seance2)

    # ======================================================
    # SERVICES
    # ======================================================

    calendar_manager = CalendarManager(seance_dao)
    sync_service = SyncService(seance_dao)

    # ======================================================
    # VIEW
    # ======================================================

    calendrier_view = CalendrierView(calendar_manager)

    print("===================================")
    print(" SMARTCALENDAR - TEST ARCHITECTURE ")
    print("===================================")

    calendrier_view.afficher_calendrier()

    # ======================================================
    # TEST DE SYNCHRONISATION
    # ======================================================

    print("\nSynchronisation de la séance 1...")

    sync_service.synchroniser_seance(1)

    calendrier_view.afficher_calendrier()

    # ======================================================
    # TEST RECHERCHE PAR DATE
    # ======================================================

    print("\nRecherche des séances du 2026-05-11 :")

    resultats = calendar_manager.rechercher_par_date("2026-05-11")

    for seance in resultats:
        print(
            f"Séance trouvée : ID {seance.id_seance}, "
            f"{seance.heure_debut} - {seance.heure_fin}, "
            f"Salle : {seance.salle}"
        )


if __name__ == "__main__":
    main()