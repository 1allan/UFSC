mais_idoso = 0
idoso = ''
qnt_idosos = int(input('Quantidade de idosos: '))

for i in range(qnt_idosos):
    nome = input('Nome do idoso: ')
    nota = int(input('Idade do idoso: '))
    
    if nota > mais_idoso:
        idoso = nome
        mais_idoso = nota

print(idoso)