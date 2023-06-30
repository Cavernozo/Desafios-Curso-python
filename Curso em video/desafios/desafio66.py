soma = cont = 0
while True:
    num = int(input('Digite um numéro [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'Foram digitados {cont} numéros e a soma deles é {soma}.')