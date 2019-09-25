import random

numeros = []

for i in range(5):
    numeros.append(random.randint(0, 100))

numeros.sort()

print(numeros)
print('Menor:', numeros [0])
print('Maior:', numeros[len(numeros) - 1])