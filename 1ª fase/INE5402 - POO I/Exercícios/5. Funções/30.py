for i in range(5) :
    cod = input('Código da cidade: ')
    veiculos = int(input('Veículos em 2018: '))
    acidentes = int(input('Acidentes de trânsido em 2018: '))

    if i == 0:
        maior_cod = cod
        maior_veiculos = veiculos
        maior_acidentes = acidentes
        menor_cod = cod
        menor_veiculos = veiculos
        menor_acidentes = acidentes
        sum_veiculos = 0
        sum_veiculos2000 = 0
        v = 0

    elif acidentes > maior_acidentes :
        maior_cod = cod
        maior_veiculos = veiculos
        maior_acidentes = acidentes

    elif acidentes < menor_acidentes :
        menor_cod = cod
        menor_veiculos = veiculos
        menor_acidentes = acidentes

    if veiculos < 2000 :
        v += 1
        sum_veiculos2000 += veiculos
        media = sum_veiculos2000 / v

    sum_veiculos += veiculos

print('Média: {}'.format(sum_veiculos / 5))
print('Média veículos < 2000: {}'.format(media))
