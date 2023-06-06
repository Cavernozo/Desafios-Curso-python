n = int(input('Digite um numero: '))
print('''Escolha uma das bases para conversao: 
[1] converter para BINARIO!
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
o = int(input('Sua opçao: '))
if o == 1:
    print('{} convertido para BINARIO e {}'.format(n, bin(n)[2:]))
elif o == 2:
    print('{} convertido para OCTAL e {}'.format(n, oct(n)[2:]))
elif o == 3:
    print('{} convertido para HEXADECIMAL e {}'.format(n, hex(n)[2:]))
else:
    print('erro no programa')
