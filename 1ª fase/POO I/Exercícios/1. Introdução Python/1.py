valor_casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = float(input('Anos: '))

print('Negado' if valor_casa / anos * 12 > salario * 1.3 else 'Aprovado')
