import smtplib
from email.mime.text import MIMEText


class Mailer(smtplib.SMTP):

    port=587
    host=''
    login=''
    password=''
   
    def __init__(self, host, port, login, password):

        self.port=port
        self.host=host
        self.login=login 
        self.password=password

        super().__init__(self.host,self.port) 
        return self

 



