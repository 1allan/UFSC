v1 = [input() for _ in range(10)]
v2 = [input() for _ in range(10)]
v3 = [input() for _ in range(10)]

v4 = []
for i in range(10):
    v4.append(v1[i])
    v4.append(v2[i])
    v4.append(v3[i])

print(v4)