i = 0

while True:
    cod = input('Código: ')
    altura = float(input('Altura: '))
    peso = float(input('Peso: '))

    if i == 0:
        menorp_cod = cod
        menorp_altura = altura
        menorp_peso = peso
        maiora_cod = cod
        maiora_altura = altura
        maiora_peso = peso
    elif altura < menora_altura :
        menora_cod = cod
        menora_altura = altura
        menora_peso = peso
    elif peso < menorp_peso :
        menorp_cod = cod
        menorp_altura = altura
        menorp_peso = peso
    
    if peso > maiora_peso :
