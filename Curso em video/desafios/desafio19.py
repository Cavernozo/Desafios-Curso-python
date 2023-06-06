import random
n = input('Digite um nome')
c = input('digite um nome')
d = input('digite um nome')
e = input('difite um nome')
nomes = [n, c, d, e]
k = random.choices(nomes)
print('o aluno escolhido foi {}' .format(k))
