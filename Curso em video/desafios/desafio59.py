from time import sleep
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
menu = 0
while menu != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    menu = int(input('>>>>> Qual sua opção? '))
    if menu == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é igual {}.'.format(valor1, valor2, soma))
    elif menu == 2:
        mult = valor1 * valor2
        print('A multiplicação entre {} e {} é igual {}.'.format(valor1, valor2, mult))
    elif menu == 3:
        if valor1 > valor2:
            print('O valor {} é maior que o valor {}.'.format(valor1, valor2))
        else:
            print('O Valor {} é maior que o valor {}.'.format(valor2, valor1))
    elif menu == 4:
        print('Informe os números novamente.')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif menu == 5:
        print('Finalizando ....')
        sleep(3)
    else:
        print('Opção invalida')
print('Fim do programa.')