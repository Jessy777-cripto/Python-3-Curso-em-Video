from datetime import date
nascimento = int(input('Digite a sua data de nascimento: : '))
atual = date.today().year
idade = atual - nascimento
print('Você nasceu no ano de {} e possui atualmente {} anos.'.format(nascimento,idade))
if idade == 18:
    print('Está na hora de você se alistar! Compareça ao quartel mais próximo.')
elif idade < 18:
    y = (18 - idade)
    print('Ainda falta {} para você se alistar.'.format(y))
elif idade > 18:
    x = atual - (idade - 18)
    print('Seu alistamento foi no ano de {}. Compareça ao quartel mais próximo IMEDIATAMENTE!.'.format(x))
