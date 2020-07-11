tempo = int(input('Quantos anos tem seu carro? '))

#condicionante
if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro velho')
print('--FIM--')

#condição simplificada
print('carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')