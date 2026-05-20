# Exercice 1
## Implémentation des DAOs des modèles DTO suivant le diagramme class_comp.puml

from dataclasses import dataclass
from datetime import date, time
from enum import Enum, auto

from typing_extensions import List

class BaseDAO:
    def __init__(
        self,
    ):
        self._storage = {}

    def get_by_id(
        self, id: int,
    ):
        return self._storage.get(id)

    def save(
        self, obj,
    ):
        
        if hasattr(obj, 'id'):
            key = obj.id
        elif hasattr(obj, 'id_ecurrence'):
            key = obj.id_ecurrence
        elif hasattr(obj, 'id_ue'):
            key = obj.id_ue
        elif hasattr(obj, 'id_notif'):
            key = obj.id_notif
        else:
            raise ValueError
        self._storage[key] = obj

    def delete(self, id: int):
        if id in self._storage:
            del self._storage[id]

class UserDAO(BaseDAO):
    def getUser(self, userId: int) -> Optional[UserDTO]:
        
        return self.get_by_id(userId)

class EventDAO(BaseDAO):
   
    def __init__(self):
        super().__init__()
       
        self._event_list = []   

    def save(self, obj):
        super().save(obj)
        if obj not in self._event_list:
            self._event_list.append(obj)

    def delete(self, id: int):
        obj = self.get_by_id(id)
        if obj and obj in self._event_list:
            self._event_list.remove(obj)
        super().delete(id)

    def get_by_cours(self, id_cours: int) -> List[EventDTO]:
        result = []
        for event in self._event_list:
            if hasattr(event, 'id_cours') and event.id_cours == id_cours:
                result.append(event)
        return result

    def get_by_date_range(self, start: date, end: date) -> List[EventDTO]:
        result = []
        for event in self._event_list:
            if start <= event.date <= end:
                result.append(event)
        return result

    def update_sync_status(self, id: int, status: str) -> bool:
        event = self.get_by_id(id)
        if event:
            event.statut_synchro = status
            return True
        return False

class UniteEnseignementDAO(BaseDAO):
    def get_by_promotion(self, id_promo: int) -> List[UniteEnseignementDTO]:
        result = []
        for obj in self._storage.values():
            if hasattr(obj, 'id_promo') and obj.id_promo == id_promo:
                result.append(obj)
        return result

class NotificationDAO(BaseDAO):
    def get_history(self) -> List[NotificationDTO]:
        return list(self._storage.values())

class EnseignantDAO(BaseDAO):
    def get_by_promotion(self, id_promo: int) -> List[EnseignantDTO]:
        result = []
        for obj in self._storage.values():
            if hasattr(obj, 'id_promo') and obj.id_promo == id_promo:
                result.append(obj)
        return result
