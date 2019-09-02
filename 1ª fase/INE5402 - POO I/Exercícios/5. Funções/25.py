def manoel(preco):
    preco = float(preco)
    total = 0

    for i in range(1, 51):
        total += preco
        print(f'{i} - R$ {total:.2f}')

preco_pao = input('Preço do pão: ')
manoel(preco_pao)
