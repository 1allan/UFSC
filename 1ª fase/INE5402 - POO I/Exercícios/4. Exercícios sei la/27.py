t_sum = 0
i = 0

while True :
    t = float(input('Temperatura: '))

    if i == 0:
        m = t
        m2 = m
    elif t < m:
        m2 = m
        m = t    
    i += 1

    print(f'Menores temperaturas: {m}ºC e {m2}ºC')
