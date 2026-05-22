# Exercice 1
# Implémentation des DAOs des modèles DTO suivant le diagramme class_comp.puml

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

        # Création de la table users
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                role TEXT,
                email TEXT,
                logedin BOOLEAN
            )
        """)

        # Création de la table etudiant
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

        # Création de la table enseignant
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS enseignant (
                id_enseignant INTEGER PRIMARY KEY,
                nom TEXT,
                prenom TEXT,
                email TEXT
            )
        """)

        # Création de la table promotion
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS promotion (
                id_promotion INTEGER PRIMARY KEY,
                nom_promotion TEXT,
                annee_academique TEXT
            )
        """)

        # Création de la table unite_enseignement
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS unite_enseignement (
                id_ue INTEGER PRIMARY KEY,
                code_ue TEXT,
                intitule TEXT,
                credits INTEGER,
                id_promotion INTEGER
            )
        """)

        # Création de la table cours
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cours (
                id_cours INTEGER PRIMARY KEY,
                intitule_cours TEXT,
                volume_horaire INTEGER,
                id_ue INTEGER,
                id_enseignant INTEGER
            )
        """)

        # Création de la table seance
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seance (
                id_seance INTEGER PRIMARY KEY,
                date TEXT,
                heure_debut TEXT,
                heure_fin TEXT,
                salle TEXT,
                synchro BOOLEAN,
                id_cours INTEGER,
                type_seance TEXT
            )
        """)

        self.conn.commit()


# Interface DAO
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