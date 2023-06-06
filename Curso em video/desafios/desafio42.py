n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
        print('Os segmentos formam um triangulo, EQUILATERO.')
    elif n1 != n2 != n3 != n1:
        print('Os segmentos formam um trinagulo, ESCALENO.')
    else:
        print('Os segmentos formam um triangulo, ISOSCELES.')
else:
    print('Os segmantos nao formam um TRINAGULO')


