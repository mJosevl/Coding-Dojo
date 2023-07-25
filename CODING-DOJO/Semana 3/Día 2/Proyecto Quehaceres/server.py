from flask import Flask, render_template

app = Flask(__name__)

quehaceres = [{
        "descripcion" : "Aprender Flask",
        "estatus" : "En proceso" 
    },
    {
        "descripcion" : "Aprender Programación Orientada a Objetos",
        "estatus" : "Completo" 
    },
    {
        "descripcion" : "Aprender Bases de Datos",
        "estatus" : "Completo" 
    },
    {
        "descripcion" : "Aprender MVC",
        "estatus" : "Pendiente" 
    }]

@app.route( "/bienvenidas", methods = ['GET'] )
def mensaje_bienvenida():
    return "Bienvenidas al mundo de Flask!"

@app.route( "/prueba", methods = ['GET'] )
def mensaje_prueba():
    return "Esto es un mensaje de prueba en nuestra segunda ruta!"

@app.route( "/multiplica/<int:num1>", methods = ['GET'] )
def multiplica_por_diez( num1 ):
    total = num1 * 10
    return f"{num1} x 10 = {total}"

@app.route( "/multiplica/<int:num1>/<int:num2>", methods = ['GET'] )
def multiplica_dos_numeros( num1, num2 ):
    total = num1 * num2
    return f"{num1} x {num2} = {total}"

@app.route( "/", methods = ['GET'] )
def home():
    print( "Vamos a renderizar el index.html" )
    return render_template( "index.html", nombre = "Alex", apellido = "Miller", quehaceres = quehaceres )

if __name__ == "__main__":
    app.run( debug = True )
