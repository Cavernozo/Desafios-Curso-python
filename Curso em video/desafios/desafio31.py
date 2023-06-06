viagem = int(input('Digite a distancia da viagem: '))
if viagem <= 200:
    print('O valor a pagar e {}R$'.format(viagem * 0.50))
else:
    print('O valor a pagar e {}R$'.format(viagem * 0.45))