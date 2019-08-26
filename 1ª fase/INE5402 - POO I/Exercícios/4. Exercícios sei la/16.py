t1 = 0
t2 = 1
t3 = 0

print(f'{t1}\n{t2}')

while t3 < 500:
	t3 = t1 + t2
	print(t3)
	t1 = t2
	t2 = t3