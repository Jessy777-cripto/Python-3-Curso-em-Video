a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))

if a > b:
    print('O valor {} é maior do que {}.'.format(a,b))
    print('O valor {} é menor do que {}.'.format(b,a))
elif b > a:
    print('O valor {} é maior do que {}.'.format(b,a))
    print('O valor {} é menor do que {}.'.format(a,b))
elif b == a:
    print('Os valores {} e {} são iguais.'.format(a,b))
