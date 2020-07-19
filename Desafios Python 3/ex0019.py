import random
a = str(input('Digite um nome: '))
b = str(input('Digite um segundo nome: '))
c = str(input('Digite um terceiro nome: '))
d = str(input('Digite um quarto nome: '))
e = [a , b, c, d]
print('O nome escolhido foi {}.'.format(random.choice(e)))