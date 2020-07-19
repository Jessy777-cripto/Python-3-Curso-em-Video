sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Informa seu sexo: [M/F] ')).upper().strip()
    if sexo != 'F' and sexo != 'M':
        sexo = str(input('Dados inválidos, informe seu sexo: [M/F] ')).upper().strip()
print('Seu sexo foi confirmado como {}.'.format(sexo))
