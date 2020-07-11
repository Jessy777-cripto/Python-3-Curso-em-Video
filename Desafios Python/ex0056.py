p = int(input('Quantas pessoas deseja analisar? '))
x = 0
for a in range(1, p+1):
    print('---- {}° PESSOA ----'.format(a))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    x += idade
    y = 0
    if sexo == 'M' and idade > y :
        y = idade
        homenmaisvelho = nome
media = x/p
print(nome)
print(media)
print(x)