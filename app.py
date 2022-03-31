from datetime import datetime, timedelta
from flask import Flask,  render_template, redirect, request
from data.estudiante import Estudiante
from data.correo import Correo
from data.PDF import PDF
from persistence.consultas import Consultas
import cx_Oracle
app   = Flask(__name__)
consultasbd = Consultas()


def verificarFe(hora1=None,hora22=None):
    f1 =datetime.now().strftime("%H:%M:%S")
    f2H = 8
    f2m = 30
    f2s = 15
    hora=datetime(year=2022 ,month=3,day=30,hour =f2H, minute=f2m, second=f2s).strftime("%H:%M:%S")
    hora2=datetime(year=2022 ,month=3,day=30,hour =f2H+2, minute=f2m+20, second=f2s).strftime("%H:%M:%S")
    
    if hora<f1 and hora2>f1 :
        return   ['asiste','#','#']
    elif f1>hora2:
        return ['#','viatic','#']
    return ['#','#','certifica']

ultima_fecha = datetime(2022, 2, 17, 7)
#cx_Oracle.init_oracle_client(r"C:\oraclexe\app\oracle\product\Cliente18")

@app.route('/')
def formularioPrincipal():
    return render_template('index.html')


@app.route('/procesar',methods=['POST'])
def procesar():
    rang=verificarFe()   
    identificacion =request.form['identificacion']
    correo =request.form['email'].upper()
    valores = []
    if (identificacion, correo) in consultasbd.empleados_con_acceso():
        print('pasa y esta mal XD')
        resultado = consultasbd.encabezado(identificacion)
        if len(resultado) > 0:#Hay obra activa
            obra, docente = resultado[0]
            fechas_eventos = consultasbd.obtener_fechas_horas(obra)
            idobra = -1
            cons = -1
            fecha_actual = datetime.now()
            for ido, consc, fechai, fechaf in fechas_eventos:
                di, moi, ai, hi, mi = fechai.split()
                df, mof, af, hf, mf = fechaf.split()
                finicio = datetime(int(ai), int(moi), int(di), int(hi), int(mi))
                ffin = datetime(int(af), int(mof), int(df), int(hf), int(mf))
                if fecha_actual > finicio and fecha_actual < ffin:
                    veri = ['asiste','#','#']
                    idobra = ido
                    cons = consc
                    return render_template('envio.html',idObra=idobra,consC=cons,veri=veri,nombre=docente, valores=valores,hora=datetime.now().strftime("%H:%M:%S"),tiObra=obra)
            else:
                ido, consc, fechai, fechaf = fechas_eventos[-1]
                df, mof, af, hf, mf = fechaf.split()
                ffin = datetime(int(af), int(mof), int(df), int(hf), int(mf))
                if fecha_actual > ffin:
                    veri = ['#','viatic','#']
                    idobra = ido
                    cons = consc
                    return render_template('envio.html',idObra=idobra,consC=cons,veri=veri,nombre=docente, valores=valores,hora=datetime.now().strftime("%H:%M:%S"),tiObra=obra)
            veri = ['#', '#', '#']
            return render_template('envio.html',veri=veri,nombre=docente, valores=valores,hora=datetime.now().strftime("%H:%M:%S"),tiObra=obra)

           
        else: #No hay obras activas
            valores = consultasbd.obras_inactivas(identificacion)
            print('------------**********',valores)
            veri = ['#','#','certifica']
            return render_template('envio.html',veri=veri,valores=valores,hora=datetime.now().strftime("%H:%M:%S"))
    else:
        return render_template('index.html');




@app.route('/muestraPDF' ,methods=['POST'])
def muestraPDF():
    c=verificarFe()
    mp = PDF()
    mp.carta()##pasarle la data de viaticos
    return render_template('viaticos.html',veri=c)



@app.route('/asiste' ,methods=['POST'])
def asiste():
    c=verificarFe()
    return render_template('asistencia.html',veri=c)




@app.route('/viatic')
def viatic():
    c=verificarFe()
    return render_template('viaticos.html',veri=c)

@app.route('/certifica')
def certifica():
    c=verificarFe()
    return render_template('certificados.html',veri=c)



if __name__ == '__main__':
    app.run(debug=True)
