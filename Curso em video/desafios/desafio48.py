soma = 0
valores = 0
for cont in range(1, 501, 2):
  if cont % 3 == 0:
      valores += 1
      soma += cont
print('A soma de todos os {} valores solicitados é {}'.format(valores, soma))


