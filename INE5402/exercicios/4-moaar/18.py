while True:
	n = int(input())
	fatorial = 1

	for i in range(1, n + 1):
		if fatorial * i > 16:
			break

		fatorial *= i

	print(fatorial)