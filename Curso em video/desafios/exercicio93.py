jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador:'))
jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou?'))
for p in range(jogos):
    gols.append(int(input(f'  Quantos gols na partida {p}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for p, v in jogador.items():
    print(f'No campo {p} tem o valor {v}.')
print('-=' * 30)
print(f"o jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for p, v in enumerate(jogador['gols']):
        print(f'Na partida {p} marcou {v} gols.')
print(f'Fes um total de {jogador["total"]} de gols.')