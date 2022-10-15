time = list()
jogador = {}
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'{c+1}ª jogo fez quantos gol? ')))
    jogador['GOl'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Você de seja continuar [S|N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO resposta apaenas sim ou não')
    if resp == 'N':
        break
print('=='*20)
print('cod',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}',end='')
    for d in v.values():
        print(f'{str(d):?<15}',end='')
    print()
print('=='*20)
while True:
    buscar = int(input('Mostre os dado do jogador ?[999] para: '))
    if buscar == 999:
        break
    if buscar >= len(time):
        print(f'Erro não existe jogador com esse {buscar} numero de codigo')
    else:
        print(f'Levantamento do jogador {time[buscar]["nome"]}')
        for i, g in enumerate(time[buscar]['GOl']):
            print(f'No jogo {i+1} fez {g} gols.')
