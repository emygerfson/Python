from datetime import date
ano = int(input('Qual ano voce quer Analisar ? Ou coloque zero se quer analisar ano atual?  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print("Esse ano {} e BISEXTO".format(ano))
else:
    print('Esse ano {} NÂO e BISEXTO'.format(ano))

