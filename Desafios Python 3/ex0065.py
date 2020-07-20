resp = ''
som = q = 0
numeros = []
while resp != 'N':
    n = int(input('Digite um número inteiro: '))
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    som += n
    q += 1
    numeros.append(n)
    if resp != 'N' and resp != 'S':
        resp = str(input('Dígito inválido, deseja recomeçar? [S/N] ')).upper().strip()
print('A média de todos os valores é {:.2f}'.format(som/q))
print('O maior valor foi {}.'.format(max(numeros)))
print('O menor valor foi {}.'.format(min(numeros)))
