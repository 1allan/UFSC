def poww():
	base = int(input('Base: '))
	expoente = int(input('Expoente: '))
	res = 1

	for i in range(expoente):
		res *= base

	print(res)

poww()
