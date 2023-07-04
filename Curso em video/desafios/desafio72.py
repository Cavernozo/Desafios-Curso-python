num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
       'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um numero de 0 até 20: '))
    cont = ' '
    if 0 <= numero <= 20:
        print(f'você digitou o numero {num[numero]}')
    else:
        print('Tente novamente! ', end = ' ')
    while cont not in 'SN':
        cont = str(input('Você quer contiuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
                break
print('Fim do programa!')




