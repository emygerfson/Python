def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não Vota '
    elif 16 <= idade < 18 or idade > 65:
        return f'Com{idade} anos: VOTO NÂO E OBRIGATORIO '
    elif idade > 18:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


nas = int(input("Em que ano voce nasceu"))

print(voto(nas))



