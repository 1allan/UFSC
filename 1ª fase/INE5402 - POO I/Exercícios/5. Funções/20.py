def primo(n):
	n = int(n)
	div = 0


	for i in range(1, n + 1):
		if n % i == 0:
			div += 1
			print(i)

	if div > 2:
		print('não é primo')
	else:
		print('é primo')


n = input('Número: ')
primo()
