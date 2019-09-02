n1 = int(input('N1: '))
n2 = int(input('N2: '))

maior, menor = (n1, n2) if n1 > n2 else (n2, n1)

soma = 0
produto = 1

for i in range(menor + 1, maior):
	soma += i
	produto *= i

print(f'Soma: {soma}\nProduto: {produto}')