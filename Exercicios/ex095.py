galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo:[M | F]  ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Erro apenas e aceito M ou F')
    pessoa['idade'] = int(input('Qual sua idade '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar [S|N] ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('Erro responda apenas S ou N')
    if resp == 'N':
        break
print(f'Ao total temos {len(galera)} pessoas cadastra')
media = soma / len(galera)
print(f'A media de  idade e {media:5.2f} anos')
print('As mulheres cadastradas são ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}')
print('E as pessoas que estão acima da media: ',end='')
for p in galera:
    if p['idade'] >= media:
        print('    ',end='')
        for k, v in p.items():
            print(f'{k} = {v} :', end='' )
            print()
print('<<< ENCERRADO >>>')