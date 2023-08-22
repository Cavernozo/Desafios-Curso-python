palavras = ('ana', 'joao', 'cama', 'campo', 'time', 'trabalho', 'muro')
for pos in palavras:
        print(f'\nNa palavra {pos} temos ', end=' ')
        for letra in pos:
            if letra.lower() in 'aeiou':
                print(letra, end=' ')