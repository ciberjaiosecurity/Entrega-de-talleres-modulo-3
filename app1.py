from flask import Flask
import logging

#crear la configuracion del logger

logging.basicConfig(
filename="tallerJeanPerez16013813.log",
format='%(asctime)s %(messajes)',
filemode='w')

#instanciar el objeto logger
logger = logging.getLogger()

#configurar que debe notificar a partir de DEBUG
logger.setLevel(logging.DEBUG)
app = Flask(__name__)
@app.route("/")
def inicio():
    return "<p>Bienvenido módulo de Desarrollo Seguro</p>"

@app.route("/cal/sum/<int:val1>/<int:val2>")
def cal_suma(val1, val2):
    resul = val1 + val2
    resp = "<p>El resultado de la suma es {}! </p>".format(resul)
    logger.info("val1:{}, val2:{}, {}".format(val1,val2,resp))
    return resp


@app.route("/cal/rest/<int:val1>/<int:val2>")
def cal_resta(val1, val2):
    resul = val1 - val2
    resp = "<p>El resultado de la resta es {}! </p>".format(resul)
    logger.info("val1:{}, val2:{}, {}".format(val1,val2,resp))
    return resp

@app.route("/cal/mult/<int:val1>/<int:val2>")
def cal_multiplicacion(val1, val2):
    resul = val1 * val2
    resp = "<p>El resultado de la multiplicación es {}! </p>".format(resul)
    logger.info("val1:{}, val2:{}, {}".format(val1,val2,resp))
    return resp

@app.route("/cal/div/<int:val1>/<int:val2>")
def cal_division(val1, val2):
    resul = val1 / val2
    resp = "<p>El resultado de la división es {}! </p>".format(resul)
    logger.info("val1:{}, val2:{}, {}".format(val1,val2,resp))
    return resp


