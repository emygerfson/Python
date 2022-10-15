def notas(*n, sit=False):
    """
    -> Função para analisar notas
    :param n: notas avaliadas
    :param sit: o analisador das notas
    :return: serva para retornar ao calculo
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 8, 7, 9 , sit=True)
print(resp)
help(notas)
