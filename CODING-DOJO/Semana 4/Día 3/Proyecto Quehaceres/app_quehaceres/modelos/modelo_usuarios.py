from app_quehaceres.config.mysqlconnection import connectToMySQL
from app_quehaceres import BASE_DE_DATOS
from app_quehaceres.modelos import modelo_quehaceres

class Usuario:
    def __init__( self, data ):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.password = data["password"]
        self.email = data["email"]
        self.tiempo_creacion = data['tiempo_creacion']
        self.tiempo_actualizacion = data['tiempo_actualizacion']
        self.quehaceres = []

    @classmethod
    def seleccionar_uno_con_quehaceres( cls, data ):
        query = """
                SELECT *
                FROM usuarios u LEFT JOIN quehaceres q
                    ON u.id = q.id_usuario
                WHERE u.id = %(id)s;
                """
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query, data )
        usuario = Usuario( resultado[0] )

        for renglon in resultado:
            if renglon["q.id"] != None:
                datos_quehacer = {
                    "id" : renglon["q.id"],
                    "descripcion" : renglon["descripcion"],
                    "estatus" : renglon["estatus"],
                    "tiempo_creacion" : renglon["q.tiempo_creacion"],
                    "tiempo_actualizacion" : renglon["q.tiempo_actualizacion"],
                    "id_usuario" : renglon["id_usuario"]
                }
                quehacer = modelo_quehaceres.Quehaceres( datos_quehacer )
                usuario.quehaceres.append( quehacer )
        
        return usuario

