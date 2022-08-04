from bdb import effective
from os import access
import smtplib    
sender_mail = 'teste@teste.com' #informar o e-mail do remetente
receivers_mail = ['teste1@teste.com'] #informar o e-mail do destinatário
#message = """\
#From: automacao%s
#To: usuarios%s
#Subject: isso e um e-mail de teste
#Teste
#"""    
message = """\
Subject: isso e um e-mail de teste
Teste
"""
try:    
   smtpObj = smtplib.SMTP('8.8.8.8', 25)  #informar ip do servidor e porta
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    #validação se o e-mail foi enviado com êxito.
except Exception:    
   print("Error: unable to send email") #validação que houve falha no e-mail
