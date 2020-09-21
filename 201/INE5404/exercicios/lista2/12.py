alunos = [[int(input()), float(input())] for _ in range(30)]
altura_m = sum([a[1] for a in alunos])/len(alunos)

altura_inferior = 0
for a in alunos:
    if a[0] > 13 and a[1] < altura_m:
        altura_inferior += 1

print(altura_inferior)
