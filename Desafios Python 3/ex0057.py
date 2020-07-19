sexo = str(input('Informa seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    if sexo not in 'MmFf':
        print('Dados incorretos.', end=' ')
        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
if sexo == 'F':
     print('Seu sexo foi registrado como FEMININO.')
else:
    print('Seu sexo foi registrado como MASCULINO.')

