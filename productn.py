class Productn:
    def __init__(self, name, rol, nota, star):
        self.name = name
        self.rol = rol
        self.nota = nota
        self.star = star

    def toDBCollection(self):
        return{
            'name': self.name,
            'rol': self.rol,
            'nota': self.nota,
            'star': self.star
        }