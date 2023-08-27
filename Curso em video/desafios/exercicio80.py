valores = []
for p in range(0, 5):
    n = (int(input('Digite um valor: ')))
    if p == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posiçao {pos} da lista....')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {valores}')
