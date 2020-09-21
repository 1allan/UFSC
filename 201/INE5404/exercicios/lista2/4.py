vogais = 'aeiou'

consoantes = []
for _ in range(4):
    caractere = input()
    if caractere not in vogais:
        consoantes.append(caractere)

print('consoantes:', len(consoantes))
for c in consoantes:
    print(c)