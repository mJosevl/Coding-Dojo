from app_dojos_ninjas.config.mysqlconnection import connectToMySQL
from app_dojos_ninjas import BASE_DATOS
from app_dojos_ninjas.modelos.modelo_ninjas import Ninja

class Dojo:
    def __init__( self, data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
        self.ninjas = []
    
    @classmethod
    def crear_uno( cls, data ):
        query = """
                INSERT INTO dojos ( nombre )
                VALUES ( %(nombre)s );
                """
        resultado = connectToMySQL( BASE_DATOS ).query_db( query, data )
        return resultado

    @classmethod
    def obtener_todos( cls ):
        query = """
                SELECT *
                FROM dojos;
                """
        resultado = connectToMySQL( BASE_DATOS ).query_db( query )
        lista_dojos = []
        
        for renglon in resultado:
            lista_dojos.append( Dojo( renglon ) )
        
        return lista_dojos
    
    @classmethod
    def obener_uno_con_ninjas( cls, data ):
        query = """
                SELECT *
                FROM dojos d LEFT JOIN ninjas n
                    ON d.id = n.id_dojo
                WHERE d.id = %(id)s;
                """
        resultado = connectToMySQL( BASE_DATOS ).query_db( query, data )
        informacion_dojo = Dojo( resultado[0] )

        for renglon in resultado:
            if renglon['n.nombre'] != None:
                datos_ninja = {
                    "nombre" : renglon['n.nombre'],
                    "apellido" : renglon['apellido'],
                    "edad" : renglon['edad'],
                    "id" : renglon['n.id'],
                    "id_dojo" : renglon['id_dojo'],
                    "fecha_creacion" : renglon['n.fecha_creacion'],
                    "fecha_actualizacion" : renglon['n.fecha_actualizacion'] 
                }
                ninja_actual = Ninja( datos_ninja )
                informacion_dojo.ninjas.append( ninja_actual )
        
        return informacion_dojo