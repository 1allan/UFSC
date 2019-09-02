def idade():
	i = 0
	soma = 0

	while True:
		i += 1
		idade = int(input('Idade: '))
		soma += idade
		media = soma / i

	if media > 0 and media <= 25:
		print('Turma jovem')
	elif media > 25 and media <= 60:
		print('Turma adulta')
	else:
		print('Turma idosa')

idade()
