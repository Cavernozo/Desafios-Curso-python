nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
media = (nota1 + nota2) / 2
print('tirando {:.1f} e {:.1f} a media e {}.'.format(nota1, nota2, media))
if media >= 7:
    print(' voce passou de ano, parabens')
elif media > 5 < 7:
    print(' voce vai precisar de recuperaçao.')
else:
    print(' voce repetiu de ano.')