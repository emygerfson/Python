from random import randint
from time import sleep
itens = ('Pedra','papel','tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[0] Pedra
[1] Pepel
[2] Tesoura''')
jogador = int(input('Qual e sua JOGADA ? ') )
print('JO')
sleep(2)
print('KEN')
sleep(2)
print('PO !!!')
print('-=-' * 12)
print('O jogador escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}.'.format(itens[computador]))
print('-=-'*12)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTAODR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JODADA INVALIDA')


