no = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão dessa PA:'))
print('Os 10 primeiros termos dessa PA são:')
q = no
for x in range(1, 11): 
    print('{}'.format(q), end= '.. ')   
    q += razao 
print('ACABOU..', end=' ')