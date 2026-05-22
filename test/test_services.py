from services.services import CalendarManager, NotificationService


def main():
    calendar = CalendarManager()
    notification_service = NotificationService()

    print("===== TOUS LES EVENEMENTS =====")
    print(calendar.afficher_tous_les_evenements())

    print("\n===== EVENEMENTS DU COURS 1 =====")
    print(calendar.afficher_evenements_par_cours(1))

    print("\n===== COURS DE L'UE 1 =====")
    print(calendar.afficher_cours_par_ue(1))

    print("\n===== HISTORIQUE NOTIFICATIONS =====")
    print(notification_service.afficher_historique_notifications())


if __name__ == "__main__":
    main()