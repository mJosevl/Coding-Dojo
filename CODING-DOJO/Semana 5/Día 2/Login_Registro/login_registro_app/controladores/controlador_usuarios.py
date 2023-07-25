from flask import session, render_template, redirect, request, flash
from flask_bcrypt import Bcrypt
from login_registro_app import app
from login_registro_app.modelos.modelo_usuarios import Usuario

bcrypt = Bcrypt( app )

@app.route( '/', methods = ['GET'] )
def desplegar_login_registro():
    return render_template( 'login_registro.html' )

@app.route( '/crear/usuario', methods = ['POST'] )
def nuevo_usuario():
    data = {
        **request.form
    }

    if Usuario.validar_registro( data ) == False:
        return redirect( '/' )
    else:
        password_encriptado = bcrypt.generate_password_hash( data['password'] )
        data['password'] = password_encriptado
        id_usuario = Usuario.crear_uno( data )
        session['nombre'] = data['nombre']
        session['apellido'] = data['apellido']
        session['id_usuario'] = id_usuario

        return redirect( '/dashboard' )
    
@app.route( '/dashboard', methods = ['GET'] )
def desplegar_dashboard():
    if 'nombre' not in session:
        return redirect( '/' )
    else:
        return render_template( 'dashboard.html' )

@app.route( '/login', methods = ['POST'] )
def procesa_login():
    data = {
        "email" : request.form['email_login']
    }
    usuario = Usuario.obtener_uno_con_email( data )

    if usuario == None:
        flash( "Email inválido.", "error_email_login")
        return redirect( '/' )
    else:
        if not bcrypt.check_password_hash( usuario.password, request.form['password_login'] ):
            flash( "Credenciales incorrectas." , "error_password_login" )
            return redirect( '/' )
        else:
            session['nombre'] = usuario.nombre
            session['apellido'] = usuario.apellido
            session['id_usuario'] = usuario.id
            return redirect( '/dashboard' ) 

@app.route( '/logout', methods = ['POST'] )
def procesa_logout():
    session.clear()
    return redirect( '/' )