from datetime import date
atual = date.today().year
mulher = str(input('Você e mulher? '))
if mulher == 'sim':
    print('Você não Precisa se ALISTAR')
elif mulher == 'não':
    nas = int(input("Qual ano que vc nasceu? "))
    idade = atual - nas
    print('Quem nasceu em {} tem {} anos em {}'.format(nas, idade, atual))
    saldo = 18 - idade
    print('Ainda falta {} anos pra vc se ALISTAR'.format(saldo))
    ano = atual + saldo
    print('Seu ALISTAMENTO sera {}'.format(ano))
    saldo = idade - 18
    print('Você deveria ja ter se ALISTADO a {}'.format(saldo))
    ano = atual -saldo
    print('Seu ALISTAMENTO era para ter sido em {}'.format(ano))











































