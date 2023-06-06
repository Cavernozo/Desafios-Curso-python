pro = float(input('Preço do profuto? R$'))
vista = pro - (pro * 10 / 100)
cartao = pro + (pro * 8 / 100)
print('o produto custa {}R$, pagando a vista ele fica {}R$ se parcelar fica {}R$' .format(pro, vista, cartao))