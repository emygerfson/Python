from ex116.LIBI.INTERFACE import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO ao criar o arquivo')
    else:
        print(f'Arquivo{nome} foi criado com sucesso')

def leiaarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler Arquivo')
    else:
        cabeçalho('PESSOAS CADSTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastre(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao escrever os dados')
        else:
            print(f'Novo registro de {nome} foi cadastrado com sucesso')
            a.close()




