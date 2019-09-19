while True :
	nome = input('Nome: ')
	idade = int(input('Idade: '))
	sal = float(input('Salário: '))
	sex = input('F ou M: ')
	civ = input('Estado civil: ')
	
	if len(nome) < 3 :
		print('O nome deve conter mais que 3 caracteres')
	elif idade < 0 or idade > 150 :
		print('A idade deve ser entre 0 e 150')
	elif sal < 0:
		print('O salário não pode ser negativo')
	elif sex != 'f' or sex != 'm':
		print('O sexo deve ser masculino ou feminino')
	elif civ != 's' or civ != 'c' or civ != 'v' or civ != 'd':
		print('Estado civil errado')
	else:
		break
