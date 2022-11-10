from flask import Flask
app = Flask(__name__)
@app.route("/")
def inicio():
    return "<p>Bienvenido al Módulo de Desarrollo Seguro</p>"
	
