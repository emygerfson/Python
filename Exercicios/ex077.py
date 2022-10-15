print('===' * 15)
print('LISTA DE COMPRAS')
print('===' * 15)
lista = ('Lapis' ,'1,50','caneta','2,50','caderno','5,30','lapiseira','3,50','cartulina','2,75','cartolina','2,75')
for posição in range(0 , len(lista)):
    if posição % 2 == 0:
        print(f'{lista[posição]:.<30}',end=' ')
    else:
        print(f'R${lista[posição]:>2}')
print('===' * 15)



