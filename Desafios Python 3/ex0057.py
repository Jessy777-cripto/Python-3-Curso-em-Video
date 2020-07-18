a = 'S'
while a == 'S':
    sex = str(input('Insira qual o seu gênero [F/M/NB]: ')).upper().strip()
    # F é feminíno, M é masculino, NB é não binário
    if sex != 'F' and sex != 'M' and sex != 'NB':
        a = str(input('Dígito errado, deseja continuar do início? [S/N] ')).upper()
print('Fim')
    # if sexo != 'F' or sexo != 'M'
    #     tent = str(input('Valor incorreto, tentar novamente? [S/N]')).upper()
    #     if tent == 'S':
    #         sexo = 'F'