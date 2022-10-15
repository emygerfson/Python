def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um  numero inteiro valido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuario prefiriu não digitar numeros\033[m')
            return 0
        else:
            return n



def leiaflot(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um  numero inteiro valido!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuario prefiriu não digitar numeros\033[m')
            return 0
        else:
            return n



n1 = leiaint('Digite um numero inteiro: ')
n2 = leiaflot('numero Real: ')
print(f' O valor digitado foi {n1} e {n2}')