#Sequência de Fibonacci
from time import sleep
n = int(input('Digite um número inteiro: '))
x = 10
while x != 0:
    print(n, end=' -> ')
    n = n + 1
    x = x - 1
    sleep(1)
    # ultimo n + resultado do último = resul
    # ultimo n = n
    # 
    # 