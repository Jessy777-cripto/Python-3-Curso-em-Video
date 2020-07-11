from math import ceil
from time import sleep
cores = { 'free' : '\033[m',
          'yellow':'\033[33m',
          'blue': '\033[34m',
          'green':'\033[32m',
          'red': '\033[31m'}

print('==='*32)
print('{}Bem vindo ao programa!\nIremos calcular o seu IMC e dizer em qual categoria de massa corporal você está nesse momento.{}'.format(cores['blue'],cores['free']))
print('==='*32)
peso = float(input('{}Por favor, digite seu peso atual: {}'.format(cores['yellow'],cores['free'])))
altura = float(input('{}Por favor, digite sua altura, em metros: {}'.format(cores['yellow'],cores['free'])))
print('=='*5)
print('{}ANALISANDO...{}'.format(cores['red'], cores['free']))
print('=='*5)
sleep(3)
IMC = peso/(altura**2)
print('{}Seu IMC atual é de {}{}.'.format(cores['green'], ceil(IMC), cores['free']))
if IMC < 18.5:
    print('{}CATEGORIA: ABAIXO DO PESO{}'.format(cores['green'], cores['free']))
elif IMC > 18.5 and IMC <= 25:
    print('{}CATEGORIA: PESO IDEAL{}'.format(cores['green'], cores['free']))
elif IMC > 25 and IMC <= 30:
    print('{}CATEGORIA: SOBREPESO{}'.format(cores['green'], cores['free']))
elif IMC > 30 and IMC <= 40:
    print('{}CATEGORIA: OBESIDADE MÓRBIDA{}'.format(cores['green'], cores['free']))
else:
     print('{}CATEGORIA: OBESIDADE MÓRBIDA{}'.format(cores['green'], cores['free']))