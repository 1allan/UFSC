n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
soma = 0

for i in range(n1 + 1, n2, n1):
    soma += i

print(soma)