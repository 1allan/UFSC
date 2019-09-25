qnt = int(input('Alunos na turma: '))
notas = []

for i in range(qnt):
    n = float(input('Nota do aluno: '))

    if 0 <= n <= 10:
        notas.append(n)

notas = sorted(notas)

print('Menor nota:', notas[0])
print('Maior nota:', notas[len(notas) - 1])