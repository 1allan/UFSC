alunos = dict()

def media(nome):
    return sum(alunos[nome])/2

while True:
    nome = input('Nome: ')
    if nome == '':
        break
    
    alunos[nome] = (input('Nota 1: '), input('Nota 2: '))

media(input('Calcular média: '))
