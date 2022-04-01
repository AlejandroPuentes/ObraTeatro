from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from os.path import join, dirname, realpath
import os.path
import shutil




class PDF2:

    def __init__(self):
        self.canvas = None

    def guardado(self):
        self.canvas = canvas.Canvas("Certificado.pdf", pagesize=letter)
        self.canvas.setLineWidth(.3)
        self.canvas.setFont('Helvetica', 12)

    def movidaPDF(self):
        source = r'C:\Users\User\Documents\Bases de Datos\ObraTeatro\Certificado.pdf'
        destination = r'C:\Users\User\Documents\Bases de Datos\ObraTeatro\static\Certificado.pdf'
        shutil.move(source, destination)

    def carta(self,docente,data):
        self.guardado()
        self.canvas.drawString(30,750,'Certificado')
        self.canvas.drawString(30,735,'Bogotá 2022')

        self.canvas.drawString(30,720,'Decanatura de la Facultad de Artes')

        self.canvas.drawString(250,650,'Certifica Que:')

        self.canvas.drawString(30,640,'el Estudiante participo en:')
        self.canvas.drawString(30,620,"cordial saludo, el siguiente correo es para informar que la universidad Distrital Francisco jose") 
        self.canvas.drawString(30,610,"de caldas Certifica por participacion en Obras de teatro de la universidad para lo cual se adjunta")
        self.canvas.drawString(30,600,"el siguiente certificado")
        datas=[('ALBERTO ACOSTA', 'MERACOPIA2000@GMAIL.COM', '2017102000', "Pepa"),('ALBERTO maria', 'MERACOPIA2000@GMAIL.COM', '2017102000', "PEP",),('Jose ACOSTA', 'MERACOPIA2000@GMAIL.COM', '2017102000',"HEt")]
        x=40
        y=550
        valor =0.0
        for i in (data):            
            nombreO,director,Periodo = (i)
            fila = nombreO+'      '+director+'      '+Periodo
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

pdf = PDF2()
data=[]
pdf.carta("jorge melo",data)