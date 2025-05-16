from models.Conectar import Conectar

class ArbolDAO:
    def __init__(self):
        self.db = Conectar()
        
    def crear_arbol(self, arbol):
        sql = "INSERT INTO Arbol"
        valores = (
            arbol.id,
            arbol.perso_id,
            arbol.usua_id,
        )
        self.db.cursor.execute(sql, valores)
        self.db.conexion.commit()
        print('Se ha creado el arbol.')