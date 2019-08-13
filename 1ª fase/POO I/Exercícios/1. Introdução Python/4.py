n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
media = (n1 + n2 + n3)/3

if media < 5:
	print('Reprovado')
elif media >= 5 and media < 7:
	print('Recuperação')
else:
	print('Aprovado')