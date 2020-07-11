from time import sleep
print('=========LOJAS AMERICANOS=========')
preço = float(input('Digite o valor do seu produto: R$'))
print("""      [ 1 ] PAGAMENTO EM DINHEIRO OU CHEQUE
      [ 2 ] PAGAMENTO NO CARTÃO DE CRÉDITO""")
pag = int(input('Digite a forma de pagamento: '))
print('PROCESSANDO...')
sleep(3)
if pag == 1:
    print('VALOR TOTAL: {:.2f}'.format(preço*0.9))
elif pag == 2:
    print("""          [ 1 ] PAGAMENTO EM 1X NO CARTÃO
          [ 2 ] PAGAMENTO EM 2X NO CARTÃO
          [ 3 ] PAGAMENTO EM 3X NO CARTÃO
          [ 4 ] PAGAMENTO EM MAIS DE 3X NO CARTÃO""")
    card = int(input('Digite opção escolhida: '))
else: 
    print('OPÇÃO INVÁLIDA')

print('PROCESSANDO...')
sleep(3)
if card == 1:
    print('VALOR DA COMPRA(s/desconto): {}'.format(preço))
    print('VALOR DA COMPRA 1X R${:.2f}'.format(preço*0.95))
elif card == 2:
    print('VALOR DA COMPRA(s/desconto): {}'.format(preço))
    print('VALOR DA COMPRA 2X R${:.2f}'.format(preço/2))
elif card == 3:
    print('VALOR DA COMPRA(c/juros): {}'.format(preço*1.2))
    print('O VALOR DA COMPRA: 3XR${:.2f}'.format((preço*1.2)/3))  
elif card == 4:  
    nparc = int(input('Digite a quantidade de parcelas que deseja divivir a compra: '))
    print('PROCESSANDO...')
    sleep(3)
    print('VALOR DA COMPRA(c/juros): R${}'.format(preço*1.2))
    print('VALOR DA COMPRA {}X R${}'.format(nparc,(preço*1.2)/nparc))
else:
    print('OPÇÃO INVÁLIDA')