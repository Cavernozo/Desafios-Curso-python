pessoas = []
dados = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        elif dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont = str(input('Quer continuar? [S/N]')).upper().strip()
    if cont == 'N':
        break
print(f'Ao todo voce cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {mai}KG. Peso de ', end= '')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}] ', end= '')
print(f'O menor peso foi de {men}KG. Peso de ', end = '')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ', end = '')



