n = int(input('Quantidade de casos: '))
res = ''
output = []

for i in range(n):
    s = input('Strings: ').split()
    
    output.append('')

    if s[0] > s[1]:
        maior = s[0]
        menor = s[1]
    else:
        maior = s[1]
        menor = s[0]

    for j in range(len(maior)):
        if j < len(menor):
            output[i] += s[0][j] + s[1][j]
        else:
            output[i] += maior[j]

for i in range(len(output)):
    print(output[i])