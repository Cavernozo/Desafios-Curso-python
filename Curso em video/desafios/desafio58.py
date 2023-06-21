from random import randint
count = 1
jogador = int(input('''Sou seu computador ...
Acabei de pensar em um numero de 0 até 10.
Será que você consegue advinhar? '''))
computador = randint(0, 10)
while computador != jogador:
    count += 1
    if jogador < computador:
        jogador = int(input('mais ... qual seu palpite?'))
    else:
        jogador = int(input('menos ... qual seu palpite? '))
print('acertou com {} tentativas.Parabéns'.format(count))