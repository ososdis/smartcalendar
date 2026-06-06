import sqlite3
from typing import Protocol

from Models.data import (
    UserDTO,
    EtudiantDTO,
    EnseignantDTO,
    PromotionDTO,
    UniteEnseignementDTO,
    CoursDTO,
    EventDTO,
    NotificationDTO,
)


# ==========================
# CLASSE DAO DE BASE
# ==========================

class DAO:
    def __init__(self, db_path=":memory:"):
        self.conn = sqlite3.connect(db_path)


# ==========================
# INTERFACE DAO
# ==========================

class BaseDAO(Protocol):

    def get_by_id(self, id):
        ...

    def get_all(self):
        ...

    def save(self, obj):
        ...

    def update(self, obj):
        ...

    def delete(self, obj):
        ...


# ==========================
# USER DAO
# ==========================

class UserDAO(DAO):

    def get_by_email(self, email):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        )
        return cursor.fetchone()


# ==========================
# ETUDIANT DAO
# ==========================

class EtudiantDAO(DAO):

    def get_by_promotion(self, id_promotion):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM etudiant WHERE id_promotion=?",
            (id_promotion,)
        )
        return cursor.fetchall()


# ==========================
# ENSEIGNANT DAO
# ==========================

class EnseignantDAO(DAO):

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM enseignant")
        return cursor.fetchall()


# ==========================
# COURS DAO
# ==========================

class CoursDAO(DAO):

    def get_by_ue(self, id_ue):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM cours WHERE id_ue=?",
            (id_ue,)
        )
        return cursor.fetchall()


# ==========================
# EVENT DAO
# ==========================

class EventDAO(DAO):

    def get_by_cours(self, id_cours):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM seance WHERE id_cours=?",
            (id_cours,)
        )
        return cursor.fetchall()

    def get_by_date_range(self, start_date, end_date):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT * FROM seance
            WHERE date BETWEEN ? AND ?
            """,
            (start_date, end_date)
        )
        return cursor.fetchall()

    def update_sync_status(self, id_seance, status):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            UPDATE seance
            SET synchro=?
            WHERE id_seance=?
            """,
            (status, id_seance)
        )
        self.conn.commit()