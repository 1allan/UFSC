numeros = []

 for i in range(5):
     n = float(input())

     if n not in numeros:
         numeros.append(n)
    

print(numeros)

for i in range(len(numeros)):
    for j in range(len(numeros)):
        if numeros[j] > numeros[i]:
            balde = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = balde

print(numeros)