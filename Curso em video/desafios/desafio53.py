frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('A frase {} ao contrario é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo.')
else:
    print('A frase digitada não é um palindromo.')