# Allan Soares 19200410
i = 1

while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: ')
    salario = float(input('Salario: '))

    if i == 1:
        sum_idade = idade
        m_sal2000 = 0
        sal_menor = salario
        ida_menor = idade
        sex_menor = sexo

    if salario < sal_menor:
        sal_menor = salario
        ida_menor = idade
        sex_menor = sexo

    if sexo == 'M' and salario >= 2000:
        m_sal2000 += 1

    sum_idade += idade
    i += 1

    if input('Deseja continuar cadastrando? ') == 'N':
        print('\nIdade media: ', sum_idade / i)
        print('Mulheres com salario maior que 2000:', m_sal2000)
        print('Menor salario:\n - Sexo {}\n - Idade {}'.format(sex_menor, ida_menor))
        break
