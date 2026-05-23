# ==========================================================
# base_dao = la classe mère des DAO
# DAO = c'est l'objet d'accès qux données
# ==========================================================

from data import *
class BaseDAO:

    def __init__(self):
        # Stockage temporaire en mémoire
        # Plus tard, cette partie pourra être remplacée par SQLite
        self.data = []

    def get_by_id(self, id_objet):
        """
        Recherche un objet par son identifiant.
        """
        for objet in self.data:
            if hasattr(objet, "id") and objet.id == id_objet:
                return objet

            if hasattr(objet, "id_etudiant") and objet.id_etudiant == id_objet:
                return objet

            if hasattr(objet, "id_enseignant") and objet.id_enseignant == id_objet:
                return objet

            if hasattr(objet, "id_promotion") and objet.id_promotion == id_objet:
                return objet

            if hasattr(objet, "id_ue") and objet.id_ue == id_objet:
                return objet

            if hasattr(objet, "id_cours") and objet.id_cours == id_objet:
                return objet

            if hasattr(objet, "id_seance") and objet.id_seance == id_objet:
                return objet

        return None

    def get_all(self):
        """
        Retourne tous les objets enregistrés.
        """
        return self.data

    def save(self, objet):
        """
        Enregistre un objet dans la liste.
        """
        self.data.append(objet)
        return objet

    def delete(self, id_objet):
        """
        Supprime un objet à partir de son identifiant.
        """
        objet = self.get_by_id(id_objet)

        if objet is not None:
            self.data.remove(objet)
            return True

        return False
# ==========================================================
# cours_dao = DAO spécialisé pour les cours
# ==========================================================


class CoursDAO(BaseDAO):

    def __init__(self):
        super().__init__()

    def get_by_ue(self, id_ue):
        """
        Retourne tous les cours appartenant à une unité d'enseignement.
        """

        resultats = []

        for cours in self.data:
            if cours.id_ue == id_ue:
                resultats.append(cours)

        return resultats

    def get_by_enseignant(self, id_enseignant):
        """
        Retourne tous les cours enseignés par un enseignant.
        """

        resultats = []

        for cours in self.data:
            if cours.id_enseignant == id_enseignant:
                resultats.append(cours)

        return resultats

# ==========================================================
# enseignant_dao = Spéciale que pour les enseignants
# ==========================================================


class EnseignantDAO(BaseDAO):

    def __init__(self):
        super().__init__()

    def get_by_email(self, email):
        """
        Recherche un enseignant à partir de son email.
        """

        for enseignant in self.data:
            if enseignant.email == email:
                return enseignant

        return None
# ==========================================================
# etudant_dao = C'est spécialisé pour les étudiants
# ==========================================================


class EtudiantDAO(BaseDAO):

    def __init__(self):

        # Hérite du constructeur de BaseDAO
        super().__init__()

    def get_by_promotion(self, id_promotion):
        """
        Retourne les étudiants d'une promotion donnée.
        """

        resultats = []

        for etudiant in self.data:

            if etudiant.id_promotion == id_promotion:
                resultats.append(etudiant)

        return resultats
    
# ==========================================================
# seance_dao = Spécialisé pour les séances ou événements
# ==========================================================


class SeanceDAO(BaseDAO):

    def __init__(self):
        super().__init__()

    def get_by_cours(self, id_cours):
        """
        Retourne toutes les séances liées à un cours.
        """

        resultats = []

        for seance in self.data:
            if seance.id_cours == id_cours:
                resultats.append(seance)

        return resultats

    def get_by_date(self, date_seance):
        """
        Retourne toutes les séances prévues à une date donnée.
        """

        resultats = []

        for seance in self.data:
            if seance.date_seance == date_seance:
                resultats.append(seance)

        return resultats

    def get_synchronisees(self):
        """
        Retourne les séances déjà synchronisées.
        """

        resultats = []

        for seance in self.data:
            if seance.est_synchronise is True:
                resultats.append(seance)

        return resultats

    def get_non_synchronisees(self):
        """
        Retourne les séances non encore synchronisées.
        """

        resultats = []

        for seance in self.data:
            if seance.est_synchronise is False:
                resultats.append(seance)

        return resultats
# ==========================================================
# UniteEnseignementDAOSpécialisé pour les unités d'enseignement
# ==========================================================


class UniteEnseignementDAO(BaseDAO):

    def __init__(self):
        super().__init__()

    def get_by_promotion(self, id_promotion):
        """
        Retourne toutes les UE d'une promotion donnée.
        """

        resultats = []

        for ue in self.data:

            if ue.id_promotion == id_promotion:
                resultats.append(ue)

        return resultats