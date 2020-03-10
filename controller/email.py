import mimetypes
import os
import smtplib

from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class email:
    def __init__(self): 
        email = 0 
        
    def enviaEmail(self,email,file):
   
        #try:
            fromaddr = "filebot0@gmail.com"
            toaddr = email
            msg = MIMEMultipart()

            msg['From'] = fromaddr 
            msg['To'] = toaddr 
            msg['Subject'] = "It's New!"
           
            ctype, encoding = mimetypes.guess_type(file)

            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'

            maintype, subtype = ctype.split('/', 1)
            print(file)
            if maintype == 'text':
                with open(file) as f:
                    mime = MIMEText(f.read(), _subtype=subtype)
            elif maintype == 'image':
                with open(file, 'rb') as f:
                    mime = MIMEImage(f.read(), _subtype=subtype)
            elif maintype == 'audio':
                with open(file, 'rb') as f:
                    mime = MIMEAudio(f.read(), _subtype=subtype)
            else:
                with open(file, 'rb') as f:
                    mime = MIMEBase(maintype, subtype)
                    mime.set_payload(f.read())

            encoders.encode_base64(mime)

            mime.add_header('Content-Disposition', 'attachment', filename=file)
            msg.attach(mime)

            name = email.split('@')
            print(name)
            name = name[0]
            print(name)

            body = (
            '<!DOCTYPE html>\n'
            '<html>\n'
            '<head>\n'
            '<style type="text/css">\n'
            'body {font-family: "Roboto"}\n'
            'h1 {text-align: center; font-size: 250%;}\n'
            'p {margin-left: 10%; margin-right: 10%; font-size: 140%;}\n'
            'img {margin-left: 27%; margin-right: 27%; width: 40%;}\n'
            '</style>\n'
            '<title></title>\n'
            '</head>\n'
            '<body>\n'
            '<h1>You have mail!</h1>\n'
            '<p>Dear ' + name + ',</p>\n'
            '<p style="margin-top: 50px;">This is the e-mail campaign program made by Paulo. This is the e-mail campaign program made by Paulo. This is the e-mail campaign program made by Paulo. This is the e-mail campaign program made by Paulo. This is the e-mail campaign program made by Paulo.</p>\n'
            '<p style="margin-top: 50px;">Kind regards ' + '</p>\n'
            '<img src="https://yoursystem.be/img/back.jpg"></img>\n'
            '</body>\n'
            '</html>\n'
                )
         
            msg.attach(MIMEText(body, 'html'))
            
        
       
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls() 
            server.login(fromaddr, 'filebot100#')
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
            print('\nEmail enviado com sucesso!')
        #except:
        #    print("\nErro ao enviar email")
pass 