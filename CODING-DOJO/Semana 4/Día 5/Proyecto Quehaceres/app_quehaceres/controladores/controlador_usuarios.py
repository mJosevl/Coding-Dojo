from flask import render_template, session, request, redirect
from app_quehaceres import app
from app_quehaceres.modelos.modelo_usuarios import Usuario

@app.route( '/', methods = ['GET'] )
@app.route( '/login', methods = ['GET'] )
@app.route( '/registro', methods = ['GET'] )
def desplegar_login_registro():
    return render_template( 'login_registro.html' )

@app.route( '/nuevo/usuario', methods = ['POST'] )
def crear_usuario():
    if Usuario.validar_registro( request.form ) == True:
        id_usuario = Usuario.crear_uno( request.form )
        # Validar que el email es único (Esto implica un query)
        session['nombre'] = request.form['nombre']
        session['apellido'] = request.form['apellido']
        session['id_usuario'] = id_usuario
        return redirect( '/quehaceres' )
    else:
        return redirect( '/' )