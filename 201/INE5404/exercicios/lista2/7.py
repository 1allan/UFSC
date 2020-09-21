numeros = [float(input()) for _ in range(5)]

produto = numeros[0]
numeros.reduce()

for n in numeros:
    produto *= n

print('soma:', sum(numeros))
print('produto:', produto)
print('numeros:', numeros)