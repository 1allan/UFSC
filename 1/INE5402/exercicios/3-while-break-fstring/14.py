while True:
    n1 = float(input('Número 1: '))
    n2 = float(input('Número 2: '))
    n3 = float(input('Número 3: '))

    if n1 > n2 > n3:
        print(f'{n1} é o maior')
    elif n2 > n1 > n3:
        print(f'{n2} é o maior')
    else:
        print(f'{n3} é o maior')

    opt = input('Desejas continuar?')
    if opt == 'n':
        break
