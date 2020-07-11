n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1+n2)/2
print('A sua média foi {:.2f}.'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! Estude mais!')

#condição simplificada
print('Parabéns! 'if m>= 6 else 'ESTUDE MAIS!')
