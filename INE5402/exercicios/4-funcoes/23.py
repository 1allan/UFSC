def investimento(qnt):
    qnt = int(qnt)
    total = 0

    for i in range(qnt):
        preco = float(input('Preço: '))
        total += preco

    print('Total gasto: {}'.format(total))
    print('Preço por médio por disco: {}'.format(total / quantidade))

q = input('Quantidade: ')
investimento(q)
