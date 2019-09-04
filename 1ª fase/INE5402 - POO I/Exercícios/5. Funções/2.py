def auth():
	user = input('Usuário: ')
	passw = input('Senha: ')
	
	if user == passw :
		print('Usuário não pode ser igual a senha!')
		auth()
	else:
		return

auth()
