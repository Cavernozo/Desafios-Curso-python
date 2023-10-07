from time import sleep
def maior(* num):
    M = 0
    print('Analisando os valores passados...')
    for p in range(len(num)):
        sleep(0.5)
        print(num[p], end=' ')
        if num[p] > M:
            M = num[p]
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {M}.')
    print('=-' * 20)


maior(2, 9, 4, 5, 7, 1)
maior(1, 7, 0)
maior(1, 2)
maior(6)
maior()


