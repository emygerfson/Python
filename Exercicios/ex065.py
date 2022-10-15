#num = cont = soma = 0
num = 0
cont = 0
soma = 0
num = int(input('Digite um um nº e quando for [999] vai parar: '))
while num != 999:
    #num = int(input('Digite um um nº e quando for [999] vai parar: '))
    soma += num
    cont += 1
    num = int(input('Digite um um nº e quando for [999] vai parar: '))
#print('Você digitou {} e a soma foi {}'.format(cont - 1, soma - 999))
print('Você digitou {} e a soma foi {}'.format(cont, soma))
print('ACABOU')
