print('Sequência de Fibonacci')
print('~' * 20)
n = int(input('que termo deseja encontrar? '))
primeiro = 0
segundo = 1
count = 2
print('{} > '.format(primeiro), end = '')
while count <= n:
    termo = primeiro + segundo
    primeiro = segundo
    segundo = termo
    count += 1
    print('{} > '.format(primeiro), end = '')
print('FIM')