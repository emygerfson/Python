from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nascimento = int(input('Em que ano {}ª nasceu? '.format(pess)))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maior de idade'.format(totmaior))
print('Tivemos ao total de {} menor de idade'.format(totmenor))
