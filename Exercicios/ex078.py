palavras = ('Emygerfson','Islane','Erick','Renata','Bruno','Antonia','Luiz','Jose','Joao','Jesus')
for p in palavras:
    print(f'\nA palavra {p.upper()} temos',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')