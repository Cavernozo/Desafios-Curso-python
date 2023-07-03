cinquenta = vinte = dez = um = 0
print('=' * 30)
print('{:^30}'.format('Banco Ibis'))
print('=' * 30)
sacar = int(input('Quanto você quer sacar: R$'))
while True:
    if sacar != 0:
        cinquenta = sacar // 50
        sacar = sacar % 50
        print(f'Total de cédulas de R$50: {cinquenta}')
        if sacar != 0:
            vinte = sacar // 20
            sacar = sacar % 20
            print(f'Total de cédulas de R$20: {vinte}')
            if sacar != 0:
                dez = sacar // 10
                sacar = sacar % 10
                print(f'Total de cédulas de R$10: {dez}')
                if sacar != 0:
                    um = sacar // 1
                    sacar = sacar % 1
                    print(f'Total de cédulas de R$1: {um}')
    if sacar == 0:
        break
print(' Volte sempre ao Banco Ibis ')

