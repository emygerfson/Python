valor = int(input('Qual valor você quer sacar R$ '))
total = valor
dinheiro = 50
totaldin = 0
while True:
    if total >= dinheiro:
        total -= dinheiro
        totaldin += 1
    else:
        if totaldin > 0:
           print(f'Total de {totaldin} de R$ {dinheiro}')
        if dinheiro == 50:
            dinheiro = 20
        elif dinheiro == 20:
            dinheiro = 10
        elif dinheiro == 10:
            dinheiro = 1
            totaldin = 0
        totaldin = 0
        if total == 0:
           break
print('Volte SEMPRE')