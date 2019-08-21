opt = ''

while opt == 's' :
    salario = float(input('Digite um salário: '))
    print(f'Salário reajustado: {salario * .11 if salario * .11 < 318.2 else 318.2}')
    opt = input('Desejas continuar?')