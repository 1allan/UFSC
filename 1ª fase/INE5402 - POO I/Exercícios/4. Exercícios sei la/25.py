preco_pao = float(input('Preço do pão: R$ '))
total = 0

for i in range(1, 51):
    total += preco_pao
    print(f'{i} - R$ {total:.2f}')