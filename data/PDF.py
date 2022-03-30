
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
class PDF:

    def __init__(self):
        self.canvas = canvas.Canvas("form.pdf", pagesize=letter)
        self.canvas.setLineWidth(.3)
        self.canvas.setFont('Helvetica', 12)

    
    def carta(self,data=None):
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

        data = [("NOMBRE",'Alejandro'), ("NOTA 1",4.2), ("NOTA 1",4.2), ("NOTA 1",4.2)]
        x=250
        y=590
        valor =0.0
        for i in range(len(data)):
            self.canvas.drawString(x,y,data[i][0]+" ")
            x=x+100
            self.canvas.drawString(x,y,str(data[i][1])+"")
            if i>0:
                valor=+data[i][1]
            x=250
            y=y-30
            
        self.canvas.line(200,y,600,y)
        self.canvas.drawString(250,y-20,"Total")
        self.canvas.drawString(360,y-20,str(valor))

        self.canvas.drawString(110,y-100,"XXXXX")
        self.canvas.line(90,y-100,300,y-100)
        self.canvas.drawString(110,y-110,"Firma")
        self.canvas.save()

pdf = PDF()
pdf.carta()