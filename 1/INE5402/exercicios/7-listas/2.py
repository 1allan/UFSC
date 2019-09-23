numeros = []

for i in range(5):
    n = int(input('N: '))

    rep = n in numeros   
    
    numeros.append(n)
    
print(rep)