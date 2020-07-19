no = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão dessa PA:'))
print('Os 10 primeiros termos dessa PA são:')
q = no
x = 10
while x != 0:
    print('{}'.format(q), end= '.. ')   
    q += razao 
    x = x - 1
print('ACABOU..', end=' ')