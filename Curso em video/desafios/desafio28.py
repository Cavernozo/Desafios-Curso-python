import random
from time import sleep
jogador = int(input('Escolha um numero de 0 ate 5: '))
maquina = random.randint(0, 5)
sleep(3)
print('O numero escolhido por voce foi {}, e o numero da maquina era {}'.format(jogador, maquina))
if jogador == maquina:
    print('Voce venceu')
else:
    print('voce perdeu,Tente na proxima')
