n = int(input('n: '))

summ_v = 0
kg = []

if 1 <= n <= 365:
    for _ in range(n):
        v = float(input('v: '))

        if 0.10 <= v <= 20.00:
            frutas = input('Frutas: ')
            kg.append(len(frutas.split()))
            summ_v += v

    for i in range(len(kg)):
        print(f'day {n}: {kg[i]} kg')
        
    print(f'{(summ_v / n):.2f}')
