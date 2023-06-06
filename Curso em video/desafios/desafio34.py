salario = float(input('Qual e o salario do funcionario: '))
if salario > 1250.00:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)
print('quem ganha {:.2f}R$, vai passar a receber {:.2f}R$'.format(salario, aumento))
