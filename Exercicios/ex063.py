print('GERADOR DE PA:')
print('-=-' * 10)
primeiro = int(input('Digite o 1º termo '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = primeiro
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razão
        cont += 1
    print('<< PAUSA >>')
    mais = int(input('Quantos termos a mais você quer? '))
print('Ao total foram mostradas {} termos'.format(total))
print('<< FIM >>')
