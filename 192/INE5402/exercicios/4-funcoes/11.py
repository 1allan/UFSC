def soma_produto():
	n = int(input('Qual tabuada desjas? '))

	print('Tabuada de {}:'.format(n))

	for i in range(11):
		print('{} x {} = {}'.format(n, i, n * i))

soma_produto()
