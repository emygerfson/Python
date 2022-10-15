soma= cont= 0
while True:
    num = int(input('Digite um um nº e quando for [999] vai parar: '))
    if num == 999:
        break
    ##else:
    soma += num
    cont += 1
print(f'Voce digitou {cont} e a soma foi {soma}')
