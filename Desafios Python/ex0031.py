import time
a = float(input('Digite quantos quilometros você irá percorrer nesta viagem: '))
print('PROCESSANDO...')
time.sleep(2.5)
print('Você irá percorrer {}km. '.format(a))
print('O valor ficará R${}.'.format(a*0.5) if a <= 200 else 'O valor da viagem ficará R${}.'.format(a*0.45))