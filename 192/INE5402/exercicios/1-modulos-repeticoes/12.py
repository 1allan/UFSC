n = int(input('Digite um número: '))
divisores = 0
divisiveis = []

for i in range(1, n + 1):
    if n % i == 0:
        divisores += 1
        divisiveis.append(i)

if divisores > 2:
    print('Não é primo', divisiveis)
else: 
    print('É primo')