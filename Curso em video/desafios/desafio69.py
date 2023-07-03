maior = h = m = 0
while True:
    print('-=' * 20)
    print('Cadastre um pessoa')
    print('-=' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().split()[0]
    continuar = ' '
    if idade > 18:
        maior += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O total de pessoas com mais de 18 anos è: {maior}.')
print(f'E temos {h} homens cadastrados.')
print(f'E temos {m} mulheres abaixo de 20 anos.')