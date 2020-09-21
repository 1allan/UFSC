v1 = [input() for _ in range(10)]
v2 = [input() for _ in range(10)]

v3 = []
for i in range(10):
    v3.append(v1[i])
    v3.append(v2[i])

print(v3)