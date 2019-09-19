def aumento():
    i = 2016
    aumento = .015

    while i < 2020:
        salario = float(input('Salário: '))
        print('Ano: {}\n Porcentagem: {}%\n Salário com aumento: R${}'.format(i, aumento * 100, salario * (1 + aumento)))
        aumento *= 2
        i += 1

aumento()
