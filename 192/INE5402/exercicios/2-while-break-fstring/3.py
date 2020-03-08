n1 = int(input('n1: '))
n2 = int(input('n2: '))
opt = int(input('Operação: '))

while opt != 5 :
    print('''
        [1] somar
        [2] multiplicar
        [3] mostrar o maior
        [4] digitar novos números
        [5] sair''')

    if opt == 1 :
        print(n1 + n2)
    elif opt == 2 :
        print(n1 * n2)
    elif opt == 3 :
        print(n1 if n1 > n2 else n2)
    elif opt == 4:
        print('Digite novos números: ')
        n1 = int(input('n1: '))
        n2 = int(input('n2: '))

    opt = int(input('Operação: '))

print('end')