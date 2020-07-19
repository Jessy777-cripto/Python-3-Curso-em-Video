from random import randint
p = 0
acertou = False
print('-=-'*20)
print('Tente adivinhar o número que eu pensei entre 1 a 10. ')
print('-=-'*20)
escolhido = randint(1,10)
while not acertou:
    num = int(input('Que número eu pensei? '))
    p = p + 1
    if num == escolhido:
        acertou = True
        print('Você acertou!', end=' ')
        print('Você precisou jogar {} vezes até acertar.'.format(p))
    elif num < escolhido:
        print('Mais... Tente outra vez.')
    elif num > escolhido: 
        print('Menos... Tente mais uma vez.')
#        print('Não.', end=' ')


