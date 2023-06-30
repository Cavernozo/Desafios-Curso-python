cont = maior = menor = media = soma = 0
continuar = 'S'
while continuar != 'N':
    n = int(input('Digite um numéro: '))
    cont += 1
    soma += n
    media = soma / cont
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'S':
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('você digitou {} numeros o maior é {} e o menor {} a media é {}.'.format(cont, maior, menor, media))



