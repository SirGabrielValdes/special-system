import mysql.connector;

class Conectar: 
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = ''
        )
        self.cursor = self.conexion.cursor(dictionary=True)