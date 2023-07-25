from app_recetas.config.mysqlconnection import connectToMySQL
from app_recetas.modelos.modelo_usuarios import Usuario
from app_recetas import BASE_DATOS
from datetime import datetime

from flask import flash

class Receta:
    def __init__( self, data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.descripcion = data['descripcion']
        self.instrucciones = data['instrucciones']
        self.fecha_elaboracion = data['fecha_elaboracion']
        self.menos_treinta = data['menos_treinta']
        self.id_usuario = data['id_usuario']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
        self.usuario = None

    def fecha_con_formato( self ):
        fecha = datetime.strptime(self.fecha_creacion, '%Y-%m-%d %H:%M:%S')
        print(self.fecha_creacion)
        return fecha.strftime('%d/%m/%Y')

    @classmethod
    def crear_uno( cls, data ):
        query = """
                INSERT INTO recetas ( nombre, descripcion, instrucciones, fecha_elaboracion, menos_treinta, id_usuario )
                VALUES ( %(nombre)s, %(descripcion)s, %(instrucciones)s, %(fecha_elaboracion)s, %(menos_treinta)s, %(id_usuario)s );
                """
        id_receta = connectToMySQL( BASE_DATOS ).query_db( query, data )
        return id_receta
    
    @classmethod
    def obtener_todas_con_usuario( cls ):
        query = """
                SELECT *
                FROM recetas r JOIN usuarios u
                    ON r.id_usuario = u.id;
                """
        resultado = connectToMySQL( BASE_DATOS ).query_db( query )
        lista_recetas = []
        
        for renglon in resultado:
            receta = Receta( renglon )
            data_usuario = {
                "id" : renglon['u.id'],
                "nombre" : renglon['u.nombre'],
                "apellido" : renglon['apellido'],
                "email" : renglon['email'],
                "password" : renglon['password'],
                "fecha_creacion" : renglon['u.fecha_creacion'],
                "fecha_actualizacion" : renglon['u.fecha_actualizacion']
            }
            usuario = Usuario( data_usuario )
            receta.usuario = usuario
            lista_recetas.append( receta )
        
        return lista_recetas

    @classmethod
    def elimina_uno( cls, data ):
        query = """
                DELETE FROM recetas
                WHERE id = %(id)s;
                """
        return connectToMySQL( BASE_DATOS ).query_db( query, data )
    
    @classmethod
    def obtener_uno_con_usuario( cls, data ):
        query = """
                SELECT *
                FROM recetas r JOIN usuarios u
                    ON r.id_usuario = u.id
                WHERE r.id = %(id)s;
                """
        resultado = connectToMySQL( BASE_DATOS ).query_db( query, data )
        renglon = resultado[0]
        receta = Receta( renglon )
        data_usuario = {
            "id" : renglon['u.id'],
            "nombre" : renglon['u.nombre'],
            "apellido" : renglon['apellido'],
            "email" : renglon['email'],
            "password" : renglon['password'],
            "fecha_creacion" : renglon['u.fecha_creacion'],
            "fecha_actualizacion" : renglon['u.fecha_actualizacion']
        }
        receta.usuario = Usuario( data_usuario )
        return receta

    @classmethod
    def obtener_uno( cls, data ):
        query = """
                SELECT *
                FROM recetas
                WHERE id = %(id)s;
                """
        resultado = connectToMySQL( BASE_DATOS ).query_db( query, data )
        receta = Receta( resultado[0] )
        return receta
    
    @classmethod
    def editar_uno( cls, data ):
        query = """
                UPDATE recetas
                SET nombre = %(nombre)s, descripcion = %(descripcion)s, instrucciones = %(instrucciones)s, fecha_elaboracion = %(fecha_elaboracion)s, menos_treinta = %(menos_treinta)s
                WHERE id = %(id)s;
                """
        return connectToMySQL( BASE_DATOS ).query_db( query, data )

    @staticmethod
    def validar_formulario_recetas( data ):
        es_valido = True
        if len( data['nombre'] ) < 3:
            es_valido = False
            flash( "Debes de proporcionar el nombre de la receta.", "error_nombre" )
        if len( data['descripcion'] ) < 3:
            es_valido = False
            flash( "Debes de proporcionar la descripcion de la receta.", "error_descripcion" )
        if len( data['instrucciones'] ) < 3:
            es_valido = False
            flash( "Debes de proporcionar las instrucciones de la receta.", "error_instrucciones" )
        if data['fecha_elaboracion'] == "":
            es_valido = False
            flash( "Debes de proporcionar la fecha de elaboración de la receta.", "error_fecha_elaboracion" )
        if "menos_treinta" not in data:
            es_valido = False
            flash( "Debes de proporcionar si la receta se elabora en menos de 30 minutos.", "error_menos_treinta" )
        return es_valido