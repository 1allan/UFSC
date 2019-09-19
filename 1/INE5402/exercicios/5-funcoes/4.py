def populacao():
	a = 80000
	b = 200000
	i = 0

	while a < b:
		a *= 1.03
		b *= 1.015
		i += 1
		print(f'Vezes: {i}\nA: {a}\nB: {b}')

populacao()
