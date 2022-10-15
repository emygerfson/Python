km = float(input('Quantos kilometro foi percorrido ? KM'))
dia = float(input('quantos dias ira usar o carro ?'))
custo = (dia * 60) + (km * 0.15)
print('O seu custo total sera {:.2f} R$'.format(custo))
