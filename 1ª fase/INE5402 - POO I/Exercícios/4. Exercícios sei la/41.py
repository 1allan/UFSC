texto = 'abcdefghijklmnopqrstuvwzxyz'
vogais = 'aeyou'
v = 0

for i in range(len(texto)):
    for j in range(len(vogais)):
        if texto[i] == vogais[j]:
            v += 1


print('Vogais:', v)
print('Consoantes:', len(texto) - 1 - v)