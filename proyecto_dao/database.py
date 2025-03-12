import mysql.connector

class Database:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mi_base_datos"
        )

    def get_connection(self):
        return self.conexion
