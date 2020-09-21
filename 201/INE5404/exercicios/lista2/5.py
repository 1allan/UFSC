numeros = [int(input()) for _ in range(20)]
n_pares = [n for n in numeros if n % 2 == 0]

print('numeros:', numeros)
print('pares:', n_pares)
print('impares:', list(set(numeros) - set(n_pares)))