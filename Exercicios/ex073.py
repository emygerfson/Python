cont = ( 'zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze','quatoze', 'quinze', 'desseis', 'desete'
        , 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num < 20:
        print(f'O numero digitado foi o {cont[num]}')
        resp = ' '
    while resp not in 'SN':
        resp = str(input('Você deseja continuar [S|N] ')).strip().upper()[0]
    if resp == 'N':
         break
    print('Tente novamente', end=' ')
