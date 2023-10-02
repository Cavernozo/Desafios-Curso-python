from time import sleep
def contador(ini, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    sleep(1)
    cont = ini
    if ini < fim:
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont += passo
        print('Fim!')
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont -= passo
        print('Fim!')

#Progrma Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('A agora é sua vez de personalizar a contagem.')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
