from random import randint
from time import sleep
itens = ('pedra', 'tesoura', 'papel')
computador = randint(0, 2)
print('''Suas opções: 
[0]PEDRA
[1]TESOURA
[2]PAPEL''')
jogador = int(input('Qual sua escolha? '))
sleep(0.5)
print('jo')
sleep(0.5)
print('ken')
sleep(0.5)
print('po')
sleep(0.5)
print('-='*20)
print('computador jogou {}.'.format(itens[computador]))
print('o jogador jogou {}.'.format(itens[jogador]))
print('-='*20)
if computador == 0:
    if jogador == 0:
        print('Deu EMPATE!')
    elif jogador == 1:
        print('Computador VENCEU!!!')
    elif jogador == 2:
        print('Você GANHOU parabéns!!!')
    else:
        print('Jogada INVALIDA!')
elif computador  == 1:
    if jogador == 0:
        print('Você GANHOU parabèns!!!')
    elif jogador == 1:
        print('Deu EMPATE!')
    elif jogador == 2:
        print('Computador VENCEU!!!')
    else:
        print('Jogada INVALIDA!')
elif computador == 2:
    if jogador == 0:
        print('Computador VENCEU!!!')
    elif jogador == 1:
        print('Você GANHOU parabèns!!!')
    elif jogador == 2:
        print('Deu EMPATE!')
    else:
        print('Jogada INVALIDA!')
