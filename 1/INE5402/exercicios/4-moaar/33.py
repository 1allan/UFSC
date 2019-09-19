opcoes = [{'nome': 'Jubileu', 'cod': 1, 'votos': 0}, {'nome': 'Bartolomeu', 'cod': 2, 'votos': 0}, {'nome': 'Astolomeu', 'cod': 3, 'votos': 0}, {'nome': 'Pintolomeu', 'cod': 4, 'votos': 0}, {'nome': 'Voto nulo', 'cod': 5, 'votos': 0}, {'nome': 'Voto em branco', 'cod': 6, 'votos': 0}]

while True:
    opt = int(input('Código: '))
    
    if(opt == 0):
        total = 0
        for i in range(len(opcoes)):
            print(f"{opcoes[i]['nome']}: {opcoes[i]['votos']} votos")
            total += opcoes[i]['votos']

        print(f"Votos nulos: {opcoes[4]['votos'] * 100 / total}%")
        print(f"Votos em branco: {opcoes[5]['votos'] * 100 / total}%")
        break

    for i in range(len(opcoes)):
        if opcoes[i]['cod'] == opt:
            print(opcoes[i]['nome'])
            opcoes[i]['votos'] += 1
    