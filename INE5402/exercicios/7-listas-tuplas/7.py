numeros = []
impares = []
pares = []

for i in range(5):
    n = float(input('N: '))
    
    numeros.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print('Números:', numeros)
print('ímpares:', impares)
print('Pares:', pares)