opt = ''

while opt != 'n':
    p1 = input('p1: ')
    p2 = input('p2: ')
    if p1 == p2:
        print('Empate')
    elif p1 == 'pedra':
        if p2 == 'papel':
            print('p2 ganhou')
        else:
            print('p1 ganhou')
    elif p1 == 'tesoura':
        if p2 == 'pedra':
            print('p2 ganhou')
        else:
            print('p1 ganhou')
    elif p1 == 'papel':
        if p2 == 'pedra':
            print('p1 ganhou')
        else:
            print('p2 ganhou')
    
    opt = input('De novo?')