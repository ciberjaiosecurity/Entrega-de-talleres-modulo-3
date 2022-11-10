from flask  import Flask
import logging

logging.basicConfig(
    filename="tallerJesusIbarra14261350.log",
    format='%(asctime)s %(message)s',
    filemode='w'
)

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

app = Flask(__name__)
@app.route('/')
def inicio():
    return "<p><b>Bienvenido al Módulo de Desarrollo Seguro<b></p>"

@app.route('/cal/sum/<int:val1>/<int:val2>')
def cal_suma(val1,val2):
    resul = val1 + val2
    rep = "<p>El resultado de la suma es {}</p>".format(resul)
    logger.info("Val1:{}, Val2:{}, {}".format(val1,val2,rep))
    return rep

@app.route('/cal/rest/<int:val1>/<int:val2>/<int:val3>')
def cal_rest(val1,val2,val3):
    resul = val1 - val2 - val3 
    rep = "<p>El resultado de la resta es {}</p>".format(resul)
    logger.info("Val1:{}, Val2:{}, Val3:{}, {}".format(val1,val2,val3,rep))
    return rep

@app.route('/cal/mult/<int:val1>/<int:val2>/<int:val3>')
def cal_mult(val1,val2,val3):
    resul = val1 * val2 * val3
    rep = "<p>El resultado de la multiplicacion es {}</p>".format(resul)
    logger.info("Val1:{}, Val2:{}, Val3:{}, {}".format(val1,val2,val3,rep))
    return rep

@app.route('/cal/div/<int:val1>/<int:val2>/<int:val3>')
def cal_div(val1,val2,val3):
    resul = val1 / val2 / val3
    rep = "<p>El resultado de la division es {}</p>".format(resul)
    logger.info("Val1:{}, Val2:{}, Val3:{}, {}".format(val1,val2,val3,rep))
    return rep
