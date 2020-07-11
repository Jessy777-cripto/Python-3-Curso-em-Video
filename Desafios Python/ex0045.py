from random import choice
from time import sleep
cl = {'free':'\033[m',
        'bluebol': '\033[1;33m',
            'red':'\033[31m',
                 'purple':'\033[35m',
                      'green':'\033[32m'}
print("="*50)
print('{}          JOGO PEDRA PAPEL TESOURA{}'.format(cl["purple"],cl["free"]))
print('='*50)
print("""DIGITE 0 PARA PEDRA
DIGITE 2 PARA TESOURA
DIGITE 5 PARA PAPEL""")
print('__'*25)
n = int(input('DIGITE O SEU NÚMERO ESCOLHIDO PARA JOGAR: '))
p = [1,2,5]
escolhido = choice(p)

if n == 2:
    print('SUA JOGADA É TESOURA.')
elif n == 0:
    print('SUA JOGADA É PEDRA.')
elif n ==5:
    print('SUA JOGADA É PAPEL.')
else:
    print('DÍGITO INVÁLIDO!')
print('-'*27)
print('JO')
sleep(1)
print('KÊN')
sleep(1)
print('PO!!')
sleep(1.2)
if escolhido == 0:
    print('JOGADA DO COMPUTADOR PEDRA.')
elif escolhido == 2:
    print('JOGADA DO COMPUTADOR É TESOURA.')
else:
    escolhido == 5
    print('JOGADA DO COMPUTADOR É PAPEL.')

if (n == escolhido) or (escolhido == n): 
    print('{}EMPATE{}'.format(cl["bluebol"],cl["free"]))
elif n == 0 and escolhido == 2:
    print('{}VOCÊ VENCEU!{}'.format(cl["green"],cl["free"]))
elif n == 2 and escolhido == 0:
    print('{}O COMPUTADOR VENCEU {}'.format(cl['red'],cl["free"]))
elif n == 0 and escolhido == 5:
    print('{}O COMPUTADOR VENCEU{}'.format(cl['red'],cl["free"]))
elif n == 5 and escolhido == 0:
    print('{}VOCÊ VENCEU!{}'.format(cl["green"],cl["free"]))
elif n == 5 and escolhido == 2:
    print('{}O COMPUTADOR VENCEU.{}'.format(cl["red"],cl["free"]))
elif n == 2 and escolhido == 5:
    print('{}VOCÊ VENCEU!.{}'.format(cl["green"],cl["free"]))
elif n == 5 and escolhido == 2:
    print('{}O COMPUTADOR VENCEU.{}'.format(cl["red"],cl["free"]))
else:
    print('JOGO INVÁLIDO.')