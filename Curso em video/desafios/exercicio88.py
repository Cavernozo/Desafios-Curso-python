from random import randint
quant = int(input('Quantos jogos você quer que eu sorteie? '))
list = []
jogos = []
tot = 1
while tot <= quant:
    cont = 0
    while True:
        numero = randint(0, 60)
        if numero not in list:
            list.append(numero)
            cont += 1
        if cont >= 6:
            break
    list.sort()
    jogos.append(list[:])
    list.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')