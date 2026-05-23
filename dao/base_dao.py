class BaseDAO:
    def __init__(self):
        self.data = []

    def get_all(self):
        """
        Retourne tous les objets enregistrés
        """
        return self.data

    def get_by_id(self, id_objet):
        """
        Recherche un objet par son identifiant
        """
        for obj in self.data:
            if hasattr(obj, "id_seance") and obj.id_seance == id_objet:
                return obj
        return None

    def save(self, obj):
        """
        Ajoute un objet dans la liste
        """
        self.data.append(obj)
        return obj

    def delete(self, id_objet):
        """
        Supprime un objet par son identifiant
        """
        obj = self.get_by_id(id_objet)

        if obj:
            self.data.remove(obj)
            return True

        return False