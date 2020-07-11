print('-=-'*50)
print('BEM VINDO AO COLÉGIO SANTOS DRUMMOND,\nAQUI IREMOS CALCULAR A MÉDIA DO SEU/SUA FILHO(A) E DIZER SE ELE FOI APROVADO OU NÃO NO FINAL DO SEMESTRE.')
print('-=-'*50)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('=='*30)
if m >= 7:
    print('                SITUAÇÃO: APROVADO.')
    print('                MÉDIA ARITMÉTICA: {}'.format(m))
elif m >= 5 and m <7:
    print('                SITUAÇÃO: RECUPERAÇÃO.')
    print('                MÉDIA ARITMÉTICA: {}'.format(m))
elif m < 5:
    print('                SITUAÇÃO: REPROVADO.')
    print('                MÉDIA ARITMÉTICA: {}'.format(m))
print('=='*30)