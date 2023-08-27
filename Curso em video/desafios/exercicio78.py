valores = []
for p in range(0, 5):
    valores.append(int(input(f'Digite um valor na posiçao {p}: ')))
    
print(f'Os valores digitador foram: {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posiçoes ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min(valores)} nas posiçoes ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end='')

