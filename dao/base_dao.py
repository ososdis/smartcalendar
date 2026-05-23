class BaseDAO:
    def __init__(self):
        self.data = []

    def get_all(self):
        return self.data

    def save(self, objet):
        self.data.append(objet)
        return objet

    def get_by_id(self, id_objet):
        for obj in self.data:
            if obj.id_seance == id_objet:
                return obj
        return None