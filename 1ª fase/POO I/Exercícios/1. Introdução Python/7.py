idade = int(input('Idade: '))

if idade <= 12:
	print('Criança')
elif idade > 12 and idade <=18:
	print('Adolescente')
else idade >= 18:
	print('Adulto')