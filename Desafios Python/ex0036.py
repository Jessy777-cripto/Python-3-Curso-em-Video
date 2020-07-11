from time import sleep
cores = {'limpa':'\033[m',
         'amarelo' : '\033[33m',
         'azul c': '\033[36m',
         'vermelho':'\033[31m',
         'verde': '\033[32m'}

print('='*110)
print('                                    BEM VINDO AO PROGRAMA DO BANCO MAXIMUS!')
print('='*110)
print('{}AQUI IREMOS ANALISAR SE VOCÊ TERÁ DIREITO A UM EMPRÉSTIMO BANCÁRIO PARA A AQUISIÇÃO DE UMA RESIDÊNCIA.\nPOR FAVOR, INSIRA SEUS DADOS COM CLAREZA QUE SERÁ ANALISADO CUIDADOSAMENTE POR NOSSA EQUIPE E O RESULTADO SERÁ IMEDIATAMENTE APÓS A ANÁLISE.{}'.format(cores['amarelo'],cores['limpa']))
print('O EMPRÉSTIMO COM A FINALIDADE DE ADQUIRIR UMA MORADIA SÓ SERÁ PERMITIDO\nSE A RESIDÊNCIA POSSUIR UM VALOR MAIOR QUE R$10.000 E SE FOR PAGA ATÉ 15 ANOS DE PRESTAÇÕES.')
casa = float(input('{}DIGITE O VALOR DA RESIDÊNCIA QUE DESEJA TER POSSE: R$ {}'.format(cores['azul c'],cores['limpa'])))
sal = float(input('{}DIGITE O VALOR DO SEU SALÁRIO LÍQUIDO OU, NO CASO DE AUTÔNOMOS, A MÉDIA SALÁRIAL DOS ÚLTIMOS TRÊS MESES: R$ {}'.format(cores['azul c'],cores['limpa'])))
ano = int(input('{}DIGITE EM QUANTOS ANOS DESEJA PAGAR PELO EMPRESTIMO: {}'.format(cores['azul c'],cores['limpa'])))
print('='*110)
parcelas = ano*12
prestação = casa / parcelas
print('PROCESSANDO...')
if prestação <= (sal*0.3) and casa > 10000:
    print('{}PARABÉNS, SEU EMPRÉSTIMO FOI APROVADO!{}'.format(cores['verde'], cores['limpa']))
    print('='*110)
elif prestação > (sal*0.3) and casa < 10000:
    print('='*110)
    print('{}SINTO MUITO, SEU EMPRÉSTIMO FOI NEGADO! VOCÊ PODE SOCILITAR OUTRA ANÁLISE DAQUI A TRÊS MESES!{} '.format(cores['vermelho'],cores['limpa']))
    print('='*110)
    input()