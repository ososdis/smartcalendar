# =========================
# Base DAO
# =========================

class BaseDAO:
    def get_by_id(self, id):
        pass

    def get_all(self):
        pass

    def save(self, obj):
        pass

    def delete(self, obj):
        pass


# =========================
# User DAO
# =========================

class UserDAO(BaseDAO):

    def __init__(self):
        super().__init__()

    def get_by_email(self, email):
        """
        Retourne un utilisateur à partir de son email
        """
        pass

    def update_token(self, user_id, token):
        """
        Met à jour le token utilisateur
        """
        pass


# =========================
# Event DAO
# =========================

class EventDAO(BaseDAO):

    def __init__(self):
        super().__init__()

    def get_by_course_id(self, course_id):
        """
        Retourne les événements liés à un cours
        """
        pass

    def get_by_date_range(self, start, end):
        """
        Retourne les événements entre deux dates
        """
        pass

    def update_sync_status(self, event_id, status):
        """
        Met à jour l’état de synchronisation
        """
        pass

    class EtudiantDAO(BaseDAO):

        def get_by_promotion(self, id_promo):
            pass

    class EnseignantDAO(BaseDAO):

        def get_by_ueid(self, ue_id):
            pass

    class CoursDAO(BaseDAO):

        def get_by_ueid(self, ue_id):
            pass

    class UniteEnseignementDAO(BaseDAO):

        def get_by_promotion(self, id_promo):
            pass

    class NotificationDAO(BaseDAO):

        def get_history(self):
            pass