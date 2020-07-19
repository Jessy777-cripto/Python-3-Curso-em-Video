maior = 0
menor = 0
for a in range(1,6):
   peso = float(input('Digite o peso da {}° pessoa: '.format(a)))
   if a == 1:  
       maior = peso
       menor = peso
   else:
        if peso > maior:
           maior = peso
        if peso < menor:
            menor = peso
print('maior = {}'.format(maior))
print('menor = {}'.format(menor))

# pesos = [ ]
# for p in range(0,5):
#     peso = float(input('Digite o peso: '))
#     pesos.append(peso)
# print('O maior peso é {}Kg' .format(max(pesos)))
# print('O menor peso é {}Kg' .format(min(pesos)))
