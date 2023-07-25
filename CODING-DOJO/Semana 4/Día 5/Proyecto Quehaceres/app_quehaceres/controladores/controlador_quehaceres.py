from flask import render_template, session, request, redirect
from app_quehaceres import app
from app_quehaceres.modelos.modelo_quehaceres import Quehaceres
from app_quehaceres.modelos.modelo_usuarios import Usuario


@app.route( "/quehaceres", methods = ['GET'] )
def obtener_quehaceres():
    if 'contador' in session:
        session['contador'] += 1
    else:
        session['contador'] = 0
    lista_quehaceres = Quehaceres.seleccionar_todos_con_usuario()
    datos_usuario = {
        "id" : session['id_usuario']
    }
    usuario_actual = Usuario.seleccionar_uno_con_quehaceres( datos_usuario )

    return render_template( "quehaceres.html", quehaceres = lista_quehaceres, usuario_actual = usuario_actual )

@app.route( "/formulario/quehacer", methods = ['GET'] )
def desplegar_formulario_quehacer():
    if 'nombre' in session:
        session['contador'] += 1
    return render_template( "formulario_quehacer.html" )

@app.route( "/nuevo/quehacer", methods = ['POST'] )
def agregar_quehacer():
    nuevo_quehacer = {
        "descripcion" : request.form["descripcion"],
        "estatus" : request.form["estatus"],
        "id_usuario" : session['id_usuario']
    }
    Quehaceres.crear_uno( nuevo_quehacer )
    return redirect( "/quehaceres" )

@app.route( "/eliminar/quehacer/<int:id>", methods=["POST"] )
def elimina_quehacer( id ):
    data = {
        "id" : id
    }
    Quehaceres.elimina_uno( data )
    return redirect( "/quehaceres" )

@app.route( "/formulario/quehacer/<int:id>", methods=["GET"] )
def desplegar_formulario_editar_quehacer( id ):
    data = {
        "id" : id
    }
    quehacer_actual = Quehaceres.selecciona_uno( data )
    return render_template( "formulario_editar_quehacer.html", quehacer_actual = quehacer_actual )

@app.route( "/actualizar/quehacer/<int:id>", methods=["POST"] )
def actualiza_quehacer( id ):
    data = {
        "id" : id,
        "descripcion" : request.form["descripcion"],
        "estatus" : request.form["estatus"],
        "id_usuario" : session['id_usuario']
    }
    Quehaceres.actualiza_uno( data )
    return redirect( "/quehaceres" )

"""
GET
Obtener toda la lista/tabla de un cierto tipo de dato
URL: "/quehaceres"
Funcion: get_all_quehaceres()
         get_quehaceres()

Obtener un solo item de la lista/tabla de un cierto tipo de dato
URL: "/quehacer/<int:id>"
Funcion: get_quehacer_by_id( id )
         get_quehacer( id )

Desplegar un formulario o página que eventualmente estará conectado con una lista/tabla
URL: "/quehacer/form"
Funcion: display_quehacer_form()

POST
Agregar un nuevo item a la lista/tabla de un cierto tipo de dato
URL: "/quehacer/new"
     "/quehacer/add"
Funcion: create_quehacer()
         add_quehacer()
         new_quehacer()

PUT (Pero utilizaremos el método POST)
Actualizar un item existente de la lista/tabla de un cierto tipo de dato
URL: "/quehacer/update/<int:id>"
     "/quehacer/edit/<int:id>"
Funcion: update_quehacer( id )
         edit_quehacer( id )

DELETE (Pero utilizaremos el método POST)
Remover un item existente de la lista/tabla de un cierto tipo de dato
URL: "/quehacer/delete/<int:id>"
     "/quehacer/remove/<int:id>"
Funcion: remove_quehacer( id )
         delete_quehacer( id )

"""