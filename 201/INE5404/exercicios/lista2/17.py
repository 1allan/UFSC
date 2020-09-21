atletas = []

while True:
    nome = input('Nome: ')
    if nome == '':
        break
    
    saltos = []
    for i in range(1, 6):
        saltos.append(input(f'Salto {i}: '))

    atletas.append([nome, saltos])

print('Resultado final: ')
for a in atletas:
    print('Atleta:', a[0])
    print('Saltos:', '- '.join(a[1]))
    print('Média dos saltos:', sum(a[1])/len(a[1]))
