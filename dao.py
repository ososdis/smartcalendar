# ==========================================================
# SMARTCALENDAR - Couche DAO
# Gestion des accès aux données
# ==========================================================

from typing import List, Optional
from datetime import date

from data import (
    PromotionDTO,
    EtudiantDTO,
    EnseignantDTO,
    UniteEnseignementDTO,
    CoursDTO,
    EventDTO,
    NotificationDTO,
    UserDTO
)


# ==========================================================
# CLASSE DE BASE
# ==========================================================

class BaseDAO:
    """
    Classe générique parent de tous les DAO.
    Fournit les opérations CRUD de base.
    """

    def __init__(self):
        self.storage = []

    def get_by_id(self, obj_id: int):

        for obj in self.storage:

            # Recherche automatique d’un attribut id
            possible_ids = [
                "id",
                "id_event",
                "id_cours",
                "id_ue",
                "id_promotion",
                "id_etudiant",
                "id_enseignant",
                "id_notif"
            ]

            for attr in possible_ids:

                if hasattr(obj, attr):

                    if getattr(obj, attr) == obj_id:
                        return obj

        return None

    def get_all(self):
        return self.storage

    def save(self, obj):

        self.storage.append(obj)

    def delete(self, obj_id: int):

        obj = self.get_by_id(obj_id)

        if obj:
            self.storage.remove(obj)
            return True

        return False


# ==========================================================
# PROMOTION DAO
# ==========================================================

class PromotionDAO(BaseDAO):
    """
    DAO de gestion des promotions.
    """

    pass


# ==========================================================
# ETUDIANT DAO
# ==========================================================

class EtudiantDAO(BaseDAO):
    """
    DAO de gestion des étudiants.
    """

    def get_by_promotion(self, id_promo: int) -> List[EtudiantDTO]:

        resultats = []

        for etudiant in self.storage:

            if hasattr(etudiant, "id_promotion"):

                if etudiant.id_promotion == id_promo:
                    resultats.append(etudiant)

        return resultats


# ==========================================================
# ENSEIGNANT DAO
# ==========================================================

class EnseignantDAO(BaseDAO):
    """
    DAO de gestion des enseignants.
    """

    def get_by_ue(self, id_ue: int) -> List[EnseignantDTO]:

        resultats = []

        for enseignant in self.storage:

            if hasattr(enseignant, "id_ue"):

                if enseignant.id_ue == id_ue:
                    resultats.append(enseignant)

        return resultats


# ==========================================================
# UNITE D'ENSEIGNEMENT DAO
# ==========================================================

class UniteEnseignementDAO(BaseDAO):
    """
    DAO de gestion des unités d’enseignement.
    """

    def get_by_promotion(self, id_promo: int) -> List[UniteEnseignementDTO]:

        resultats = []

        for ue in self.storage:

            if hasattr(ue, "id_promotion"):

                if ue.id_promotion == id_promo:
                    resultats.append(ue)

        return resultats


# ==========================================================
# COURS DAO
# ==========================================================

class CoursDAO(BaseDAO):
    """
    DAO de gestion des cours.
    """

    def get_by_ue(self, id_ue: int) -> List[CoursDTO]:

        resultats = []

        for cours in self.storage:

            if hasattr(cours, "id_ue"):

                if cours.id_ue == id_ue:
                    resultats.append(cours)

        return resultats


# ==========================================================
# EVENT DAO
# ==========================================================

class EventDAO(BaseDAO):
    """
    DAO de gestion des événements calendrier.
    """

    def get_by_courseid(self, course_id: int) -> List[EventDTO]:

        resultats = []

        for event in self.storage:

            if hasattr(event, "id_cours"):

                if event.id_cours == course_id:
                    resultats.append(event)

        return resultats

    def get_by_date_range(
            self,
            start: date,
            end: date
    ) -> List[EventDTO]:

        resultats = []

        for event in self.storage:

            if hasattr(event, "date"):

                if start <= event.date <= end:
                    resultats.append(event)

        return resultats

    def update_sync_status(
            self,
            event_id: int,
            status: str
    ) -> bool:

        event = self.get_by_id(event_id)

        if event:

            event.status_synchro = status
            return True

        return False


# ==========================================================
# USER DAO
# ==========================================================

class UserDAO(BaseDAO):
    """
    DAO de gestion des utilisateurs.
    """

    def get_by_email(self, email: str) -> Optional[UserDTO]:

        for user in self.storage:

            if hasattr(user, "email"):

                if user.email == email:
                    return user

        return None

    def update_token(
            self,
            user_id: int,
            token: str
    ) -> bool:

        user = self.get_by_id(user_id)

        if user:

            user.google_token = token
            return True

        return False


# ==========================================================
# NOTIFICATION DAO
# ==========================================================

class NotificationDAO(BaseDAO):
    """
    DAO de gestion des notifications.
    """

    def get_history(self) -> List[NotificationDTO]:

        return self.storage