from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('vou pensar em um numero entre  0 e 5 tente adivinhar... ')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei '))
print('PROCESSANDO... ')
sleep(4)
if jogador == computador:
    print('Parabens voce acertou')
else:
    print('Tente novamete')


