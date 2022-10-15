c = ('\033[m', # sem cor
      '\033[0;30;41m', # vermelho
      '\033[0;30;41m', # verde
      '\033[0;30;41m', # Amarelo
      '\033[0;30;41m', # Azul
      '\033[0;30;41m', # Roxo
      '\033[0;30;41m') # Branco

def ajuda(com):
    titulo(f'Acessando o manual \ {com}\'', 3)
    print(c[6], end='')
    help(com)
    print(c[6], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA',2)
    comando = str(input("Função ou Biblioteca >>"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!...', 3)