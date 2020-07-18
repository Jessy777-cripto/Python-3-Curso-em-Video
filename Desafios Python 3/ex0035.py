print('-'*35)
print( '    ANALISADOR DE TRIÂNGULOS' )
print('-'*35)
a = float(input('Digite um valor para o primeiro lado do triângulo: '))
b = float(input('Digite um valor para o segundo lado do triângulo: '))
c = float(input('Digite um valor para o terceiro lado do triângulo: '))

if a < c + b and  c < a + b and b < a + c:
    print('É possível obter um triângulo com esses valores!')
else:
    print(('Não é possível obter um triângulo com esses valores!'))