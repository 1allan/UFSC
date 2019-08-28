i = 0
total = 0

print('Lojas Tabajara')

while True :
    i += 1
    preco = float(input(f'Produto {i}: R$ '))
    total += preco

    if preco == 0 :
        print(f'Total: {total}')
        dinheiro = float(input('Dinheiro: '))
        print(f'Troco: {dinheiro - total}')
        break