jogador = {}
partidas = list()
jogador['nome'] = str(input('Nome: '))
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range(0,tot):
    partidas.append(int(input(f'{c+1}ª jogo fez quantos gol? ')))
jogador['GOl'] = partidas[:]
jogador['total'] = sum(partidas)
print('=='*20)
print(jogador)
print('=='*20)
for k,v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('=='*20)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["GOl"])} partidas')
for i, v in enumerate(jogador['GOl']):
    print(f'Na {i +1}º partida ele fez {v} gols')
print(f'Foi o total de {jogador["total"]}')
