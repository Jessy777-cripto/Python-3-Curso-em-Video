from time import sleep
from playsound import playsound
print('CONTAGEM REGRESSIVA DO LANÇAMENTO DE FOGOS DE ARTIFÍCIO')
for c in range(10, 0, -1 ):
    print(c)
    sleep(1)
print('LANÇAMENTO INICIADO.')
playsound('fogos.mp3')