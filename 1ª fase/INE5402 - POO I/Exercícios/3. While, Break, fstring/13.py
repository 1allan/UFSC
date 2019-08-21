#Deu preguiça no meio e utilizei do artefato da gambiarra
opt = ''

while opt != 'n' :
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    media = (n1 + n2) / 2
    conceito = ''

    if  10 >= media > 9:
        conceito = 'A\n Aprovado!'
    elif 9 >= media > 7.5:
        conceito = 'B\n Aprovado!'
    elif 7.5 >= media > 6:
        conceito = 'C\n Aprovado!'
    elif 6 >= media > 4:
        conceito = 'D\n Reprovado!'
    else:
        conceito = 'E\n Reprovado!'
        
    print(f'Nota 1: {n1}\nNota 2: {n2}\nMédia: {media}\nConceito: {conceito}')

    opt = input('Desejas continuar? ')