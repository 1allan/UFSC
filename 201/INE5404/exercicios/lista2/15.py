notas = []

while True:
    nota = float(input())
    if nota == -1:
        break
    
    notas.append(nota)

print('Quantidade:', len(notas))
print(' '.join(notas))

for i in range(len(notas)):
    print(notas[len(notas) - 1 - i])

print('Soma:', sum(notas))
media = sum(notas)/len(notas)
print('Média:', media)
print('Acima da média:', ' '.join([n for n in notas if n > media]))
print('Abaixo de 7:', ' '.join([n for n in notas if n > 7]))
print('Dor')