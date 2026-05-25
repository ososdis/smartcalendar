import sqlite3
from typing import List, Optional

from Models.data import (
    UserDTO,
    SeanceDTO,
    TypeSeance,
)


# ==========================================
# BASE DAO
# ==========================================

class DAO:

    def __init__(self, db_path: str = "smartcalendar.db"):

        self.conn = sqlite3.connect(
            db_path,
            check_same_thread=False
        )

        self._setup_db()

    def _setup_db(self):

        cursor = self.conn.cursor()

        # ==========================================
        # USERS
        # ==========================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id_user INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            logged_in BOOLEAN NOT NULL
        )
        """)

        # ==========================================
        # SEANCES
        # ==========================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS seances (
            id_seance INTEGER PRIMARY KEY AUTOINCREMENT,
            date_seance TEXT NOT NULL,
            heure_debut TEXT NOT NULL,
            heure_fin TEXT NOT NULL,
            salle TEXT NOT NULL,
            est_synchro BOOLEAN NOT NULL,
            cours_id INTEGER NOT NULL,
            type_seance TEXT NOT NULL
        )
        """)

        self.conn.commit()


# ==========================================
# USER DAO
# ==========================================

class UserDAO(DAO):

    def __init__(self):
        super().__init__()

    def save(self, user: UserDTO):

        cursor = self.conn.cursor()

        cursor.execute(
        return cursor.fetchall()