from flask import render_template, session, request, redirect, flash
from app_quehaceres import app
from flask_bcrypt import Bcrypt
from app_quehaceres.modelos.modelo_usuarios import Usuario

bcrypt = Bcrypt( app )

@app.route( '/', methods = ['GET'] )
@app.route( '/login', methods = ['GET'] )
@app.route( '/registro', methods = ['GET'] )
def desplegar_login_registro():
    return render_template( 'login_registro.html' )

@app.route( '/nuevo/usuario', methods = ['POST'] )
def crear_usuario():
    if Usuario.validar_registro( request.form ) == True:
        password_encriptado = bcrypt.generate_password_hash( request.form['password'] )
        nuevo_usuario = {
            **request.form,
            "password" : password_encriptado
        }

        id_usuario = Usuario.crear_uno( nuevo_usuario )
        # Validar que el email es único (Esto implica un query)
        session['nombre'] = request.form['nombre']
        session['apellido'] = request.form['apellido']
        session['id_usuario'] = id_usuario
        return redirect( '/quehaceres' )
    else:
        return redirect( '/' )
    
@app.route( '/login', methods = ['POST'] )
def procesa_login():
    data = {
        "email" : request.form['email_login'],
        "password" : request.form['password_login']
    }
    usuario = Usuario.obtener_uno_con_email( data )

    if Usuario.validar_login( usuario ) == True:
        print( usuario.nombre, usuario.apellido, usuario.password )
        if not bcrypt.check_password_hash( usuario.password, data['password'] ):
            flash( "Credenciales incorrectas.", "error_password_login")
            return redirect( '/login' );
        else:
            session['nombre'] = usuario.nombre
            session['apellido'] = usuario.apellido
            session['id_usuario'] = usuario.id
            return redirect( '/quehaceres' )
    else:
        return redirect( '/login' )
    

@app.route( '/logout', methods = ['POST'] )
def procesa_logout():
    session.clear()
    return redirect( '/login' )