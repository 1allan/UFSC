while True:
    n = int(input('n: '))

    if n == 0:
        break
    elif n == 1:
        print([1])
    else:
        res = []
        ln = [1] * n
        par = n % 2 == 0
        r = int(n / 2) if par else int((n + 1) / 2)

        res.append(ln[:])

        for i in range(1, r):
            for j in range(i, n - i):
                ln[j] += 1
            res.append(ln[:])

        res += (res[::-1] if par else res[::-1][1:])

        for r in res:
            print(r)