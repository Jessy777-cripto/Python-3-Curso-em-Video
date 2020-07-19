resp = ''
som = 0
q = 0
numeros = []
while resp != 'N':
    n = int(input('Digite um número inteiro: '))
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip() 
    som += n
    q += 1
    numeros.append(n)
    if resp != 'N' and resp != 'S':
        resp = str(input('Dígito inválido, deseja recomeçar? [S/N] ')).upper().strip()
print('Acabou')
print(som/q)
print(max(numeros))
print(min(numeros))
