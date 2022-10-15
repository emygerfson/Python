n = (int(input('Digite 1º numero ')),
     int(input('Digite 2º numero ')),
     int(input('Digite 3º numero ')),
     int(input('Digite 4º numero ')))
print(f'os numero são {n}')
print(f'o numero 9 aparece {n.count(9)} vez')
if 3 in n:
     print(f'o numero 3 esta na {n.index(3) + 1} posicão')
else:
     print(f'o numero 3 não apareceu na tupla')
print('o numeros pares sao',end=' ')
for num in n:
     if num % 2 == 0:
          print(num, end=' ')



