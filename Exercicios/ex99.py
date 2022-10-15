from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
       p = 1
    print('=='* 15)
    print(f'contagem de {i} ate {f} de {p} em {p}')
    sleep(2)
    print('=='* 15)
    if i < f:
        cont = i
        while cont <= f:
            print(f' {cont} ',end='' , flush=True)
            sleep(0.5)
            cont += p
        print(' Fim ')
    else:
        cont = i
        while cont >= f:
            print(f' {cont} ',end='', flush=True)
            sleep(0.5)
            cont -= p
        print(' Fim ')
print('=='* 15)


contador(1, 10, 1)
contador(10, 0, 2)
print('=='* 15)
print('Agora e sua vez de personazinar a contagem')
ini = int(input('Inicio  '))
fim = int(input('Fim     '))
pas = int(input('Passe   '))
contador(ini, fim, pas)

