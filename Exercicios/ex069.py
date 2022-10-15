from random import randint
v = 0
while True:
    jogador = int(input('Digite um nº'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Vai ser PAR ou IMPAR [P|I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador} e o total e {total}')
    print('Deu PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('E PAR e voce Venceu')
            v += 1
        else:
            print('Voce Perdeu ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('E IMPAR voce venceu')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos JOGAR NOVAMENTE')
print(f'GAME OVER , Você consegui venceu apenas {v}')


