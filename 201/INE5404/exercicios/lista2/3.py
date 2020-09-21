notas = []

for _ in range(4):
    notas.append(float(input()))

for n in notas:
    print(n)

print('média:', sum(notas)/len(notas))
