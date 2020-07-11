from random import randint
from time import sleep
print('-=-'*20)
print('Tente adivinhar o número que eu pensei entre 1 a 5. ')
print('-=-'*20)
num = int(input('Que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
escolhido = randint(1,5)
if num == escolhido:
    print('Parabéns, você venceu!')
else:
  print('Você perdeu! Eu pensei no número {} e não {}!'.format(escolhido, num))

input()

