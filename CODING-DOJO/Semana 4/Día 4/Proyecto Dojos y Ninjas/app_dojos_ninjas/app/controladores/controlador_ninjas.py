from flask import render_template, request, redirect
from app_dojos_ninjas import app
from app_dojos_ninjas.modelos.modelo_dojos import Dojo
from app_dojos_ninjas.modelos.modelo_ninjas import Ninja

@app.route( '/formulario/ninja', methods = ['GET'] )
def desplegar_formulario_ninja():
    lista_dojos = Dojo.obtener_todos()
    return render_template( 'formulario_ninja.html', lista_dojos = lista_dojos )

@app.route( '/nuevo/ninja', methods = ['POST'] )
def crear_ninja():
    Ninja.crear_uno( request.form )
    return redirect( '/dojos' )