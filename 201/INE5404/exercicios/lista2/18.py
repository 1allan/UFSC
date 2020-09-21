jogadores = [0] * 23

print('Enquete: Quem foi o melhor jogador?')
while True:
    voto = int(input('Número do jogador (0=fim): '))
    if 0 > voto > 23:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
    elif voto == 0:
        break
    else:
        jogadores[voto - 1] += 1

print('Resultado da votação:')
print(f'Foram computados {sum(jogadores)} votos.')

porcentagem = lambda v: v * 100/total

print('Jogador          Votos           %')
for i, votos in enumerate(jogadores):
    if votos > 0:
        print(f'{i + 1}         {votos}         {porcentagem(votos, sum(jogadores))}')

mais_votado = jogadores.index(max(jogadores))
print(f'O melhor jogador foi o número {mais_votado}, com {jogadores[mais_votado - 1]} votos, correspondendo a {porcentagem(jogadores[mais_votado - 1], sum(jogadores))}% do total de votos.')
