a = float(input('DIGITE O PRIMEIRO LADO DO TRIÂNGULO: '))
b = float(input('DIGITE O SEGUNDO LADO DO TRIÂNGULO: '))
c = float(input('DIGITE O TERCEIRO LADO DO TRIÂNGULO: '))
if a < b+c and b < a+c and c < a+c:
    print('Pode-se formar um triângulo com essas medidas!!')
    if a == b and b == c and a == c:
        print('ESSE TRIÂNGULO É EQUILÁTERO.')
    elif a == b or b == c or c == a:
        print('ESSE TRIÂNGULO É ISÓSCELES.')
    else:
        # > b and b > c and c > a or a < b and  b < c and c < a
        a != b != c != a
        print('ESSE TRIÂNGULO É ESCALENO.')
else:
    print('Não se pode formar um triângulo com essas medidas!')