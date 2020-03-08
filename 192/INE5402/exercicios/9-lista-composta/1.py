pessoas = []
pesadas = [['', 0, 0]]
leves = [['', 0, 0]]
i = 0

while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    peso = float(input('Peso: '))

    pessoas.append([nome, idade, peso])

    if i == 0 or peso > pesadas[0][2]:
        leves = [['', 0, 0]]
        pesadas[0] = [nome, idade, peso]

    elif peso < pesadas[0][2]:
        if leves[0][2] == peso:
            leves.append([nome, idade, peso])
        elif peso < leves[0][2]:
            leves = [['', 0, 0]]
            leves[0] = [nome, idade, peso]

    elif peso == pesadas[0][2]:
        pesadas.append([nome, idade, peso])

    i += 1
    if input('Desejas continuar cadastrando? ').upper() == 'N':
        break

print('Qnt pessoas cadastradas:', len(pessoas))

print('Pessoas mais pesadas:')
for i in range(len(pesadas)):
    print(pesadas[i])

print('Pessoas mais leves:')
for i in range(len(leves)):
    print(leves[i])

print('Pessoas com mais de 20 anos:')
for i in range(len(pessoas)):
    if pessoas[i][1] > 20:
        print(pessoas[i])
