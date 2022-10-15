compras = float ( input('Qual foi o valor de suas COmpra R$ '))
print('''Qual vai ser sua Opção.
[1] A Vista
[2] Avista no cartão
[3] em ate 2x no cartão
[4] em 3x no cartão ''')
opção = int(input('Qual OPÇÂO '))
if opção == 1:
    desconto = compras - (compras * 10 / 100)
    print('Suas compras vai ficar {} com desconto'.format(desconto))
elif opção == 2:
    desconto2 = compras - (compras * 5 / 100)
    print('Suas compras via ficar {} reas com desconto'.format(desconto2))
elif opção == 3:
    cartão = compras / 2
    print('Suas compras de {} reais vai ficar 2x de {} reais'.format(compras, cartão))
elif opção == 4:
    cartão2 = (compras + (compras * 20 / 100))
    parcelas = int(input('Em quantas parcelas'))
    total = cartão2 / parcelas
    print('Suas compras de {} vai ficar em 3x de {:.2f} com 20% de juros'.format(compras, total))




