people = []
women = []
summ = 0

for i in range(2):
    name = input('Nome: ')
    sex = input('Sexo: ')
    age = int(input('Age:'))
    
    person = {
        'name': name,
        'sex': sex,
        'age': age
    }

    summ += age

    if sex.upper() == 'F':
        women.append(person)

    people.append(person)

print('Pessoas cadastradas:', len(people))
print('Média de idade:', summ / len(people))
print('Mulheres:', women)

average = summ / len(people)

for p in people:
    if p['age'] > avarage
        print(p)