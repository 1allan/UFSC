numeros = [[],[]]

for i in range(7):
    n = int(input())

    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

for i in range(len(numeros[0])):
    if i == len(numeros[0]) - 1:
        break
    if numeros[0][i] > numeros[0][i + 1]:
        numeros[0][i], numeros[0][i + 1] = numeros[0][i + 1], numeros[0][i]

print('Pares:', numeros[0])
print('Impares:', numeros[1])
