#Média aritmética
print('Bem vindo ao programa pertencente ao Colégio São Marinho, aqui iremos calcular a nota do aluno e dar a sua média aritmética.')
print('----------------------------------------------------------------------------------------------------------------------------------------')
nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
print('-----------------------------------------------------------------------------------------------------------------------------------------')
print('A média aritmética do aluno(a) {} é igual a: {:.2f}. '.format(nome, ((n1+n2+n3+n4)/4)))