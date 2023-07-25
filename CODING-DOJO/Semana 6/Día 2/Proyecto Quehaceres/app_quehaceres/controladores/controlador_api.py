from flask import json, jsonify, request
from flask_cors import cross_origin
from app_quehaceres.modelos.modelo_quehaceres import Quehaceres
from app_quehaceres import app

@app.route( '/api/quehaceres', methods = ['GET'] )
@cross_origin( origins = ['http://127.0.0.1:5500'] )
def api_obtener_quehaceres():
    lista_quehaceres = Quehaceres.api_seleccionar_todos()
    return ( jsonify( lista_quehaceres ), 200 )

@app.route( '/api/quehacer/nuevo', methods = ['POST'] )
@cross_origin( origins = ['http://127.0.0.1:5500'] )
def api_crear_quehacer():
    nuevo_quehacer = json.loads( request.data.decode( 'UTF-8' ) )
    id_quehacer = Quehaceres.crear_uno( nuevo_quehacer )
    respuesta = {
        "mensaje" : "Quehacer agregado debidamente",
        "id_quehacer" :  id_quehacer,
        "status" : 201
    }
    return ( jsonify( respuesta ), 201 )

@app.route( '/api/eliminar/quehacer/<int:id>', methods = ['DELETE'] )
@cross_origin( origins = ['http://127.0.0.1:5500'] )
def api_eliminar_quehacer( id ):
    data = {
        "id" : id
    }
    Quehaceres.elimina_uno( data )
    """
    Estatus 204 es para eliminar, pero no envía nada de vuelta.
    
    respuesta = {
        "mensaje" : "Quehacer eliminado debidamente",
        "status" : 204
    }
    """
    return ( {}, 204 )

@app.route( '/api/actualizar/quehacer/<int:id>', methods = ['PUT'] )
@cross_origin( origins = ['http://127.0.0.1:5500'] )
def api_actualizar_quehacer( id ):
    quehacer_a_actualizar = json.loads( request.data.decode( 'UTF-8' ) )
    quehacer_a_actualizar['id'] = id
    Quehaceres.actualiza_uno( quehacer_a_actualizar )
    respuesta = {
        "mensaje" : "Quehacer actualizado debidamente",
        "status" : 206
    }
    return ( jsonify( respuesta ), 206 )
