n = int(input('Quantidade de casos: '))
res = ''

for i in range(n):
    s = input('Strings: ').split()
    
    if s[0] > s[1]:
        maior = s[0]
        menor = s[1]
    else:
        maior = s[1]
        menor = s[0]

    for i in range(len(maior)):
        if i < len(menor):
            res += s[0][i] + s[1][i]
        else:
            res += maior[i]
    res += ' '

print(res.split()[0])
print(res.split()[1])