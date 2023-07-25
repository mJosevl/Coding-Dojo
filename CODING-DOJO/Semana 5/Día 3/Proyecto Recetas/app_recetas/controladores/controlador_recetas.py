from flask import render_template, request, session, redirect
from app_recetas.modelos.modelo_recetas import Receta
from app_recetas import app

@app.route( '/recetas', methods = ['GET'] )
def desplegar_recetas():
    if "id_usuario" not in session:
        return redirect( '/' )
    else:
        lista_recetas = Receta.obtener_todas_con_usuario()
        return render_template( 'recetas.html', lista_recetas = lista_recetas )

@app.route( '/formulario/receta', methods = ['GET'] )
def desplegar_formulario_receta():
    if "id_usuario" not in session:
        return redirect( '/' )
    else:
        return render_template( 'formulario_receta.html' )

@app.route( '/crear/receta', methods = ['POST'] )
def nueva_receta():
    data = {
        **request.form,
        "id_usuario" : session['id_usuario']
    }
    if Receta.validar_formulario_recetas( data ) == False:
        return redirect( '/formulario/receta' )
    else:
        id_receta = Receta.crear_uno( data )
        return redirect( '/recetas' ) 
    
@app.route( '/eliminar/receta/<int:id>', methods = ['POST'] )
def eleminar_receta( id ):
    data = {
        "id" : id
    }
    Receta.elimina_uno( data )
    return redirect( '/recetas' )

@app.route( '/receta/<int:id>', methods = ['GET'] )
def desplegar_receta( id ):
    if "id_usuario" not in session:
        return redirect( '/' )
    else:
        data = {
            "id" : id
        }
        receta = Receta.obtener_uno_con_usuario( data )
        return render_template( 'receta.html', receta = receta )

@app.route( '/formulario/editar/receta/<int:id>', methods = ['GET'] )
def desplegar_editar_receta( id ):
    if "id_usuario" not in session:
        return redirect( '/' )
    else:
        data = {
            "id" : id
        }
        receta = Receta.obtener_uno( data )
        return render_template( 'editar_receta.html', receta = receta )

@app.route( '/editar/receta/<int:id>', methods = ['POST'] )# VALIDAR EL FORMULARIO DE RECETAS
def editar_receta( id ):
    if Receta.validar_formulario_recetas( request.form ) == False:
        return redirect( f'/formulario/editar/receta/{id}' )
    else:
        data = {
            **request.form,
            "id" : id
        }
        Receta.editar_uno( data )
        return redirect( '/recetas' )
    