num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um numero ')))
    resp = str(input('Quer continuar [S|N] '))
    if resp in 'Nn':
        break
print(num)
for i , v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Estes valores são PAR {pares}')
print(f'Estes valores são IMPARES {impares} ')


