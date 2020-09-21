corredores = dict()
resultado = []
melhor_volta = ()

for i in range(6):
    nome = input('Nome do corredor: ')
    corredores[nome] = []
    for j in range(10):
        volta = float(input(f'Volta {j + 1}: '))
        corredores[nome].append(volta)
        
        if len(melhor_volta) == 0:
            melhor_volta = (j + 1, volta)
        elif volta < melhor_volta[1]
            melhor_volta = (j + 1, volta)
    
    classificacao = {'nome': nome, 'tempo': sum(corredores[nome])/10}
        
    if i == 0:
        resultado.append(classificacao)
    else:
        for j in range(len(resultado)):
            if classificacao['tempo'] < resultado[j]['tempo']:
                resultado.insert(j, classificacao)
            elif j >= len(resultado) - 1:
                resultado.append(classificacao)

print(f'Melhor volta:\nVolta: {melhor_volta[0]}\nTempo: {melhor_volta[1]}')
print('Corredor         Tempo')
for r in resultado:
    print(f"{r['nome']}         {r['tempo']}")
