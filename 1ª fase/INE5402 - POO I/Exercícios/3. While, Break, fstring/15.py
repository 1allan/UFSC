sum_idade = 0
i =1

while True:
    idade = int(input('Digite uma idade: '))
    sum_idade += idade
    i += 1

    opt = input('Desejas continuar? ')
    
    if opt == 'n':
        print(f'A média de idade é: {sum_idade / i}')
        break