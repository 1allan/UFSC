numeros = []

qnt = int(input('Quantidade: '))

for i in range(qnt):
    n = float(input('N: '))
    numeros.append(n)

    if i == 0:
        maior = n
        menor = n

    if n > maior:
        maior = n
    
    if n < menor:
        menor = n

print('Posição do menor número:', numeros.index(menor))
print('Posição do maior número:', numeros.index(maior))