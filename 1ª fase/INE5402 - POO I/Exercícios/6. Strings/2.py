qnt = int(input('Quantidade de senhas: '))
table = 'GQaku ISblv EOYcmw FPZnx JTeoy DNXfpz AKUgq CMWhr BLVis HRjt'
table = table.split()

for i in range(qnt):
    senha = input('Senha: ')
    cript = ''

    for j in range(len(senha)):
        for k in range(len(table)):
            if senha[j] in table[k]:
                cript += str(k)

    print(cript[:12])
