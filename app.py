from datetime import datetime, timedelta
from flask import Flask,  render_template, redirect, request
from data.estudiante import Estudiante
from data.correo import Correo
from data.PDF import PDF
from persistence.consultas import Consultas
import cx_Oracle
app   = Flask(__name__)
consultasbd = Consultas()
identificacion = ''
nombre_docente = ''
idobra = ''
consecutivo_calendario = ''

@app.route('/')
def formularioPrincipal():
    return render_template('index.html')


@app.route('/procesar',methods=['POST'])
def procesar(): 
    global identificacion, nombre_docente, idobra, consecutivo_calendario
    identificacion =request.form['identificacion']
    correo =request.form['email'].upper()
    valores = []
    if (identificacion, correo) in consultasbd.empleados_con_acceso():
        nombre_docente, correo_docente = consultasbd.info_docente(identificacion)[0]
        resultado = consultasbd.obra_activa(identificacion)
        if len(resultado) > 0:#Hay obra activa
            idobra, titulo_obra = resultado[0]
            fechas_eventos = consultasbd.obtener_fechas_horas(idobra)
            fecha_actual = datetime.now()
            for ido, consc, fechai, fechaf in fechas_eventos:
                di, moi, ai, hi, mi = fechai.split()
                df, mof, af, hf, mf = fechaf.split()
                finicio = datetime(int(ai), int(moi), int(di), int(hi), int(mi))
                ffin = datetime(int(af), int(mof), int(df), int(hf), int(mf))
                if fecha_actual > finicio and fecha_actual < ffin:
                    veri = ['asiste','#','#']
                    consecutivo_calendario = consc
                    return render_template('envio.html',veri=veri,nombre=nombre_docente,hora=datetime.now().strftime("%H:%M:%S"),tiObra=titulo_obra)
            else:
                ido, consc, fechai, fechaf = fechas_eventos[-1]
                df, mof, af, hf, mf = fechaf.split()
                ffin = datetime(int(af), int(mof), int(df), int(hf), int(mf))
                if fecha_actual > ffin:
                    veri = ['#','viatic','#']
                    idobra = ido
                    consecutivo_calendario = consc
                    return render_template('envio.html',veri=veri,nombre=nombre_docente,hora=datetime.now().strftime("%H:%M:%S"),tiObra=titulo_obra)    
        else: #No hay obras activas
            valores = consultasbd.obras_inactivas(identificacion)
            veri = ['#','#','#']
            return render_template('listaobras.html',veri=veri,nombre=nombre_docente,valores=valores,hora=datetime.now().strftime("%H:%M:%S"))
    else:
        return render_template('index.html');




@app.route('/muestraPDF' ,methods=['POST'])
def muestraPDF():
    mp = PDF()
    mp.carta()##pasarle la data de viaticos
    return render_template('viaticos.html')



@app.route('/asiste', methods=['GET', 'POST'])
def asiste():
    global identificacion, nombre_docente, idobra, consecutivo_calendario
    valores = consultasbd.asistentes_obra(idobra, consecutivo_calendario)
    if request.method=="POST":
        for dato in request.form:
            conscal = consultasbd.consecutivo_asistencia()
            consultasbd.actualizar_asistencia(conscal+1, dato, idobra, consecutivo_calendario)
            
    return render_template('asistencia.html',valores=valores)

@app.route('/viatic', methods=['GET', 'POST'])
def viatic():
    global identificacion, nombre_docente, idobra
    valores = consultasbd.estudiantes_viaticos(idobra)
    pdf = ''
    if request.method=="POST":
        pdf = '/static/form.pdf'
        
        Gpdf= PDF()
        Gpdf.carta()
        #desactivar obra y generar pdf
    return render_template('viaticos.html',valores=valores,pdf=pdf)

@app.route('/certifica', methods=['GET','POST'])
def certifica():
    global identificacion, nombre_docente, idobra
    ##
    if request.method == 'POST':
        idEstudiante=request.form['codigo']
        valores=consultasbd.estudianteObra(idEstudiante)
        print (valores)
        return render_template('certificados2.html', valores=valores)
    return render_template('certificados.html')
    



@app.route('/listaobras', methods=['POST', 'GET'])
def listaobras():
    global identificacion, nombre_docente, idobra
    if request.method=="POST":
        idobra=request.form['obras']
        valores = consultasbd.obras_inactivas(identificacion)
        veri = ['#','#','certifica']
        return render_template('listaobras.html',veri=veri,nombre=nombre_docente,valores=valores,hora=datetime.now().strftime("%H:%M:%S"))


    valores = consultasbd.obras_inactivas(identificacion)
    veri = ['#','#','#']
    return render_template('listaobras.html',veri=veri,nombre=nombre_docente,valores=valores,hora=datetime.now().strftime("%H:%M:%S"))


if __name__ == '__main__':
    app.run(debug=True)
