from random import sample, randint

frozensets = []
resultado = dict()

for i in range(10):
    conjunto = frozenset([(randint(0, 30)) for _ in range(30)])
    frozensets.append(conjunto)
    for n in conjunto:
        if n not in resultado.keys():
            resultado[n] = 1
        else:
            resultado[n] += 1

for key in sorted(resultado):
    print(f'{key}: {resultado[key]}')