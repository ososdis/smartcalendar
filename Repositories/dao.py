# Exercice 1
## Implémentation des DAOs des modèles DTO suivant le diagramme class_comp.puml

# Avec Python, les class Interfaces peuvent être implémentées comme des classes abstraites
# heritant de Protocol
import sqlite3
from random import randint
from typing import List, Optional, Protocol

from Models import EnseignantDTO, EtudiantDTO, UserDTO


# Exercice 2
class DAO:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._setup_db()

    def _setup_db(self):
        cursor = self.conn.cursor()

        # Réquêtes de création lors de l'initialisation des tables si elles n'existent pas
        # 1. Création de la table Users sur base de la classe UserDTO

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, role TEXT, email TEXT, logedin BOOLEAN)"
        )

        # 2. Création de la table Etudiant
        cursor.execute("""
CREATE TABLE IF NOT EXISTS etudiant (
    id_etudiant INTEGER PRIMARY KEY,
    matricule TEXT,
    nom TEXT,
    prenom TEXT,
    email TEXT,
    id_promotion INTEGER
)
""")
        # 3. Création de la table Enseignant
        cursor.execute("""
CREATE TABLE IF NOT EXISTS enseignant (
    id_enseignant INTEGER PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    email TEXT,
    id_ue INTEGER
)
""")
        # 4. Création de la table Promotion
        cursor.execute("""
CREATE TABLE IF NOT EXISTS promotion (
    id_promotion INTEGER PRIMARY KEY,
    nom_promo TEXT,
    annee_academique TEXT
)
""")

        # 5. Création de la table UniteEnseignement
        cursor.execute("""
CREATE TABLE IF NOT EXISTS unite_enseignement (
    id_ue INTEGER PRIMARY KEY,
    code_ue TEXT,
    intitule TEXT,
    credits_ects INTEGER,
    id_promotion INTEGER
)
""")
        # 6. Création de la table Cours
        cursor.execute("""
CREATE TABLE IF NOT EXISTS cours (
    id_cours INTEGER PRIMARY KEY,
    intitule_cours TEXT,
    volume_horaire INTEGER,
    id_ue INTEGER
)
""")
        # 7. Création de la table Seance
cursor.execute("""
CREATE TABLE IF NOT EXISTS seance (
    id_seance INTEGER PRIMARY KEY,
    titre TEXT,
    date TEXT,
    heure_debut TEXT,
    heure_fin TEXT,
    salle TEXT,
    statut_synchro TEXT,
    type TEXT,
    id_cours INTEGER
)
""")
        # Confirmation des réquêtes dans la transaction
        self.conn.commit()


class BaseDAO(Protocol):
    def get_by_id(self, id) -> DAO: ...

    def get_all(self) -> list[DAO]: ...

    def save(self, obj) -> int | None: ...

    def update(self, obj) -> int | None: ...

    def delete(self, obj) -> int | None: ...


class UserDAO(DAO):
    def __init__(
        self,
    ):
        # Initialisation de la connexion à la base de données
        super().__init__()

    def get_by_id(self, id: int) -> Optional[UserDTO]:
        cursor = self.conn.cursor()
        # Requete de récupération d'un utilisateur par son ID
        cursor.execute("SELECT id, role, email, logedin FROM users WHERE id = ?", (id,))
        id_user, role, email, logedin = cursor.fetchone()

        if not id_user:
            return None

        return UserDTO(id_user, role, email, logedin)

    def get_all(self) -> List[UserDTO]:
        cursor = self.conn.cursor()
        # Requete de récupération de tous les utilisateurs
        cursor.execute("SELECT * FROM users")

        return [UserDTO(r[0], r[1], r[2], r[3]) for r in cursor.fetchall()]

    def save(self, user: UserDTO) -> int | None:
        cursor = self.conn.cursor()
        auto_id = (
            user.id_user
            if user.id_user
            else (
                randint(1, 100) + cursor.lastrowid
                if cursor.lastrowid
                else randint(1, 100)
            )
        )
        cursor.execute(
            "INSERT INTO users (id, role, email, logedin) VALUES (?, ?, ?, ?)",
            (auto_id, user.role, user.email, user.logedin),
        )
        self.conn.commit()
        return cursor.lastrowid

    def update(self, user: UserDTO) -> int | None:
        cursor = self.conn.cursor()
        role, email, logedin, id = (
            user.role,
            user.email,
            user.logedin,
            user.id_user,
        )
        cursor.execute(
            "UPDATE users SET role = ? , email = ? , logedin = ? WHERE id = ?",
            (role, email, logedin, id),
        )
        self.conn.commit()
        return cursor.lastrowid

    def delete(self, user: UserDTO) -> int | None:
        cursor = self.conn.cursor()
        id = user.id_user
        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (id,),
        )
        self.conn.commit()
        return cursor.lastrowid

    def get_by_email(self, user: UserDTO) -> Optional[UserDTO]:
        cursor = self.conn.cursor()
        email = user.email
        cursor.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,),
        )
        result = cursor.fetchone()
        if result:
            return UserDTO(result[0], result[1], result[2], result[3])
        return None


# Exercice 3


class EtudiantDAO(DAO):
    def __init__(self):
        pass

    def get_by_id(self, id) -> EtudiantDTO: ...

    def get_all(self) -> list[EtudiantDTO]: ...

    def save(self, UserDTO) -> int | None: ...

    def delete(self, id: int) -> int | None: ...

    def get_by_promotion(self, promotion_id) -> list[EtudiantDTO]: ...


class EnseignantDAO(DAO):
    def __init__(self):
        pass

    def get_by_id(self, id) -> EnseignantDTO: ...

    def get_all(self) -> list[EnseignantDTO]: ...

    def save(self, EnseignantDAO) -> int | None: ...

    def delete(self, id_enseignant) -> int | None: ...

    def get_by_ue(self, ue_id) -> list[EnseignantDTO]: ...


class PromotionDAO(DAO):
    def __init__(self) -> None:
        pass


class EventDAO(DAO):
    def __init__(
        self,
    ) -> None:
        pass
