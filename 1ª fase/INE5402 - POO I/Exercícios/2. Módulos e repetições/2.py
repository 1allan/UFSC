maior_nota = 0
nome_maior_nota = ''
qnt_alunos = int(input('Quantidade de alunos: '))

for i in range(qnt_alunos):
    nome = input('Nome do aluno: ')
    nota = int(input('Nota do aluno: '))
    
    if nota > maior_nota:
        nome_maior_nota = nome
        maior_nota = nota

print(nome_maior_nota)