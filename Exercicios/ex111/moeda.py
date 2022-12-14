def aumentar(preço=0, taxa=0, formato=False):
    resp = preço + (preço * taxa / 100)
    return resp if formato is False else moeda(resp)


def diminuir(preço=0, taxa=0, formato= False):
    resp = preço - (preço * taxa / 100)
    return resp if formato is False else moeda(resp)


def dobro(preço=0, formato=False):
    resp = preço * 2
    return resp if formato is False else moeda(resp)


def metade(preço=0, formato=False):
    resp = preço / 2
    return resp if formato is False else moeda(resp)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'O preço analisado :\t {moeda(preço)}')
    print(f'O dobro do preço:\t {dobro(preço, True)}')
    print(f'A metade do preço:\t {metade(preço, True)}')
    print(f'{taxaa}% de aumento :\t {aumentar(preço,taxaa, True)}')
    print(f'{taxar}% de desconto:\t {diminuir(preço,taxar, True)}')
    print('-' * 30)
