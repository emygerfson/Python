aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Qual e a MEDIA de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['media']  < 7:
    aluno['situação'] = 'RECUPERAÇÂO'
else:
    aluno['situação'] = 'REPROVADO'
print(aluno)
for k , v in aluno.items():
    print(f'{k} e igual a {v}' )





