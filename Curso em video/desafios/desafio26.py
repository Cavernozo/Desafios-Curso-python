nome = str(input('Qual seu nome completo?')).upper().strip()
print('Quantas vezes aparace a letra {}'.format(nome.count('A')))
print('A letra A aparece a primeira vez na posiçao {}'.format(nome.find('A')+1))
print('A letra A aparece pela ultima vez na posiçao {}'.format(nome.rfind('A')+1))


