matriz = [[], [], []]
totp = colun = linha =  0
for p in range(len(matriz)):
    for i in range(0, 3):
        valor = int(input(f'Digite o valor na posiçao [{p}, {i}]: '))
        matriz[p].append(valor)
        if valor % 2 == 0:
            totp = totp + valor
for l in range(0, 3):
    colun += matriz[l] [2]
for c in matriz[1]:
    if c > linha:
        linha = c
for i in range(0, 3):
    for p in range(0, 3):
        print(f'[{matriz[i] [p]:^5}]', end='')
    print()
print(f'O total de valores pares digitados foi de {totp}')
print(f'A soma dos valores da terceira coluna é de {colun}')
print(f'o maior valor da segunda linha é {linha}')