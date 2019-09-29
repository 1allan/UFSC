numeros = []

for i in range(5):
     n = float(input())

     if n not in numeros:
         numeros.append(n)
    
for i in range(len(numeros)):
    for j in range(len(numeros)):
        if numeros[j] > numeros[i]:
            numeros[i], numeros[j] = numeros[j], numeros[i]

print(numeros)