
while True:
    a = int(input('a: '))
    
    if a == 0:
        print('Não é uma equação de 2 grau.')
        break

    b = int(input('b: '))
    c = int(input('c: '))

    delta = b**2 - 4 * a * c

    if delta < 0:
        print('A equação não possui raizes reais')
        break
    else delta == 0:
        bhaskara = (-b + (delta ** .5)) / 2 * a
        print(f'A equação possui uma raiz real: {bhaskara}')
    else:
        bhaskara1 = (-b + (delta ** .5)) / 2 * a
        bhaskara2 = (-b - (delta ** .5)) / 2 * a
        print(f'A equação possui duas raizes reais: {bhaskara1} e {bhaskara2}')