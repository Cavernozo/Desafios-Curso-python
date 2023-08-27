valores = []
while True:
    valores.append(int(input('Digite um valor? ')))
    cont = str(input('Quer continuar? [S/N]')).upper().strip()
    if cont in 'N':
        break
if 5 in valores:
    print('O valor 5 esta na lista.')
else:
    print('O valor 5 nao esta na lista')
valores.sort(reverse= True)
print(f'O total de valores digitados foram {len(valores)}')
print(f'A lista em ordem decrescente é {valores}')

