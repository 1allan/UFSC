N = int(input('Maior número que pode ser representado: '))
P = int(input('Primeiro termo da equação: '))
Op = input('Operação: ')
Q = int(input('Segundo termo da equação: '))

if N >= 1 and N <= 500000 and P >= 0 and P <= 1000 and Q >= 0 and Q <= 1000 :
    if Op == '+' and Q + P > N or Op == '*' and Q * P > N:
        print('OVERFLOW')
    elif Op == '+' or Op == '*':
        print('OK')
