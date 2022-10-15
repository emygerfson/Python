va = []
while True:
    va.append(int(input('Digite um valor ')))
    r = str( input('Você deseja contunuar [S|N] '))
    if r in 'Nn':
        break
print(f'Voce digitou {len(va)} valores')
va.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente {va}')
if 5 in va:
    print('Temos o valor 5 ')
else:
    print('Valor 5 não encontrado')
    
