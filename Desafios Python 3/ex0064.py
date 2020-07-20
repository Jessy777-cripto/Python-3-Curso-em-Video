x = n = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    x = x + 1
    nant= n
    soma += nant
print('Você digitou {} números e '.format(x-1), end= '')
print('a soma de todos os números é igual a: {}'.format(soma-999))