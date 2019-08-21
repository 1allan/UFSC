n = input('Digite um número: ')
i = 0
n_sum = 0

while n != 'n' :
    i += 1
    n_sum = int(n)
    n = input('Deseja continuar? ')

    if n == 's' :
        n = input('Digite outro número: ')
    
print('fim', n_sum / i)