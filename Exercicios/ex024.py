'''num = int(input('digite um numero:  '))
n = str(num)
print('Analisando o numero {}'.format(num))
print('A Unidade e {}'.format(n[3]))
print('A Dezena e {}'.format(n[2]))
print('A Centena e {}'.format(n[1]))
print('o milhar e {}'.format(n[0]))'''

num = int(input('digite um numero:  '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('A Unidade e {}'.format(u))
print('A Dezena e {}'.format(d))
print('A Centena e {}'.format(c))
print('o milhar e {}'.format(m))