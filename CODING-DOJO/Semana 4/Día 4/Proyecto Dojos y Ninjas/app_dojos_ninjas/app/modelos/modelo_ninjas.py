from app_dojos_ninjas.config.mysqlconnection import connectToMySQL
from app_dojos_ninjas import BASE_DATOS

class Ninja:
    def __init__( self, data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.id_dojo = data['id_dojo']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion'] 

    @classmethod
    def crear_uno( cls, data ):
        query = """
                INSERT INTO ninjas ( nombre, apellido, edad, id_dojo )
                VALUES ( %(nombre)s, %(apellido)s, %(edad)s, %(id_dojo)s ); 
                """
        resultado = connectToMySQL( BASE_DATOS ).query_db( query, data )
        return resultado