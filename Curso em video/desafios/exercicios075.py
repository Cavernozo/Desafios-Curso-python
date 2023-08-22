Valores = (int(input('Digite um numero: ')),
            int(input('Digite outro valor: ')),
            int(input('Digite outro valor: ')),
            int(input('Digite o ultimo valor: ')))
print(f'Os valores digitados foram {Valores}')
print(f'O valor 9 foi digitado {Valores.count(9)} vezes')
if 3 in Valores:
    print(f'O valor 3 foi digitado na {Valores.index(3)+1}ª posição')
else:
    print('O valor 3 nao foi digitado')
print('Os valores pares digitados foram: ', end='')
for n in Valores:
    if n % 2 == 0:
        print(n , end=' ')