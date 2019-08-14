C = int(input('Número de competidores: '))
P = int(input('Folhas especiais: '))
F = int(input('Quantidade necessária: '))

if C >= 0 and C <= 1000 and P >= 0 and P <= 1000 and F >= 0 and F <= 1000 :
    if P - (C * F) >= 0 :
        print('S')
    else: 
        print('N')