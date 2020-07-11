num = int(input('Digite um número: '))
tot = 0
for a in range(1, num + 1):
    if num % a == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(a), end='')
print('\n\033[mO número {} foi dividido {} vezes.'.format(num, tot))
if tot == 2:
    print('Esse número é primo.')
else:
    print('Esse número não é primo.')