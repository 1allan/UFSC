alturas = []
idades = []

for _ in range(5):
    alturas.append(float(input()))
    idades.append(int(input()))

for i in range(5):
    print(alturas[4 - i])
    print(idades[4 - i])