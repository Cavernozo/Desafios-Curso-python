pessoas = {}
cadastro = []
mulheres = []
mediaI = soma = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo: [F/M]')).upper().strip()
    while pessoas['Sexo'] not in 'FM':
        print('Erro. Digite F ou M.')
        pessoas['Sexo'] = str(input('Sexo: [F/M]')).upper().strip()
    pessoas['Idade'] = int(input('Idade: '))
    cadastro.append(pessoas.copy())
    soma += pessoas['Idade']
    res = str(input('Quer continuar? [S/N]')).upper().strip()
    while res not in 'SN':
        print('ERRO. Digite S ou N.')
        res = str(input('Quer continuar? [S/N]')).upper().strip()
    if res == 'N':
        break
print('-=' *30)
print(f'A) Foram cadastrados um total de {len(cadastro)} pessoas.')
mediaI = soma / len(cadastro)
print(f'B) A media de idade é {mediaI:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in cadastro:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print(f'D) Lista de pessoas acima da media:')
for p in cadastro:
    if p['Idade'] > mediaI:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v} ;', end='')
        print()
print('<<< ENCERRADO >>>')
