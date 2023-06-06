s = float(input('Digite seu salario? R$'))
a = (s * 15) / 100
b = s + a
print('seu salario e {:.2f} R$, voce teve um aumento de {:.2f} R$, seu novo salario e {:.2f} R$' .format(s, a, b))