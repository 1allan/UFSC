def maior():
	maior = 0

	for i in range(5) :
		n = int(input('N: '))

		if n > maior:
			maior = n

	print(maior)

maior()
