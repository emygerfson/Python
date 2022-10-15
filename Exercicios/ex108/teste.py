import moeda
p = float(input('Digite um preço: '))
print(f'A metado de {p} e {moeda.metade(p)}')
print(f'O dobro {p} e {moeda.dobro(p)}')
print(f'Aumentanto o preço em 10% vai ficar {moeda.aumentar(p, 10)}')
print(f'Se eu tiver 20% de desconto fica {moeda.diminuir(p, 20)}')



