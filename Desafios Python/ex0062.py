x = int(input('Quantos termos deseja que mostre na tela? '))
no = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão dessa PA: '))
q = no
while x != 0:
    print('{}'.format(q), end= '.. ')   
    q += razao
    x = x - 1 
print('ACABOU..', end=' ')