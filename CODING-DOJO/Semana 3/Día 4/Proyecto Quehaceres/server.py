from flask import Flask, render_template, request, redirect

app = Flask(__name__)

quehaceres = [{
        "descripcion" : "Aprender Flask",
        "estatus" : "En proceso",
        "id" : 123 
    },
    {
        "descripcion" : "Aprender Programación Orientada a Objetos",
        "estatus" : "Completo",
        "id" : 456 
    },
    {
        "descripcion" : "Aprender Bases de Datos",
        "estatus" : "Completo",
        "id" : 789 
    },
    {
        "descripcion" : "Aprender MVC",
        "estatus" : "Pendiente",
        "id" : 555
    }]

@app.route( "/quehaceres", methods = ['GET'] )
def obtener_quehaceres():
    return render_template( "quehaceres.html", nombre = "Alex", apellido = "Miller", quehaceres = quehaceres )

@app.route( "/formulario/quehacer", methods = ['GET'] )
def desplegar_formulario_quehacer():
    return render_template( "formulario_quehacer.html" )

@app.route( "/nuevo/quehacer", methods = ['POST'] )
def agregar_quehacer():
    nuevo_quehacer = {
        "descripcion" : request.form["descripcion"],
        "estatus" : request.form["estatus"],
        "id" : request.form["identificador"]
    }
    quehaceres.append( nuevo_quehacer )
    return redirect( "/quehaceres" )


if __name__ == "__main__":
    app.run( debug = True)


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