import moeda
p = float(input('Digite um preço: R$'))
print(f'A metado de {moeda.moeda(p)} e {moeda.moeda(moeda.metade(p))}')
print(f'O dobro {moeda.moeda(p)} e {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentanto o preço em 10% vai ficar {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Se eu tiver 20% de desconto fica {moeda.moeda(moeda.diminuir(p, 20))}')



