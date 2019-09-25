produtos = ('a', 1, 'b', 2, 'c', 3, 'd', 4)
total = 0

for i in range(0, len(produtos) - 1, 2):
    print(f'{produtos[i]}:  R${produtos[i + 1]}')
    qnt = int(input('Quantidade: '))
    total += qnt * produtos[i + 1]
    
    if input('Desejas continuar? ') != 'S':
        break

print('Total: R$', total)

