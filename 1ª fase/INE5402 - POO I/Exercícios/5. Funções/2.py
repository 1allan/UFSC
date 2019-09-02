def auth():
	while True :
		user = input('Usuário: ')
		passw = input('Senha: ')
		
		if user == passw :
			print('Usuário não pode ser igual a senha!')
		else:
			break

auth()
