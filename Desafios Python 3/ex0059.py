a = 'S'
while a == 'S':
    v1 = int(input('Digite um valor: '))
    v2 = int(input('Digite outro valor: '))
    print('==='*30)
    print("""        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NÚMEROS
        [ 5 ] SAIR DO PROGRAMA""")
    decision = int(input(' Oque deseja fazer? '))
    if decision == 1: 
        print('A soma dos valores {} e {} é igual a {}. '.format(v1, v2, v1+v2))
    elif decision == 2:
        print('A multiplicação entre os valores {} e {} é igual a {}'.format(v1, v2, v1*v2))
    elif decision == 3:
        if v1 > v2:
            print('O valor {} é maior que {}.'.format(v1,v2))
        else:
            print('O valor {} é maior que {}.'.format(v2,v1))
    elif decision == 4:
        a = str(input('Tem certeza que deseja modificar os números? [S/N] ')).upper()
    elif decision == 5:
        break
    break
print('Obrigado por usar nosso programa!')
    