print('\033[1;31;43mOlá, mundo!\033[m')
print('\033[1;7;30mOlá, mundo \033[m')
print('\033[mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m.'.format(a,b))

nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}.'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa' :'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco': '\033[7;30m'}

print('Olá, Muito prazer em te conhecer, {}{}{}.'.format(cores['azul'],nome, cores['limpa']))