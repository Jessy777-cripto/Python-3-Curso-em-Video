from time import sleep
print('Digite os valores para saber qual valor é o maior e qual é o menor.')

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))
print('PROCESSANDO...')
sleep(3)
maior = a
if c > a  and c > b:
    maior = c
if b > a and b > c:
    maior = b
# verificando quem é o maior
menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c

print('O maior valor é {}. '.format(maior))
print('O menor valor é {}. '.format(menor))