print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
decimo = termo
cont = 1
while cont <= 10:
    print('{} > '.format(decimo), end = '')
    decimo += razao
    cont += 1
print('Fim')