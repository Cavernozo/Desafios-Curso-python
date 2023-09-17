jogador = {}
gols = []
jogadores = []
while True:
    jogador.clear()
    gols.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantos jogos o {jogador["Nome"]} jogou?'))
    for p in range(jogos):
        gols.append(int(input(f'  Quantos gols foram marcados na partida {p+1}?')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    jogadores.append(jogador.copy())
    while True:
        res = str(input('Quer continuar? [S/N]')).upper().strip()
        if res in 'SN':
            break
        print('ERRO. Digite S ou N.')
    if res == 'N':
        break
print('-=' * 30)
print()
print(f'{"Cod":<4}{"Nome":<10}{"Gols":<10}{"Total":<10}')
print('-' * 30)
for p, v in enumerate(jogadores):
    print(f'{p:<4} ', end='')
    for i in v.values():
        print(f'{str(i):<10}', end='')
    print()
    print('-' * 30)

while True:
    cont = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if cont == 999:
        break
    if cont >= len(jogadores):
        print('Erro !!! jogador nao existe!')
    else:
        print(f'-- Levantamento do jogador {jogadores[cont]["Nome"]}:')
        for j, g in enumerate(jogadores[cont]['Gols']):
            print(f'    no jogo {j+1} marcou {g} gols.')
    print('-' * 30)
print('<<< Fim do programa >>>')


