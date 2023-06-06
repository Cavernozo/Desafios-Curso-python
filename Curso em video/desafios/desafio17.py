from math import hypot
co = float(input('Digite o valor do cateto oposto'))
ca = float(input('Digite o valor do cateto adjacente'))
hipotenusa = hypot(co, ca)
print('o valor da hipotenusa e {:.2f}' .format(hipotenusa))
