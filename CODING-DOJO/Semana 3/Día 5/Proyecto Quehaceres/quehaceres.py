from mysqlconnection import connectToMySQL

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

        resultado = connectToMySQL( "bd_quehaceres" ).query_db( query )
        
        lista_quehaceres = []
        for renglon in resultado:
            lista_quehaceres.append( Quehaceres( renglon ) )
        print( lista_quehaceres )
        return lista_quehaceres