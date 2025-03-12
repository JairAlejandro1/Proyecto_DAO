class Usuario:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Usuario(ID: {self.id}, Nombre: {self.nombre}, Email: {self.email})"
