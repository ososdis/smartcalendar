#<<<<<<< Updated upstream
#=======
# Exercice 1
## Implémentation des DAOs des modèles DTO suivant le diagramme class_comp.puml
from data import UserDTO, EtudiantDTO, CoursDTO, SeanceDTO,EnseignantDTO


class BaseDAO:

def __init__(
self, ):
pass
def get_by_id(self, id) -> UserDTO:
pass
def get_all(self) -> list:
pass
def save(self, obj) -> None:
pass
def delete(self,id) -> None:

class EtudiantDAO:
def __init__(
self,
):
pass
def get_by_id(self, id) -> EtudiantDTO:
pass
def get_all(self) -> list[EtudiantDTO]:
pass
def save(self, obj) -> None:
pass
def delete(self,id) -> None:
pass
def get_by_promotion(self, promotion_id) -> list[EtudiantDTO]:
pass

class EnseignantDAO:

def __init__(
self,
):
pass
def get_by_id(self, id) -> EnseignantDTO:
pass
def get_all(self) -> list[EnseignantDTO]:
pass
def save(self, obj) -> None:
pass
def delete(self,id) -> None:
pass
def get_by_ue(self, ue_id) -> list[EnseignantDTO]:
pass


pass
class UserDAO:
def __init__(
self,
):
pass
def get_by_id(self, id) -> UserDTO:
pass
def get_all(self) -> list[UserDTO]:
pass
def save(self, obj) -> None:
pass
def delete(self,id) -> None:
pass
def get_by_email(self, email) -> UserDTO:
pass
def update_token(self, username) -> UserDTO:
pass

class CoursDAO:

def __init__(
self,
):
pass
def get_by_id(self, id) -> CoursDTO:
pass
def get_all(self) -> list[CoursDTO]:
pass
def save(self, obj) -> None:
pass
def delete(self,id) -> None:
pass
def get_by_ue(self, ue_id) -> list[CoursDTO]:
pass

class SeanceDAO:

def __init__(
self,
):
pass
def get_by_id(self, id) -> SeanceDAO:
pass
def get_all(self) -> list[SeanceDAO]:
pass
def save(self, obj) -> None:
pass
def delete(self,id) -> None:
pass
def get_by_cours(self, cours_id) -> list[SeanceDAO]:
pass


class NotificationDAO:

def __init__(
self,
):
pass
def get_by_id(self, id) -> NotificationDAO:
pass
def get_all(self) -> list[NotificationDAO]:
pass
def save(self, obj) -> None:
pass
def delete(self,id) -> None:
pass
def get_history(self) -> list[NotificationDAO]:
pass

class UniteEnseignementDAO:

def __init__(
self,
):
pass
def get_by_id(self, id) -> UniteEnseignementDAO:
pass
def get_all(self) -> list[UniteEnseignementDAO]:
pass
def save(self, obj) -> None:
pass
def delete(self,id) -> None:
pass
def get_by_promotion(self, promotion_id) -> list[UniteEnseignementDAO]:
pass

class EventDAO:

def __init__(
self,
):
pass
def get_by_id(self, id) -> EventDAO:
pass

def get_all(self) -> list[EventDAO]:
pass
def save(self, obj) -> None:
pass
def delete(self,id) -> None:
pass
def get_by_cours(self, cours_id) -> list[EventDAO]:
pass
def get_by_date_range(self, start, end) -> list[EventDAO]:
pass
def get_sync_status(self, id, status) -> None:
pass

#>>>>>>> Stashed changes
