from  random import randint
from time import sleep
from operator import itemgetter
jogo = {'1ª jogador': randint(1,6),
        '2º jogador':randint(1,6),
        '3º jogador': randint(1,6),
        '4º jogador': randint(1,6)}
rank = dict
for k , v in jogo.items():
    print(f'O {k} tirou  o numero {v} do DADO ')
    sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(' == RANK DOS JOGADORES ==')
for i , v in enumerate(rank):
    print(f'{i + 1}º lugar {v[0]} com {v[1]}')
    sleep(1)



