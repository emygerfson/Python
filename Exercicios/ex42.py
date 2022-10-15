from datetime import date

nas = int(input('Qual seu ano de nascimento '))
ano = date.today().year
categoria = ano - nas
if categoria <= 9:
    print('Voce tem {} anos e sua categoria e Mirim'.format(categoria))
elif categoria > 9 and categoria < 14:
    print('Voce tem {} anos e sua categoria e Infantil'.format(categoria))
elif categoria > 14 and categoria < 19:
    print('Voce tem {} anos e sua categoria e JUNIOR'.format(categoria))
elif categoria > 19 and categoria < 25:
    print('Você tem {} anos e sua categoria e a SENIOR'.format(categoria))
elif categoria > 25:
    print('Você tem {} anos e sua categoria e a MASTER'.format(categoria))
