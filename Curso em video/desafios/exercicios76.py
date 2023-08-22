Listagem = ('Lapis', 1,
            'Borracha', 0.50,
            'Lapiseira', 2.50,
            'Caderno', 5,
            'Mochila', 40 )
print('-' * 40)
print(f'{"Listagem de Preços":^40}')
print('-' * 40)
for pos in range(0 ,len(Listagem)):
    if pos % 2 == 0:
        print(f'{Listagem[pos]:.<30}', end=' ')
    else:
        print(f'{Listagem[pos]:>7.2f}')