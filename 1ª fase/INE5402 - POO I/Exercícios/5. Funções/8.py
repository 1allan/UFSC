def soma_media():
	soma = 0
	media = 0

	for i in range(5):
		n = float(input('n: '))
		soma += n
		media = soma / 5

	print('Soma: {}\nMédia: {}'.format(soma, media))

soma_media()
