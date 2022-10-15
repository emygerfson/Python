p = float(input('Digite seu peso '))
a = float(input('Digite sua altura e CM  '))
'''i = float(input('Digite sua idade '))
HB = 66 + (13.8 * p) + (5.0 * a) - (6.8 * i)'''
imc = p / (a ** 2)
print('E o seu IMC e de {:.2f}'.format(imc))
if imc <= 18:
    print('Cuidado você esta abaixo do peso ')
elif imc > 18 and imc <= 25:
    print('Parabens você esta no peso ideal')
elif imc > 25 and imc <= 30:
    print('Você esta com SOBREPESO')
elif imc > 30 and imc <= 40:
    print('Você esta com OBSIDADE')
elif imc >= 40:
    print('Você esta com OBSIDADE MORBIDA cidado!')
#print('Seu metaboliosmo basal e de {:.2f} calorias'.format(HB))''

