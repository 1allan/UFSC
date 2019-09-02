def count_a():
    a = 0
    for i in range(len(frase)):
        if frase[i] == 'a':
            a += 1
    return a

a_n = count_a(input('Frase: '))

print(a_n)
