n = int(input('Digite um número: '))
i = 0
n_sum = 0

while n != 123:
    i += 1
    n_sum += n
    n = int(input('Nope, novamente: '))

print(f'Tentativas: {i}\nSomatória: {n_sum}')