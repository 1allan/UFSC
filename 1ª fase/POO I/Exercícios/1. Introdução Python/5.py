nascimento = int(input('Idade: '))

if 2019 - nascimento < 18:
	print('Ainda vai se alistar')
elif 2019 - nascimento == 18:
	print('Está no momento de se alistar')
else:
	print('Passou do tempo de se alistar')