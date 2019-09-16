bussola = 'NLSO'

while True:
    n = int(input('Quantidade de comandos: '))

    if n == 0:
        break

    if 1 <= n <= 1000:
        comandos = input()
        frente = ''

        if len(comandos) == n:
            v = 0

            for i in range(n):
                if comandos[i] == 'D':
                    v += 1
                elif comandos[i] == 'E':
                    v -= 1

                if v == -1:
                    v = 3

                if v == 4:
                    v = 0
            print(bussola[v])
    else:
        print('Quantidade inválida!')
