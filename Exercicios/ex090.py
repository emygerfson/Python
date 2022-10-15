ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = int(input('1º nota: '))
    nota2 = int(input('2º nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1 , nota2], media])
    resp = str(input('Voce deseja continuar [S|N]: '))
    if resp in 'Nn':
        break
print(f'{"Nª":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    opc = int(input('Mostrar a nota de qual ALUNO?(999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha)- 1:
        print(f'notas de {ficha[opc][0]} são {ficha[opc][1]}')


