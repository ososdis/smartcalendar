from dataclasses import dataclass, field
from datetime import date, time, datetime
from typing import List, Optional, Dict, Any
from enum import Enum

# -------------------- DTOs --------------------
@dataclass
class UserDTO:
    id: int
    username: str
    role: str
    google_link: bool
    token: Optional[str] = None  # ajouté pour update_token

@dataclass
class EventDTO:
    id_seance: int
    titre: str
    date: date
    heure_debut: time
    heure_fin: time
    salle: str
    statut_synchro: str
    type_seance: str  # "COURS_MAGISTRAL", "TD", "TP", "EXAMEN", "AUTRE_EVENEMENT"
    cours_id: int     # ajouté pour get_by_cours

class Status(Enum):
    SUCCESS = "success"
    FAILURE = "failure"

# -------------------- BaseDAO --------------------
class BaseDAO:
    """DAO générique avec les opérations de base."""
    _storage: Dict[int, Any] = {}  # simulation d'une table

    @classmethod
    def get_by_id(cls, id: int) -> Optional[Any]:
        return cls._storage.get(id)

    @classmethod
    def save(cls, obj: Any) -> None:
        cls._storage[obj.id] = obj

    @classmethod
    def delete(cls, id: int) -> None:
        if id in cls._storage:
            del cls._storage[id]

# -------------------- UserDAO --------------------
class UserDAO(BaseDAO):
    _storage: Dict[int, UserDTO] = {}

    @classmethod
    def get_by_email(cls, email: str) -> Optional[UserDTO]:
        """Recherche un utilisateur par son email (simulation)."""
        # En réalité l'email n'est pas un champ de UserDTO.
        # On suppose ici que l'email est stocké quelque part.
        # Pour l'exemple, on va chercher dans un mapping email -> id.
        # On initialise un mapping fictif.
        if not hasattr(cls, '_email_index'):
            cls._email_index = {
                "alice@univ.fr": 1,
                "bob@univ.fr": 2
            }
        user_id = cls._email_index.get(email)
        if user_id:
            return cls.get_by_id(user_id)
        return None

    @classmethod
    def update_token(cls, token: str, user_id: int) -> Optional[UserDTO]:
        """Met à jour le token d'un utilisateur et retourne l'utilisateur modifié."""
        user = cls.get_by_id(user_id)
        if user:
            user.token = token
            cls.save(user)
            return user
        return None

# -------------------- EventDAO --------------------
class EventDAO(BaseDAO):
    _storage: Dict[int, EventDTO] = {}

    @classmethod
    def get_by_cours(cls, id_cours: int) -> List[EventDTO]:
        """Retourne tous les événements associés à un cours."""
        return [e for e in cls._storage.values() if e.cours_id == id_cours]

    @classmethod
    def get_by_date_range(cls, start: date, end: date) -> List[EventDTO]:
        """Retourne les événements dont la date est comprise entre start et end (inclus)."""
        return [e for e in cls._storage.values() if start <= e.date <= end]

    @classmethod
    def update_sync_status(cls, id_seance: int, status: str) -> Status:
        """Met à jour le statut de synchronisation d'un événement."""
        event = cls.get_by_id(id_seance)
        if event:
            event.statut_synchro = status
            cls.save(event)
            return Status.SUCCESS
        return Status.FAILURE

# -------------------- Exemple d'utilisation --------------------
if __name__ == "__main__":
    # Création de quelques utilisateurs
    u1 = UserDTO(id=1, username="alice", role="etudiant", google_link=True)
    u2 = UserDTO(id=2, username="bob", role="enseignant", google_link=False)
    UserDAO.save(u1)
    UserDAO.save(u2)

    # Test get_by_email
    user = UserDAO.get_by_email("alice@univ.fr")
    print("Utilisateur trouvé :", user)

    # Test update_token
    updated = UserDAO.update_token("abc123", 1)
    print("Token mis à jour :", updated)

    # Création d'événements
    e1 = EventDTO(id_seance=101, titre="CM Java", date=date(2025,5,10),
                  heure_debut=time(9,0), heure_fin=time(11,0),
                  salle="Amphi A", statut_synchro="OK", type_seance="COURS_MAGISTRAL",
                  cours_id=1001)
    e2 = EventDTO(id_seance=102, titre="TD Python", date=date(2025,5,12),
                  heure_debut=time(14,0), heure_fin=time(16,0),
                  salle="Salle 204", statut_synchro="PENDING", type_seance="TD",
                  cours_id=1002)
    EventDAO.save(e1)
    EventDAO.save(e2)

    # Test get_by_cours
    events_cours = EventDAO.get_by_cours(1001)
    print("Événements du cours 1001 :", events_cours)

    # Test get_by_date_range
    events_range = EventDAO.get_by_date_range(date(2025,5,10), date(2025,5,12))
    print("Événements du 10 au 12 mai :", events_range)

    # Test update_sync_status
    status_res = EventDAO.update_sync_status(102, "SYNCHRONIZED")
    print("Résultat update :", status_res)
    print("Événement après mise à jour :", EventDAO.get_by_id(102))