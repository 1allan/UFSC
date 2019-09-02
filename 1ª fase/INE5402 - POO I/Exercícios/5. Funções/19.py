def primo(n):
	div = 0

	for i in range(1, n + 1):
		if n % i == 0:
			div += 1

	if div > 2:
		print('não é primo')
	else:
		print('é primo')


n = int(input('Número: '))
primo(n)
