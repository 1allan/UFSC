maior_media = 0
nome_maior_media = ''
sum_notas = 0

for i in range(2):
    nome = input('Nome do aluno: ')
    n1 = float(input('Nota 1 do aluno: '))
    n2 = float(input('Nota 2 do aluno: '))
    media = (n1 + n2) / 2

    if media > maior_media:
        nome_maior_media = nome
        maior_media = media

if maior_media >= 5.75:
    print('Aprovado', nome_maior_media, media)
elif maior_media >= 2.75:
    print('Recuperação', nome_maior_media, media)
else:
    print('Reprovado', nome_maior_media, media)
    