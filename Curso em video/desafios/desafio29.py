v = int(input('Qual era sua velocidade? '))
if v > 80:
    print('voce foi multado e vai pagar {:.2f}R$'.format((v - 80 )*7))
else:
    print('Tenha uma boa viagem')
