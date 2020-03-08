n = int(input())

if 1 <= n <= 10:
    notas = [ int(x) for x in input().split()]
    mais_frequente = -1
    qntd_mais_frequente = 0
    
    if len(notas) == n:
        for i in range(len(notas)):
            
            if 0 <= notas[i] <= 10:
                if notas.count(notas[i]) > qntd_mais_frequente:
                    mais_frequente = notas[i]
                    qntd_mais_frequente = notas.count(notas[i])
                elif notas.count(notas[i]) == qntd_mais_frequente and notas[i] > mais_frequente:
                    mais_frequente = notas[i]
                    qntd_mais_frequente = notas.count(notas[i])
            else:
                print('Notas inválidas')
                break
        
        print(mais_frequente)