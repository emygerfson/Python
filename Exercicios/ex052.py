primeiro = int(input('digite o primeiro Termo '))
razão = int(input('Digite a RAZÂO '))
decimo = primeiro + (10 -1) * razão
for c in range(primeiro, decimo + razão, razão):
    print('{}'.format(c),end=' - ')
print('ACABOU')