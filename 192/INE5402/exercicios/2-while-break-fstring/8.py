i = 0
opt = ''

while opt != 'n' :
    i += 1
    nome = input('Nome do funcionário: ')
    salario = float(input('Salário do funcionário: '))
    salario_reajustado = salario

    if 1500 <= salario_reajustado < 1750 :
        salario_reajustado *= 1.12
    elif 1750 <= salario_reajustado < 2000 :
        salario_reajustado *= 1.1
    elif  2000 <= salario_reajustado < 3000  :
        salario_reajustado *= 1.07
    else: 
        salario_reajustado *= 1.05
    
    print(f'Funcionário: {nome}\nSalário: {salario}\nSalário reajustado: {salario_reajustado}')
    
    if i >= 3: 
        opt = input('Deseja continuar? ')
