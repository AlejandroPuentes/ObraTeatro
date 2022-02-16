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


    def mensaje(self, fecha, teatro):
        msm=MIMEMultipart("alternative")
        msm["Subject"]="Registro Exitoso"
        msm["From"]=self.user_mail
        msm["To"]=self.email


        self.html= f'''
        <html>
            Buen día <i>{self.name}</i> se ha registrado exitosamente al grupo de teatro de la Universidad Distrital<br>
            Recuerde presentarse en el teatro {teatro} en la fecha: {fecha}.<br>
            Que tenga un excelente día.
        </html> '''
        parte_html=MIMEText(self.html,"html")
        
        msm.attach(parte_html)
        return msm


    def send(self, fecha, teatro):
        envi=self.mensaje(fecha, teatro)
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain, self.port, context=ssl_context)
        try:
            service.login(self.user_mail, self.password)
            print('sesion iniciada')
        except:
                print('no se ha podiodo iniciar sesion')
        
        try:
            service.sendmail(self.user_mail,self.email,envi.as_string())
            print("mensaje Enviado")
        except Exception:
            print("no se ha podido  hacer el envio debido a ", Exception)

        service.quit()

if __name__ == '__main__':
    email=Correo()
    email.send()