sexo = str(input('digite seu sexo [M\F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dado invalidos digite um sexo valido ')).strip().upper()
print('sexo {} cadastrado com sucesso'.format(sexo))