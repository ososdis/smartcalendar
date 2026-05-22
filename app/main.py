# main.py
# Point d’entrée de l’application SmartCalendar

from services.services import CalendarManager, NotificationService


def main():
    calendar = CalendarManager()
    notification_service = NotificationService()

    print("=" * 40)
    print("        SMART CALENDAR")
    print("=" * 40)

    # =========================
    # 1. Tous les événements
    # =========================
    print("\n1. Événements disponibles :")
    events = calendar.afficher_tous_les_evenements()

    if not events:
        print("Aucun événement disponible.")
    else:
        for event in events:
            print(event)

    # =========================
    # 2. Notifications
    # =========================
    print("\n2. Notifications :")
    notifications = notification_service.afficher_historique_notifications()

    if not notifications:
        print("Aucune notification.")
    else:
        for notification in notifications:
            print(notification)

    # =========================
    # 3. Emploi du temps étudiant
    # =========================
    print("\n3. Emploi du temps de l'étudiant 1 :")
    emploi = calendar.emploi_du_temps_etudiant(1)

    if not emploi:
        print("Aucun événement trouvé pour cet étudiant.")
    else:
        for event in emploi:
            print(event)


if __name__ == "__main__":
    main()