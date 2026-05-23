import sqlite3
from typing import Optional

from Models.data import (
    UserDTO,
    EtudiantDTO,
    EnseignantDTO,
)


# ==========================================
# BASE DAO
# ==========================================

class BaseDAO:

    def get_by_id(self, id):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def save(self, obj):
        raise NotImplementedError

    def delete(self, id):
        raise NotImplementedError


# ==========================================
# USER DAO
# ==========================================

class UserDAO(BaseDAO):

    def __init__(self, connection):

        self.conn = connection

    def get_by_id(self, id_user: int) -> Optional[UserDTO]:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT id, role, email, logged_in
            FROM users
            WHERE id = ?
            """,
            (id_user,)
        )

        result = cursor.fetchone()

        if result is None:
            return None

        return UserDTO(*result)

    def get_all(self) -> list[UserDTO]:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT id, role, email, logged_in
            FROM users
            """
        )

        results = cursor.fetchall()

        return [UserDTO(*row) for row in results]

    def save(self, user: UserDTO) -> None:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT INTO users (
                id,
                role,
                email,
                logged_in
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                user.id_user,
                user.role,
                user.email,
                user.logged_in
            )
        )

        self.conn.commit()

    def delete(self, id_user: int) -> None:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            DELETE FROM users
            WHERE id = ?
            """,
            (id_user,)
        )

        self.conn.commit()

    def get_by_email(self, email: str) -> Optional[UserDTO]:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT id, role, email, logged_in
            FROM users
            WHERE email = ?
            """,
            (email,)
        )

        result = cursor.fetchone()

        if result is None:
            return None

        return UserDTO(*result)


# ==========================================
# ETUDIANT DAO
# ==========================================

class EtudiantDAO(BaseDAO):

    def __init__(self, connection):

        self.conn = connection

    def get_by_id(self, id_etudiant: int) -> Optional[EtudiantDTO]:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                id_etudiant,
                matricule,
                nom,
                prenom,
                email,
                promotion_id
            FROM etudiants
            WHERE id_etudiant = ?
            """,
            (id_etudiant,)
        )

        result = cursor.fetchone()

        if result is None:
            return None

        return EtudiantDTO(*result)

    def get_all(self) -> list[EtudiantDTO]:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                id_etudiant,
                matricule,
                nom,
                prenom,
                email,
                promotion_id
            FROM etudiants
            """
        )

        results = cursor.fetchall()

        return [EtudiantDTO(*row) for row in results]

    def save(self, etudiant: EtudiantDTO) -> None:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT INTO etudiants (
                id_etudiant,
                matricule,
                nom,
                prenom,
                email,
                promotion_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                etudiant.id_etudiant,
                etudiant.matricule,
                etudiant.nom,
                etudiant.prenom,
                etudiant.email,
                etudiant.promotion_id
            )
        )

        self.conn.commit()

    def delete(self, id_etudiant: int) -> None:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            DELETE FROM etudiants
            WHERE id_etudiant = ?
            """,
            (id_etudiant,)
        )

        self.conn.commit()

    def get_by_promotion(
        self,
        promotion_id: int
    ) -> list[EtudiantDTO]:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                id_etudiant,
                matricule,
                nom,
                prenom,
                email,
                promotion_id
            FROM etudiants
            WHERE promotion_id = ?
            """,
            (promotion_id,)
        )

        results = cursor.fetchall()

        return [EtudiantDTO(*row) for row in results]


# ==========================================
# ENSEIGNANT DAO
# ==========================================

class EnseignantDAO(BaseDAO):

    def __init__(self, connection):

        self.conn = connection

    def get_by_id(
        self,
        id_enseignant: int
    ) -> Optional[EnseignantDTO]:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                id_enseignant,
                nom,
                prenom,
                email
            FROM enseignants
            WHERE id_enseignant = ?
            """,
            (id_enseignant,)
        )

        result = cursor.fetchone()

        if result is None:
            return None

        return EnseignantDTO(*result)

    def get_all(self) -> list[EnseignantDTO]:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                id_enseignant,
                nom,
                prenom,
                email
            FROM enseignants
            """
        )

        results = cursor.fetchall()

        return [EnseignantDTO(*row) for row in results]

    def save(self, enseignant: EnseignantDTO) -> None:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT INTO enseignants (
                id_enseignant,
                nom,
                prenom,
                email
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                enseignant.id_enseignant,
                enseignant.nom,
                enseignant.prenom,
                enseignant.email
            )
        )

        self.conn.commit()

    def delete(self, id_enseignant: int) -> None:

        cursor = self.conn.cursor()

        cursor.execute(
            """
            DELETE FROM enseignants
            WHERE id_enseignant = ?
            """,
            (id_enseignant,)
        )

        self.conn.commit()

    def get_by_ue(
        self,
        ue_id: int
    ) -> list[EnseignantDTO]:

        # A compléter selon relations SQL
        return []


# ==========================================
# PROMOTION DAO
# ==========================================

class PromotionDAO(BaseDAO):

    def __init__(self, connection):

        self.conn = connection


# ==========================================
# EVENT DAO
# ==========================================

class EventDAO(BaseDAO):

    def __init__(self, connection):

        self.conn = connection