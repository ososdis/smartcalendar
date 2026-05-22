from dao.DAO  import (
    UserDAO,
    EtudiantDAO,
    EnseignantDAO,
    PromotionDAO,
    CoursDAO,
    EventDAO,
    UniteEnseignementDAO,
    NotificationDAO
)


def main():
    user_dao = UserDAO()
    etudiant_dao = EtudiantDAO()
    enseignant_dao = EnseignantDAO()
    promotion_dao = PromotionDAO()
    ue_dao = UniteEnseignementDAO()
    cours_dao = CoursDAO()
    event_dao = EventDAO()
    notification_dao = NotificationDAO()

    print("===== USERS =====")
    print(user_dao.get_all())

    print("\n===== USER PAR EMAIL =====")
    print(user_dao.get_by_email("admin@gmail.com"))

    print("\n===== ETUDIANTS PROMOTION 1 =====")
    print(etudiant_dao.get_by_promotion(1))

    print("\n===== ENSEIGNANTS UE 1 =====")
    print(enseignant_dao.get_by_ue(1))

    print("\n===== PROMOTIONS =====")
    print(promotion_dao.get_all())

    print("\n===== UNITES ENSEIGNEMENT PROMOTION 1 =====")
    print(ue_dao.get_by_promotion(1))

    print("\n===== COURS UE 1 =====")
    print(cours_dao.get_by_ue(1))

    print("\n===== EVENTS COURS 1 =====")
    print(event_dao.get_by_cours(1))

    print("\n===== NOTIFICATIONS =====")
    print(notification_dao.get_history())


if __name__ == "__main__":
    main()