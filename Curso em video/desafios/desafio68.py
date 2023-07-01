import random
vitorias = 0
print('-=' * 20)
print('Jogo do PAR ou IMPAR')
print('-=' * 20)
while True:
    jogador = int(input('Diga um valor: '))
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR? [P/I]')).upper().split()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. o total è {total}', end = ' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu.')
            vitorias +=1
        else:
            print('Você perdeu.')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu.')
            vitorias +=1
        else:
            print('Você perdeu.')
            break
    print('Vamos jogar novamente ....')
print(f'Game over!!! Você teve um total de {vitorias} consecutivas.')

