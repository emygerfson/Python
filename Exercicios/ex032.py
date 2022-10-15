'''viagem = float(input('Qual vai ser a distancia de sua viage? '))
print('Voce vai começar um viagem de {}km'.format(viagem))
if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print('o preso de sua viagem vai ser de {}R$'.format(preço))'''

viagem = float(input('Qual vai ser a distancia de sua viage? '))
print('Voce vai começar um viagem de {}km'.format(viagem))
preço = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('o preso de sua viagem vai ser de {}R$'.format(preço))

