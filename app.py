from datetime import datetime, timedelta
from flask import Flask,  render_template, redirect, request
from data.estudiante import Estudiante
from data.correo import Correo
from persistence.estudianteDAO import EstudianteDAO
import cx_Oracle
app   = Flask(__name__)


ultima_fecha = datetime(2022, 2, 17, 7)
#cx_Oracle.init_oracle_client(r"C:\oraclexe\app\oracle\product\Cliente18")

@app.route('/')
def formularioPrincipal():
    return render_template('index.html')


@app.route('/procesar',methods=['POST'])
def procesar():
    nombre =request.form['nombre']
    apellidos =request.form['apellido']
    identificacion =request.form['identificacion']
    correo =request.form['email']
    codigo =request.form['codigo']
    fecha = f"'{request.form['fecha']}'"
    estudiante = Estudiante(nombre,apellidos,identificacion,fecha,codigo,correo)
    eDAO = EstudianteDAO()
    eDAO.guardar(Estudiante.registrados, estudiante, 1, 1)
    inc_hora()
    envioCorreo=Correo(nombre,correo)
    envioCorreo.send(ultima_fecha.ctime(), 'Macarena')
    return render_template('envio.html',n=nombre,apellido=apellidos,horas=ultima_fecha.ctime())


def inc_hora():
    global ultima_fecha

    if ultima_fecha.hour == 17:
        if ultima_fecha.isoweekday() == 5:
            ultima_fecha += timedelta(hours=14, days=2)
        else:
            ultima_fecha += timedelta(hours=14)
    else:
        ultima_fecha += timedelta(hours=1)



if __name__ == '__main__':
    app.run()
