velocidade = float(input('Qual e a velocidade do seu carro ?  '))
if velocidade > 80:
    print('Voce foi multado')
    multa = (velocidade - 80) * 7
    print('Sua multa ficou em {}'.format(multa))
print('Tenha um bom dia ! Dirija com cuidado')