a = int(input('digite o primeiro nº '))
b = int(input('digite o seguendo nº '))
c = int(input('digite o terceiro nº '))
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if a <= b or a <= c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o menor nº digitado e {}'.format(menor))
print('o maior nº digitado e {}'.format(maior))
