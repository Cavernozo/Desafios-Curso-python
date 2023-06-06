peso = float(input('Qual seu peso? (Kg)'))
altura = float(input('Qual sua altura? (m)'))
imc = peso / (altura ** 2)
print('O seu imc é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO do Peso.')
elif imc < 25:
    print('Voce esta com o Peso IDEAL.')
elif imc < 30:
    print('Voce esta ACIMA do Peso.')
elif imc < 40:
    print('Voce esta com Obesidade.')
elif imc > 40:
    print('Voce esta com OBESIDADE MORBIDA.')
else:
    print('erro')