# Repositories/dao.py
# Implémentation complète DAO avec SQLite

import sqlite3
from typing import Protocol

from Models.data import (
    UserDTO,
    EtudiantDTO,
    EnseignantDTO,
    PromotionDTO,
    UniteEnseignementDTO,
    CoursDTO,
    SeanceDTO,
)


class DAO:
    def __init__(self, db_path: str = "smartcalendar.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._setup_db()

    def _setup_db(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                role TEXT,
                email TEXT,
                google_linked BOOLEAN
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS promotions (
                id_promotion INTEGER PRIMARY KEY,
                nom_promotion TEXT,
                annee_academique TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS etudiants (
                id_etudiant INTEGER PRIMARY KEY,
                matricule TEXT,
                nom TEXT,
                prenom TEXT,
                email TEXT,
                id_promotion INTEGER
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS enseignants (
                id_enseignant INTEGER PRIMARY KEY,
                nom TEXT,
                prenom TEXT,
                email TEXT,
                id_ue INTEGER
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS unites_enseignement (
                id_ue INTEGER PRIMARY KEY,
                code_ue TEXT,
                intitule TEXT,
                credits_ects INTEGER,
                id_promotion INTEGER
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cours (
                id_cours INTEGER PRIMARY KEY,
                intitule TEXT,
                volume_horaire INTEGER,
                id_ue INTEGER
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seances (
                id_seance INTEGER PRIMARY KEY,
                titre TEXT,
                date TEXT,
                heure_debut TEXT,
                heure_fin TEXT,
                salle TEXT,
                status_synchro TEXT,
                type TEXT,
                id_cours INTEGER
            )
        """)

        self.conn.commit()


class BaseDAO(Protocol):
    def get_by_id(self, id): ...
    def get_all(self): ...
    def save(self, obj): ...
    def delete(self, id): ...


class UserDAO(DAO):
    def get_all(self):
        rows = self.conn.cursor().execute("SELECT * FROM users").fetchall()

        return [
            UserDTO(row["id"], row["role"], row["email"], bool(row["google_linked"]))
            for row in rows
        ]

    def get_by_id(self, id):
        row = self.conn.cursor().execute(
            "SELECT * FROM users WHERE id = ?",
            (id,)
        ).fetchone()

        if row is None:
            return None

        return UserDTO(
            row["id"],
            row["role"],
            row["email"],
            bool(row["google_linked"])
        )

    def save(self, user: UserDTO):
        self.conn.cursor().execute(
            "INSERT OR REPLACE INTO users VALUES (?, ?, ?, ?)",
            (
                user.id,
                user.role,
                user.email,
                int(user.google_linked)
            )
        )
        self.conn.commit()

    def delete(self, id):
        self.conn.cursor().execute(
            "DELETE FROM users WHERE id = ?",
            (id,)
        )
        self.conn.commit()

    def get_by_email(self, email):
        row = self.conn.cursor().execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        if row is None:
            return None

        return UserDTO(
            row["id"],
            row["role"],
            row["email"],
            bool(row["google_linked"])
        )


class EtudiantDAO(DAO):
    def get_all(self):
        rows = self.conn.cursor().execute("SELECT * FROM etudiants").fetchall()
        return [EtudiantDTO(*row) for row in rows]

    def get_by_id(self, id):
        row = self.conn.cursor().execute(
            "SELECT * FROM etudiants WHERE id_etudiant = ?",
            (id,)
        ).fetchone()

        if row is None:
            return None

        return EtudiantDTO(*row)

    def save(self, etudiant: EtudiantDTO):
        self.conn.cursor().execute(
            "INSERT OR REPLACE INTO etudiants VALUES (?, ?, ?, ?, ?, ?)",
            (
                etudiant.id_etudiant,
                etudiant.matricule,
                etudiant.nom,
                etudiant.prenom,
                etudiant.email,
                etudiant.id_promotion
            )
        )
        self.conn.commit()

    def delete(self, id):
        self.conn.cursor().execute(
            "DELETE FROM etudiants WHERE id_etudiant = ?",
            (id,)
        )
        self.conn.commit()

    def get_by_promotion(self, promotion_id):
        rows = self.conn.cursor().execute(
            "SELECT * FROM etudiants WHERE id_promotion = ?",
            (promotion_id,)
        ).fetchall()

        return [EtudiantDTO(*row) for row in rows]


class EnseignantDAO(DAO):
    def get_all(self):
        rows = self.conn.cursor().execute("SELECT * FROM enseignants").fetchall()
        return [EnseignantDTO(*row) for row in rows]

    def get_by_id(self, id):
        row = self.conn.cursor().execute(
            "SELECT * FROM enseignants WHERE id_enseignant = ?",
            (id,)
        ).fetchone()

        if row is None:
            return None

        return EnseignantDTO(*row)

    def save(self, enseignant: EnseignantDTO):
        self.conn.cursor().execute(
            "INSERT OR REPLACE INTO enseignants VALUES (?, ?, ?, ?, ?)",
            (
                enseignant.id_enseignant,
                enseignant.nom,
                enseignant.prenom,
                enseignant.email,
                enseignant.id_ue
            )
        )
        self.conn.commit()

    def delete(self, id):
        self.conn.cursor().execute(
            "DELETE FROM enseignants WHERE id_enseignant = ?",
            (id,)
        )
        self.conn.commit()

    def get_by_ue(self, ue_id):
        rows = self.conn.cursor().execute(
            "SELECT * FROM enseignants WHERE id_ue = ?",
            (ue_id,)
        ).fetchall()

        return [EnseignantDTO(*row) for row in rows]


class PromotionDAO(DAO):
    def get_all(self):
        rows = self.conn.cursor().execute("SELECT * FROM promotions").fetchall()
        return [PromotionDTO(*row) for row in rows]

    def get_by_id(self, id):
        row = self.conn.cursor().execute(
            "SELECT * FROM promotions WHERE id_promotion = ?",
            (id,)
        ).fetchone()

        if row is None:
            return None

        return PromotionDTO(*row)

    def save(self, promotion: PromotionDTO):
        self.conn.cursor().execute(
            "INSERT OR REPLACE INTO promotions VALUES (?, ?, ?)",
            (
                promotion.id_promotion,
                promotion.nom_promotion,
                promotion.annee_academique
            )
        )
        self.conn.commit()

    def delete(self, id):
        self.conn.cursor().execute(
            "DELETE FROM promotions WHERE id_promotion = ?",
            (id,)
        )
        self.conn.commit()


class UniteEnseignementDAO(DAO):
    def get_all(self):
        rows = self.conn.cursor().execute("SELECT * FROM unites_enseignement").fetchall()
        return [UniteEnseignementDTO(*row) for row in rows]

    def get_by_id(self, id):
        row = self.conn.cursor().execute(
            "SELECT * FROM unites_enseignement WHERE id_ue = ?",
            (id,)
        ).fetchone()

        if row is None:
            return None

        return UniteEnseignementDTO(*row)

    def save(self, ue: UniteEnseignementDTO):
        self.conn.cursor().execute(
            "INSERT OR REPLACE INTO unites_enseignement VALUES (?, ?, ?, ?, ?)",
            (
                ue.id_ue,
                ue.code_ue,
                ue.intitule,
                ue.credits_ects,
                ue.id_promotion
            )
        )
        self.conn.commit()

    def delete(self, id):
        self.conn.cursor().execute(
            "DELETE FROM unites_enseignement WHERE id_ue = ?",
            (id,)
        )
        self.conn.commit()

    def get_by_promotion(self, promotion_id):
        rows = self.conn.cursor().execute(
            "SELECT * FROM unites_enseignement WHERE id_promotion = ?",
            (promotion_id,)
        ).fetchall()

        return [UniteEnseignementDTO(*row) for row in rows]


class CoursDAO(DAO):
    def get_all(self):
        rows = self.conn.cursor().execute("SELECT * FROM cours").fetchall()
        return [CoursDTO(*row) for row in rows]

    def get_by_id(self, id):
        row = self.conn.cursor().execute(
            "SELECT * FROM cours WHERE id_cours = ?",
            (id,)
        ).fetchone()

        if row is None:
            return None

        return CoursDTO(*row)

    def save(self, cours: CoursDTO):
        self.conn.cursor().execute(
            "INSERT OR REPLACE INTO cours VALUES (?, ?, ?, ?)",
            (
                cours.id_cours,
                cours.intitule,
                cours.volume_horaire,
                cours.id_ue
            )
        )
        self.conn.commit()

    def delete(self, id):
        self.conn.cursor().execute(
            "DELETE FROM cours WHERE id_cours = ?",
            (id,)
        )
        self.conn.commit()

    def get_by_ue(self, ue_id):
        rows = self.conn.cursor().execute(
            "SELECT * FROM cours WHERE id_ue = ?",
            (ue_id,)
        ).fetchall()

        return [CoursDTO(*row) for row in rows]


class EventDAO(DAO):
    def get_all(self):
        rows = self.conn.cursor().execute("SELECT * FROM seances").fetchall()
        return [SeanceDTO(*row) for row in rows]

    def get_by_id(self, id):
        row = self.conn.cursor().execute(
            "SELECT * FROM seances WHERE id_seance = ?",
            (id,)
        ).fetchone()

        if row is None:
            return None

        return SeanceDTO(*row)

    def save(self, seance: SeanceDTO):
        self.conn.cursor().execute(
            "INSERT OR REPLACE INTO seances VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                seance.id_seance,
                seance.titre,
                seance.date,
                seance.heure_debut,
                seance.heure_fin,
                seance.salle,
                seance.status_synchro,
                seance.type,
                seance.id_cours
            )
        )
        self.conn.commit()

    def delete(self, id):
        self.conn.cursor().execute(
            "DELETE FROM seances WHERE id_seance = ?",
            (id,)
        )
        self.conn.commit()

    def get_by_cours(self, cours_id):
        rows = self.conn.cursor().execute(
            "SELECT * FROM seances WHERE id_cours = ?",
            (cours_id,)
        ).fetchall()

        return [SeanceDTO(*row) for row in rows]

    def get_by_date_range(self, start_date, end_date):
        rows = self.conn.cursor().execute(
            "SELECT * FROM seances WHERE date BETWEEN ? AND ?",
            (start_date, end_date)
        ).fetchall()

        return [SeanceDTO(*row) for row in rows]

    def update_sync_status(self, id_seance, status):
        self.conn.cursor().execute(
            "UPDATE seances SET status_synchro = ? WHERE id_seance = ?",
            (status, id_seance)
        )
        self.conn.commit()