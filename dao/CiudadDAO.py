from models.Conectar import Conectar

class CiudadDAO:
    def __init__(self):
        self.db = Conectar()
        
    def insertar_Ciudad(self, ciudad):
        sql = "INSERT INTO Ciudad"
        valores = (
            ciudad.id,
            ciudad.antece.id,
            ciudad.pais_id,
            ciudad.nombre,
        )
        self.db.cursor.execute(sql, valores)
        self.db.conexion.commit()
        print('Se ha creado el arbol.')

        
    