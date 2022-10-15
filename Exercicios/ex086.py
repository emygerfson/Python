n = [[] , []]
for c in range(1,8):
    valor = int(input(f'Digite {c}º numero: '))
    if valor % 2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
n[0].sort()
n[1].sort()
print(f'Os valores PARES são {n[0]}')
print(f'Os valores IMPARES são{n[1]}')
