pares = 0
impares = 0

for i in range(3):
	n = int(input('Número: '))

	if n % 2 == 0:
		pares += 1
	else:
		impares += 1

print(f'Impares: {impares}\nPares: {pares}')