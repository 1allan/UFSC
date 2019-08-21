p1 = float(input('Digite o preço do produto: R$'))
p2 = float(input('Digite o preço de outro produto: R$'))
p3 = float(input('Digite o preço de outro produto: R$'))
opt = ''

while opt != 'n' :
    if p1 < p2 and p1 < p3:
        print('O primeiro produto é a melhor opção')
    elif p2 < p1 and p2 < p3:
        print('O segundo produto é a melhor opção')
    else:
        print('O terceiro produto é a melhor opção')

    opt = input('Desejas continuar? ')
    
    if opt != 'n':
        p1 = float(input('Digite o preço do produto: R$'))
        p2 = float(input('Digite o preço de outro produto: R$'))
        p3 = float(input('Digite o preço de outro produto: R$'))
