total = cont = menor = cont2 = 0
barato = ' '
while True:
    produto = str(input('Qual e o nome do produto '))
    preço = float(input('Qual e o preço R$'))
    cont2 += 1
    total += preço
    if preço > 1000:
        cont += 1
    if cont2 == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S|N] ')).strip().upper()[0]
    if resp == 'N':
            break
print(f'A soma dos produtos foi {total}')
print(f'E temos {cont} maior de 1000 reais')
print(f'E o pruduto de menor preceso e {barato} que custa R${menor} ')
