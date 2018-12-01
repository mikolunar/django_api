#toolkit

import smtplib
import re
from email.mime.text import MIMEText
import getpass




class Email:

    domains=['pl', 'es']
    valid_email_re=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    total_emails_sent=0
    instance_emails_sent=0
  
    def __init__(self, subject, sender, recipient, message):

        self.subject=subject
        self.sender=sender
        self.recipient=recipient
        self.message=message



    @classmethod
    def set_total_emails(cls, total):
        cls.total_emails_sent=total

    @classmethod
    def set_email_re(cls, regex):
        cls.valid_email_re=regex

    @staticmethod
    def validate_email(email):
        if re.match(Email.valid_email_re, email):
            return True
        else:
            return False

   
    def validate_sender(self):

        if re.match(self.valid_email_re,self.sender):
            return True
        else:
            return False

        
    def validate_recipient(self):
        if re.match(self.valid_email_re,self.recipient):
            return True
        else:
            return False


      
    
    def validate(self):

        if self.validate_recipient():
            if self.validate_sender():
                if isinstance(self.subject, str):
                    return True
        
        return False
        


    def sent(self):
       
        self.instance_emails_sent+=1
        Email.total_emails_sent+=1

        return True

    def print_email(self):

        return 'Subject: '+self.subject+'\n'+'From: '+ self.sender+'\n'+'To: '+ self.recipient +'\n'+'Msg: '+ self.message


        
    def __str__(self):
        return self.print_email()

    def __repr__(self):
        return "Email('{}','{},'{}','{})".format(self.subject, self.sender, self.recipient, self.message)



class Mailer:

    server=''

    def __init__(self,host, port, login, password):
        self.server=smtplib.SMTP(host,port)
        login=self.server.login(login,password)
    
    def sendmail(self, msg):

        self.server.sendmail(msg['From'], msg['To'], msg.as_string())


# HOST='serwer1880861.home.pl'
# PORT=587
# LOGIN='me@serwer1880861.home.pl'
# PASS=getpass.getpass()
# mailer=Mailer(HOST, PORT, LOGIN, PASS)

msg = MIMEText('This is improved MIME message')
msg['Subject'] = 'The contents of'
msg['From'] = 'me@sintetics.pl'
msg['To'] = 'mr@marcinros.net'

#mailer.sendmail(msg)

email1=Email(msg['Subject'], msg['From'], msg['To'], msg.get_payload())

print(email1)
