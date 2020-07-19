x = 0
n = 0
soma = 0
while n != 999:
    n = int(input('Digite um número inteiro: '))
    x = x + 1
    nant= n
    soma += nant
print('Você digitou {} números com exceção do 999.'.format(x-1))
print('A soma de todos os números que você digitou é igual a: {}'.format(soma-999))