from random import randint
from time import sleep
tentativas = 1
print('-=-'*20)
print('Tente adivinhar o número que eu pensei entre 1 a 10. ')
print('-=-'*20)
a = 'S'
while a == 'S':
    escolhido = randint(1,10)
    num = int(input('Que número eu pensei? '))
    if num == escolhido:
        print('Parabéns! Você venceu!')
        break
    else:
        print('Não')
        tentativas += 1
print('Você fez {} tentativas até acertar.'.format(tentativas))
