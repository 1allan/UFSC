def cen_dez_uni():
    n = int(n)
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

cen_dez_uni(input('Número: '))
