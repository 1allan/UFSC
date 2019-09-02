n = int(input('Número: '))
for i in range(1, n):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    print(fibonacci(i))
