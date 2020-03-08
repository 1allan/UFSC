n = int(input('Qual tabuada desjas? '))
inicio = int(input('Início da tabuada: '))
fim = int(input('Fim da ta buada: '))

print(f'Tabuada de {n}:')

for i in range(inicio, fim + 1):
	print(f'{n} x {i} = {n * i}')