num = int(input('Qual tabuada você quer saber? '))
for t in range(1, 11):
    print('{} x {} = {}'.format(num, t, num*t))