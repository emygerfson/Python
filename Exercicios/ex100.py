from time import sleep
def maior(*num):
    cont = maoir = 0
    print('\nAnalisando o valor passado:')
    print('=='*15)
    for valor in num:
        print(f'{valor} ',end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informado {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')



maior(2, 4, 5, 8, 9, 10, 15)
maior(5, 6, 7, 9)
maior(1, 2, 3)
maior(4, 5)
maior(0)

