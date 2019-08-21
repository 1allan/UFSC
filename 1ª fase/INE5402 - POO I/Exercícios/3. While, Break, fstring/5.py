n = int(input('Digite um número: '))
t1 = 0
t2 = 1
i = 3

print(f'{t1}\n{t2}')

while i <= n :
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    i += 1