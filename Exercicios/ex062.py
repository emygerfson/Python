#primeiro = int(input('digite o primeiro Termo '))
#razão = int(input('Digite a RAZÂO '))
#decimo = primeiro + (10 -1) * razão
#for c in range(primeiro, decimo + razão, razão):
 #   print('{}'.format(c),end=' - ')
#print('ACABOU')
print('GERADOR DE PA:')
print('-=-' * 10)
primeiro = int(input('Digite o 1º termo '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += razão
    cont += 1
print('<< FIM >>)