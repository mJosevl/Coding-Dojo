from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route( "/hola", methods = ["GET"])
def hola():
    return "Hola desde el proyecto dos!"

if __name__ == "__main__":
    app.run( debug = True )
