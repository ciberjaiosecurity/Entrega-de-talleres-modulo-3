from flask import Flask
app = Flask(__name__)
@app.route("/")
def inicio():
    return "<p>Bienvenido al Módulo de Desarrollo Seguro</p>"
	
@app.route("cal/sum/<int:val1>/<int:val2>")
def cal_suma(val1, val2):
    resul = val1 + val2
    resp = "<p>El resultado de la suma es { }!</p>".format(resul)
    return resp 

