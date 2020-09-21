numeros = []

for _ in range(10):
    numeros.append(float(input()))

for i in range(len(numeros)):
    print(int(numeros[len(numeros) - 1 - i]))