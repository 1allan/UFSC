qnt_pessoas = int(input('Quantidade de pessoas: '))
sum_idade = 0

for i in range(qnt_pessoas):
    idade = int(input('Idade: '))
    sum_idade += idade 

if 0 < sum_idade <= 25:
    print('Turma jovem')
elif 25 < sum_idade <= 60:
    print('Turma adulta')
else:
    print('Turma idosa')