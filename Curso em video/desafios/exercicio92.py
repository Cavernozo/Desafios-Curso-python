from datetime import date
dados = {}
dados['Nome'] = str(input('Nome: '))
dados['idade'] = int((input('Ano de nascimento: ')))
dados['Carteira'] = int(input('Carteira de trabalho: [0 nem tem] '))
if dados['Carteira'] != 0:
    dados['contrato'] = int(input('Ano de contrataçao: '))
    dados['Salario'] = int(input('Salario: R$ '))
    reforma = (dados['contrato'] - dados['idade']) + 35
    dados['aposentadoria'] = reforma
dados['idade'] = date.today().year - dados['idade']
print('-='* 30)
for p, v in dados.items():
    print(f'{p} tem o valor {v}')
print()