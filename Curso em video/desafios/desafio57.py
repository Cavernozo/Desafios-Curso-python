sexo = str(input('Informe seu sexo: [M/F]')).upper().strip()
while sexo != 'M' and sexo != 'F':
    print('Dados invalidos!', end = ' ')
    sexo = str(input('Informe seu sexo: [M/F]')).upper().strip()
print('Sexo {} registrado com sucesso'.format(sexo))
