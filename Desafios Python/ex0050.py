s = 0
c = 0
for c in range (0,6,1):
    n = int(input('{})Digite um número: '.format(c+1)))
    if n%2 == 0:
        c += 1
        s += n
print('O somatório de todos os {} números pares é igual: {}'.format(c ,s))