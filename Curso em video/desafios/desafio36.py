casa = float(input('Qual o valor da casa: '))
salario = float(input('quanto e o seu salario: '))
anos = int(input('Quantos anos voce quer pagar: '))
emprestimo = casa / (anos * 12)
parcela = salario * 30 / 100
print('Para pagar uma casa de R${:.2f}, em {}anos a prestaçao vai sair R${:.2f} por mes.'.format(casa, anos, emprestimo))
if emprestimo <= parcela:
    print('Seu emprestimo foi APROVADO!')
else:
    print('Seu emprestimo foi Negado!')

