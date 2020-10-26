#!/usr/bin/python
#encoding: ISO-8859-1
from datetime import datetime
import aiml
k = aiml.Kernel()
k.setTextEncoding("Latin1")
k.learn("AIML.aiml")
user_input = "begin"
print ("Nueva charla, Fecha: "+repr(datetime.now().day)+"/"+repr(datetime.now().month)+"/"+repr(datetime.now().year))
print ("Inicio de la charla: "+repr(datetime.now().hour)+":"+repr(datetime.now().minute)+":"+repr(datetime.now().second))
while (user_input != "quit") and (user_input != "QUIT"):
    user_input = input("Usuario: ")
    answer = k.respond(user_input)
    print ("Esteban: "+ repr(answer)[2:-1])
print ("Fin de la charla: "+repr(datetime.now().hour)+":"+repr(datetime.now().minute)+":"+repr(datetime.now().second))