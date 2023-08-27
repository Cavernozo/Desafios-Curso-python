valores = []
pares = []
impar = []
while True:
    valores.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? [S/N]')).upper().strip()
    if cont in 'N':
        break
for pos in range(0, len(valores)):
    if valores[pos] % 2 == 0:
        pares.append(valores[pos])
    else:
        impar.append(valores[pos])
print(f'Os valores digitados foram {valores}')
print(f'Os valores pares sao {pares}')
print(f'Os valores impares sao {impar}')
