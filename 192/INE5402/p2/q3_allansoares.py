numeros = []
pares = []

for i in range(10):
    n = float(input())
    numeros.append(n)
    
    if n % 2 == 0:
        pares.append(n)
        
print(count(9) if count(9) > 0 else 'O 9 não consta na lista')
print(numeros.index(3))
print(pares)