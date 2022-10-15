tot = totH = mulher = 0
while True:
    idade = int(input('Qual sua Idade '))
    sexo = ' '
    while sexo not in 'MF':
       sexo = str(input('SEXO [M|F]: ')).strip().upper()[0]
    if idade >= 18:
        tot += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar SIM OU NÂO [S|N] ')).strip().upper()[0]
    if resp == 'N':
         break
print(f'o Total de pessoas acima de 18 e {tot}')
print(f'e o total de homens são {totH}')
print(f'Temos {mulher} mulheres menor de 20 anos')

