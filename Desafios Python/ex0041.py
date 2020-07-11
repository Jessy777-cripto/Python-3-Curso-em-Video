from datetime import date
print('-=-'*25)
print('BEM VINDO AO PROGRAMA DA CONFEDERAÇÃO NACIONAL DE NATAÇÃO,\nDE ACORDO COM SUA IDADE IREMOS CALCULAR QUAL A MELHOR CATEGORIA DE COMPETIÇÃO PARA VOCÊ!')
print('-=-'*25)
nascimento = int(input('DIGITE A SUA DATA DE NASCIMENTO: '))
atual = date.today().year
idade = atual - nascimento
print('=='*10)
if idade <=9:
    print('CATEGORIA: MIRIM.')
elif idade > 9 and idade <=14:
    print('CATEGORIA: INFANTIL.')
elif idade > 14 and idade <=19:
    print('CATEGORIA: JUNIOR.')
elif idade > 19 and idade <= 20:
    print('CATEGORIA: SÊNIOR.')
elif idade > 20:
    print('CATEGORIA: MASTER.')
print('=='*10)