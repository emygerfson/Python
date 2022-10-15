'''co = float(input('digite o vlor do cateto oposto'))
ca = float(input('digite o volor do cateto adjasente'))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa e {:.2f}'.format(hip))'''
'''import math
co = float(input('digite o valor do cateto oposto '))
ca = float(input('digite o valoe do cateto adjasente'))
hip = math.hypot(co,ca)
print('A hipotenusa e {:.2f}'.format(hip))'''

from math import hypot
co = float(input('digite op valor do cateto oposto'))
ca = float(input('digite o valor do cateto adjasente'))
hip = hypot(co ,ca)
print('a hipotenusa e {:.4f}'.format(hip))

