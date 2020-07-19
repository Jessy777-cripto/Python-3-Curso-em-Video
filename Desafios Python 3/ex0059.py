from time import sleep
maior = 0
a = False
while not a:
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite um segundo número inteiro: '))
    print("""    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA """)
    escolha = int(input('>>>> O que deseja fazer? '))
    if escolha == 1:
        print('{} + {} = {}.'.format(n1, n2, (n1+n2)))
        a = True
    elif escolha == 2:
        print('{} x {} = {}'.format(n1,n2,(n1*n2)))
        a = True
    elif escolha == 3:
        if n1 > n2:
            print('Maior número: {}'.format(n1))
        else:
            print('Maior número: {}'.format(n2))
        a = True
    elif escolha == 4:
        print('Aguarde...')
        sleep(2.5)
        print('Informe os números novamente.', end= ' ')
        False
    else:
        print('Finalizando...')
        sleep(2.5)
        a = True
print('Obrigada por utilizar nosso programa!')