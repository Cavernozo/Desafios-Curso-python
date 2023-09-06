matriz = [[], [], []]
for p in range(len(matriz)):
    for i in range(0, 3):
        valor = int(input(f'Digite um valor na posiçao [{p}, {i}]: '))
        matriz[p].append(valor)
for i in range(0, 3):
    for p in range(0, 3):
        print(f'[{matriz[i] [p]:^5}]', end='')
    print()



