from flask import Flask,  render_template, redirect, request
from data.estudiante import Estudiante
from persistence.estudianteDAO import EstudianteDAO
app   = Flask(__name__)



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
    yy, mm, dd = request.form['fecha'].split('-')
    fecha = f"'{dd}/{mm}/{yy}'"
    estudiante = Estudiante(nombre,apellidos,identificacion,fecha,codigo,correo)
    eDAO = EstudianteDAO()
    eDAO.guardar(estudiante, 1, 1)
    return render_template('index.html')




if __name__ == '__main__':
    app.run()


