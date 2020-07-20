x = int(input('Quantos termos deseja que mostre na tela? '))
no = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão dessa PA: '))
p = False
nt = 0
while not p:
    while x != 0:
        print('{}'.format(no), end= '.. ')   
        no += razao
        x = x - 1 
        nt += 1
    resposta = int(input('\nQuantos termos você quer mostrar mais? '))
    if resposta != 0:
        x = resposta
    else:
        p = True
print('ACABOU..', end=' ')
print('Progressão finalizada com {} termos. '.format(nt))