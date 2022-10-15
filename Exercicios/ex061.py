#from math import factorial
#n1 = int(input('Digite um numero para calcular o Fatorial: '))
#f = factorial(n1)
#print('O fatorial de {} e {}'.format(n1, f))

n = int(input('Digite um numero para calcular o seu FATORIAL: '))
c = n
f = 1
print('Calculando o FATORIAL de {} = '.format(n), end='')
while c > 0:
    print('{}'.format(c) , end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

