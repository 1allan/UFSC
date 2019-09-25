def auth():
	nome = input('Nome: ')
	idade = int(input('Idade: '))
	sal = float(input('Salário: '))
	sex = input('F ou M: ')
	civ = input('Estado civil: ')

	if len(nome) < 3 :
		print('O nome deve conter mais que 3 caracteres')
		auth()
	elif idade < 0 or idade > 150 :
		print('A idade deve ser entre 0 e 150')
		auth()
	elif sal < 0:
		print('O salário não pode ser negativo')
		auth()
	elif sex != 'f' and sex != 'm':
		print('O sexo deve ser masculino ou feminino')
		auth()
	elif civ != 's' and civ != 'c' and civ != 'v' and civ != 'd':
		print('Estado civil errado')
		auth()
	else:
		return

auth()
