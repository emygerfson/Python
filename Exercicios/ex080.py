num = list()
while True:
    n = int(input('Digite um numero '))
    if n not in num:
        num.append(n)
        print('valor adiconado com sucesso')
    else:
        print('valor duplicado não vou adiconar')
    r = str(input('Desaja continuar[S|N] '))
    if r in 'Nn':
        break
num.sort()
print(f'voce digitou o volor de {num}')
