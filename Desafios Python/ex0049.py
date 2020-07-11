num = int(input('Digite um número para criar sua tabualda automaticamente: '))
for n in range(1,11):
    calculo = n*num
    print('{} x {:2} = {}'.format(num, n, calculo ))
    