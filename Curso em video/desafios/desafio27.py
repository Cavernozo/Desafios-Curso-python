nome = str(input('Digite seu nome completo:').strip())
b = nome.split()
print('seu primeiro nome e {}'.format(b[0]))
print('seu ultimo nome e {}'.format(b[len(b)-1]))
