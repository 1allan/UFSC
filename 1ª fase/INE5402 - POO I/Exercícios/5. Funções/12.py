def tabuada():
	n = int(input('Qual tabuada desjas? '))
	inicio = int(input('Início da tabuada: '))
	fim = int(input('Fim da ta buada: '))

	print('Tabuada de {}:'.format(n))

	for i in range(inicio, fim + 1):
		print('{} x {} = {}'.format(n, i, n * i))

tabuada()
