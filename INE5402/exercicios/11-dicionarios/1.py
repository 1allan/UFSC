n = int(input('Quantidade de alunos: '))
students = []


for i in range(n):
    name = input('Nome: ')
    avg = float(input('Média: '))
    disc = input('Disciplina: ')

    students.append({
        'name': name,
        'average': avg,
        'discipline': disc
    })

for s in students:
    print(s)