from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nas = int(input('Ano de nascismento: '))
dados['idade'] = datetime.now().year - nas
dados['CTPS'] = int(input('CTPS ( 0 não tem ): '))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Qual seu salario: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('=='*15)
for k , v in dados.items():
    print(f'{k} tem o valor {v}.')
print('=='*15)
