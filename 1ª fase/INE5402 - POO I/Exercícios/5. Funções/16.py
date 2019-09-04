f = 0
i = 0

while f < 500:
    i += 1
    def fibonacci(n):
        if n <= 1:
          return n
        else:
                return fibonacci(n - 1) + fibonacci(n - 2)

    f = fibonacci(i)
    print(f)