import math
ang = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(ang))
print('O seno de {}° é {:.2f} '.format(ang, s))
c = math.cos(math.radians(ang))
print('O cosseno de {}° é {:.2f}'.format(ang, c))
t = math.tan(math.radians(ang))
print('A tangente de {}° é igual a {:.2f}'.format(ang, t))

