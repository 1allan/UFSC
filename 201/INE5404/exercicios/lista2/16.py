salarios = []

while True:
    semanas = int(input('Semanas: '))
    bruto = float(input('Vendas brutas'))
    salario = semanas * 200 + bruto * .09
    salarios.append(salario)

    if input('Continuar? ').lower() == 'y':
        break

intervalos = round(max(salarios)/100)

for i in range(intervalos):
    qnt = 0
    bound = (i + 1) * 100
    bound_min = bound + 100
    bound_max = bound + 199
    for s in salarios:
        if bound_min <= s < bound_max:
            qnt += 1
    print(f'R${bound_min} - R${bound_max}: {qnt}')