print('-=-' * 20)
print('Analisador de Triangulos')
print('-=-' * 20)
r1 = float(input('digite o valor da primeira reta '))
r2 = float(input('digite o valor da segunda reta '))
r3 = float(input('digite o valor da terceira reta '))
if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r2 + r1:
    print('Os segmentos acima podem formar triangulo! ' ,end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSELES')
else:
    print('Os segmentos acima não podem formar triangulo')
