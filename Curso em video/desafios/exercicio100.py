from random import randint
from time import sleep
def sorteia(sorteio):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(0, 10)
        sorteio.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)
    print('PRONTO!')

def somarPar(pares):
    soma = 0
    for p in pares:
        if p % 2 == 0:
            soma += p
    print(f'Somando dos valores pares de {pares}, temos {soma} ')



numeros = list()
sorteia(numeros)
somarPar(numeros)
