def par_impar():
	pares = 0
	impares = 0

	for i in range(3):
		n = int(input('Número: '))

		if n % 2 == 0:
			pares += 1
		else:
			impares += 1

	print('Impares: {}\nPares: {}'.format(impares, pares))

par_impar()
