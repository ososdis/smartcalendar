import sqlite3
from typing import List, Optional, Protocol

from Models import EnseignantDTO, EtudiantDTO, UserDTO


class DAO:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._setup_db()

    def _setup_db(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT,
                email TEXT UNIQUE,
                logedin BOOLEAN
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS promotion (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS etudiant (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user INTEGER,
                matricule TEXT,
                promotion_id INTEGER,
                FOREIGN KEY(id_user) REFERENCES users(id),
                FOREIGN KEY(promotion_id) REFERENCES promotion(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS enseignant (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user INTEGER,
                matricule TEXT,
                specialite TEXT,
                FOREIGN KEY(id_user) REFERENCES users(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS unite_enseignement (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                enseignant_id INTEGER,
                FOREIGN KEY(enseignant_id) REFERENCES enseignant(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cours (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                ue_id INTEGER,
                FOREIGN KEY(ue_id) REFERENCES unite_enseignement(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cours_id INTEGER,
                date TEXT,
                heure_debut TEXT,
                heure_fin TEXT,
                FOREIGN KEY(cours_id) REFERENCES cours(id)
            )
        """)

        self.conn.commit()


class BaseDAO(Protocol):
    def get_by_id(self, id): ...

    def get_all(self): ...

    def save(self, obj) -> int | None: ...

    def update(self, obj) -> int | None: ...

    def delete(self, obj) -> int | None: ...


class UserDAO(DAO):
    def __init__(self, db_path: str = ":memory:"):
        super().__init__(db_path)

    def get_by_id(self, id: int) -> Optional[UserDTO]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, role, email, logedin FROM users WHERE id = ?", (id,))
        result = cursor.fetchone()

        if result is None:
            return None

        return UserDTO(result[0], result[1], result[2], result[3])

    def get_all(self) -> List[UserDTO]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, role, email, logedin FROM users")

        return [UserDTO(r[0], r[1], r[2], r[3]) for r in cursor.fetchall()]

    def save(self, user: UserDTO) -> int | None:
        cursor = self.conn.cursor()

        cursor.execute(
            "INSERT INTO users (role, email, logedin) VALUES (?, ?, ?)",
            (user.role, user.email, user.logedin),
        )

        self.conn.commit()
        return cursor.lastrowid

    def update(self, user: UserDTO) -> int | None:
        cursor = self.conn.cursor()

        cursor.execute(
            """
            UPDATE users
            SET role = ?, email = ?, logedin = ?
            WHERE id = ?
            """,
            (user.role, user.email, user.logedin, user.id_user),
        )

        self.conn.commit()
        return cursor.rowcount

    def delete(self, user: UserDTO) -> int | None:
        cursor = self.conn.cursor()

        cursor.execute("DELETE FROM users WHERE id = ?", (user.id_user,))

        self.conn.commit()
        return cursor.rowcount

    def get_by_email(self, email: str) -> Optional[UserDTO]:
        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT id, role, email, logedin FROM users WHERE email = ?",
            (email,),
        )

        result = cursor.fetchone()

        if result is None:
            return None

        return UserDTO(result[0], result[1], result[2], result[3])


class EtudiantDAO(DAO):
    def __init__(self, db_path: str = ":memory:"):
        super().__init__(db_path)

    def get_by_id(self, id: int) -> Optional[EtudiantDTO]:
        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT id, id_user, matricule, promotion_id
            FROM etudiant
            WHERE id = ?
            """,
            (id,),
        )

        result = cursor.fetchone()

        if result is None:
            return None

        return EtudiantDTO(result[0], result[1], result[2], result[3])

    def get_all(self) -> List[EtudiantDTO]:
        cursor = self.conn.cursor()

        cursor.execute("SELECT id, id_user, matricule, promotion_id FROM etudiant")

        return [EtudiantDTO(r[0], r[1], r[2], r[3]) for r in cursor.fetchall()]

    def save(self, etudiant: EtudiantDTO) -> int | None:
        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT INTO etudiant (id_user, matricule, promotion_id)
            VALUES (?, ?, ?)
            """,
            (
                etudiant.id_user,
                etudiant.matricule,
                etudiant.promotion_id,
            ),
        )

        self.conn.commit()
        return cursor.lastrowid

    def update(self, etudiant: EtudiantDTO) -> int | None:
        cursor = self.conn.cursor()

        cursor.execute(
            """
            UPDATE etudiant
            SET id_user = ?, matricule = ?, promotion_id = ?
            WHERE id = ?
            """,
            (
                etudiant.id_user,
                etudiant.matricule,
                etudiant.promotion_id,
                etudiant.id_etudiant,
            ),
        )

        self.conn.commit()
        return cursor.rowcount

    def delete(self, id: int) -> int | None:
        cursor = self.conn.cursor()

        cursor.execute("DELETE FROM etudiant WHERE id = ?", (id,))

        self.conn.commit()
        return cursor.rowcount

    def get_by_promotion(self, promotion_id: int) -> List[EtudiantDTO]:
        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT id, id_user, matricule, promotion_id
            FROM etudiant
            WHERE promotion_id = ?
            """,
            (promotion_id,),
        )

        return [EtudiantDTO(r[0], r[1], r[2], r[3]) for r in cursor.fetchall()]


class EnseignantDAO(DAO):
    def __init__(self, db_path: str = ":memory:"):
        super().__init__(db_path)

    def get_by_id(self, id: int) -> Optional[EnseignantDTO]:
        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT id, id_user, matricule, specialite
            FROM enseignant
            WHERE id = ?
            """,
            (id,),
        )

        result = cursor.fetchone()

        if result is None:
            return None

        return EnseignantDTO(result[0], result[1], result[2], result[3])

    def get_all(self) -> List[EnseignantDTO]:
        cursor = self.conn.cursor()

        cursor.execute("SELECT id, id_user, matricule, specialite FROM enseignant")

        return [EnseignantDTO(r[0], r[1], r[2], r[3]) for r in cursor.fetchall()]

    def save(self, enseignant: EnseignantDTO) -> int | None:
        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT INTO enseignant (id_user, matricule, specialite)
            VALUES (?, ?, ?)
            """,
            (
                enseignant.id_user,
                enseignant.matricule,
                enseignant.specialite,
            ),
        )

        self.conn.commit()
        return cursor.lastrowid

    def update(self, enseignant: EnseignantDTO) -> int | None:
        cursor = self.conn.cursor()

        cursor.execute(
            """
            UPDATE enseignant
            SET id_user = ?, matricule = ?, specialite = ?
            WHERE id = ?
            """,
            (
                enseignant.id_user,
                enseignant.matricule,
                enseignant.specialite,
                enseignant.id_enseignant,
            ),
        )

        self.conn.commit()
        return cursor.rowcount

    def delete(self, id_enseignant: int) -> int | None:
        cursor = self.conn.cursor()

        cursor.execute("DELETE FROM enseignant WHERE id = ?", (id_enseignant,))

        self.conn.commit()
        return cursor.rowcount

    def get_by_ue(self, ue_id: int) -> List[EnseignantDTO]:
        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT e.id, e.id_user, e.matricule, e.specialite
            FROM enseignant e
            INNER JOIN unite_enseignement ue
                ON ue.enseignant_id = e.id
            WHERE ue.id = ?
            """,
            (ue_id,),
        )

        return [EnseignantDTO(r[0], r[1], r[2], r[3]) for r in cursor.fetchall()]


class PromotionDAO(DAO):
    def __init__(self, db_path: str = ":memory:"):
        super().__init__(db_path)


class EventDAO(DAO):
    def __init__(self, db_path: str = ":memory:"):
        super().__init__(db_path)