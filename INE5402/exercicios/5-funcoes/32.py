def lanchonete():
    cardapio = [{ 'nome': 'Cachorro Quente', 'cod': 100, 'preco': 1.20 }, {'nome': 'Bauru Simples', 'cod': 101, 'preco': 1.30}, {'nome': 'Bauru com ovo', 'cod': 102, 'preco': 1.50}, {'nome': 'Hambúrguer', 'cod': 103, 'preco': 1.20}, {'nome': 'Cheeseburguer', 'cod': 104, 'preco': 1.30}, {'nome': 'Refrigerante', 'cod': 105, 'preco': 1.00}]

    total = 0

    while True:
        item = int(input('Código do item: '))
        qnt = int(input('Quantidade: '))

        for i in range(len(cardapio)):
            if cardapio[i]['cod'] == item :
                total += cardapio[i]['preco'] * qnt
                print(f"{qnt}x {cardapio[i]['nome']} R${cardapio[i]['preco'] * qnt}")
                break

        if input('Desejas continuar? ') == 'n':
            print(f'Total: R${total}')
            break

lanchonete()
