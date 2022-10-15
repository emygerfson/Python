from random import randint
computador = randint(0, 10)
print('Eu sou o computador estou pesnado em um nº de 0 a 10')
print('Você consegue adivinhar')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Jogador qual seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...tente outra vez')
        if jogador > computador:
            print('Menos....tente outra vez')
print('Voçê acertou com {} tentativas'.format(palpite))




