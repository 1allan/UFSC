from operator import itemgetter

jogadas = {}
res = {}

for i in range(4):
    n = int(input())

    jogadas[f'{i}'] = n

for i in sorted(jogadas.items(), key=itemgetter(1)):
    res[i[0]] = i[1]

print(res)