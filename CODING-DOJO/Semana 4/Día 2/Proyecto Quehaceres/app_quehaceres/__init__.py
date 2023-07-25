from flask import Flask

app = Flask(__name__)
app.secret_key = "esto es secreto"

BASE_DE_DATOS = "bd_quehaceres"