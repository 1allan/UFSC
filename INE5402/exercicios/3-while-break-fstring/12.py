l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

while True:
    if l1 + l2 > l3 or l1 + l3 > l2 or l2 + l3 > l1:
        if l1 == l2 and l2 == l3:
            print('É um equilátero')
        elif l1 == l2 or l2 == l3 or l2 == l1:
            print('É um isósceles')
        else:    
            print('É um escaleno')
    else:
        print('Não é um triângulo')
