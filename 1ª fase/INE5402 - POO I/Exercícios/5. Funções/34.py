def soma_fracao(n, m):
    n = int(n)
    m = int(m)
    total = 0
    i = 1
    j = 1

    while i <= n :
        total += i / j
        i += 1
        j += 2

    print(total)

n = input('n: ')
m = input('m: ')
soma_fracao(n, m)
