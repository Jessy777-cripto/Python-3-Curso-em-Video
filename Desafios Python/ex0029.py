v = float(input('Digite a velocidade do seu carro em km/hora: '))
print('Está tudo bem!, tenha um bom dia!' if v <= 88 else 'Você receberá uma multa de R${} por ter ultrapassado o limite de 88km/h.'.format((v-88)*7))
