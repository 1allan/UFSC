n = int(input())

res = [True] * n
for i in range(n):
    matriz = []

    for j in range(9):
        linha = [int(j) for j in input().split()]
        for k in range(1, 10):
            if k not in linha:
                res[i] = False
                break
        
        if not res[i]:
            break
        
        matriz.append(linha)
    
    if not res[i]:
        break

    for j in range(3):
        aux = matriz[j * 3 : (j + 1) * 3]
        c = 0
        for k in range(3):
            for l in range(3):
                aux2 = aux[k][l * 3 : (l + 1) * 3]
                print(aux2)
                for m in range(1, 11):
                    if m in aux2:
                        c += 1
        
        if c < 9:
            res[i] = False
            break
    
    if not res[i]:
        break
   
print(res)