num = int(input('DIGITE UM NUMERO ' ))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m', end='')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\nO numero {} foi dividido {} vezes'.format(num, tot))
if tot == 2:
    print('ELE E PRIMO')
else:
    print('ELE NÂO E PRIMO')