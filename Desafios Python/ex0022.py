nome = str(input('Digite seu nome completo: ')).strip()
print('O nome completo em maiúsculo é: {}.'.format(nome.upper()))
print('O nome completo em minúsculo é: {}.'.format(nome.lower()))
print('O nome tem no total {} letras.'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras. '(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras. '.format(separa[0], len(separa[0])))