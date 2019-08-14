Av = int(input('Vitórias(A): '))
Ae = int(input('Empates(A): '))
As = int(input('Gols(A): '))
Bv = int(input('Vitórias(B): '))
Be = int(input('Empates(B): '))
Bs = int(input('Gols(B): '))

if Av >= 0 and Av <= 100 and Bv >= 0 and Bv <= 100 and As >= -1000 and As <= 1000
    if Av * 3 + Ae > Bv * 3 + Be :
        print('Time A melhor classificado')
    elif Av * 3 + Ae < Bv * 3 + Be :
        print('Time B melhor classificado')
    else:
        if As > Bs :
            print('Time A melhor classificado')
        elif As < Bs :
            print('Time B melhor classificado')
        else :
            print('Empate')
