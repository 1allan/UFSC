numeros = ()
numeros_pares = ()

for i in range(10):
    n = float(input('N: '))
    numeros += (n,)

    if n % 2 == 0:
        numeros_pares += (n,)

print('Quantidade 9:', numeros.count(9))
print('Primeiro 3:', numeros.index(3))
print('Números pares:', numeros_pares)