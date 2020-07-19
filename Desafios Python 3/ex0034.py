sl = float(input('Digite o valor do seu salário: '))
if sl > 1250:
    print('Seu novo salário será de R${:.2f}'.format(sl*1.1))
if sl <= 1250:
     print('Seu novo salário é de R${:.2f}'.format(sl*1.15))