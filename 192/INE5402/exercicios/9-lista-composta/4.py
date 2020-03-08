from random import randrange

n = int(input('Quantidade de jogos: '))
matriz = []

for i in range(n):
    matriz.append([])
    for j in range(6):
        matriz[i].append(randrange(1, 60))

for i in range(n):
    print(f'Jogo {i + 1}: {matriz[i]}')