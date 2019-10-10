matriz = []
sum_pares = 0
sum_tercol = 0
  
for i in range(3):
    matriz.append([])
    
    for j in range(3):
        n = int(input('n: '))

        if i == 1 and j == 0:
            maior_sln = n
        elif i == 1 and j > 0 and n > maior_sln:
            maior_sln = n
            
        if n % 2 == 0:
            sum_pares += n

        matriz[i].append(n)

    sum_tercol += matriz[i][2]

print('Soma dos números pares:', sum_pares)
print('Soma da terceira coluna:', sum_tercol)
print('Maior valor da segunda linha:', maior_sln)