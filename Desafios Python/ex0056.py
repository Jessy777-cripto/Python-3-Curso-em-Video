somaidade = 0
homemmaisvelho = 0
media = 0
nomedovelho = ''
totmulher = 0
for a in range(1, 5):
    print('---- {}° PESSOA ----'.format(a))
    nome = str(input('Nome: '))
    idade = float(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if a == 1 and sexo in 'Mm':
        homemmaisvelho = idade
        nomedovelho = nome
    if sexo in 'Mm' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomedovelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher +=1
media = somaidade / 4
print('O nome do homem mais velho do grupo é {}.'.format(nome))
print('A média de idade dos participantes do grupo é de {:.2f}'.format(media))
print('O número de mulheres que possuem menos de 20 anos é de {}.'.format(totmulher))