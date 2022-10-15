salario = float (input('Qual e o valor do seu salario? R$'))
if salario > 1200:
    salario = (1200 * 10 / 100) + salario
else:
    salario = (1200  * 15 / 100) + salario
print('Seu novo salario vai ser R$ {}'.format(salario))
