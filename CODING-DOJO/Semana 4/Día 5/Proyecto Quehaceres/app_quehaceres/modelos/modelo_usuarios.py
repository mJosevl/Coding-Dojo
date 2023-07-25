from app_quehaceres.config.mysqlconnection import connectToMySQL
from flask import flash
from app_quehaceres import BASE_DE_DATOS, EMAIL_REGEX
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

    @classmethod
    def crear_uno( cls, data ):
        query = """
                INSERT INTO usuarios ( nombre, apellido, email, password )
                VALUES ( %(nombre)s, %(apellido)s, %(email)s, %(password)s );
                """
        resultado = connectToMySQL( BASE_DE_DATOS ).query_db( query, data )
        return resultado

    @staticmethod
    def validar_registro( data ):
        es_valido = True

        if len( data['nombre'] ) < 3:
            es_valido = False
            flash( "Necesitas proporcionar tu nombre.", "error_nombre" )
        if len( data['apellido'] ) < 3:
            es_valido = False
            flash( "Necesitas proporcionar tu apellido.", "error_apellido" )
        if len( data['password'] ) < 8:
            es_valido = False
            flash( "Tu password necesita tener al menos 8 caracteres.", "error_password" )
        if data['password'] != data['confirmar_password']:
            es_valido = False
            flash( "Los passwords no coincided.", "error_password" )
        if not EMAIL_REGEX.match( data['email'] ):
            es_valido = False
            flash( "Por favor porporciona un email válido", "error_email" )
        
        return es_valido