# Exercice 1
## Implémentation des DAOs des modèles DTO suivant le diagramme class_comp.puml
class UserDAO:
    def __init__(
        self,
    ):
        pass


class EventDAO:
    def __init__(
        self,
    ):
        pass
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Any
from enum import Enum
import csv


# Énumérations 
class TypeSeance(Enum):
    COURS_MAGISTRAL = "CM"
    TD = "TD"
    TP = "TP"
    EXAMEN = "Examen"
    AUTRE_EVENEMENT = "Autre"


#  DTO (Data Transfer Objects) 
@dataclass
class PromotionDTO:
    id: Optional[int] = None
    nom: str = ""
    annonce_academique: str = ""


@dataclass
class UserDTO:
    id: Optional[int] = None
    username: str = ""
    role: str = "etudiant"  # etudiant, enseignant, admin
    google_link: bool = False
    email: str = ""
    prenom: str = ""
    nom: str = ""
    promotion_id: Optional[int] = None


@dataclass
class EnseignantDTO:
    id: Optional[int] = None
    username: str = ""
    nom: str = ""
    prenom: str = ""
    email: str = ""
    promotion_ids: List[int] = field(default_factory=list)  # promotions enseignées


@dataclass
class UniteEnseignementDTO:
    id: Optional[int] = None
    code: str = ""
    intitule: str = ""
    credits_ects: int = 0
    promotion_id: Optional[int] = None


@dataclass
class EventDTO:
    id: Optional[int] = None
    event_type: str = "cours"
    date_start: datetime = None
    date_end: datetime = None
    type_seance: TypeSeance = TypeSeance.COURS_MAGISTRAL
    unite_enseignement_id: Optional[int] = None
    description: str = ""
    sync_status: str = "synced"   # synced, pending, error


@dataclass
class NotificationDTO:
    id: Optional[int] = None
    user_id: int = 0
    message: str = ""
    date_created: datetime = field(default_factory=datetime.now)
    is_read: bool = False


#  BaseDAO abstrait 
class BaseDAO(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Any]:
        pass

    @abstractmethod
    def save(self, obj: Any) -> Any:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass


#  Implémentation concrète des DAO (mémoire) 
class InMemoryDAO(BaseDAO):
    """Implémentation générique en mémoire pour éviter la duplication de code."""
    def __init__(self):
        self._store: Dict[int, Any] = {}
        self._next_id: int = 1

    def get_by_id(self, id: int) -> Optional[Any]:
        return self._store.get(id)

    def save(self, obj: Any) -> Any:
        if obj.id is None or obj.id not in self._store:
            obj.id = self._next_id
            self._next_id += 1
        self._store[obj.id] = obj
        return obj

    def delete(self, id: int) -> bool:
        if id in self._store:
            del self._store[id]
            return True
        return False


class EventDAO(InMemoryDAO):
    def get_by_cours(self, cours_id: int) -> List[EventDTO]:
        return [ev for ev in self._store.values() if ev.unite_enseignement_id == cours_id]

    def get_by_date_range(self, start: datetime, end: datetime) -> List[EventDTO]:
        return [
            ev for ev in self._store.values()
            if start <= ev.date_start <= end
        ]

    def update_sync_status(self, event_id: int, status: str) -> Optional[EventDTO]:
        event = self.get_by_id(event_id)
        if event:
            event.sync_status = status
            self.save(event)
        return event


class UniteEnseignementDAO(InMemoryDAO):
    def get_by_promotion(self, promo_id: int) -> List[UniteEnseignementDTO]:
        return [ue for ue in self._store.values() if ue.promotion_id == promo_id]


class NotificationDAO(InMemoryDAO):
    def get_by_history(self) -> List[NotificationDTO]:
        # Retourne toutes les notifications triées par date décroissante
        return sorted(self._store.values(), key=lambda n: n.date_created, reverse=True)


class UserDAO(InMemoryDAO):
    def get_by_email(self, email: str) -> Optional[UserDTO]:
        for user in self._store.values():
            if user.email == email:
                return user
        return None

    def get_by_promotion(self, promo_id: int) -> List[UserDTO]:
        return [u for u in self._store.values() if u.promotion_id == promo_id]


class EnseignantDAO(InMemoryDAO):
    def get_by_username(self, username: str) -> Optional[EnseignantDTO]:
        for ens in self._store.values():
            if ens.username == username:
                return ens
        return None

    def get_by_promotion(self, promo_id: int) -> List[EnseignantDTO]:
        return [ens for ens in self._store.values() if promo_id in ens.promotion_ids]


