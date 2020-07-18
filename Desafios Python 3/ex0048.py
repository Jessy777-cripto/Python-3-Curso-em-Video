s = 0
c = 0
for n in range(1,501,2):
    if n%2 != 0 and n%3 == 0:
      print(n, end=' ..')
      c += 1
      s += n
print(' ', end=' ')
print('A quantidade de valores solicitados é igual a {}'.format(c))
print('O somatório de todos os ímpares e múltiplos de 3 é igual a: {}'.format(s))