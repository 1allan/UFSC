acima = 0

for i in range(10):
    notas = []
    for _ in range(4):
        notas.append(float(input()))
    acima += 1 if sum(notas)/4 >= 7 else 0

print(acima)    