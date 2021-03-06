
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from os.path import join, dirname, realpath
import os.path
import shutil




class PDF:

    def __init__(self):
        self.canvas = None

    def guardado(self):
        self.canvas = canvas.Canvas("form.pdf", pagesize=letter)
        self.canvas.setLineWidth(.3)
        self.canvas.setFont('Helvetica', 12)

    def movidaPDF(self):
        source = r'C:\Users\User\Documents\Bases de Datos\ObraTeatro\form.pdf'
        destination = r'C:\Users\User\Documents\Bases de Datos\ObraTeatro\static\form.pdf'
        shutil.move(source, destination)

    def carta(self,docente,data):
        self.guardado()
        self.canvas.drawString(30,750,'CARTA IQUIDACION DE VIATICOS')
        self.canvas.drawString(30,735,'Bogotá 2022')
        self.canvas.drawString(500,750,"27/10/2022")
        self.canvas.line(480,747,580,747)

        self.canvas.drawString(30,720,'ESTIMADO:')
        self.canvas.drawString(225,725,"Decanatura de la Facultad de Artes")
        self.canvas.line(378,723,580,723)

        self.canvas.drawString(250,690,'Solicitud:')
        self.canvas.line(60,680,580,680)
        self.canvas.drawString(60,650,'El presente comunidado tiene como fin la referencia sobre la indicacion de la liquidacion  ')
        self.canvas.drawString(60,630,'de los viaticos de los estudiantes de la obra TAL, los cuales inician el dia')
        self.canvas.drawString(60,610,'TAl y terminan  el dia Tal.')

        ##datas=[('ALBERTO ACOSTA', 'MERACOPIA2000@GMAIL.COM', '2017102000', 2, 2),('ALBERTO maria', 'MERACOPIA2000@GMAIL.COM', '2017102000', 2, 2),('Jose ACOSTA', 'MERACOPIA2000@GMAIL.COM', '2017102000', 2, 2)]
        x=30
        y=590
        valor =0.0
        for i in (data):            
            nombre,correo,codigo,seciones,horas = (i)
            fila = nombre+'      '+correo+'      '+codigo+'      '+str(seciones)+'      '+str(horas)
            self.canvas.drawString(x,y,fila+" ")            
            y=y-10
            self.canvas.line(20,y,600,y)
            y=y-20
            x=30
                
            

        self.canvas.drawString(110,y-100,docente)
        self.canvas.line(90,y-100,300,y-100)
        self.canvas.drawString(110,y-110,"Firma")
        self.canvas.save()
        self.movidaPDF()

pdf = PDF()
data=[]
pdf.carta("jorge melo",data)
'''number='informe'
pdf_name = number + ".pdf"
save_name = os.path.join(os.path.expanduser("~"), "static/", pdf_name)
print(save_name)'''