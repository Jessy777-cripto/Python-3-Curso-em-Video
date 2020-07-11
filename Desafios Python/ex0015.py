d = int(input('Digite a quantidade de dias que o carro foi alugado: '))
q = float(input('Digite a quantos quilômetros foi percorrido: '))
print('O total a pagar é de R${:.2f} '.format((d*60)+(0.15*q)))