# Exercice 1
## Implémentation des DAOs des modèles DTO suivant le diagramme class_comp.puml

# Avec Python, les class Interfaces peuvent être implémentées comme des classes abstraites
# heritant de Protocol
import sqlite3
from typing import Protocol

from Models import EnseignantDTO, EtudiantDTO, UserDTO, PromotionDTO, UniteEnseignementDTO, CoursDTO, SeanceDTO


class DAO:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._setup_db()

    def _setup_db(self):
        cursor = self.conn.cursor()

        # Réquêtes de création lors de l'initialisation des tables si elles n'existent pas
        # 1. Création de la table Users sur base de la classe UserDTO

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, role TEXT, email TEXT, google_linked BOOLEAN)"
        )
       
        # 3. Création de la table Enseignant
        # 4. Création de la table Promotion
        # 5. Création de la table UniteEnseignement
        # 6. Création de la table Cours
        # 7. Création de la table Seance

        # Confirmation des réquêtes dans la transaction
        self.conn.commit()

# Interface DAO

class BaseDAO(Protocol):

    def get_by_id(self, id):
        ...

    def get_all(self):
        ...

    def save(self, obj):
        ...

    def delete(self, id):
        ...


# USER DAO


class UserDAO(DAO):

    def save(self, user: UserDTO):

        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO users(id_user, role, email, google_linked)
        VALUES (?, ?, ?, ?)
        """, (
            user.id_user,
            user.role,
            user.email,
            user.google_linked
        ))

        self.conn.commit()

    def get_by_id(self, id_user):

        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE id_user=?",
            (id_user,)
        )

        return cursor.fetchone()

    def get_all(self):

        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM users")

        return cursor.fetchall()

    def delete(self, id_user):

        cursor = self.conn.cursor()

        cursor.execute(
            "DELETE FROM users WHERE id_user=?",
            (id_user,)
        )

        self.conn.commit()

    def get_by_email(self, email):

        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        )

        return cursor.fetchone()

# PROMOTION DAO


class PromotionDAO(DAO):

    def save(self, promotion: PromotionDTO):

        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO promotion
        VALUES (?, ?, ?)
        """, (
            promotion.id_promotion,
            promotion.nom_promotion,
            promotion.annee_academique
        ))

        self.conn.commit()

    def get_by_id(self, id_promotion):

        cursor = self.conn.cursor()

        cursor.execute("""
        SELECT * FROM promotion
        WHERE id_promotion=?
        """, (id_promotion,))

        return cursor.fetchone()

    def get_all(self):

        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM promotion")

        return cursor.fetchall()

    def delete(self, id_promotion):

        cursor = self.conn.cursor()

        cursor.execute("""
        DELETE FROM promotion
        WHERE id_promotion=?
        """, (id_promotion,))

        self.conn.commit()

#   # 2. Création de la table Etudiant ETUDIANT DAO

class EtudiantDAO(DAO):

    def save(self, etudiant: EtudiantDTO):

        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO etudiant
        VALUES (?, ?, ?, ?, ?)
        """, (
            etudiant.id_etudiant,
            etudiant.nom,
            etudiant.prenom,
            etudiant.email,
            etudiant.id_promotion
        ))

        self.conn.commit()

    def get_by_id(self, id_etudiant):

        cursor = self.conn.cursor()

        cursor.execute("""
        SELECT * FROM etudiant
        WHERE id_etudiant=?
        """, (id_etudiant,))

        return cursor.fetchone()

    def get_all(self):

        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM etudiant")

        return cursor.fetchall()

    def delete(self, id_etudiant):

        cursor = self.conn.cursor()

        cursor.execute("""
        DELETE FROM etudiant
        WHERE id_etudiant=?
        """, (id_etudiant,))

        self.conn.commit()

    def get_by_promotion(self, id_promotion):

        cursor = self.conn.cursor()

        cursor.execute("""
        SELECT * FROM etudiant
        WHERE id_promotion=?
        """, (id_promotion,))

        return cursor.fetchall()

# ENSEIGNANT DAO

class EnseignantDAO(DAO):

    def save(self, enseignant: EnseignantDTO):

        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO enseignant
        VALUES (?, ?, ?, ?)
        """, (
            enseignant.id_enseignant,
            enseignant.nom,
            enseignant.prenom,
            enseignant.specialite,
        ))

        self.conn.commit()

    def get_by_id(self, id_enseignant):

        cursor = self.conn.cursor()

        cursor.execute("""
        SELECT * FROM enseignant
        WHERE id_enseignant=?
        """, (id_enseignant,))

        return cursor.fetchone()

    def get_all(self):

        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM enseignant")

        return cursor.fetchall()

    def delete(self, id_enseignant):

        cursor = self.conn.cursor()

        cursor.execute("""
        DELETE FROM enseignant
        WHERE id_enseignant=?
        """, (id_enseignant,))

        self.conn.commit()

    def get_by_specialite(self, specialite):

        cursor = self.conn.cursor()

        cursor.execute("""
        SELECT * FROM enseignant
        WHERE specialite=?
        """, (specialite,))

        return cursor.fetchall()

# UE DAO

class UniteEnseignementDAO(DAO):

    def save(self, ue: UniteEnseignementDTO):

        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO unite_enseignement
        VALUES (?, ?, ?)
        """, (
            ue.id_ue,
            ue.nom_ue,
            ue.credit
        ))

        self.conn.commit()

    def get_all(self):

        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM unite_enseignement")

        return cursor.fetchall()

# COURS DAO

class CoursDAO(DAO):

    def save(self, cours: CoursDTO):

        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO cours
        VALUES (?, ?, ?, ?)
        """, (
            cours.id_cours,
            cours.titre,
            cours.id_ue,
            cours.id_enseignant
        ))

        self.conn.commit()

    def get_all(self):

        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM cours")

        return cursor.fetchall()

# SEANCE DAO

class SeanceDAO(DAO):

    def save(self, seance: SeanceDTO):

        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO seance
        VALUES (?, ?, ?, ?, ?)
        """, (
            seance.id_seance,
            seance.date,
            seance.heure,
            seance.synchro,
            seance.id_cours
        ))

        self.conn.commit()

    def get_all(self):

        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM seance")

        return cursor.fetchall()

    def get_by_date(self, date):

        cursor = self.conn.cursor()

        cursor.execute("""
        SELECT * FROM seance
        WHERE date=?
        """, (date,))

        return cursor.fetchall()

    def update_sync_status(self, id_seance, statut):

        cursor = self.conn.cursor()

        cursor.execute("""
        UPDATE seance
        SET synchro=?
        WHERE id_seance=?
        """, (
            statut,
            id_seance
        ))

        self.conn.commit()


# EXEMPLE D'UTILISATION


if __name__ == "__main__":

    user_dao = UserDAO()

    user = UserDTO(
        1,
        "Admin",
        "admin@gmail.com",
        True
    )

    user_dao.save(user)

    print(user_dao.get_all())
