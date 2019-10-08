l = input('Texto: ')

if 1 <= len(l) <= 500:
    print('Sim' if len(l) < 80 else 'Não')