#conversor de medidas
print('--------------------------------------------------------')
print('Bem vindo ao nosso conversor de medidas! \ninsira um valor abaixo em metros para saber suas outras medidas. ')
print('--------------------------------------------------------')
v = int(input('Digite um valor em metros: '))
print('\n--------------------------------------------------------')
print('{} km'.format(v/1000))
print('{} hm'.format(v/100))
print('{} dam'.format(v/10))
print('{} dm'.format(v*10))
print('{} cm'.format(v*100))
print('{} mm'.format(v*1000))
print(' --------------------------------------------------------')
print('|       Obrigado(a) por utilizar nosso programa!         |')
print(' --------------------------------------------------------')

