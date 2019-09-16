qnt = int(input('Quantidade de senhas: '))
table = 'GQaku ISblv EOYcmw FPZnx JTeoy DNXfpz AKUgq CMWhr BLVis HRjt'
table = table.split()
res = ''

for i in range(qnt):
    senha = input('Senha: ')
    cript = ''

    if i == qnt - 1:
        for j in range(len(senha)):
            for k in range(len(table)):
                if senha[j] in table[k]:
                    cript += str(k)

        res += cript[:12] + '\n'

print(res)
