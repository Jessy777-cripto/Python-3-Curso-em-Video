n = int(input('Digite um número para calcularmos o seu fatorial: '))
p = 1
print('Calculando {}! = '.format(n), end= '')
while n > 0:
    print(n, end= '')
    print(' x ' if n > 1 else ' = ', end='')
    p = p*n
    n = (n - 1)
print('{}'.format(p), end= '')