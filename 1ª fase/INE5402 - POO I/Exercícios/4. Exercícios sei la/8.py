soma = 0
media = 0

for i in range(5):
	n = float(input('n: '))
	soma += n
	media = soma / 5

print(f'Soma: {soma}\nMédia: {media}')