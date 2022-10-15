pesomaior = 0
pesomenor = 0
for pess in range(1, 6):
    peso = float(input('Qual e {}º peso? '.format(pess)))
    if pess == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print('O maior peso lido foi {}kg'.format(pesomaior))
print('o menor peso lido foi {}kg'.format(pesomenor))


