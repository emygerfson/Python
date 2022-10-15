import moeda
p = float(input('Digite um preço: R$'))
print(f'A metado de {moeda.moeda(p)} e {moeda.metade(p, True)}')
print(f'O dobro {moeda.moeda(p)} e {moeda.dobro(p, True)}')
print(f'Aumentanto o preço em 10% vai ficar {moeda.aumentar(p, 10, True)}')
print(f'Se eu tiver 20% de desconto fica {moeda.diminuir(p, 20, True)}')




