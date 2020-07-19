from datetime import date
ano = int(input('Digite o ano atual para saber se ele é bissexto ou não: '))
if ano == 0:
    ano = date.today().year
print('O ano de {} é um ano bissexto! '.format(ano) if (ano % 4 == 0) and ano % 100 !=0 or ano % 400 ==0 else 'O ano de {} não é um ano bissexto! '.format(ano))