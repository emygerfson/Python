casa = float(input('Qual o valor da casa que você quer comprar?R$  '))
salario = float(input('Qual e o valor do seu salario ? R$ '))
anos = int(input('Enquanto anos você quer pagar '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Com esse valor {} a prestação vai ser de {:.2f}'.format(casa, prestação))
if prestação < minimo:
    print('Emprestigo CONSEDIDO')
else:
    print('Emprestimo NEGADO')
