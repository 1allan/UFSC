import random

op = input()
matriz = []
sum_n = 0

for i in range(12):
    matriz.append([])
    for j in range(12):
        matriz[i].append(random.randint(0, 10))
        if j < i:
            sum_n += matriz[i][j] + 1

for i in range(len(matriz)):
    print(matriz[i])

if op == 's':
    print('Soma:', sum_n)
else:
    print('Média:', sum_n / 60)