def fatorial(n,show=False):
    '''
    -> Calculo do fatorial
    :param n: o numero a ser calculado
    :param show: opcional mostra ou não a conta
    :return: o valor fatorial de numero 'n'
    '''
    f = 1
    for c in range(n, 0, -1 ):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f


#print(fatorial(5, show=True))
help(fatorial)
