class Product:
    def __init__(self, name, rol, mail, pwd):
        self.name = name
        self.rol = rol
        self.mail = mail
        self.pwd = pwd

    def toDBCollection(self):
        return{
            'name': self.name,
            'rol': self.rol,
            'mail': self.mail,
            'pwd': self.pwd
        }