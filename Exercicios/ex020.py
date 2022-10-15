'''import random
n1 = str(input('Digite o nome do primeiro Aluno'))
n2 = str(input('Digite  onome do segundo Aluno'))
n3 = str(input('Digite o nome do terciro Aluno'))
n4 =str(input('Digite o nome do Quarto Aluno'))
lista = [n1,n2,n3,n4]
escolido = random.choice(lista)
print(' O aluno escolhido foi {}'.format(escolido))'''

from random import choice
n1 = str(input('Digite o nome do primeiro Aluno'))
n2 = str(input('Digite o nome do segundo Aluno'))
n3 = str(input('digite o nome do terceiro Aluno'))
n4 = str(input('Digite o nome do quarto Aluno'))
lista = [n4,n3,n2,n1]
escolhido = choice(lista)
print('O Aluno escolhido foi {}'.format(escolhido))

