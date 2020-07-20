#Sequência de Fibonacci
a = 0
b = 1
n = int(input('Quantos números você quer ver? '))
while n != 0:
    print(' -> {}'.format(a), end='')
    a = a + b
    b = a - b
    n -= 1
