from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    nascimento = int(input('Que ano a pessoa {}ª nasceu: '.format(c)))
    idade = atual - nascimento
    if idade > 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas que atingiram a maior idade.'.format(maior))
print('E tivemos {} pessoas com menores de idade.'.format(menor))