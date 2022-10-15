temp = []
princ = []
maior = menor= 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp [1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar [S|N] '))
    if resp in 'Nn':
        break
print(f'os nomes digitaods e {princ}')
print(f'Ao todo foi cadastrada {len(princ)} pessoas')
print(f'o maior peso e {maior}, e foi de ',end= '')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'o menor peso foi {menor}, e foi de ',end=' ')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}',end=' ')
print()
