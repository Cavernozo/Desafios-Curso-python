from datetime import date
ano = int(input('Qual seu ano de nascimento: '))
alistamento = date.today().year - ano
if alistamento > 18:
    print('Voce tem {} anos, no ano de {}.'.format(alistamento, date.today().year))
    print('Deveria ter se alistado ha {} ano.'.format(alistamento - 18))
    print('Seu alistamento foi em {}.'.format(ano + 18))
elif alistamento < 18:
    print('Voce tem {} anos, no ano de {}.'.format(alistamento, date.today().year))
    print('Devera se alistar daqui {} anos.'.format(18 - alistamento))
    print('Seu alistamento vai ser em {}.'.format(ano +18))
else:
    print('Voce tem {} anos, no ano de {}.'.format(alistamento, date.today().year))
    print('Voce deve se alistar imediatamente!')



