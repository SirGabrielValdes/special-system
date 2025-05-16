from models.Conectar import Conectar

class AntecedentesDAO:
    def __init__(self):
        self.db = Conectar()
        
    def insertar_Antecedentes(self, antecedentes): 
        sql = "INSERT INTO Antecedentes"
        valores = (
            antecedentes.id,
            antecedentes.pais,
            antecedentes.perso.id,
            antecedentes.ciud.id,
            antecedentes.fecha,
            antecedentes.tipo,
        )
        self.db.cursor.execute(sql, valores)
        self.db.conexion.commit()
        print('Se ha insertado los datos.')
        
    def modificar_Antecedentes(self):
        buscar_antecedente = """
            SELECT * FROM Antecedentes
        """
        
        