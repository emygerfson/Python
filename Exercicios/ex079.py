valor = []
maior = 0
menor = 0
for cont in range(0, 5):
    valor.append(int(input('Digite um numero:')))
    if cont == 0:
        maior = menor = valor[cont]
    else:
        if valor[cont] > maior:
            maior = valor[cont]
        if valor[cont] < menor:
            menor = valor[cont]
print(f'os valores digitados foi {valor}')
print(f'O maior numero digitado foi {maior} na posição', end=' ')
for c, v in enumerate(valor):
    if v == maior:
        print(f'{c}...', end=' ')
print()
print(f'\no menor valor digita foi {menor} na posição' , end=' ')
for c , v in enumerate(valor):
    if v == menor:
        print(f'{c}...', end=' ')
print()

