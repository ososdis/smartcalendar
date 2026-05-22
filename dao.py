from database import connexion, curseur

from data import (
    EtudiantDTO,
    SeanceDTO,
    TypeSeance,
)

from datetime import datetime


# =========================
# USER DAO
# =========================

class UserDAO:

    def ajouter_user(self, user):

        curseur.execute(
            """
            INSERT INTO users (
                matricule,
                nom,
                prenom,
                email,
                promotion_id
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                user.matricule,
                user.nom,
                user.prenom,
                user.email,
                user.promotion_id,
            ),
        )

        connexion.commit()

    def afficher_users(self):

        curseur.execute(
            "SELECT * FROM users"
        )

        data = curseur.fetchall()

        users = []

        for u in data:

            user = EtudiantDTO(
                id_etudiant=u[0],
                matricule=u[1],
                nom=u[2],
                prenom=u[3],
                email=u[4],
                promotion_id=u[5],
            )

            users.append(user)

        return users

    def rechercher_user(self, email):

        curseur.execute(
            """
            SELECT * FROM users
            WHERE email=?
            """,
            (email,),
        )

        u = curseur.fetchone()

        if u:

            return EtudiantDTO(
                id_etudiant=u[0],
                matricule=u[1],
                nom=u[2],
                prenom=u[3],
                email=u[4],
                promotion_id=u[5],
            )

        return None


# =========================
# EVENT DAO
# =========================

class EventDAO:

    def ajouter_event(self, event):

        curseur.execute(
            """
            INSERT INTO events (
                date,
                heure_debut,
                heure_fin,
                salle
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                str(event.date_seance),
                str(event.heure_debut),
                str(event.heure_fin),
                event.salle,
            ),
        )

        connexion.commit()

    def afficher_events(self):

        curseur.execute(
            "SELECT * FROM events"
        )

        data = curseur.fetchall()

        events = []

        for e in data:

            event = SeanceDTO(
                id_seance=e[0],

                date_seance=datetime.strptime(
                    e[1],
                    "%Y-%m-%d"
                ).date(),

                heure_debut=datetime.strptime(
                    e[2],
                    "%H:%M:%S"
                ).time(),

                heure_fin=datetime.strptime(
                    e[3],
                    "%H:%M:%S"
                ).time(),

                salle=e[4],

                est_synchro=True,
                cours_id=101,
                type=TypeSeance.COURS_MAGISTRAL,
            )

            events.append(event)

        return events

    def rechercher_par_date(self, date_recherche):

        curseur.execute(
            """
            SELECT * FROM events
            WHERE date=?
            """,
            (date_recherche,),
        )

        data = curseur.fetchall()

        events = []

        for e in data:

            event = SeanceDTO(
                id_seance=e[0],

                date_seance=datetime.strptime(
                    e[1],
                    "%Y-%m-%d"
                ).date(),

                heure_debut=datetime.strptime(
                    e[2],
                    "%H:%M:%S"
                ).time(),

                heure_fin=datetime.strptime(
                    e[3],
                    "%H:%M:%S"
                ).time(),

                salle=e[4],

                est_synchro=True,
                cours_id=101,
                type=TypeSeance.COURS_MAGISTRAL,
            )

            events.append(event)

        return events