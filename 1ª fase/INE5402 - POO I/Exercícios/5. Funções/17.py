def fatorial(n):
    if n <= 1:
        return n
    else:
        return fatorial(n - 1) * n

a = int(input('Max: '))
print(fatorial(a))