from email import encoders
from email.mime.base import MIMEBase
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Correo:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.port=465
        self.smtp_server_domain="smtp.gmail.com"
        self.user_mail="programpros0222@gmail.com"
        self.password="Bapcjsmz2017*"
        self.html=None


    def mensaje(self):
        msm=MIMEMultipart("alternative")
        msm["Subject"]="Registro Exitoso"
        msm["From"]=self.user_mail
        msm["To"]=self.email


        self.html= f'''
        <html>
            cordial saludo, el siguiente correo es para informar que la universidad Distrital 
            Francisco jose de caldas Certifica a ${self.name} por participacion en Obras de teatro de la universidad para lo cual
            se adjunta el siguiente certificado.
        </html> '''
        parte_html=MIMEText(self.html,"html")
        
        msm.attach(parte_html)
        archivo ="./static/Certificado.pdf"
        with open(archivo,"rb") as adjunto:
            contenido = MIMEBase("application", "octet-stream")
            contenido.set_payload(adjunto.read())
        
        encoders.encode_base64(contenido)
        contenido.add_header("Content-Disposition", 
                            f"attachment; filename={archivo}",)
        msm.attach(contenido)

        return msm


    def send(self):
        envi=self.mensaje()
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain, self.port, context=ssl_context)
        try:
            service.login(self.user_mail, self.password)
            print('sesion iniciada')
        except Exception:
                print('no se ha podiodo iniciar sesion')
                print(Exception)
        

        
        try:
            service.sendmail(self.user_mail,self.email,envi.as_string())
            print("mensaje Enviado")
        except Exception:
            print("no se ha podido  hacer el envio debido a ", Exception)

        service.quit()

if __name__ == '__main__':
    email=Correo('alejo',"programpros0222@gmail.com")
    email.send('21-05-65','agustiniano')