name = 0
maior = 0
menor = 0
mulheres = 0
idades = 0
for p in range(1, 5):
    print('-'*5, '{}ªPessoa'.format(p), '-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper().strip()
    idades += idade
    if sexo == 'M' and p == 1:
        maior = idade
        name = nome
    else:
        if idade > maior:
            maior = idade
            name = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1

media = idades / 4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, name))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres))