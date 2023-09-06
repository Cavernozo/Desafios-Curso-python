alunos = []
notas = []
while True:
    if len(notas) < 1:
        notas.append(str(input('Nome: ')))
        for i in range(0, 2):
           notas.append(float(input(f'Nota {i+1}:')))
        alunos.append(notas[:])
        notas.clear()
    cont = str(input('Quer continuar? [S/N]')).upper().strip()
    if cont == 'N':
        break
print(f'{"Nº":<4}{"Nome":<10}{"Media":>8}')
for p , i in enumerate(alunos):
    media = (i[1] + i[2]) / 2
    print(f'{p:<4}  {i[0]:<10}   {media:>8.1f}')

while True:
    cont = int(input('Mostar nota de qual aluno? [999 para sair]:'))
    for p , i in enumerate(alunos):
        if cont == p:
            print(f'As notas do aluno {i[0]} sao: [{i[1]}, {i[2]}]')
            print()
    if cont == 999:
        break
print('<<<  VOLTE SEMPRE  >>>')
