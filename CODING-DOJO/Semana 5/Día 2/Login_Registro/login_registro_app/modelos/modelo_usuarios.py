from login_registro_app.config.mysqlconnection import connectToMySQL
from login_registro_app import BASE_DATOS, EMAIL_REGEX, NOMBRE_REGEX
from flask import flash

class Usuario:
    def __init__( self, data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']

    @classmethod
    def crear_uno( cls, data ):
        query = """
                INSERT INTO usuarios ( nombre, apellido, email, password )
                VALUES ( %(nombre)s, %(apellido)s, %(email)s, %(password)s );
                """
        resultado = connectToMySQL( BASE_DATOS ).query_db( query, data )
        return resultado
    
    @classmethod
    def obtener_uno_con_email( cls, data ):
        query = """
                SELECT *
                FROM usuarios
                WHERE email = %(email)s;
                """
        resultado = connectToMySQL( BASE_DATOS ).query_db( query, data )

        if len( resultado ) == 0:
            return None
        else:
            return Usuario( resultado[0] )
    
    @staticmethod
    def validar_registro( data ):
        es_valido = True
        if len( data['nombre'] ) < 2:
            es_valido = False
            flash( "Tu nombre debe de contener al menos 2 caracteres.", "error_nombre" )

        if not NOMBRE_REGEX.match( data['nombre'] ):
            es_valido = False
            flash( "Por favor proporciona un nombre válido (solo letras).", "error_nombre" )
        
        if len( data['apellido'] ) < 2:
            es_valido = False
            flash( "Tu apellido debe de contener al menos 2 caracteres.", "error_apellido" )

        if not NOMBRE_REGEX.match( data['apellido'] ):
            es_valido = False
            flash( "Por favor proporciona un apellido válido (solo letras).", "error_apellido" )

        if not EMAIL_REGEX.match( data['email'] ):
            es_valido = False
            flash( "Por favor proporciona un email válido.", "error_email" )

        if len( data['password'] ) < 8:
            es_valido = False
            flash( "Tu contraseña necesita tener al menos 8 caracteres.", "error_password" )

        if data['password'] != data['confirmacion_password']:
            es_valido = False
            flash( "Tus contraseñas no coinciden.", "error_password" )
        
        return es_valido
        