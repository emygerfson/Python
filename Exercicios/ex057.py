somaidade = 0
mediaidade = 0
maioridadehomem = 0
homemvelho = 0
totmulher20 = 0
mulhernova = 0
for p in range(1, 5):
    print('------{}-------'.format(p))
    nome = str(input('Qual seu nome? ')).strip()
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Sexo [M\F] ' )).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        homemvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
        mulhernova = nome
    mediaidade = somaidade / 4
print('A media de idade do grupo e de {} anos'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}'.format(maioridadehomem, homemvelho))
print('Temos {} mulher menor que 20 anos e nome e {}'.format(totmulher20, mulhernova))