maior_nota = 0
nome_maior_nota = ''
mensalidade_maior_nota = 0
sum_notas = 0
media =  0

for i in range(2):
    nome = input('Nome do aluno: ')
    nota = float(input('Nota do aluno: '))
    mensalidade = float(input('Valor da mensalidade: '))

    sum_notas += nota

    if nota > maior_nota:
        nome_maior_nota = nome
        maior_nota = nota
        mensalidade_maior_nota = mensalidade

print('Aprovado', nome_maior_nota, mensalidade_maior_nota, mensalidade_maior_nota * .7)
    