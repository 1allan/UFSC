
def posto(combustivel, litros):
    if combustivel == 'A':
        if litros < 20:
            print(f'Total: {1.9 * litros - litros * .03}')
        else:
            print(f'Total: {1.9 * litros - litros * .05}')
    else:
        if litros < 20:
            print(f'Total: {2.5 * litros - litros * .04}')
        else:
            print(f'Total: {2.5 * litros - litros * .06}')

c = input('Álcool ou gasosa? ')
l = input('Quantos litros? ')
posto(c, l)
