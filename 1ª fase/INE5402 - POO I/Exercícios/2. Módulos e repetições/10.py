impares = 0
pares = 0

for i in range(10) :
    n = int(input('Digite um número: '))

    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print('Pares: ', pares)
print('Ímpares: ', impares)