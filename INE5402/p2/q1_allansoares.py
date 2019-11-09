n, m = [int(x) for x in input().split()]
carros = []

if 3 <= n <= 100 and 1 <= m <= 100:
    for i in range(n):
        tempos = input().split()
        carros.append(0)
    
        if len(tempos) < m:
            break
        
        for j in range(len(tempos)):
            tempos[j] = int(tempos[j])
    
            if 1 <= tempos[j] <= 1000:
                carros[i] += tempos[j]
    
            else:
                break
    
    aux = sorted(carros)

    for i in range(3):
        print(carros.index(aux[i]) + 1)
        
        
