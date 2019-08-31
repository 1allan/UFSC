n = int(input('Número: '))

if n < 1000:
    centenas = 0
    dezenas = 0

    while n >= 100 :
        centenas += 1
        n -= 100
    
    while n >= 10 :
        dezenas += 1
        n -= 10

    print(f'Centenas: {centenas}')
    print(f'Dezenas: {dezenas}')
    print(f'Unidades: {n}')