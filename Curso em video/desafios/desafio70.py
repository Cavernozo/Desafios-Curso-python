total = maior = menor = conta = 0
nome = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont = ' '
    total += preco
    conta +=1
    if preco > 1000:
        maior += 1
    if conta == 1 or preco < menor:
        menor = preco
        nome = produto
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
            break
print('====== Fim do programa ======')
print(f'O total gasto na compra foi R${total:.2f}.')
print(f'E temos {maior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custou {menor:.2f}.')

