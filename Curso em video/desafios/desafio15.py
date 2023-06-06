dias = int(input('Quantos dias alugados?'))
km = int(input('Quantos km rodados?'))
preco = (60 * dias) + (0.15 * km)
print('O preço a pagar e {:.2f}R$' .format(preco))
