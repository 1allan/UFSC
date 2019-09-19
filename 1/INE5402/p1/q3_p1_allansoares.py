# Allan Soares 19200410
def serie():
    limite = int(input('Tam: '))
    sum = 0
    m = 1

    for n in range(1, limite + 1):
        print('{} {}'.format(n, m))
        sum += n / m
        m += 2

    print('Resultado: ', sum)

serie()
