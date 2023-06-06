from datetime import date
sexo = str(input('Qual seu sexo? '))
atual = date.today().year
if sexo == 'feminino':
    print('Voce nao precisa se alistar.')
elif sexo == 'masculino':
    ano = int(input('Qual ano voce nasceu? '))
    idade = atual - ano
    if idade > 18:
        print('quem nasceu em {}, tem {} anos.'.format(ano, atual - ano))
        print('Voce deveria ter se alistado a {} anos.'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(ano + 18))
    elif idade < 18:
        print('Quem nasceu em {}, tem {} anos.'.format(ano, atual - ano))
        print('Devera se alistar daqui {} anos.'.format(18 - idade))
        print('Seu alistamento vai ser em {}.'.format(ano + 18))
    else:
        print('quem nasceu em {}, tem {} anos.'.format(ano , atual - ano))
        print('Voce deve se alistar imediatamente!')
        




