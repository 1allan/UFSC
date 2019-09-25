alunos = ()

for i in range(10):
    nome = input('Nome: ')
    alunos += (nome,)

print('Posição Pedro:', alunos.index('Pedro'))
print('Qnt Maria:', alunos.count('Maria'))