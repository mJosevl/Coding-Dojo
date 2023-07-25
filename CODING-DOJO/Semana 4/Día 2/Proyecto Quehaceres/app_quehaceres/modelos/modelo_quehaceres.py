from app_quehaceres.config.mysqlconnection import connectToMySQL
from app_quehaceres import BASE_DE_DATOS

class Quehaceres:
    def __init__( self, data ):
        self.id = data['id']
        self.descripcion = data['descripcion']
        self.estatus = data['estatus']
        self.id_usuario = data['id_usuario']
        self.tiempo_creacion = data['tiempo_creacion']
        self.tiempo_actualizacion = data['tiempo_actualizacion']
    
    @classmethod
    def seleccionar_todos( cls ):
        query = """
                SELECT * 
                FROM quehaceres;
                """

        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query )
        
        lista_quehaceres = []
        for renglon in resultado:
            lista_quehaceres.append( Quehaceres( renglon ) )
        return lista_quehaceres
    
    @classmethod
    def crear_uno( cls, data ):
        query = """
                INSERT INTO quehaceres( descripcion, estatus, id_usuario )
                VALUES ( %(descripcion)s, %(estatus)s, %(id_usuario)s );
                """
        
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query, data )

        return resultado

    @classmethod
    def elimina_uno( cls, data ):
        query = """
                DELETE FROM quehaceres
                WHERE id = %(id)s;
                """
        return connectToMySQL( BASE_DE_DATOS ).query_db( query, data )
    
    @classmethod
    def selecciona_uno( cls, data ):
        query = """
                SELECT *
                FROM quehaceres
                WHERE id = %(id)s;
                """
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query, data )
        quehacer_actual = Quehaceres( resultado[0] )
        return quehacer_actual
    
    @classmethod
    def actualiza_uno( cls, data ):
        query = """
                UPDATE quehaceres
                SET descripcion = %(descripcion)s, estatus = %(estatus)s, id_usuario = %(id_usuario)s
                WHERE id = %(id)s;
                """
        return connectToMySQL( BASE_DE_DATOS ).query_db( query, data )