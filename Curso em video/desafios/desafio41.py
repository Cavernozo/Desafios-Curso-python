from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
categoria = atual -nascimento
print('quem nasceu em {} tem tantos anos {}.'.format(nascimento, categoria))
if categoria <= 9:
    print('e da categoria MIRIM.')
elif categoria <= 14:
    print('e da categoria INFANTIL.')
elif categoria <= 19:
    print('e da categoria JUNIOR.')
elif categoria <= 25:
    print('e da categoria SENIOR.')
else:
    print('e da categoria MASTER.')
