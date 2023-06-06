print('{:=^40}'.format(' Lojas do seu Zé '))
preco= float(input('Valor do produto: R$'))
print('''Formas de pagamento
[1] Á vista dinheiro/cheque
[2] Á vista no cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')
forma = int(input('Qual a forma de pagamento? '))
if forma == 1:
    final = preco - (preco * 10 /100)
elif forma == 2:
    final = preco - (preco * 5 /100)
elif forma == 3:
    final = preco / 2
    print('Sua compra  vai sair por 2x de R${:.2f} no final.'.format( final))
elif forma == 4:
    final = preco + (preco * 20 / 100)
    parcela = int(input('Quantas parcelas?'))
    total = final / parcela
    print('Sua compra vai sair por {}x de R${:.2f} no final.'.format(parcela, total))
else:
    final = preco
    print('Tentativa invalida de pagamento, tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, final))