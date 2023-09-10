aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media do aluno: '))
print(f'Nome igual a {aluno["nome"]}')
print(f"A media do aluno é igual {aluno['media']}")
if aluno['media'] < 7:
    print('Situação é igual a Reprovado')
else:
    print('Situação é igual Aprovado')