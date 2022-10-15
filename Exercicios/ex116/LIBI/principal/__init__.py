from ex116.LIBI.INTERFACE import *
from ex116.LIBI.arquivo import *
from time import sleep



arq = 'Emygerfson.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver Pessoa Cadastra', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
       leiaarquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastre(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('SAIR do SISTEMA .... ATE LOGO! ')
        break
    else:
        print('\033[31mERRO: Digite um opçao valida!!!\033[m')
    sleep(2)