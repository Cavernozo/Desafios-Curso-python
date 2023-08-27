valores = []

while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adcionado com sucesso...')
    else:
        print('Valor duplicado.Não vou adicionar...')
    cont = str(input('Quer continuar? [S/N]')).upper().strip()
    if cont in 'N':
            break
valores.sort()
print(f'Os valores digitados foram {valores}')