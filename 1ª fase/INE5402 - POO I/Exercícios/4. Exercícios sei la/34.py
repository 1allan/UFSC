n = int(input('N: '))
m = int(input('M: '))
total = 0
i = 1
j = 1

while i <= n :
    total += i / j
    i += 1
    j += 2
    
print(total)