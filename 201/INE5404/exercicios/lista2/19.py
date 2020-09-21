respostas = [['Windows Server', 0], ['Unix', 0], ['Linux', 0], ['Netware', 0], ['Mac OS', 0], ['Outro', 0]]

print('Qual o melhor Sistema Operacional para uso em servidores?\nAs possíveis respostas são:')
for i, r in respostas:
    print(f'{i + 1}- {r}')

while True:
    resposta = input('')
    if 0 < resposta <= 6:
        respostas[resposta][1] += 1
    else:
        break

total = sum([v[1] for v in respostas])
print('Sistema Operacional          Votos       %')
print('-------------------          -----       ---')
mais_votado = respostas[0]
for r in respostas:
    print(f'{r[0]}          {r[1]}       {r[1] * 100/total}%')
    if r[1] > mais_votado[1]:
        mais_votado = r
print('-------------------          -----       ---')
print(f'O Sistema Operacional mais votado foi o {mais_votado[0]}, com {mais_votado[1]} votos, correspondendo a {mais_votado[1] * 100/total} dos votos.')