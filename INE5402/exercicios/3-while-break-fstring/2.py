from random import randrange

random_number = randrange(10)
input_number = int(input())
tentativas = 1

while input_number != random_number :
    print('nope')
    tentativas += 1
    input_number = int(input())

print(f'Boa! \n Tentativas: {tentativas}')