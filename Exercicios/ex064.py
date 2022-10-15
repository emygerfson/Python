print('Seguencia de FIBONACCI')
print('~~~~' * 10)
num = int(input('Quantos termos vc quer adicionar? '))
t1 = 0
t2 = 1
print('~~~~' * 10)
print('{} - {} '.format(t1, t2), end='')
contagem = 3
while contagem <= num:
    t3 = t1 + t2
    print('- {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contagem += 1
print('<< FIM >>')