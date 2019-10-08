n = input('algarismos de M: ')

if 1 <= n <= 10:
    m = input('M: ')
    
    if 1<= int(m) <= 1000000000:
        summ = 0

        for i in range(len(m)):
            summ += int(m[i])

        if summ % 3 == 0:
            print(summ, 'sim')
        else:
            print(summ, 'não')