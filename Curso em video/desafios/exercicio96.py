def area(a, b):
    area = a * b
    print(f'A área de um terrone de {a} x {b} é de {area}m².')


print('-=' * 20)
print('<<< Controle de Terrenos >>>')
print('-=' * 20)
largura = float(input('Largura do terreno? '))
compri = float(input('Comprimento do terreno? '))
area(largura, compri)