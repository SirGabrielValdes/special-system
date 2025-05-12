import mysql.connector;

class Conectar: 
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'genealogia'
        )
        self.cursor = self.conexion.cursor(dictionary=True)
        
    def cerrar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()