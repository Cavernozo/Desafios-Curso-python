times = ('Botafogo', 'Gremio', 'Flamengo', 'Palmeiras', 'Bragantino',
         'Fluminense', 'Sao paulo', 'Internacinal', 'Atletico-PR',
         'Atletico-MG', 'Fortaleza', 'Cruzeiro', 'Cuiaba', 'Santos',
         'Bahia', 'Corinthians', 'Goias', 'Vasco', 'America-mg', 'Coritiba')
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os ultimos 4 colocados são: {times[-4:]}')
print(f'Os times em ordem alfabetica: {sorted(times)}')
print(f'O palmeiras está na {times.index("Palmeiras")+1}ª colocação.')