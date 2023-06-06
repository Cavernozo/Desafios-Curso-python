p = float(input('Digite o preço do produto? R$'))
d = p * 5 / 100  # 5%
v = p - d
print('preço do produto e {}R$, teve um desconto de {}R$, valor final = {}R$' .format(p, d, v))
