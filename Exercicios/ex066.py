resp = 'S'
soma = quantidade = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um nº '))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar [S|N]')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} nº , e a media e {} '.format(quantidade, media))
print('O maior nº foi {} e menor foi {}'.format(maior, menor))
