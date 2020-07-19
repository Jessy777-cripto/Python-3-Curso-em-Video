import math
ca = float(input('Qual é o valor do cateto adjacente? '))
co = float(input('Qual o valor do cateto oposto? '))
#h = sqrt((ca**2)+(co**2))
# o hypot é uma forma de calcular a hipotenusa, so colocar os valores do co e ca.
hi = math.hypot(co,ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))