perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? "
]

i = 0
afirmacoes = 0

for i in range(len(perguntas)):
    res = input(perguntas[i])

    if res == 's':
        afirmacoes += 1

if afirmacoes == 2:
    print('Suspeito!')
elif afirmacoes == 3 or afirmacoes == 4:
    print('Cúmplice!')
elif afirmacoes == 5:
    print('Assasino!')
else:
    print('Inocente')