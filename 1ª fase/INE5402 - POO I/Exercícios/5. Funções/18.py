def fatorial(n):
    if n <= 1:
        return n
    else:
        return fatorial(n - 1) * n

while True:
    a = int(input('Max: '))
    if a > 16:
        print(fatorial(a))
    else:
        print('O número deve ser maior que 16: ')