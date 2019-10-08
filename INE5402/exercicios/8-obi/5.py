qnt = int(input('Casos de teste: '))
res = []
nota = 'ABCDE'

for i in range(qnt):
    numeros = input('Números: ').split()
    menor = 255
    res.append('')

    for j in range(len(numeros)):
        
        if 0 <= int(numeros[j]) <= 255 and len(numeros) == 5:
            
            if numeros.count(numeros[j]) > 1:
                res[i] = '*'
                break
            
            if int(numeros[j]) < menor:
                menor = int(numeros[j])
                res[i] = nota[j]

        else:
            res[i] = '*'
            break

for i in range(len(res)):
    print(res[i])