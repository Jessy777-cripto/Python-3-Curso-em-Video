#conversor de moedas
print(' -'* 39)
print('Bem vindo ao conversor de moedas,\nno momento nos trabalhamos unicamente na conversão entre REAL(BR) e DOLAR(EUA).')
print(' -'* 39)
r = float(input('Insira o valor atual que deseja converter em REAIS para DOLARES: R$'))
print('Seu dinheiro em dolares ficará: US${:.2f}'.format(r/5.32))