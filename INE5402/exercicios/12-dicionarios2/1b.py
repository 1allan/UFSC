jogadas = {}
aux = []

for i in range(4):
    n = int(input())
    
    aux.append([i, n])


for i in range(3):
    if aux[i][1] < aux[i + 1][1]:
        aux[i][1], aux[i + 1][1] = aux[i + 1][1], aux[i][1]
    
if aux[3][1] > aux[0][1]:
    aux.insert(0, aux[3])
    aux.pop() 
print(aux)
    