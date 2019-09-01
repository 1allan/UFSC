sum_n = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        sum_n += i

print(sum_n)