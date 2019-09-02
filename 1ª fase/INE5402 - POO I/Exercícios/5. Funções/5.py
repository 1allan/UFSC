def populacao():
	i = 0
	while True :
		a = float(input('População cidade A: '))
		ia = float(input('Índice de crescimento cidade A: '))
		b = float(input('População cidade B: '))
		ib = float(input('Índice de crescimento cidade B: '))

		a *= ia
		b *= ib
		i += 1

		if a > b :
			break

	print('Vezes: {}\nA: {}\nB: {}'.format(i, a, b))

populacao()
