n = count = soma = 0
n = int(input('Digite um numéro [999 para parar]: '))
while n != 999:
    count +=1
    soma += n
    n = int(input('Digite um numéro [999 para parar]: '))
print('foram digitados {} numéros e a soma deles é {}.'.format(count, soma))
