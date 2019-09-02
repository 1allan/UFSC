def primo(n):
	n = int(n)
	for i in range(1, n + 1):
		div = 0

		for j in range(1, n + 1):
			if i % j == 0:
				div += 1

		if div <= 2:
			print(i)

n = input('Número: ')
primo(n)
