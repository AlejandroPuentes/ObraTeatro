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
        self.canvas = canvas.Canvas("Certificado.pdf", pagesize=letter)
        self.canvas.setLineWidth(.3)
        self.canvas.setFont('Helvetica', 12)

    def movidaPDF(self):
        source = r'C:\Users\User\Documents\Bases de Datos\ObraTeatro\Certificado.pdf'
        destination = r'C:\Users\User\Documents\Bases de Datos\ObraTeatro\static\Certificado.pdf'
        shutil.move(source, destination)

    def carta(self,docente,data=None):
        self.guardado()
        self.canvas.drawString(30,750,'Certificado')
        self.canvas.drawString(30,735,'Bogotá 2022')
        self.canvas.line(480,747,580,747)

        self.canvas.drawString(30,720,'Decanatura de la Facultad de Artes Certifica que:')
        self.canvas.line(378,723,580,723)

        self.canvas.drawString(250,690,'el Estudiante participo en:')
        

        x=100
        y=590
        valor =0.0
        for i in range(len(data)):
            for j in range(len(i)):
                self.canvas.drawString(x,y,data[i][0]+" ")
                x=x+30
            x=100
            y=y-30          
        

        self.canvas.drawString(110,y-100,docente)
        self.canvas.line(90,y-100,300,y-100)
        self.canvas.drawString(110,y-110,"Firma")
        self.canvas.save()
        self.movidaPDF()