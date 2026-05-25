from dataclasses import dataclass, field
from typing import List


# ==========================================
# ENUMS
# ==========================================

class TypeSeance(Enum):
    COURS_MAGISTRAL = auto()
    TD = auto()
    TP = auto()
    EXAMEN = auto()
    AUTRE_EVENEMENT = auto()


# ==========================================
# DTOs
# ==========================================

@dataclass
class UserDTO:
    id_user: int
    role: str
    email: str
    logged_in: bool


@dataclass
class EtudiantDTO:
    id_etudiant: int
    matricule: str
    nom: str
    prenom: str
    email: str
    promotion_id: int


@dataclass
class EnseignantDTO:
    id_enseignant: int
    nom: str
    prenom: str
    email: str


@dataclass
class PromotionDTO:
    id_promotion: int
    nom_promo: str
    annee_academique: str

    etudiants: List[EtudiantDTO] = field(default_factory=list)


@dataclass
class UniteEnseignementDTO:
    id_ue: int
    code_ue: str
    intitule: str
    credit_ects: int
    promotion_id: int


@dataclass
class CoursDTO:
    id_cours: int
    intitule: str
    volume_horaire: int
    ue_id: int
    enseignant_id: int


@dataclass
class SeanceDTO:
    id_seance: int
    date_seance: date
    heure_debut: time
    heure_fin: time
    salle: str
    est_synchro: bool
    cours_id: int
    type_seance: TypeSeance