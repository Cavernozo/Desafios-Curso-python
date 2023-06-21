''' forma Tradicional
n= int(input('Digite umn numero: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ' , end = '')
    f *= c
    c -= 1
print('{}'.format(f)'''
from math import factorial
n = int(input('Digite um numero para calcular seu factorial: '))
f = factorial(n)
print('O factorial de {} é {}.'.format(n, f))

