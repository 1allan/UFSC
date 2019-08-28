qnt = int(input('Quantidade: '))
total = 0

for i in range(qnt):
    preco = float(input('Preço: '))
    total += preco

print(f'Total gasto: {total}')
print(f'Preço por médio por disco: {total / qnt}')