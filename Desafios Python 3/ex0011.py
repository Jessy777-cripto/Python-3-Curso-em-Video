#Pintando a parede
print('-'*91)
print('Bem vindo! Aqui iremos calcular quantos litros você precisa de tinta para pintar sua parede.')
print('-'*91)
h = float(input('Digite a altura da sua parede(em metros): '))
c = float(input('Digite o comprimento da sua pare3de(em metros): '))
print('Como sua parede tem a altura {} e o comprimento {}, a área dessa parede portanto é {}m².'.format(h,c,h*c))
print('Dessa forma, a quantidade de tinta, em litros, necessária para pintar uma parede de {}m² é de {} litros.'.format(h*c,(h*c)/2))
print('-'*91)