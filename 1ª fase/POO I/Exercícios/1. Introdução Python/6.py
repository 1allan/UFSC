a = int(input('Valor 1:'))
b = int(input('Valor 2:'))

if a >= 0 and a <= 1000 and b >= 0 and b <= 1000:
	print(a * 3 if a > b else b * 3)