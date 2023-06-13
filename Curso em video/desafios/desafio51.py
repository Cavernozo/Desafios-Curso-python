print('-=' * 10)
print(' 10 Termos de uma PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 -1) * razao
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end = '> ')
print('Acabou')