#  Service de synchronisation 
class SyncService:
    def __init__(self, event_dao: EventDAO, ue_dao: UniteEnseignementDAO):
        self.event_dao = event_dao
        self.ue_dao = ue_dao

    def import_from_csv(self, file_path: str) -> int:
        """
        Importe des événements depuis un fichier CSV.
        Format attendu : event_type,date_start,date_end,type_seance,unite_enseignement_code,description
        """
        imported_count = 0
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    # Recherche de l'unité d'enseignement par son code
                    ue = None
                    for existing_ue in self.ue_dao._store.values():
                        if existing_ue.code == row['unite_enseignement_code']:
                            ue = existing_ue
                            break
                    if not ue:
                        raise ValueError(f"UE avec code {row['unite_enseignement_code']} non trouvée")

                    event = EventDTO(
                        event_type=row['event_type'],
                        date_start=datetime.fromisoformat(row['date_start']),
                        date_end=datetime.fromisoformat(row['date_end']),
                        type_seance=TypeSeance(row['type_seance']),
                        unite_enseignement_id=ue.id,
                        description=row.get('description', ''),
                        sync_status='synced'
                    )
                    self.event_dao.save(event)
                    imported_count += 1
                except Exception as e:
                    print(f"Erreur ligne {reader.line_num}: {e}")
        return imported_count

    def reschedule_event(self, event_dto: EventDTO, new_start: datetime, new_end: datetime) -> Optional[EventDTO]:
        """Modifie les dates d'un événement."""
        existing = self.event_dao.get_by_id(event_dto.id)
        if not existing:
            raise ValueError(f"Événement avec id {event_dto.id} introuvable")
        existing.date_start = new_start
        existing.date_end = new_end
        existing.sync_status = "rescheduled"
        self.event_dao.save(existing)
        return existing


#  Exemple d'utilisation 
if __name__ == "__main__":
    # Création des DAO
    event_dao = EventDAO()
    ue_dao = UniteEnseignementDAO()
    user_dao = UserDAO()
    enseignant_dao = EnseignantDAO()
    notif_dao = NotificationDAO()

    # Peupler quelques données de test
    promo = PromotionDTO(id=1, nom="INFO3", annonce_academique="Bienvenue en L3 Info")
    ue1 = UniteEnseignementDTO(code="UE101", intitule="Architecture logicielle", credits_ects=6, promotion_id=1)
    ue2 = UniteEnseignementDTO(code="UE102", intitule="Base de données", credits_ects=5, promotion_id=1)
    ue_dao.save(ue1)
    ue_dao.save(ue2)

    user = UserDTO(username="jdupont", email="jd@univ.fr", role="etudiant", promotion_id=1)
    user_dao.save(user)

    enseignant = EnseignantDTO(username="m.martin", nom="Martin", prenom="Marie", email="marie.martin@univ.fr", promotion_ids=[1])
    enseignant_dao.save(enseignant)

    # Création d'événements
    event = EventDTO(
        event_type="cours",
        date_start=datetime(2025, 3, 10, 8, 0),
        date_end=datetime(2025, 3, 10, 10, 0),
        type_seance=TypeSeance.COURS_MAGISTRAL,
        unite_enseignement_id=ue1.id,
        description="CM Architecture"
    )
    event_dao.save(event)

    # Test des méthodes
    print("=== Récupération des événements d'une UE ===")
    events_ue1 = event_dao.get_by_cours(ue1.id)
    print(events_ue1)

    print("\n=== Synchronisation depuis CSV ===")
    # Création d'un fichier CSV temporaire pour l'exemple
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', newline='', suffix='.csv', delete=False) as f:
        writer = csv.writer(f)
        writer.writerow(['event_type','date_start','date_end','type_seance','unite_enseignement_code','description'])
        writer.writerow(['cours','2025-04-01T14:00:00','2025-04-01T16:00:00','TD','UE102','TD SQL'])
        writer.writerow(['examen','2025-05-20T09:00:00','2025-05-20T11:00:00','Examen','UE101','Final'])
        temp_csv = f.name
    sync = SyncService(event_dao, ue_dao)
    imported = sync.import_from_csv(temp_csv)
    print(f"{imported} événements importés")

    print("\n=== Evénements après import ===")
    all_events = list(event_dao._store.values())
    for ev in all_events:
        print(f"- {ev.type_seance.value} : {ev.date_start} -> {ev.date_end} (UE {ev.unite_enseignement_id})")

    print("\n=== Replanification d'un événement ===")
    ev_to_resched = event_dao.get_by_id(1)
    if ev_to_resched:
        new_start = datetime(2025, 3, 12, 10, 0)
        new_end = datetime(2025, 3, 12, 12, 0)
        sync.reschedule_event(ev_to_resched, new_start, new_end)
        print(f"Événement replanifié : {event_dao.get_by_id(1).date_start}")

    # Nettoyage du fichier temporaire
    import os
    os.unlink(temp_csv)