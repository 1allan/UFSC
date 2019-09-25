def caixa(saque):
    saque = int(saque)
    if 10 <= saque <= 600 :
        um = 0
        cinco = 0
        dez = 0
        cinquenta = 0
        cem = 0

        while saque >= 1:
            if saque >= 100:
                cem += 1
                saque -= 100

            elif saque >= 50:
                cinquenta += 1
                saque -= 50

            elif saque >= 10 :
                dez += 1
                saque -= 10

            elif saque >= 5:
                cinco += 1
                saque -= 5

            else:
                um += 1
                saque -= 1

        print(f'R$100: {cem}')
        print(f'R$50: {cinquenta}')
        print(f'R$10: {dez}')
        print(f'R$5: {cinco}')
        print(f'R$1: {um}')

    else:
        print('Saque permitido 10R$ a 600R$')

caixa(input('Quanto desejas sacar? '))
