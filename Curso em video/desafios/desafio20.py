import random
k = input('Digite um nome:')
c = input('Digite um nome:')
v = input('Digite um nome:')
x = input('Digite um nome:')
nomes =[k, c, v, x]
random.shuffle(nomes)
print('A ordem de apresentaçao e:')
print(nomes)