a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno:'))
c = str(input('Terceiro Aluno: '))
d = str(input('Quarto aluno: '))
from random import shuffle
lista = [a,b,c,d]
shuffle(lista)
print('A ordem de apresentação será. ')
print(lista)