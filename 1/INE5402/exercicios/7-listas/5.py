x = list(range(21))
s = x[:]

for i in range(len(x)):
    x[i] = s[len(x) - 1 - i] 

print(x)