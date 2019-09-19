i = 2016
aumento = .015

while i < 2020:
    salario = float(input('Salário: '))
    print(f'Ano: {i}\n Porcentagem: {aumento * 100}%\n Salário com aumento: R${salario * (1 + aumento)}')
    aumento *= 2  
    i += 1