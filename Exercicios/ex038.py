num = int(input('Digite um numero inteiro '))
print('''escolha e conversão que você quer
[1] para BINARIO
[2] para OCTAL
[3] para HEXADECIMAL''')
opção = int(input('escolha a opção '))
if opção == 1:
    print('{} convertido para BINARIO e {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print(' {} convertido para OCTAL e {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL e {}'.format(num, hex(num)[2:]))
else:
    print('Tente uma das ESCOLHAS')