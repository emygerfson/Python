n1 = int(input('digite o 1ª valor? '))
n2 = int(input('Digite o 2º valor? '))
opção = 0
while opção != 5:

    print('''Opção:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] DIGITE NOVO Nº
    [5] SAIR''')
    opção = int(input('Qual e a sua OPÇÂO: '))
    if opção == 1:
        num = n1 + n2
        print('A soma entre {} + {} e {}'.format(n1, n2, num))
    elif opção ==2:
        num2 = n1 * n2
        print('A multiplicação entre {} * {} = {}'.format(n1, n2, num2))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor e {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os novos valores: ')
        n1 = int(input('Digite o 1º valor'))
        n2 = int(input('Digite o 2º valor'))
    elif opção == 5:
        print('<<<<<FINALIZANDO >>>>>')
    else:
        print('Opção invalida digite novamente')
print('Fim do Processo')

