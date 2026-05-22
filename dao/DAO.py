# DAO.py
# Couche DAO : Data Access Objects
# Ces classes servent à récupérer les données depuis le fichier data.py
# Auteur : Toussaint Kitsa
# Projet : SmartCalendar
# Description : Implémentation DAO + Services
import data.data as data


class BaseDAO:
    def __init__(self, source_name: str):
        self.source_name = source_name

    def _get_source(self):
        return getattr(data, self.source_name, [])

    def get_by_id(self, id_value):
        for obj in self._get_source():
            if hasattr(obj, "id") and obj.id == id_value:
                return obj
            if hasattr(obj, "id_user") and obj.id_user == id_value:
                return obj
            if hasattr(obj, "id_etudiant") and obj.id_etudiant == id_value:
                return obj
            if hasattr(obj, "id_enseignant") and obj.id_enseignant == id_value:
                return obj
            if hasattr(obj, "id_cours") and obj.id_cours == id_value:
                return obj
            if hasattr(obj, "id_promotion") and obj.id_promotion == id_value:
                return obj
            if hasattr(obj, "id_ue") and obj.id_ue == id_value:
                return obj
            if hasattr(obj, "id_notif") and obj.id_notif == id_value:
                return obj
        return None

    def get_all(self):
        return self._get_source()

    def save(self, obj):
        self._get_source().append(obj)
        return obj

    def delete(self, id_value):
        source = self._get_source()

        for obj in source:
            if (
                getattr(obj, "id", None) == id_value
                or getattr(obj, "id_user", None) == id_value
                or getattr(obj, "id_etudiant", None) == id_value
                or getattr(obj, "id_enseignant", None) == id_value
                or getattr(obj, "id_cours", None) == id_value
                or getattr(obj, "id_promotion", None) == id_value
                or getattr(obj, "id_ue", None) == id_value
                or getattr(obj, "id_notif", None) == id_value
            ):
                source.remove(obj)
                return True

        return False


class UserDAO(BaseDAO):
    def __init__(self):
        super().__init__("users")

    def get_by_email(self, email: str):
        for user in self.get_all():
            if getattr(user, "email", None) == email:
                return user
        return None

    def update_token(self, user_id: int, token: str):
        user = self.get_by_id(user_id)
        if user is not None:
            user.google_linked = True
            user.token = token
            return user
        return None


class EtudiantDAO(BaseDAO):
    def __init__(self):
        super().__init__("etudiants")

    def get_by_promotion(self, id_promo: int):
        return [
            etudiant for etudiant in self.get_all()
            if getattr(etudiant, "id_promotion", None) == id_promo
        ]


class EnseignantDAO(BaseDAO):
    def __init__(self):
        super().__init__("enseignants")

    def get_by_ue(self, id_ue: int):
        return [
            enseignant for enseignant in self.get_all()
            if getattr(enseignant, "id_ue", None) == id_ue
        ]


class PromotionDAO(BaseDAO):
    def __init__(self):
        super().__init__("promotions")


class CoursDAO(BaseDAO):
    def __init__(self):
        super().__init__("cours")

    def get_by_ue(self, id_ue: int):
        return [
            cours for cours in self.get_all()
            if getattr(cours, "id_unite_cours", None) == id_ue
            or getattr(cours, "id_ue", None) == id_ue
        ]


class EventDAO(BaseDAO):
    def __init__(self):
        super().__init__("events")

    def get_by_cours(self, id_cours: int):
        return [
            event for event in self.get_all()
            if getattr(event, "id_cours", None) == id_cours
        ]

    def get_by_date_range(self, start_date, end_date):
        return [
            event for event in self.get_all()
            if start_date <= getattr(event, "date", None) <= end_date
        ]

    def update_sync_status(self, id_event: int, status: str):
        event = self.get_by_id(id_event)
        if event is not None:
            event.status_synchro = status
            return event
        return None


class UniteEnseignementDAO(BaseDAO):
    def __init__(self):
        super().__init__("unites_enseignement")

    def get_by_promotion(self, id_promo: int):
        return [
            ue for ue in self.get_all()
            if getattr(ue, "id_promotion", None) == id_promo
        ]


class NotificationDAO(BaseDAO):
    def __init__(self):
        super().__init__("notifications")

    def get_history(self):
        return self.get_all()