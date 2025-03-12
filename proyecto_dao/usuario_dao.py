from database import Database
from usuario import Usuario

class UsuarioDAO:
    def __init__(self):
        self.db = Database()
        self.conexion = self.db.get_connection()

    def agregar_usuario(self, usuario):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
        valores = (usuario.nombre, usuario.email)
        cursor.execute(sql, valores)
        self.conexion.commit()
        cursor.close()

    def obtener_usuarios(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = []
        for (id, nombre, email) in cursor.fetchall():
            usuarios.append(Usuario(id, nombre, email))
        cursor.close()
        return usuarios

    def buscar_usuario(self, id_usuario):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id_usuario,))
        usuario = cursor.fetchone()
        cursor.close()
        if usuario:
            return Usuario(usuario[0], usuario[1], usuario[2])
        return None

    def actualizar_usuario(self, usuario):
        cursor = self.conexion.cursor()
        sql = "UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s"
        valores = (usuario.nombre, usuario.email, usuario.id)
        cursor.execute(sql, valores)
        self.conexion.commit()
        cursor.close()

    def eliminar_usuario(self, id_usuario):
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
        self.conexion.commit()
        cursor.close()